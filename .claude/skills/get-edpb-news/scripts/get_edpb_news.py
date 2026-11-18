#!/usr/bin/env python3
"""Busca noticias del EDPB (edpb.europa.eu) de un mes o un año.

    python get_edpb_news.py month 2026 10
    python get_edpb_news.py year 2026
    python get_edpb_news.py month 2026 10 --words 0

Imprime una línea por noticia, cada línea un JSON con url, title, date,
type, countries, topics, file, ya_bajado, links y body (las primeras 300
palabras del texto, --words N para otra cantidad, --words 0 para el texto
completo).

El script no decide qué se incluye ni escribe documentos: eso lo hace
quien lo use, a partir del log de revisión.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlsplit

import requests
from bs4 import BeautifulSoup

BASE = "https://www.edpb.europa.eu"
LISTING = f"{BASE}/news_en"
OUT_DIR = Path("knowledge-base/edpb.europa.eu")
# El feed RSS (/feed/news_en) responde 503 a clientes automáticos; el
# listado HTML sí responde y está ordenado de más reciente a más antiguo.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

MAX_PAGES = 100
DELAY = 1.0
TIMEOUT = 20
RETRIES = 3
BACKOFF = 3.0


def get(session: requests.Session, url: str, params: dict | None = None) -> str:
    last_error: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            resp = session.get(url, params=params, timeout=TIMEOUT)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as exc:
            last_error = exc
            time.sleep(BACKOFF * attempt)
    raise RuntimeError(f"No se pudo consultar {url} {params or ''}: {last_error}")


def text_of(node, selector: str) -> str:
    found = node.select_one(selector)
    return found.get_text(" ", strip=True) if found else ""


def parse_listing(html_text: str) -> list[dict]:
    """Tarjetas de una página del listado: url, título, fecha, tipo y países."""
    soup = BeautifulSoup(html_text, "html.parser")
    cards = []
    for card in soup.select(".node-article-card"):
        link = card.select_one("a.node-article-card__link[href]")
        time_tag = card.select_one(".node-article-card__date time[datetime]")
        if not link or not time_tag:
            continue
        cards.append({
            "url": urljoin(BASE, link["href"]),
            "title": text_of(card, ".node-article-card__title"),
            "date": time_tag["datetime"][:10],
            "type": text_of(card, ".node-article-card__news-type"),
            "countries": [
                c.get_text(strip=True)
                for c in card.select(".member-country-token__code")
            ],
        })
    return cards


def list_period(session: requests.Session, prefix: str) -> list[dict]:
    """Recorre el listado hasta pasar el periodo; devuelve sus noticias en orden cronológico."""
    found: dict[str, dict] = {}
    for page in range(MAX_PAGES):
        if page:
            time.sleep(DELAY)
        cards = parse_listing(get(session, LISTING, {"page": page}))
        if not cards:
            break
        for card in cards:
            if card["date"].startswith(prefix):
                found.setdefault(card["url"], card)
        # Orden descendente: si la última tarjeta ya es anterior al periodo, no hay más.
        if cards[-1]["date"][: len(prefix)] < prefix:
            break
    else:
        print(f"[aviso] se alcanzó el límite de {MAX_PAGES} páginas", file=sys.stderr)
    return sorted(found.values(), key=lambda c: c["date"])


def slug_of(url: str) -> str:
    last = urlsplit(url).path.rstrip("/").rsplit("/", 1)[-1]
    return re.sub(r"_[a-z]{2}$", "", last)


def to_item(session: requests.Session, card: dict, n_words: int) -> dict:
    soup = BeautifulSoup(get(session, card["url"]), "html.parser")
    article = soup.select_one(".node-article-full") or soup
    body_node = article.select_one(".node-article-full__body")

    links: dict[str, None] = {}
    words: list[str] = []
    if body_node:
        for a in body_node.select("a[href]"):
            href = urljoin(BASE, a["href"].strip())
            if href.startswith("http"):
                links.setdefault(href, None)
        words = body_node.get_text(" ", strip=True).split()

    if n_words and len(words) > n_words:
        body = " ".join(words[:n_words]) + " …"
    else:
        body = " ".join(words)

    yyyy, mm, dd = card["date"].split("-")
    # Bajada = ya existe su documento.
    file = OUT_DIR / yyyy / mm / f"{dd}-{slug_of(card['url'])}.md"
    return {
        "url": card["url"],
        "title": text_of(article, ".node-article-full__title") or card["title"],
        "date": card["date"],
        "type": card["type"],
        "countries": card["countries"],
        "topics": list(dict.fromkeys(
            t.get_text(" ", strip=True)
            for t in article.select(".node-article-full__relevant-topics-item")
        )),
        "file": str(file),
        "ya_bajado": file.is_file(),
        "links": list(links),
        "body": body,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_year = sub.add_parser("year", help="todas las noticias de un año")
    p_year.add_argument("year", type=int, help="ej. 2026")
    p_month = sub.add_parser("month", help="un mes concreto")
    p_month.add_argument("year", type=int, help="ej. 2026")
    p_month.add_argument("month", type=int, choices=range(1, 13), metavar="month", help="número de mes, ej. 10")

    for p in (p_year, p_month):
        p.add_argument(
            "--words", type=int, default=300, metavar="N",
            help="palabras del body de cada noticia (300 por defecto, 0 = texto completo)",
        )

    args = parser.parse_args()
    prefix = f"{args.year}" if args.command == "year" else f"{args.year}-{args.month:02d}"

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    try:
        for card in list_period(session, prefix):
            time.sleep(DELAY)
            print(json.dumps(to_item(session, card, args.words), ensure_ascii=False), flush=True)
    except RuntimeError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
