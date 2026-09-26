"""Read cards.tsv and read/write progress.json (see DESIGN.md, "Datos")."""

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from app import config

MODEL_REVERSED = "Basic (and reversed card)"
MODEL_TYPED = "Basic (type in the answer)"
MODELS = (MODEL_REVERSED, MODEL_TYPED)

ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ID_MAX_LENGTH = 40
COLUMNS = ("id", "model", "front", "back", "alternatives", "image")
ALTERNATIVES_SEPARATOR = "|"


class CardsFileError(Exception):
    """cards.tsv has an invalid line."""


@dataclass
class Note:
    id: str
    model: str
    front: str
    back: str
    alternatives: list[str] = field(default_factory=list)
    image: str = ""


@dataclass
class Card:
    id: str
    note_id: str
    model: str
    question: str
    answer: str
    alternatives: list[str]
    image: str
    sibling_id: str | None

    @property
    def is_typed(self) -> bool:
        return self.model == MODEL_TYPED


def load_notes(path: Path | None = None) -> list[Note]:
    """Read and validate cards.tsv. Stops at the first invalid line."""
    path = path or config.CARDS_FILE
    notes: list[Note] = []
    seen: dict[str, int] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        values = line.split("\t")
        if len(values) > len(COLUMNS):
            raise CardsFileError(f"cards.tsv línea {line_number}: hay más de {len(COLUMNS)} columnas")
        values += [""] * (len(COLUMNS) - len(values))
        note_id, model, front, back, alternatives, image = (value.strip() for value in values)

        if not ID_PATTERN.match(note_id) or len(note_id) > ID_MAX_LENGTH:
            raise CardsFileError(
                f'cards.tsv línea {line_number}: id "{note_id}" no cumple el formato '
                f"(minúsculas sin tildes, dígitos y guiones, máximo {ID_MAX_LENGTH} caracteres)"
            )
        if note_id in seen:
            raise CardsFileError(
                f'cards.tsv línea {line_number}: id duplicado "{note_id}" (ya usado en la línea {seen[note_id]})'
            )
        if model not in MODELS:
            raise CardsFileError(f'cards.tsv línea {line_number}: modelo desconocido "{model}"')
        if not front or not back:
            raise CardsFileError(f"cards.tsv línea {line_number}: faltan la pregunta o la respuesta")

        seen[note_id] = line_number
        notes.append(Note(
            id=note_id,
            model=model,
            front=front,
            back=back,
            alternatives=[a.strip() for a in alternatives.split(ALTERNATIVES_SEPARATOR) if a.strip()],
            image=image,
        ))
    return notes


def expand_cards(notes: list[Note]) -> list[Card]:
    """Model 1 -> "<id>:forward" and "<id>:reverse"; model 2 -> "<id>"."""
    cards: list[Card] = []
    for note in notes:
        if note.model == MODEL_REVERSED:
            forward_id, reverse_id = f"{note.id}:forward", f"{note.id}:reverse"
            cards.append(Card(forward_id, note.id, note.model, note.front, note.back, [], note.image, reverse_id))
            cards.append(Card(reverse_id, note.id, note.model, note.back, note.front, [], note.image, forward_id))
        else:
            cards.append(Card(note.id, note.id, note.model, note.front, note.back,
                              note.alternatives, note.image, None))
    return cards


def load_cards(path: Path | None = None) -> list[Card]:
    return expand_cards(load_notes(path))


def progress_exists(path: Path | None = None) -> bool:
    path = path or config.PROGRESS_FILE
    return path.exists()


def load_progress(path: Path | None = None) -> dict:
    path = path or config.PROGRESS_FILE
    if not path.exists():
        return {"cards": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_progress(progress: dict, path: Path | None = None) -> None:
    """Atomic write: a crash never leaves a half-written file."""
    path = path or config.PROGRESS_FILE
    temp_path = path.with_name(path.name + ".tmp")
    temp_path.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(temp_path, path)


def set_image(note_id: str, file_name: str, path: Path | None = None) -> None:
    """Write file_name in the image column of the note, keeping the rest of the file as is."""
    path = path or config.CARDS_FILE
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("#"):
            continue
        values = line.split("\t")
        if values[0].strip() == note_id:
            values += [""] * (len(COLUMNS) - len(values))
            values[COLUMNS.index("image")] = file_name
            lines[index] = "\t".join(values)
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return
    raise CardsFileError(f'cards.tsv: no existe ninguna nota con id "{note_id}"')
