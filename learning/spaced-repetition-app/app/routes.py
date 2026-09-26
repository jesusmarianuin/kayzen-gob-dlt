"""HTTP routes (see DESIGN.md, "Navegación")."""

import threading
from datetime import datetime

from flask import Flask, abort, current_app, redirect, render_template, request, session, url_for

from app import checker, config, planner, scheduler, stats, storage

WEEKDAYS = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
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


def register(app: Flask) -> None:
    app.jinja_env.globals["image_url"] = _image_url

    @app.get("/")
    def index():
        # Primera vez: manual de ayuda antes de la primera tarjeta
        if not storage.progress_exists():
            return redirect(url_for("help_page"))
        return redirect(url_for("study"))

    @app.get("/study")
    def study():
        now = datetime.now()
        cards = storage.load_cards()
        progress = storage.load_progress()
        card = planner.next_card(cards, progress, now)
        if card is None:
            next_due = planner.next_due_date(progress, now)
            return render_template("done.html", mode="review",
                                   next_due=spanish_date(next_due) if next_due else None)
        return render_template("review.html", card=card, mode="review", stage="question",
                               version=_version(card.id))

    @app.post("/answer/<card_id>")
    def answer(card_id: str):
        card = _find_card(card_id)
        typed = request.form.get("typed", "")
        version = request.form.get("version", "")
        correct = checker.is_correct(typed, card.answer, card.alternatives)
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
        summary = stats.summary(storage.load_cards(), storage.load_progress(), datetime.now().date())
        return render_template("progress.html", summary=summary)

    @app.get("/help")
    def help_page():
        return render_template("help.html", config=config)

    @app.get("/free/start")
    def free_start():
        session["free_order"] = planner.free_order(storage.load_cards())
        session["free_position"] = 0
        return redirect(url_for("free"))

    @app.get("/free")
    def free():
        order = session.get("free_order")
        if order is None:
            return redirect(url_for("free_start"))
        position = session.get("free_position", 0)
        cards = {card.id: card for card in storage.load_cards()}
        # Tarjetas borradas de cards.tsv durante el estudio libre se saltan
        while position < len(order) and order[position] not in cards:
            position += 1
        session["free_position"] = position
        if position >= len(order):
            return render_template("done.html", mode="free", reviewed=len(order))
        return render_template("review.html", card=cards[order[position]], mode="free", stage="question",
                               position=position + 1, total=len(order))

    @app.post("/free/answer/<card_id>")
    def free_answer(card_id: str):
        card = _find_card(card_id)
        typed = request.form.get("typed", "")
        correct = checker.is_correct(typed, card.answer, card.alternatives)
        return render_template("review.html", card=card, mode="free", stage="right" if correct else "wrong",
                               typed=typed, position=session.get("free_position", 0) + 1,
                               total=len(session.get("free_order", [])))

    @app.post("/free/next")
    def free_next():
        session["free_position"] = session.get("free_position", 0) + 1
        return redirect(url_for("free"))

    @app.post("/quit")
    def quit_app():
        shutdown = current_app.config.get("SHUTDOWN")
        if shutdown:
            # Se detiene después de enviar la pantalla de despedida
            threading.Timer(0.5, shutdown).start()
        return render_template("goodbye.html")
