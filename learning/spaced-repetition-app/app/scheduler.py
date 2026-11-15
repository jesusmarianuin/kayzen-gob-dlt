"""SM-2 scheduling (see DESIGN.md, "Planificación: SM-2")."""

import math
from datetime import datetime, time, timedelta

from app import config

AGAIN = "again"
HARD = "hard"
GOOD = "good"
EASY = "easy"
RATINGS = (AGAIN, HARD, GOOD, EASY)

INITIAL_EASE = 2.5
MIN_EASE = 1.3


def new_state() -> dict:
    return {"reps": 0, "interval_days": 0, "ease": INITIAL_EASE, "lapses": 0}


def _days(value: float) -> int:
    # El redondeo previo evita que un error de coma flotante (p. ej. 20.0000001) sume un día
    return math.ceil(round(value, 6))


def next_interval(state: dict, rating: str) -> tuple[float, int]:
    """Return (new ease, new interval in days) for a correct answer."""
    reps, interval, ease = state["reps"], state["interval_days"], state["ease"]
    if rating == HARD:
        ease = max(MIN_EASE, ease - 0.15)
        days = 1 if reps == 0 else max(interval + 1, _days(interval * 1.2))
    elif rating == GOOD:
        days = 1 if reps == 0 else 3 if reps == 1 else _days(interval * ease)
    elif rating == EASY:
        ease += 0.15
        days = 4 if reps == 0 else _days(interval * ease * 1.3)
    else:
        raise ValueError(f"Puntuación desconocida: {rating}")
    return round(ease, 2), min(days, config.MAX_INTERVAL_DAYS)


def apply_rating(state: dict | None, rating: str, now: datetime) -> dict:
    """Return the new state of a card after a rating, with its due date."""
    state = dict(state or new_state())
    if rating == AGAIN:
        state["ease"] = round(max(MIN_EASE, state["ease"] - 0.20), 2)
        state["reps"] = 0
        state["interval_days"] = 0
        state["lapses"] += 1
        due = now + timedelta(minutes=config.RELEARN_MINUTES)
    else:
        state["ease"], state["interval_days"] = next_interval(state, rating)
        state["reps"] += 1
        # Los repasos en días vencen a las 00:00 para estar disponibles todo el día
        due = datetime.combine(now.date() + timedelta(days=state["interval_days"]), time.min)
    state["due"] = due.isoformat(timespec="seconds")
    state["last_review"] = now.isoformat(timespec="seconds")
    state.setdefault("first_seen", now.date().isoformat())
    return state


# Resultados del examen: fijan el grupo de la tarjeta, suba o baje
EXAM_FAIL = "fail"
EXAM_PASS = "pass"
EXAM_EASY = "easy"
EXAM_RESULTS = (EXAM_FAIL, EXAM_PASS, EXAM_EASY)
# reps mínimas tras el examen, para que el siguiente "Bien" en Estudiar multiplique el intervalo
EXAM_MIN_REPS = 2


def apply_exam(state: dict | None, result: str, now: datetime) -> dict:
    """Return the new state of a card after an exam answer.

    fail -> "no las sé" (como "Fallé"), pass -> "medio", easy -> "buen progreso".
    """
    if result not in EXAM_RESULTS:
        raise ValueError(f"Resultado de examen desconocido: {result}")
    is_new = state is None
    if result == EXAM_FAIL:
        state = apply_rating(state, AGAIN, now)
    else:
        state = dict(state or new_state())
        interval = state["interval_days"]
        if result == EXAM_EASY:
            interval = config.MAX_INTERVAL_DAYS
        elif not config.MEDIUM_FROM_DAYS <= interval < config.MAX_INTERVAL_DAYS:
            # Si ya estaba en "medio" conserva su intervalo; si no, entra en "medio" por abajo
            interval = config.MEDIUM_FROM_DAYS
        state["interval_days"] = interval
        state["reps"] = max(state["reps"], EXAM_MIN_REPS)
        due = datetime.combine(now.date() + timedelta(days=interval), time.min)
        state["due"] = due.isoformat(timespec="seconds")
        state["last_review"] = now.isoformat(timespec="seconds")
        state.setdefault("first_seen", now.date().isoformat())
    if is_new:
        # Una tarjeta vista por primera vez en el examen no gasta el límite diario de nuevas de Estudiar
        state["from_exam"] = True
    return state
