# Cementerio

![R.I.P](rip.png)

Aquí descansan las cosas que dejaron de funcionar o de tener sentido, pero que no merecían el olvido de un `rm -rf`. Nada de lo que hay en esta carpeta se usa, se ejecuta ni se mantiene. Si algo resucita, se saca de aquí y se vuelve a poner en su sitio.

Normas del cementerio:

- Cada subcarpeta tiene su entrada en el inventario, con la causa de la muerte
- Lo que entra aquí no se arregla aquí: si se quiere recuperar, se mueve fuera primero
- Se permite el luto, no el apego

## Inventario

### scrape-pae-news

Skill de Claude Code que scrapeaba las noticias del Portal de Administración Electrónica (PAe), las triaba contra `assets/INTEREST.md` y fichaba las relevantes en `knowledge-base/pae-news/`.

- Nació: 2026, en `.claude/skills/scrape-pae-news/`
- Murió: 2026-11-21
- Causa de la muerte: migración web súbita. El PAe se mudó de `pae_Home/pae_Actualidad/pae_Noticias/...` a `/actualidad/noticias/...`, dejó de poner la fecha en las URL y empezó a cargar los listados por mes y año con JavaScript. El script siguió buscando enlaces con el formato antiguo y devolvía cero noticias sin quejarse, que es la peor forma de morir para un script.
- Intentos de reanimación: el RSS de `/rss/noticias`, que solo trae 10 noticias y lleva parado desde el 7 de octubre de 2026. No respondió al tratamiento.
- Deja en herencia: `assets/INTEREST.md`, un criterio de interés bien trabajado; `log/`, el triaje completo de 2026 hasta septiembre; y `scripts/scrape_pae_news.py`, buen conocedor de los tres esquemas de URL históricos del PAe, ninguno de los cuales existe ya.
- Epitafio: "Esperó entre petición y petición para no molestar a nadie. Al final, nadie le respondió".

Si alguien quiere resucitarla, la portada nueva sí trae las 10 últimas noticias en el HTML (tarjetas `div.dnt-date` y `div.dnt-title a.dnt-link`), lo que basta para una ejecución diaria programada.
