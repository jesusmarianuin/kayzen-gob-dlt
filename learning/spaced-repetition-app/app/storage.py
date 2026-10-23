"""Read cards.csv and read/write progress.json (see DESIGN.md, "Datos")."""

import csv
import io
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path

from app import config

MODEL_REVERSED = "reversed"
MODEL_TYPED = "typed"
MODELS = (MODEL_REVERSED, MODEL_TYPED)
# Nombres de los tipos de nota equivalentes en Anki, para exportar
ANKI_MODELS = {MODEL_REVERSED: "Basic (and reversed card)", MODEL_TYPED: "Basic (type in the answer)"}

ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ID_MAX_LENGTH = 40
COLUMNS = ("id", "enabled", "model", "front", "back", "image")
# En una respuesta typed: ";" separa los elementos de una lista (AND, en cualquier orden)
# y "|" las formas válidas de un elemento (OR). "a|b;c" es "(a o b) y c"
LIST_SEPARATOR = ";"
OPTION_SEPARATOR = "|"
LIST_DISPLAY_SEPARATOR = ", "
OPTION_DISPLAY_SEPARATOR = " / "
# enabled vacío equivale a true
ENABLED_VALUES = {"": True, "true": True, "false": False}
COMMENT_PREFIX = "#"


class CardsFileError(Exception):
    """cards.csv has an invalid line."""


@dataclass
class Note:
    id: str
    model: str
    front: str
    back: str
    image: str = ""
    enabled: bool = True


@dataclass
class Card:
    id: str
    note_id: str
    model: str
    question: str
    answer: str
    image: str
    sibling_id: str | None

    @property
    def is_typed(self) -> bool:
        return self.model == MODEL_TYPED

    @property
    def is_list(self) -> bool:
        return self.is_typed and len(answer_items(self.answer)) > 1

    @property
    def display_answer(self) -> str:
        return display(self.answer, self.model)


def answer_items(text: str) -> list[list[str]]:
    """Elements of a typed answer, each with its valid forms.

    "Legislativo|Parlamento;Ejecutivo" -> [["Legislativo", "Parlamento"], ["Ejecutivo"]]
    """
    items = []
    for item in text.split(LIST_SEPARATOR):
        options = [option.strip() for option in item.split(OPTION_SEPARATOR) if option.strip()]
        if options:
            items.append(options)
    return items


def display(text: str, model: str) -> str:
    """Answer as shown on screen. Only typed answers are interpreted; reversed ones are shown as written."""
    if model != MODEL_TYPED:
        return text
    return LIST_DISPLAY_SEPARATOR.join(OPTION_DISPLAY_SEPARATOR.join(options) for options in answer_items(text))


def _parse_line(line: str) -> list[str]:
    return next(csv.reader([line]))


def _format_line(values: list[str]) -> str:
    buffer = io.StringIO()
    csv.writer(buffer, lineterminator="").writerow(values)
    return buffer.getvalue()


def _is_skipped(line: str) -> bool:
    return not line.strip() or line.startswith(COMMENT_PREFIX)


def load_notes(path: Path | None = None) -> list[Note]:
    """Read and validate cards.csv, enabled or not. Stops at the first invalid line."""
    path = path or config.CARDS_FILE
    name = path.name
    notes: list[Note] = []
    seen: dict[str, int] = {}
    header_found = False
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if _is_skipped(line):
            continue
        values = _parse_line(line)
        # La primera fila de datos es la cabecera con los nombres de columna
        if not header_found:
            if tuple(value.strip() for value in values) != COLUMNS:
                raise CardsFileError(
                    f"{name} línea {line_number}: la cabecera debe ser {','.join(COLUMNS)}"
                )
            header_found = True
            continue
        if len(values) > len(COLUMNS):
            raise CardsFileError(
                f"{name} línea {line_number}: hay más de {len(COLUMNS)} columnas "
                "(si un texto lleva comas, ponlo entre comillas dobles)"
            )
        values += [""] * (len(COLUMNS) - len(values))
        note_id, enabled, model, front, back, image = (value.strip() for value in values)

        if not ID_PATTERN.match(note_id) or len(note_id) > ID_MAX_LENGTH:
            raise CardsFileError(
                f'{name} línea {line_number}: id "{note_id}" no cumple el formato '
                f"(minúsculas sin tildes, dígitos y guiones, máximo {ID_MAX_LENGTH} caracteres)"
            )
        if note_id in seen:
            raise CardsFileError(
                f'{name} línea {line_number}: id duplicado "{note_id}" (ya usado en la línea {seen[note_id]})'
            )
        if enabled.lower() not in ENABLED_VALUES:
            raise CardsFileError(
                f'{name} línea {line_number}: enabled "{enabled}" no es válido (true, false o vacío)'
            )
        if model not in MODELS:
            raise CardsFileError(
                f'{name} línea {line_number}: modelo desconocido "{model}" (usa {" o ".join(MODELS)})'
            )
        if not front or not back or (model == MODEL_TYPED and not answer_items(back)):
            raise CardsFileError(f"{name} línea {line_number}: faltan la pregunta o la respuesta")

        seen[note_id] = line_number
        notes.append(Note(
            id=note_id,
            model=model,
            front=front,
            back=back,
            image=image,
            enabled=ENABLED_VALUES[enabled.lower()],
        ))
    if not header_found:
        raise CardsFileError(f"{name}: falta la cabecera {','.join(COLUMNS)}")
    return notes


def expand_cards(notes: list[Note]) -> list[Card]:
    """Model 1 -> "<id>:forward" and "<id>:reverse"; model 2 -> "<id>"."""
    cards: list[Card] = []
    for note in notes:
        if note.model == MODEL_REVERSED:
            forward_id, reverse_id = f"{note.id}:forward", f"{note.id}:reverse"
            cards.append(Card(forward_id, note.id, note.model, note.front, note.back, note.image, reverse_id))
            cards.append(Card(reverse_id, note.id, note.model, note.back, note.front, note.image, forward_id))
        else:
            cards.append(Card(note.id, note.id, note.model, note.front, note.back, note.image, None))
    return cards


def load_cards(path: Path | None = None) -> list[Card]:
    """Cards of the enabled notes. Disabled notes keep their progress but are not shown."""
    return expand_cards([note for note in load_notes(path) if note.enabled])


def export_anki(notes: list[Note]) -> str:
    """Enabled notes as an Anki text import file (tab separated, with Anki headers)."""
    buffer = io.StringIO()
    buffer.write("#separator:tab\n#html:false\n#guid column:1\n#notetype column:2\n")
    buffer.write("#columns:" + "\t".join(("id", "model", "front", "back", "image")) + "\n")
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    for note in notes:
        if note.enabled:
            writer.writerow([note.id, ANKI_MODELS[note.model], note.front, display(note.back, note.model),
                             note.image])
    return buffer.getvalue()


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
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    for index, line in enumerate(lines):
        if _is_skipped(line):
            continue
        values = _parse_line(line)
        if values[0].strip() == note_id:
            values += [""] * (len(COLUMNS) - len(values))
            values[COLUMNS.index("image")] = file_name
            lines[index] = _format_line(values)
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return
    raise CardsFileError(f'{path.name}: no existe ninguna nota con id "{note_id}"')
