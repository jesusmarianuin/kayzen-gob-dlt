"""HTTP routes (see DESIGN.md, "Navegación")."""

import threading
from datetime import datetime

from flask import Flask, Response, abort, current_app, redirect, render_template, request, session, url_for

from app import checker, config, planner, scheduler, stats, storage

WEEKDAYS = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
AREA_ENDPOINTS = ("study", "progress_page", "free_start", "free", "exam_welcome", "exam_start", "exam")
EXAM_KEYS = ("exam_order", "exam_position", "exam_results")
EXAM_SCOPES = ("all", "exclude-good")
MONTHS = ("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic")


def spanish_date(moment: datetime) -> str:
    return f"{WEEKDAYS[moment.weekday()]} {moment.day} {MONTHS[moment.month - 1]}"


def _image_url(card: storage.Card) -> str | None:
    if card.image and (config.IMAGES_DIR / card.image).exists():
        return url_for("static", filename=f"images/{card.image}")
    return None


def _find_card(card_id: str) -> storage.Card:
    for card in storage.load_cards():
        if card.id == card_id:
            return card
    abort(404)


def _version(card_id: str) -> str:
    """Momento de la última respuesta de la tarjeta ("" si es nueva). Viaja oculto en cada formulario."""
    state = storage.load_progress()["cards"].get(card_id)
    return state["last_review"] if state else ""


def _rate(card_id: str, rating: str, version: str) -> bool:
    """Apply the rating only if the page was up to date. Return whether it was applied.

    Un doble clic, el botón "Atrás" o recargar la página envían una versión antigua:
    esa puntuación ya se registró y se ignora.
    """
    progress = storage.load_progress()
    state = progress["cards"].get(card_id)
    if (state["last_review"] if state else "") != version:
        return False
    progress["cards"][card_id] = scheduler.apply_rating(state, rating, datetime.now())
    storage.save_progress(progress)
    return True


def _exam_answer(card_id: str, result: str, version: str) -> None:
    """Apply an exam result and move to the next card, only if the page was up to date (see _rate)."""
    progress = storage.load_progress()
    state = progress["cards"].get(card_id)
    if (state["last_review"] if state else "") != version:
        return
    progress["cards"][card_id] = scheduler.apply_exam(state, result, datetime.now())
    storage.save_progress(progress)
    results = session.get("exam_results", {})
    results[result] = results.get(result, 0) + 1
    session["exam_results"] = results
    session["exam_position"] = session.get("exam_position", 0) + 1


def _current_area() -> storage.Area | None:
    """Area chosen in this run of the app. The session is lost on restart, so each run starts on /areas."""
    area_id = session.get("area")
    return next((area for area in storage.load_areas() if area.id == area_id), None)


def register(app: Flask) -> None:
    app.jinja_env.globals["image_url"] = _image_url
    app.jinja_env.globals["current_area"] = _current_area

    @app.before_request
    def require_area():
        # Repaso, progreso, estudio libre y examen trabajan sobre un área: sin elegirla, pantalla de áreas
        if request.endpoint in AREA_ENDPOINTS and _current_area() is None:
            return redirect(url_for("areas"))
        return None

    @app.get("/")
    def index():
        # Primera vez: manual de ayuda antes de elegir área
        if not storage.progress_exists():
            return redirect(url_for("help_page"))
        return redirect(url_for("areas"))

    @app.get("/areas")
    def areas():
        now = datetime.now()
        progress = storage.load_progress()
        rows = []
        for area in storage.load_areas():
            cards = storage.load_cards(area=area.id)
            rows.append((area, len(cards), planner.pending_today(cards, progress, now)))
        return render_template("areas.html", rows=rows)

    @app.post("/areas/<area_id>")
    def choose_area(area_id: str):
        if area_id not in {area.id for area in storage.load_areas()}:
            abort(404)
        session["area"] = area_id
        # Un estudio libre o un examen a medias era de otra área
        for key in ("free_order", "free_position", *EXAM_KEYS):
            session.pop(key, None)
        return redirect(url_for("study"))

    @app.get("/study")
    def study():
        now = datetime.now()
        cards = storage.load_cards(area=_current_area().id)
        progress = storage.load_progress()
        if not cards:
            return render_template("done.html", mode="empty")
        card = planner.next_card(cards, progress, now)
        if card is None:
            next_due = planner.next_due_date(cards, progress, now)
            return render_template("done.html", mode="review",
                                   next_due=spanish_date(next_due) if next_due else None)
        return render_template("review.html", card=card, mode="review", stage="question",
                               version=_version(card.id))

    @app.post("/answer/<card_id>")
    def answer(card_id: str):
        card = _find_card(card_id)
        typed = request.form.get("typed", "")
        version = request.form.get("version", "")
        correct = checker.is_correct(typed, card.answer)
        if not correct:
            # Fallo al teclear: cuenta como "fallé" sin preguntar
            _rate(card.id, scheduler.AGAIN, version)
        return render_template("review.html", card=card, mode="review",
                               stage="right" if correct else "wrong", typed=typed, version=version)

    @app.post("/rate/<card_id>")
    def rate(card_id: str):
        rating = request.form.get("rating", "")
        if rating not in scheduler.RATINGS:
            abort(400)
        _rate(_find_card(card_id).id, rating, request.form.get("version", ""))
        return redirect(url_for("study"))

    @app.get("/progress")
    def progress_page():
        summary = stats.summary(storage.load_cards(area=_current_area().id), storage.load_progress(),
                                datetime.now().date())
        return render_template("progress.html", summary=summary)

    @app.get("/export/anki")
    def export_anki():
        # Descarga para Anki: Archivo → Importar. Solo notas activas, sin progreso
        return Response(storage.export_anki(storage.load_notes()), mimetype="text/tab-separated-values",
                        headers={"Content-Disposition": "attachment; filename=cards-anki.txt"})

    @app.get("/help")
    def help_page():
        return render_template("help.html", config=config)

    @app.get("/free/start")
    def free_start():
        session["free_order"] = planner.free_order(storage.load_cards(area=_current_area().id))
        session["free_position"] = 0
        return redirect(url_for("free"))

    @app.get("/free")
    def free():
        order = session.get("free_order")
        if order is None:
            return redirect(url_for("free_start"))
        position = session.get("free_position", 0)
        cards = {card.id: card for card in storage.load_cards(area=_current_area().id)}
        # Tarjetas borradas o desactivadas en cards.csv durante el estudio libre se saltan
        while position < len(order) and order[position] not in cards:
            position += 1
        session["free_position"] = position
        if not order:
            return render_template("done.html", mode="empty")
        if position >= len(order):
            return render_template("done.html", mode="free", reviewed=len(order))
        return render_template("review.html", card=cards[order[position]], mode="free", stage="question",
                               position=position + 1, total=len(order))

    @app.post("/free/answer/<card_id>")
    def free_answer(card_id: str):
        card = _find_card(card_id)
        typed = request.form.get("typed", "")
        correct = checker.is_correct(typed, card.answer)
        return render_template("review.html", card=card, mode="free", stage="right" if correct else "wrong",
                               typed=typed, position=session.get("free_position", 0) + 1,
                               total=len(session.get("free_order", [])))

    @app.post("/free/next")
    def free_next():
        session["free_position"] = session.get("free_position", 0) + 1
        return redirect(url_for("free"))

    @app.get("/exam/welcome")
    def exam_welcome():
        cards = storage.load_cards(area=_current_area().id)
        states = storage.load_progress()["cards"]
        good = sum(1 for card in cards if stats.group_of(states.get(card.id)) == stats.GOOD)
        return render_template("exam-welcome.html", config=config, total=len(cards), without_good=len(cards) - good)

    @app.post("/exam/start")
    def exam_start():
        scope = request.form.get("scope", "")
        if scope not in EXAM_SCOPES:
            abort(400)
        cards = storage.load_cards(area=_current_area().id)
        if scope == "exclude-good":
            states = storage.load_progress()["cards"]
            cards = [card for card in cards if stats.group_of(states.get(card.id)) != stats.GOOD]
        session["exam_order"] = planner.free_order(cards)
        session["exam_position"] = 0
        session["exam_results"] = {}
        return redirect(url_for("exam"))

    @app.get("/exam")
    def exam():
        order = session.get("exam_order")
        if order is None:
            return redirect(url_for("exam_welcome"))
        position = session.get("exam_position", 0)
        cards = {card.id: card for card in storage.load_cards(area=_current_area().id)}
        # Tarjetas borradas o desactivadas en cards.csv durante el examen se saltan
        while position < len(order) and order[position] not in cards:
            position += 1
        session["exam_position"] = position
        if position >= len(order):
            results = session.get("exam_results", {})
            return render_template("done.html", mode="exam", total=len(order),
                                   failed=results.get(scheduler.EXAM_FAIL, 0),
                                   passed=results.get(scheduler.EXAM_PASS, 0),
                                   easy=results.get(scheduler.EXAM_EASY, 0))
        card = cards[order[position]]
        return render_template("review.html", card=card, mode="exam", stage="question",
                               version=_version(card.id), position=position + 1, total=len(order))

    @app.post("/exam/answer/<card_id>")
    def exam_answer(card_id: str):
        card = _find_card(card_id)
        typed = request.form.get("typed", "")
        version = request.form.get("version", "")
        correct = checker.is_correct(typed, card.answer)
        position = session.get("exam_position", 0) + 1
        if not correct:
            # Fallo al teclear: suspende sin preguntar
            _exam_answer(card.id, scheduler.EXAM_FAIL, version)
        return render_template("review.html", card=card, mode="exam", stage="right" if correct else "wrong",
                               typed=typed, version=version, position=position,
                               total=len(session.get("exam_order", [])))

    @app.post("/exam/rate/<card_id>")
    def exam_rate(card_id: str):
        result = request.form.get("result", "")
        if result not in scheduler.EXAM_RESULTS:
            abort(400)
        _exam_answer(_find_card(card_id).id, result, request.form.get("version", ""))
        return redirect(url_for("exam"))

    @app.post("/quit")
    def quit_app():
        shutdown = current_app.config.get("SHUTDOWN")
        if shutdown:
            # Se detiene después de enviar la pantalla de despedida
            threading.Timer(0.5, shutdown).start()
        return render_template("goodbye.html")
