"""Fetch a background image for a note from Wikimedia Commons.

Usage (from the repository root):
    python learning/spaced-repetition-app/scripts/fetch_images.py <note_id> "<search term>"
"""

import re
import sys
from html import unescape
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config, storage  # noqa: E402

API_URL = "https://commons.wikimedia.org/w/api.php"
# Wikimedia exige un User-Agent identificativo
USER_AGENT = "spaced-repetition-app/1.0 (personal study tool; python-requests)"
IMAGE_WIDTH = 800
TIMEOUT_SECONDS = 30
CREDITS_HEADER = "| Fichero | Autor | Licencia | Origen |"


class ImageNotFoundError(Exception):
    """No JPEG image found for the search term."""


def _plain_text(html: str) -> str:
    text = unescape(re.sub(r"<[^>]+>", "", html or ""))
    return " ".join(text.split()) or "Desconocido"


def search_image(term: str) -> dict:
    """Return url, author, license and source of the first JPEG result."""
    response = requests.get(API_URL, timeout=TIMEOUT_SECONDS, headers={"User-Agent": USER_AGENT}, params={
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": term,
        "gsrnamespace": 6,
        "gsrlimit": 20,
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
        "iiurlwidth": IMAGE_WIDTH,
    })
    response.raise_for_status()
    pages = response.json().get("query", {}).get("pages", {})
    for page in sorted(pages.values(), key=lambda p: p.get("index", 0)):
        info = (page.get("imageinfo") or [{}])[0]
        if info.get("mime") != "image/jpeg" or "thumburl" not in info:
            continue
        metadata = info.get("extmetadata", {})
        return {
            "url": info["thumburl"],
            "author": _plain_text(metadata.get("Artist", {}).get("value", "")),
            "license": _plain_text(metadata.get("LicenseShortName", {}).get("value", "")),
            "source": info.get("descriptionurl", ""),
        }
    raise ImageNotFoundError(f'No se ha encontrado ninguna imagen JPEG para "{term}"')


def download(url: str, target: Path) -> None:
    response = requests.get(url, timeout=TIMEOUT_SECONDS, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    target.write_bytes(response.content)


def add_credit(file_name: str, image: dict, path: Path | None = None) -> None:
    """Add or replace the credits row of file_name."""
    path = path or config.CREDITS_FILE
    row = (f"| `{file_name}` | {image['author'].replace('|', '/')} | "
           f"{image['license'].replace('|', '/')} | <{image['source']}> |")
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith(f"| `{file_name}` |")]
    header_index = lines.index(CREDITS_HEADER)
    # La fila va detrás de las existentes, para mantener el orden de alta
    insert_at = header_index + 2
    while insert_at < len(lines) and lines[insert_at].startswith("| `"):
        insert_at += 1
    lines.insert(insert_at, row)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    note_id, term = argv
    try:
        notes = storage.load_notes()
        if note_id not in {note.id for note in notes}:
            raise storage.CardsFileError(f'cards.tsv: no existe ninguna nota con id "{note_id}"')
        image = search_image(term)
        file_name = f"{note_id}.jpg"
        config.IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        download(image["url"], config.IMAGES_DIR / file_name)
        storage.set_image(note_id, file_name)
        add_credit(file_name, image)
    except (storage.CardsFileError, ImageNotFoundError, requests.RequestException) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"{file_name}: {image['author']} ({image['license']}) - {image['source']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
