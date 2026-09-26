"""Progress summary (see DESIGN.md, "Pantalla de progreso")."""

from dataclasses import dataclass
from datetime import date, datetime

from app import config, scheduler
from app.storage import Card

UNKNOWN = "unknown"
MEDIUM = "medium"
GOOD = "good"


@dataclass
class Summary:
    total: int
    good: int
    medium: int
    unknown: int
    answers_left: int
    days_left: int


def group_of(state: dict | None) -> str:
    if state is None or state["interval_days"] < config.MEDIUM_FROM_DAYS:
        return UNKNOWN
    if state["interval_days"] >= config.MAX_INTERVAL_DAYS:
        return GOOD
    return MEDIUM


def _answers_and_waits(state: dict) -> tuple[int, int]:
    """Simulate "good" answers until the cap. Return (answers, days waited before the last one)."""
    answers, waited = 0, 0
    while state["interval_days"] < config.MAX_INTERVAL_DAYS:
        if answers:
            waited += state["interval_days"]
        _, state["interval_days"] = scheduler.next_interval(state, scheduler.GOOD)
        state["reps"] += 1
        answers += 1
    return answers, waited


def summary(cards: list[Card], progress: dict, today: date) -> Summary:
    states = progress["cards"]
    groups = {UNKNOWN: 0, MEDIUM: 0, GOOD: 0}
    answers_left, days_left, new_index = 0, 0, 0

    for card in cards:
        state = states.get(card.id)
        groups[group_of(state)] += 1
        if state is None:
            # La tarjeta nueva número i empieza el día i // NEW_CARDS_PER_DAY
            start = new_index // config.NEW_CARDS_PER_DAY
            new_index += 1
            simulated = scheduler.new_state()
        else:
            due_day = datetime.fromisoformat(state["due"]).date()
            start = max(0, (due_day - today).days)
            simulated = {"reps": state["reps"], "interval_days": state["interval_days"], "ease": state["ease"]}
        answers, waited = _answers_and_waits(simulated)
        if answers:
            answers_left += answers
            days_left = max(days_left, start + waited)

    return Summary(len(cards), groups[GOOD], groups[MEDIUM], groups[UNKNOWN], answers_left, days_left)
