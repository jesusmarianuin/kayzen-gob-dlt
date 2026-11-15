"""Read areas.csv and cards.csv and read/write progress.json (see DESIGN.md, "Datos")."""

import csv
import io
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path

from app import config

MODEL_BASIC = "basic"
MODEL_TYPED = "typed"
MODELS = (MODEL_BASIC, MODEL_TYPED)
# Nombres de los tipos de nota equivalentes en Anki, para exportar
ANKI_MODELS = {MODEL_BASIC: "Basic", MODEL_TYPED: "Basic (type in the answer)"}

ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ID_MAX_LENGTH = 40
COLUMNS = ("id", "enabled", "area", "model", "front", "back", "image")
AREA_COLUMNS = ("id", "name", "description")
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
    """areas.csv or cards.csv has an invalid line."""


@dataclass
class Area:
    id: str
    name: str
    description: str = ""


@dataclass
class Note:
    id: str
    model: str
    front: str
    back: str
    image: str = ""
    enabled: bool = True
    area: str = ""


@dataclass
class Card:
    id: str
    model: str
    question: str
    answer: str
    image: str
    area: str = ""

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
    """Answer as shown on screen. Only typed answers are interpreted; basic ones are shown as written."""
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


def _read_rows(path: Path, columns: tuple[str, ...]):
    """Yield (line number, values) of each data row, after checking the header. Values are stripped."""
    name = path.name
    header_found = False
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if _is_skipped(line):
            continue
        values = _parse_line(line)
        # La primera fila de datos es la cabecera con los nombres de columna
        if not header_found:
            if tuple(value.strip() for value in values) != columns:
                raise CardsFileError(
                    f"{name} línea {line_number}: la cabecera debe ser {','.join(columns)}"
                )
            header_found = True
            continue
        if len(values) > len(columns):
            raise CardsFileError(
                f"{name} línea {line_number}: hay más de {len(columns)} columnas "
                "(si un texto lleva comas, ponlo entre comillas dobles)"
            )
        values += [""] * (len(columns) - len(values))
        yield line_number, [value.strip() for value in values]
    if not header_found:
        raise CardsFileError(f"{name}: falta la cabecera {','.join(columns)}")


def _check_id(name: str, line_number: int, item_id: str, seen: dict[str, int]) -> None:
    if not ID_PATTERN.match(item_id) or len(item_id) > ID_MAX_LENGTH:
        raise CardsFileError(
            f'{name} línea {line_number}: id "{item_id}" no cumple el formato '
            f"(minúsculas sin tildes, dígitos y guiones, máximo {ID_MAX_LENGTH} caracteres)"
        )
    if item_id in seen:
        raise CardsFileError(
            f'{name} línea {line_number}: id duplicado "{item_id}" (ya usado en la línea {seen[item_id]})'
        )
    seen[item_id] = line_number


def load_areas(path: Path | None = None) -> list[Area]:
    """Read and validate areas.csv. The order of the file is the order on the area screen."""
    path = path or config.AREAS_FILE
    areas: list[Area] = []
    seen: dict[str, int] = {}
    for line_number, (area_id, area_name, description) in _read_rows(path, AREA_COLUMNS):
        _check_id(path.name, line_number, area_id, seen)
        if not area_name:
            raise CardsFileError(f"{path.name} línea {line_number}: falta el nombre del área")
        areas.append(Area(area_id, area_name, description))
    return areas


def load_notes(path: Path | None = None, areas_path: Path | None = None) -> list[Note]:
    """Read and validate cards.csv, enabled or not. Stops at the first invalid line."""
    path = path or config.CARDS_FILE
    name = path.name
    area_ids = [area.id for area in load_areas(areas_path)]
    notes: list[Note] = []
    seen: dict[str, int] = {}
    for line_number, values in _read_rows(path, COLUMNS):
        note_id, enabled, area, model, front, back, image = values

        _check_id(name, line_number, note_id, seen)
        if area not in area_ids:
            raise CardsFileError(
                f'{name} línea {line_number}: área "{area}" no definida en {config.AREAS_FILE.name} '
                f'(usa {", ".join(area_ids)})'
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

        notes.append(Note(
            id=note_id,
            model=model,
            front=front,
            back=back,
            image=image,
            enabled=ENABLED_VALUES[enabled.lower()],
            area=area,
        ))
    return notes


def to_cards(notes: list[Note]) -> list[Card]:
    """One line of cards.csv, one card, with the same id."""
    return [Card(note.id, note.model, note.front, note.back, note.image, note.area) for note in notes]


def load_cards(path: Path | None = None, area: str | None = None) -> list[Card]:
    """Cards of the enabled notes, of one area or of all. Disabled notes keep their progress but are not shown."""
    return to_cards([note for note in load_notes(path)
                         if note.enabled and (area is None or note.area == area)])


def export_anki(notes: list[Note]) -> str:
    """Enabled notes as an Anki text import file (tab separated, with Anki headers). The area goes as a tag."""
    buffer = io.StringIO()
    buffer.write("#separator:tab\n#html:false\n#guid column:1\n#notetype column:2\n#tags column:6\n")
    buffer.write("#columns:" + "\t".join(("id", "model", "front", "back", "image", "tags")) + "\n")
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    for note in notes:
        if note.enabled:
            writer.writerow([note.id, ANKI_MODELS[note.model], note.front, display(note.back, note.model),
                             note.image, note.area])
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
