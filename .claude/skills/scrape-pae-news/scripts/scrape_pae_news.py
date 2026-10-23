#!/usr/bin/env python3
"""Busca noticias del PAe (administracionelectronica.gob.es).

    python scrape_pae_news.py home
    python scrape_pae_news.py year 2026
    python scrape_pae_news.py month 2026 Enero
    python scrape_pae_news.py month 2026 Enero --words 100

Imprime una línea por noticia, cada línea un JSON con url, title y body
(las primeras 300 palabras del texto, o --words N para otra cantidad).

El script no decide relevancia: eso lo hace quien lo use, con
INTEREST.md como criterio.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse

import requests
from bs4 import BeautifulSoup

BASE = "https://administracionelectronica.gob.es/pae_Home/pae_Actualidad/pae_Noticias"
HOME_URL = f"{BASE}.html"
MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
]
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# El PAe tiene varios esquemas de URL según la antigüedad de la noticia:
#   moderno: pae_Noticias/2026/Febrero/noticia-2026-02-24-slug.html
#   legado:  pae_Noticias/Anio2010/Diciembre/pae_Noticia_2010-12-16_slug.html
#   legado:  pae_Noticias/Anio-2019/Enero/Noticia-2019-01-31-slug.html
# En todos, lo que distingue un enlace de noticia real (y no un widget
# tipo "noticias-relacionadas.html") es que el nombre de archivo lleva
# una fecha AAAA-MM-DD o AAAA_MM_DD.
NOTICIA_URL_RE = re.compile(
    r"https://administracionelectronica\.gob\.es/pae_Home/pae_Actualidad/"
    r"pae_Noticias/(?:Anio-?)?\d{4}/[^/]+/[^/\"'\s)]*\d{4}[-_]\d{2}[-_]\d{2}[^/\"'\s)]*\.html",
    re.IGNORECASE,
)

# El sitio bloquea peticiones muy seguidas, así que se va con calma.
DELAY = 1.5
TIMEOUT = 20
RETRIES = 3
BACKOFF = 3.0
MAX_PAGES = 40


class NotFound(Exception):
    """El año/mes no existe (el sitio redirige a su página de error 404)."""


class Blocked(Exception):
    """El sitio ha respondido con su página de bloqueo anti-bot."""


def fetch(session: requests.Session, url: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            resp = session.get(url, timeout=TIMEOUT)
        except requests.RequestException as exc:
            last_error = exc
            time.sleep(BACKOFF * attempt)
            continue

        hops = [h.url for h in resp.history] + [resp.url]
        if any("error404.html" in u or "errorhttp=404" in u for u in hops):
            raise NotFound(f"{url} no existe")
        if "Request Rejected" in resp.text[:200]:
            if attempt == RETRIES:
                raise Blocked(f"{url}: el sitio ha bloqueado la petición, prueba más tarde")
            time.sleep(BACKOFF * attempt * 2)
            continue
        if resp.status_code != 200:
            last_error = requests.HTTPError(f"HTTP {resp.status_code} en {url}")
            time.sleep(BACKOFF * attempt)
            continue

        return resp.text

    raise last_error or RuntimeError(f"No se pudo descargar {url}")


def max_page(soup: BeautifulSoup) -> int:
    pages = [1]
    for a in soup.select("a.mp-item-link"):
        title = a.get("title", "")
        if title.isdigit():
            pages.append(int(title))
    return max(pages)


def news_items(soup: BeautifulSoup) -> list[dict]:
    items = []
    for a in soup.select("a.mnl-link[href]"):
        url = urllib.parse.urljoin(BASE, a["href"])
        if NOTICIA_URL_RE.match(url):
            title = (a.get("title") or a.get_text(strip=True) or "").strip()
            items.append({"url": url, "title": title})
    return items


def fetch_first(session: requests.Session, candidates: list[str]) -> tuple[str, BeautifulSoup]:
    """Prueba cada URL candidata en orden y devuelve la primera que exista."""
    last_exc: NotFound | None = None
    for url in candidates:
        try:
            return url, BeautifulSoup(fetch(session, url), "html.parser")
        except NotFound as exc:
            last_exc = exc
    raise last_exc or NotFound("sin candidatas")


def scrape_listing(session: requests.Session, candidates: list[str]) -> list[dict]:
    first_url, soup = fetch_first(session, candidates)
    total_pages = min(max_page(soup), MAX_PAGES)
    items = news_items(soup)

    # El WAF del sitio a veces responde 200 con la página vacía (sin
    # noticias, sin texto de bloqueo) en cuanto ve "?currentPage=" en la
    # URL — y dicha sesión queda "envenenada": las peticiones siguientes,
    # aunque sean a otra URL sin paginar, también vuelven vacías. Si pasa,
    # se avisa y se corta la paginación de este listado en vez de seguir
    # gastando peticiones con una sesión ya inservible.
    for page in range(2, total_pages + 1):
        time.sleep(DELAY)
        html = fetch(session, f"{first_url}?currentPage={page}")
        soup = BeautifulSoup(html, "html.parser")
        page_items = news_items(soup)
        if not page_items:
            print(
                f"[aviso] {first_url}?currentPage={page} no devolvió noticias "
                "(el sitio bloquea la paginación); pueden faltar noticias de "
                "este listado más allá de la página 1",
                file=sys.stderr,
            )
            break
        items.extend(page_items)

    return items


def article_excerpt(session: requests.Session, url: str, n_words: int) -> str | None:
    """Primeras n_words palabras del cuerpo de la noticia, o None si falla.

    En noticias modernas el cuerpo está en un único article.mod-detail; en
    noticias antiguas viene repartido en varios (uno por párrafo), así que
    se juntan todos en orden.
    """
    try:
        html = fetch(session, url)
    except (NotFound, Blocked, requests.RequestException) as exc:
        print(f"[aviso] no se pudo leer {url}: {exc}", file=sys.stderr)
        return None
    soup = BeautifulSoup(html, "html.parser")
    blocks = soup.select("article.mod-detail")
    if not blocks:
        return None
    text = " ".join(b.get_text(" ", strip=True) for b in blocks)
    words = text.split()
    excerpt = " ".join(words[:n_words])
    return excerpt + " …" if len(words) > n_words else excerpt


# El sitio no usa un único esquema para años antiguos: se han visto
# "Anio2010" (sin guion) y "Anio-2019" (con guion) para distintos años.
# En vez de adivinar cuál toca, se prueban los tres en orden.
YEAR_PREFIXES = ["", "Anio", "Anio-"]


def year_candidates(year: str) -> list[str]:
    return [f"{BASE}/{p}{year}.html" for p in YEAR_PREFIXES]


def month_candidates(year: str, month: str) -> list[str]:
    return [f"{BASE}/{p}{year}/{month}.html" for p in YEAR_PREFIXES]


def month_links(session: requests.Session, year: str) -> list[str]:
    """Meses con noticias en un año, en los que el propio archivo del año diga que existen."""
    year_url, soup = fetch_first(session, year_candidates(year))
    prefix = next(p for p in YEAR_PREFIXES if year_url == f"{BASE}/{p}{year}.html")
    pattern = re.compile(rf"/pae_Noticias/{re.escape(prefix)}{year}/([^/]+)\.html$")
    found: dict[str, str] = {}
    for a in soup.select("a[href]"):
        m = pattern.search(a["href"])
        if m:
            found[m.group(1).lower()] = urllib.parse.urljoin(BASE, a["href"])
    return [found[mes.lower()] for mes in MESES if mes.lower() in found]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("home", help="portada de noticias (últimas ~20)")
    p_year = sub.add_parser("year", help="todos los meses con noticias de un año")
    p_year.add_argument("year", help="ej. 2026")
    p_month = sub.add_parser("month", help="un mes concreto")
    p_month.add_argument("year", help="ej. 2026")
    p_month.add_argument("month", help="nombre del mes en español, ej. Enero")

    for p in (sub.choices["home"], p_year, p_month):
        p.add_argument(
            "--words", type=int, default=300, metavar="N",
            help="palabras del body de cada noticia (300 por defecto)",
        )

    args = parser.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "es-ES,es;q=0.9"})

    try:
        if args.command == "home":
            items = scrape_listing(session, [HOME_URL])
        elif args.command == "year":
            items = []
            for i, month_url in enumerate(month_links(session, args.year)):
                if i:
                    time.sleep(DELAY)
                    # Sesión nueva por mes: si el mes anterior disparó el
                    # bloqueo de paginación (ver scrape_listing), su sesión
                    # queda inservible y arrastraría a los meses siguientes.
                    session = requests.Session()
                    session.headers.update(
                        {"User-Agent": USER_AGENT, "Accept-Language": "es-ES,es;q=0.9"}
                    )
                items.extend(scrape_listing(session, [month_url]))
        else:
            items = scrape_listing(session, month_candidates(args.year, args.month))
    except NotFound as exc:
        print(f"[no encontrado] {exc}", file=sys.stderr)
        return 1
    except Blocked as exc:
        print(f"[bloqueado] {exc}", file=sys.stderr)
        return 2

    seen: dict[str, dict] = {}
    for item in items:
        seen.setdefault(item["url"], item)  # dedup conservando el orden y el primer título visto

    for i, item in enumerate(seen.values()):
        if i:
            time.sleep(DELAY)
        item["body"] = article_excerpt(session, item["url"], args.words)
        print(json.dumps(item, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
