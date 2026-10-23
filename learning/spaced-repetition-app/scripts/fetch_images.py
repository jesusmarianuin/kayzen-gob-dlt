"""Fetch a background image for a note from Pixabay, Openverse or Wikimedia Commons.

Usage (from the repository root):
    python learning/spaced-repetition-app/scripts/fetch_images.py <note_id> "<search term>"
    python learning/spaced-repetition-app/scripts/fetch_images.py <note_id> "<search term>" --list 8 --preview-dir <dir>
    python learning/spaced-repetition-app/scripts/fetch_images.py <note_id> "<search term>" --pick 3
    Pixabay is the default source when PIXABAY_API_KEY is set (environment or .env); otherwise, Openverse.
    Add --source openverse|wikimedia|pixabay to choose another source.
"""

import argparse
import os
import re
import sys
import time
from html import unescape
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config, storage  # noqa: E402

PIXABAY_URL = "https://pixabay.com/api/"
# La clave se lee de la variable de entorno o del fichero .env de la app, que no se versiona
PIXABAY_KEY_NAME = "PIXABAY_API_KEY"
ENV_FILE = config.BASE_DIR / ".env"
OPENVERSE_URL = "https://api.openverse.org/v1/images/"
WIKIMEDIA_URL = "https://commons.wikimedia.org/w/api.php"
# Wikimedia y Openverse piden un User-Agent identificativo
USER_AGENT = "spaced-repetition-app/1.0 (personal study tool; python-requests)"
IMAGE_WIDTH = 800
# Por encima de este tamaño se descarga la miniatura en lugar del original
MAX_DOWNLOAD_BYTES = 3_000_000
TIMEOUT_SECONDS = 30
MAX_RETRIES = 4
CANDIDATES = 20
CREDITS_HEADER = "| Fichero | Autor | Licencia | Origen |"
SOURCES = ("pixabay", "openverse", "wikimedia")


class ImageNotFoundError(Exception):
    """No JPEG image found for the search term."""


def _plain_text(html: str) -> str:
    text = unescape(re.sub(r"<[^>]+>", "", html or ""))
    return " ".join(text.split()) or "Desconocido"


def _get(url: str, **kwargs) -> requests.Response:
    """GET with retries when the server answers 429 Too Many Requests."""
    for attempt in range(MAX_RETRIES + 1):
        response = requests.get(url, timeout=TIMEOUT_SECONDS, headers={"User-Agent": USER_AGENT}, **kwargs)
        if response.status_code != 429 or attempt == MAX_RETRIES:
            response.raise_for_status()
            return response
        retry_after = response.headers.get("Retry-After", "")
        time.sleep(int(retry_after) if retry_after.isdigit() else 5 * 2 ** attempt)
    raise AssertionError("unreachable")


def pixabay_key() -> str:
    """Return the Pixabay API key from the environment or the .env file, or an empty string."""
    key = os.environ.get(PIXABAY_KEY_NAME, "")
    if not key and ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            name, _, value = line.partition("=")
            if name.strip() == PIXABAY_KEY_NAME:
                key = value.strip().strip('"')
    return key


def search_pixabay(term: str) -> list[dict]:
    """Return photo candidates from Pixabay (Pixabay Content License, no attribution required)."""
    key = pixabay_key()
    if not key:
        raise ImageNotFoundError(f"Falta la clave de Pixabay: define {PIXABAY_KEY_NAME} o añádela a {ENV_FILE}")
    response = _get(PIXABAY_URL, params={
        "key": key,
        "q": term,
        "image_type": "photo",
        "orientation": "horizontal",
        "safesearch": "true",
        "per_page": CANDIDATES,
    })
    return [{
        "title": item.get("tags", ""),
        "url": item["largeImageURL"],
        "thumbnail": item.get("webformatURL") or item["largeImageURL"],
        "author": item.get("user") or "Desconocido",
        "license": "Pixabay Content License",
        "source": item.get("pageURL", ""),
    } for item in response.json().get("hits", []) if item.get("largeImageURL")]


def _openverse_license(item: dict) -> str:
    code = (item.get("license") or "").lower()
    if code == "pdm":
        return "Public domain"
    if code == "cc0":
        return "CC0 1.0"
    return f"CC {code.upper()} {item.get('license_version') or ''}".strip()


def search_openverse(term: str) -> list[dict]:
    """Return JPEG candidates from Openverse (Flickr, Wikimedia and other open collections)."""
    response = _get(OPENVERSE_URL, params={
        "q": term,
        "extension": "jpg",
        "aspect_ratio": "wide",
        "mature": "false",
        "page_size": CANDIDATES,
    })
    return [{
        "title": _plain_text(item.get("title", "")),
        "url": item["url"],
        "thumbnail": item.get("thumbnail") or item["url"],
        "author": _plain_text(item.get("creator", "")),
        "license": _openverse_license(item),
        "source": item.get("foreign_landing_url") or item["url"],
    } for item in response.json().get("results", []) if item.get("url")]


def search_wikimedia(term: str) -> list[dict]:
    """Return JPEG candidates from Wikimedia Commons."""
    response = _get(WIKIMEDIA_URL, params={
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": term,
        "gsrnamespace": 6,
        "gsrlimit": CANDIDATES,
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
        "iiurlwidth": IMAGE_WIDTH,
    })
    pages = response.json().get("query", {}).get("pages", {})
    candidates = []
    for page in sorted(pages.values(), key=lambda p: p.get("index", 0)):
        info = (page.get("imageinfo") or [{}])[0]
        if info.get("mime") != "image/jpeg" or "thumburl" not in info:
            continue
        metadata = info.get("extmetadata", {})
        candidates.append({
            "title": page.get("title", "").removeprefix("File:"),
            "url": info["thumburl"],
            "thumbnail": info["thumburl"],
            "author": _plain_text(metadata.get("Artist", {}).get("value", "")),
            "license": _plain_text(metadata.get("LicenseShortName", {}).get("value", "")),
            "source": info.get("descriptionurl", ""),
        })
    return candidates


def search_images(term: str, source: str) -> list[dict]:
    search = {"pixabay": search_pixabay, "openverse": search_openverse, "wikimedia": search_wikimedia}[source]
    candidates = search(term)
    if not candidates:
        raise ImageNotFoundError(f'No se ha encontrado ninguna imagen JPEG para "{term}" en {source}')
    return candidates


def download(image: dict, target: Path) -> None:
    content = _get(image["url"]).content
    if len(content) > MAX_DOWNLOAD_BYTES:
        content = _get(image["thumbnail"]).content
    target.write_bytes(content)


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


def list_candidates(note_id: str, candidates: list[dict], count: int, preview_dir: Path | None) -> None:
    """Print the first candidates and, with preview_dir, save their thumbnails to review them."""
    if preview_dir:
        preview_dir.mkdir(parents=True, exist_ok=True)
    for number, image in enumerate(candidates[:count], start=1):
        print(f"{number}. {image['title'][:80]} | {image['author']} ({image['license']}) | {image['source']}")
        if not preview_dir:
            continue
        # Si falla la miniatura, se intenta con el original; si falla también, se sigue con el resto
        for url in dict.fromkeys((image["thumbnail"], image["url"])):
            try:
                (preview_dir / f"{note_id}-{number}.jpg").write_bytes(_get(url).content)
                break
            except requests.RequestException:
                continue
        else:
            print("   (sin miniatura)")


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("note_id")
    parser.add_argument("term")
    # Pixabay por defecto si hay clave; si no, Openverse, que no la necesita
    parser.add_argument("--source", choices=SOURCES, default="pixabay" if pixabay_key() else "openverse")
    parser.add_argument("--list", type=int, metavar="N", help="muestra N candidatos sin descargar")
    parser.add_argument("--preview-dir", type=Path, help="con --list, guarda aquí las miniaturas")
    parser.add_argument("--pick", type=int, default=1, metavar="K", help="descarga el candidato K (por defecto, 1)")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    try:
        notes = storage.load_notes()
        if args.note_id not in {note.id for note in notes}:
            raise storage.CardsFileError(f'{config.CARDS_FILE.name}: no existe ninguna nota con id "{args.note_id}"')
        candidates = search_images(args.term, args.source)
        if args.list:
            list_candidates(args.note_id, candidates, args.list, args.preview_dir)
            return 0
        if not 1 <= args.pick <= len(candidates):
            raise ImageNotFoundError(f"Solo hay {len(candidates)} candidatos para \"{args.term}\"")
        image = candidates[args.pick - 1]
        file_name = f"{args.note_id}.jpg"
        config.IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        download(image, config.IMAGES_DIR / file_name)
        storage.set_image(args.note_id, file_name)
        add_credit(file_name, image)
    except (storage.CardsFileError, ImageNotFoundError, requests.RequestException) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"{file_name}: {image['author']} ({image['license']}) - {image['source']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
