"""Pick the next card of the session (see DESIGN.md, "Orden de la sesión")."""

import random
from datetime import date, datetime

from app import config
from app.storage import Card


def _due(state: dict) -> datetime:
    return datetime.fromisoformat(state["due"])


def _reviewed_on(state: dict | None, day: date) -> bool:
    return bool(state) and datetime.fromisoformat(state["last_review"]).date() == day


def _is_relearning_today(state: dict, today: date) -> bool:
    # Fallada hoy: reps a 0 y respondida hoy
    return state["reps"] == 0 and _reviewed_on(state, today)


def new_cards_left_today(cards: list[Card], progress: dict, today: date) -> int:
    # El límite se cuenta sobre las tarjetas recibidas: con las de un área, es un límite por área
    states = progress["cards"]
    seen_today = sum(1 for card in cards
                     if card.id in states and states[card.id].get("first_seen") == today.isoformat()
                     and not states[card.id].get("from_exam"))
    return max(0, config.NEW_CARDS_PER_DAY - seen_today)


def next_card(cards: list[Card], progress: dict, now: datetime, last_id: str | None = None) -> Card | None:
    """Return the next card to show, or None when the session is over.

    La última tarjeta respondida (last_id) no se repite seguida mientras haya otra que mostrar.
    """
    others = [card for card in cards if card.id != last_id]
    return _pick(others, cards, progress, now) or _pick(cards, cards, progress, now)


def _pick(candidates: list[Card], cards: list[Card], progress: dict, now: datetime) -> Card | None:
    # El límite de nuevas se cuenta sobre todas las tarjetas del área (cards), no solo las candidatas
    today = now.date()
    states = progress["cards"]

    relearning, reviews, new = [], [], []
    for card in candidates:
        state = states.get(card.id)
        if state is None:
            new.append(card)
        elif _is_relearning_today(state, today):
            relearning.append(card)
        elif _due(state) <= now:
            reviews.append(card)

    # Falladas en esta sesión, en cuanto se cumplen sus minutos
    ready = sorted((c for c in relearning if _due(states[c.id]) <= now), key=lambda c: _due(states[c.id]))
    if ready:
        return ready[0]
    # 1. Repasos vencidos, del más atrasado al más reciente (incluye falladas de otros días)
    if reviews:
        return min(reviews, key=lambda c: _due(states[c.id]))
    # 2. Nuevas en orden de cards.csv, con límite diario
    if new and new_cards_left_today(cards, progress, today) > 0:
        return new[0]
    # 3. Si solo quedan falladas esperando, la que venza antes, sin esperar
    if relearning:
        return min(relearning, key=lambda c: _due(states[c.id]))
    return None


def next_due_date(cards: list[Card], progress: dict, now: datetime) -> datetime | None:
    """Next due date among the given cards (the ones of the current area)."""
    states = progress["cards"]
    upcoming = [_due(states[card.id]) for card in cards if card.id in states and _due(states[card.id]) > now]
    return min(upcoming) if upcoming else None


def pending_today(cards: list[Card], progress: dict, now: datetime) -> int:
    """Cards left for today: due reviews plus the new ones the daily limit allows."""
    states = progress["cards"]
    due = sum(1 for card in cards if card.id in states and _due(states[card.id]) <= now)
    new = sum(1 for card in cards if card.id not in states)
    return due + min(new, new_cards_left_today(cards, progress, now.date()))


def free_order(cards: list[Card]) -> list[str]:
    """All card ids in random order, for free study."""
    ids = [card.id for card in cards]
    random.shuffle(ids)
    return ids
