---
name: scrape-pae-news
description: Scrapear y triar noticias del PAe (administracionelectronica.gob.es) contra INTEREST.md y fichar las relevantes en pae-news/. Usar siempre que se pida revisar, buscar o fichar noticias del PAe, novedades de EBSI, o actualizar pae-news/, aunque no se mencione el script.
---

# scrape-pae-news

Herramientas de meta-trabajo para `pae-news/`.

Noticias desde 2010 hasta el año actual. El sitio no usa siempre la
misma URL para años antiguos (`pae_Noticias/2026/...`,
`pae_Noticias/Anio2010/...`, `pae_Noticias/Anio-2019/...`) y el script
prueba las variantes solo; no hace falta indicar cuál usar.

## Lanzar el script

Entorno: el mismo `.venv` de [CONTRIBUTING.md](../../../../CONTRIBUTING.md). Los comandos se lanzan desde la raíz del repositorio.

```bash
python knowledge-base/pae-news/_skills/scrape-pae-news/scripts/scrape_pae_news.py home
python knowledge-base/pae-news/_skills/scrape-pae-news/scripts/scrape_pae_news.py year 2026
python knowledge-base/pae-news/_skills/scrape-pae-news/scripts/scrape_pae_news.py month 2026 Enero
```

Salida: una línea por noticia. Cada línea un JSON con `url`, `title` y
`body` (las primeras 300 palabras del texto). Para otra cantidad:
`--words 100`.

`home` no es "las noticias de hoy": es la portada de noticias del PAe,
las últimas ~20 publicadas en cualquier fecha (así que puede traer
noticias de meses anteriores si no ha habido publicaciones recientes).

El sitio bloquea peticiones muy seguidas, así que el script ya espera
entre una y otra. Si pides un año sin archivo, el script lo dice y sale
con error.

Límite conocido: si un listado (mes o portada) tiene más de una
página, el sitio a veces responde a la página 2+ con un 200 vacío (sin
noticias, sin aviso) en vez de un error — probablemente su protección
antibot. El script lo detecta y avisa por stderr
(`[aviso] ...no devolvió noticias...`) en vez de fallar en silencio,
pero esas noticias de más allá de la página 1 se quedan sin recoger.
Si ves ese aviso, conviene revisar luego esa página a mano.

El script solo busca enlaces — no decide relevancia ni escribe fichas.
Eso es cosa de quien lo ejecute, usando [INTEREST.md](../scrape-pae-news/assets/INTEREST.md).

## Prompts de ejemplo

- "Ejecuta el script para septiembre de 2026, mira cuáles de esos
  enlaces no tienen ya ficha en `pae-news/`, y de esos cuáles encajan
  con INTEREST.md."
- "Revisa la portada (`home`) y dime si hay algo de EBSI (ver
  INTEREST.md) que no tengamos ya."

## Trabajar los grises

Como agente deberás mejor preguntarme por las noticias que tengas dudas, no sea que algo sea de mi interés.

Claro está en nuestro diálogo, si ves que [INTEREST.md](assets/INTEREST.md) se puede mejorar para usar como criterio mucho mejor, porque al final ese archivo es para servirte de ayuda a futuras consultas.

## Formato del informe

Cualquier ejemplo como [2026-03-13-CRED-MITOS.md](../../2026/2026-03-13-CRED-MITOS.md) indica cómo debe ser el informe. A destacar:

- Nombre del archivo como se ve es la fecha y una palabra clave en mayúsculas.
- Debe tener titulo relevante, típicamente la URL que inicia la noticia como "cred.digital.gob.es".
- Poner el enlace de noticia original es fundamente
- El resumen es importante y sobre todo poner enlaces de referencia que trae la noticia (como se ve en el ejemplo)

## Log

Ejecutar el script (sobre todo `year`) y triar cada noticia contra
INTEREST.md es trabajo costoso — no lo tires al terminar la sesión.

Al acabar una pasada, guarda en `knowledge-base/pae-news/_skills/scrape-pae-news/log/AAAA-MM-DD-<alcance>.jsonl`
(p. ej. `2026-09-15-year-2026.jsonl`) una línea JSON por noticia
encontrada, con al menos:

- `url`, `title`
- `ya_fichada`: si ya existía ficha para esa URL antes de esta pasada
- `decision`: `candidata` / `descartada` / `grey` (para las que no
  estaban ya fichadas)
- `motivo`: por qué, en corto (qué punto de INTEREST.md aplica, o por
  qué se descarta)

Así, otra sesión (o tú más adelante) puede retomar el trabajo sin volver a scrapear ni a triar desde cero, y se puede auditar si algo se quedó fuera por error.

---
