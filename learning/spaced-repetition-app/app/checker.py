"""Typed answer comparison with tolerance (see DESIGN.md, "Comparación de la respuesta tecleada")."""

import re
import unicodedata

from app.storage import answer_items

# Tilde de la ñ: se conserva porque la ñ es otra letra
_TILDE = "̃"


def _strip_accents(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text)
    kept = []
    for index, char in enumerate(decomposed):
        is_mark = unicodedata.category(char) == "Mn"
        is_enye = char == _TILDE and index > 0 and decomposed[index - 1] in "nN"
        if not is_mark or is_enye:
            kept.append(char)
    return unicodedata.normalize("NFC", "".join(kept))


def normalize(text: str) -> str:
    text = " ".join(text.casefold().split())
    if text.endswith("."):
        text = text[:-1].rstrip()
    return _strip_accents(text)


# Separador entre elementos de una lista tecleada: coma, punto y coma, "y" o "e" (también ", y")
_TYPED_SEPARATOR = re.compile(r"\s*[,;]\s*(?:[ye]\s+)?|\s+[ye]\s+")


def _matches_list(text: str, items: list[list[str]]) -> bool:
    """text contains exactly the items, in any order, joined by separators. Each item is a list of valid forms.

    Se recorre el texto buscando al principio alguna forma de los elementos que faltan,
    así un elemento con "y" dentro ("ciencia y tecnologia") no se parte.
    """
    for index, options in enumerate(items):
        remaining = items[:index] + items[index + 1:]
        for option in options:
            if not text.startswith(option):
                continue
            rest = text[len(option):]
            if not remaining:
                if not rest:
                    return True
                continue
            separator = _TYPED_SEPARATOR.match(rest)
            if separator and _matches_list(rest[separator.end():], remaining):
                return True
    return False


def is_correct(typed: str, answer: str) -> bool:
    """answer is the back of a typed note: ";" separates list elements (any order), "|" valid forms."""
    typed_normalized = normalize(typed)
    if not typed_normalized:
        return False
    items = [[normalize(option) for option in options] for options in answer_items(answer)]
    return _matches_list(typed_normalized, items)
