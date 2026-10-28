#!/usr/bin/env python3
"""Busca posts de inza.blog a través de la API pública de WordPress.com.

    python get_inza_posts.py month 2026 10
    python get_inza_posts.py year 2026
    python get_inza_posts.py month 2026 10 --words 0

Imprime una línea por post, cada línea un JSON con url, title, date,
categories, file, ya_bajado, links y body (las primeras 300 palabras del
texto, --words N para otra cantidad, --words 0 para el texto completo).

El script no decide qué se incluye ni escribe documentos: eso lo hace
quien lo use, a partir del log de revisión.
"""
from __future__ import annotations

import argparse
import html
import json
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup

API = "https://public-api.wordpress.com/rest/v1.1/sites/inza.blog/posts/"
FIELDS = "date,title,URL,slug,categories,content"
OUT_DIR = Path("knowledge-base/inza.blog")
# Las imágenes del blog cuelgan de cualquiera de sus dos dominios; no son
# referencias. Otros sitios WordPress (p. ej. whitehouse.gov) sí publican
# documentos en /wp-content/, por eso se filtra solo por dominio propio.
OWN_UPLOADS = ("inza.blog/wp-content/", "inza.wordpress.com/wp-content/")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# La API devuelve como máximo 100 posts por petición. Se pide mes a mes,
# y ningún mes del blog se acerca a esa cifra; si alguno la supera, se avisa.
MAX_PER_REQUEST = 100
DELAY = 1.0
TIMEOUT = 20
RETRIES = 3
BACKOFF = 3.0


def fetch_month(session: requests.Session, year: int, month: int) -> list[dict]:
    """Posts publicados en un mes, en orden cronológico.

    La API interpreta after/before en UTC y las fechas de los posts van en
    hora local (+01:00/+02:00), así que se pide con un día de margen por
    cada lado y se filtra por la fecha local del post.
    """
    first = date(year, month, 1)
    nxt = date(year + month // 12, month % 12 + 1, 1)
    params = {
        "after": f"{first - timedelta(days=1)}T00:00:00",
        "before": f"{nxt + timedelta(days=1)}T00:00:00",
        "number": MAX_PER_REQUEST,
        "order_by": "date",
        "order": "ASC",
        "fields": FIELDS,
    }

    last_error: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            resp = session.get(API, params=params, timeout=TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            break
        except (requests.RequestException, ValueError) as exc:
            last_error = exc
            time.sleep(BACKOFF * attempt)
    else:
        raise RuntimeError(f"No se pudo consultar {year}-{month:02d}: {last_error}")

    if data.get("found", 0) > MAX_PER_REQUEST:
        print(
            f"[aviso] {year}-{month:02d} tiene más de {MAX_PER_REQUEST} posts; "
            "pueden faltar posts de este mes",
            file=sys.stderr,
        )

    prefix = f"{year}-{month:02d}"
    return [p for p in data.get("posts", []) if p["date"].startswith(prefix)]


def post_links(soup: BeautifulSoup) -> list[str]:
    """Enlaces que cita el post, sin duplicados ni imágenes del propio blog."""
    links: dict[str, None] = {}
    for a in soup.select("a[href]"):
        href = a["href"].strip()
        if not href.startswith("http") or any(d in href for d in OWN_UPLOADS):
            continue
        links.setdefault(href, None)
    return list(links)


def to_item(post: dict, n_words: int) -> dict:
    url = post["URL"].replace("http://", "https://", 1)
    day = post["date"][:10]
    soup = BeautifulSoup(post.get("content") or "", "html.parser")
    words = soup.get_text(" ", strip=True).split()
    if n_words and len(words) > n_words:
        body = " ".join(words[:n_words]) + " …"
    else:
        body = " ".join(words)
    yyyy, mm, dd = day.split("-")
    # Bajado = ya existe su documento. Buscar la URL en el texto daría por
    # bajados los posts que solo aparecen citados desde otros documentos.
    file = OUT_DIR / yyyy / mm / f"{dd}-{post['slug']}.md"
    return {
        "url": url,
        "title": html.unescape(post["title"]),
        "date": day,
        "categories": list(post.get("categories", {})),
        "file": str(file),
        "ya_bajado": file.is_file(),
        "links": post_links(soup),
        "body": body,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_year = sub.add_parser("year", help="todos los meses de un año")
    p_year.add_argument("year", type=int, help="ej. 2026")
    p_month = sub.add_parser("month", help="un mes concreto")
    p_month.add_argument("year", type=int, help="ej. 2026")
    p_month.add_argument("month", type=int, choices=range(1, 13), metavar="month", help="número de mes, ej. 10")

    for p in (p_year, p_month):
        p.add_argument(
            "--words", type=int, default=300, metavar="N",
            help="palabras del body de cada post (300 por defecto, 0 = texto completo)",
        )

    args = parser.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    months = [args.month] if args.command == "month" else list(range(1, 13))

    try:
        for i, month in enumerate(months):
            if i:
                time.sleep(DELAY)
            for post in fetch_month(session, args.year, month):
                print(json.dumps(to_item(post, args.words), ensure_ascii=False))
    except RuntimeError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
