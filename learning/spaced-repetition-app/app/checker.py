"""Typed answer comparison with tolerance (see DESIGN.md, "Comparación de la respuesta tecleada")."""

import unicodedata

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


def is_correct(typed: str, answer: str, alternatives: list[str]) -> bool:
    typed_normalized = normalize(typed)
    if not typed_normalized:
        return False
    return any(typed_normalized == normalize(valid) for valid in [answer, *alternatives])
