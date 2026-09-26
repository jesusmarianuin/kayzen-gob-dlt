"""Tunable constants (see DESIGN.md, "Parámetros")."""

from pathlib import Path

NEW_CARDS_PER_DAY = 10
RELEARN_MINUTES = 10
# Tope de intervalo y límite de "buen progreso"
MAX_INTERVAL_DAYS = 21
# Límite entre "no la sé" y "medio"
MEDIUM_FROM_DAYS = 3

HOST = "127.0.0.1"
PORT = 5000

APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent
CARDS_FILE = BASE_DIR / "data" / "cards.tsv"
PROGRESS_FILE = BASE_DIR / "data" / "progress.json"
CREDITS_FILE = BASE_DIR / "data" / "image-credits.md"
IMAGES_DIR = APP_DIR / "static" / "images"
