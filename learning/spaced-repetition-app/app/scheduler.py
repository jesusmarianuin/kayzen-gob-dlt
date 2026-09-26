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
