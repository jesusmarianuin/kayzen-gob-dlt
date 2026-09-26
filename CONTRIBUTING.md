# Cómo trabajo en este repositorio

Este repositorio es de trabajo personal: no acepto contribuciones externas (pull requests de terceros, forks para fusionar, etc.). Lo que sigue no es una invitación a colaborar, sino la plantilla que uso para documentar cómo trabajo yo mismo, para que sea coherente a lo largo del tiempo.

Sí son bienvenidos los comentarios e issues (ver [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)).

Este proyecto está licenciado bajo [**Creative Commons Zero v1.0 Universal (CC0)**](https://creativecommons.org/publicdomain/zero/1.0/), dedicando el trabajo al dominio público.

## Pautas de trabajo

### Atribución

Siempre doy el crédito correspondiente cuando incluyo material o contenido de fuentes externas.

### Estilo

Las directrices de estilo están en [`AGENTS.md`](AGENTS.md).

Mantengo la estructura y lo operativo en inglés, pero el contenido explicativo puede estar en español.

### Licencia

- El contenido de este repositorio se dedica al dominio público bajo la licencia **Creative Commons Zero v1.0 Universal (CC0)**.

## Código de Conducta

Ver el documento [Código de Conducta](CODE_OF_CONDUCT.md).

## Reporte de problemas

- Si encuentras errores o tienes sugerencias de mejora, puedes abrir un issue en el repositorio.
- Describe claramente el problema, incluyendo pasos para reproducirlo si aplica.

## Trabajo sobre el código o el contenido

Para los agentes tienen disponible [`AGENTS.md`](AGENTS.md).

### Creando ramas de git

Lo normal es hacer ramas bien acotadas para el trabajo planificado, pero en una metodología kayzen realmente no tienes tan claro que es lo siguiente, por eso realmente la forma simplificada es crear una rama de la siguiente forma:

```bash
git checkout -b wip/<usuario>/$(date +%Y%m%d)-short-description
```

Por ejemplo: `wip/jesus/20260416-update-docs`.

Puedes saber más al respecto en [método simplificado de crear ramas](docs/guides/pull-requests-vscode.md#flujo-simplificado-cuando-aún-no-sabes-qué-contendrá-la-rama).

Peo es posible querer hacer una rama, a si que continuación se detalla cómo hacer cambios en repositorios existentes o crear nuevos repositorios siguiendo [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow). Inspirado en **[un modelo de ramas de Git exitoso](https://nvie.com/posts/a-successful-git-branching-model/)**, se usa la siguiente convención de nombres de rama:

- **Feature branches**: para nuevas funcionalidades. Ejemplo: `feature/chapter-1-ipfs` o `feature/install-proxy`.
- **Bugfix branches**: para corregir errores. Ejemplo: `bugfix/issue-123` o `bugfix/review-inconsistent-steps`.
- **Repository documentation**: para cambios en la documentación del repositorio. Ejemplo: `docs/initial-documentation`.

  > La documentación interna del repositorio, basada en instrucciones, cuenta como una feature.

- **Experiments**: para probar ideas o experimentos que podrían no incluirse finalmente. Ejemplo: `experiment/test-alternative-installation`.

Los nombres de rama deben usar palabras clave en inglés en `kebab-case`, con las secciones separadas únicamente por `-`.

### Haciendo commits en git

Se usa [Conventional Commits](https://www.conventionalcommits.org/) para escribir los mensajes de commit en inglés. Ten en cuenta que `init` y `security` son extensiones locales a la especificación de Conventional Commits. Ejemplos:

- `init`: para el arranque de un proyecto o módulo, creando la estructura, si todavía no se ha añadido contenido real:

   ```plaintext
   init: initialize project with base structure
   ```

- `feat`: para nuevas funcionalidades:

   ```plaintext
   feat: first draft section on how to create ipfs node
   ```

   > Aunque la funcionalidad sea documentación o instrucciones, se entiende como contenido funcional.

- `refactor`: para reestructurar sin cambiar la funcionalidad:

   ```plaintext
   refactor: clarify explanation instructions module xyz
   ```

- `revert`: para revertir un cambio anterior:

   ```plaintext
   revert: revert commit 1234abcd due to causing errors
   ```

- `fix`: para especificar la corrección de un `bug`:

   ```plaintext
   fix: resolve issue 123 section xyz
   ```

- `security`: para indicar que se revisan aspectos o funcionalidades de seguridad:

   ```plaintext
   security: critical security indication for section xyz
   ```

- `docs`: cambios en la documentación del repositorio, no en el contenido en sí:

   ```plaintext
   docs: update getting started guide in README.md
   ```

- `style`: para cambios de formato que no afectan al contenido:

   ```plaintext
   style: adjust indentation in instructions
   ```

- `test`: para añadir o modificar pruebas sobre el propio contenido:

   ```plaintext
   test: add tests
   ```

   > Si parte de las instrucciones para el usuario final incluye pruebas descritas, eso sería `feat`, ya que son pruebas que ayudan a la propia creación del contenido.

- `ci`: para cambios relacionados con la entrega en GitHub:

   ```plaintext
   ci: fix GitHub Actions pipeline for deployment
   ```

- `chore`: para tareas menores o mantenimiento que no justifican otra indicación:

   ```plaintext
   chore: fix folder name
   ```

   ```plaintext
   chore: add xyz to .gitignore
   ```

**Al hacer commit**, puede que te hayas equivocado y solo quieras corregir el commit anterior; en ese caso, sigue estos pasos:

- Corregir un commit anterior y poner un mensaje nuevo (si lo quieres así):

   ```bash
   git commit --amend -m "New message"
   ```

   > Si no quieres poner un mensaje nuevo, omite `-m "New message"`

- Si ya subiste el cambio al remoto:

   ```bash
   git push origin <Branch_Name> --force-with-lease
   ```

   > Usar `--force-with-lease` es más seguro, porque verifica que nadie más haya actualizado el remoto mientras trabajabas, minimizando el riesgo de sobrescribir cambios ajenos.

**Reglas:**

- Usa el modo imperativo en la descripción ("add" en vez de "added" o "adds").
- Limita la línea de asunto a 72 caracteres.
- Separa el asunto del cuerpo con una línea en blanco.
- Referencia issues y pull requests cuando sea relevante.

### Flujo de trabajo con ramas y pull requests

Se disponen dos formas:

- [método simplificado de crear ramas](docs/guides/pull-requests-vscode.md#flujo-simplificado-cuando-aún-no-sabes-qué-contendrá-la-rama).
- [método formal de crear ramas](docs/guides/pull-requests-vscode.md#flujo-de-trabajo-con-ramas-y-pull-requests).

> Claramente se usa el método simplificado.

## Herramientas recomendadas

Recomiendo las siguientes herramientas:

1. [`vscode`](https://code.visualstudio.com/).
   > Aunque puedes usar tu editor favorito.
2. Usando `vscode` como referencia, necesitas las siguientes extensiones:
   - [`GitHub Pull Requests`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) para crear, revisar y fusionar pull requests sin salir de VS Code.
   - [`Markdown Preview Mermaid Support`](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) o cualquier otra que permita usar `Mermaid`.
   - [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) para detectar errores o malas prácticas al escribir en [markdown](https://es.wikipedia.org/wiki/Markdown).
   - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) para corregir la ortografía.

---

## Entorno ejecución

### Entorno python

> Asegúrate de estar en la carpeta kayzen-gob-dlt (si no, haz antes: cd kayzen-gob-dlt)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Para salir del entorno: `deactivate`

---
