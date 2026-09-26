# Gestión de pull requests desde VS Code

Esta guía explica cómo crear, revisar y fusionar pull requests (PR) sin salir de VS Code, usando la extensión [`GitHub Pull Requests`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github).

Los nombres de botones y paneles se muestran tal como aparecen en la interfaz de la extensión, en inglés.

## Requisitos previos

- [VS Code](https://code.visualstudio.com/) instalado.
- Extensión [`GitHub Pull Requests`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) instalada.
- El repositorio (o tu fork) clonado en local y una rama con los cambios que quieres proponer.
- La opción **Allow squash merging** habilitada en la configuración del repositorio en GitHub (**Settings → General → Pull Requests**). Sin ella, el método **Squash and Merge** no aparece.

## Parte 1 — Autor: trabaja en su rama

### Flujo de trabajo con ramas y pull requests

> Cuando no se elige usar el simplificado.

Aunque trabajo en solitario, mantengo el flujo de ramas y pull requests (contra mí mismo) porque me obliga a revisar el trabajo antes de fusionarlo a `main`:

1. Crea una rama nueva para tu cambio siguiendo la metodología Git Flow. Ejemplo:

```bash
git checkout -b feature/feature-name
```

2. Recuerda traer periódicamente los cambios de la rama `main` usando `rebase`:

- Traer los cambios de main:

```bash
git fetch origin main
```

- Hacer un `rebase` sobre la rama local:

   ```bash
   git rebase main
   ```

- Resolver conflictos (si los hay): si hay conflictos, resuélvelos y continúa:

   ```bash
   git add <resolved_file>
   git rebase --continue
   ```

3. Haz commit de tu trabajo periódicamente, con cada actividad significativa.

   > **Tip**: si usas VS Code, el panel de control de código fuente muestra un botón ✨ para generar mensajes de commit automáticamente.

4. Sube los cambios a tu rama remota y comprueba desde ahí que todo está correcto. Las cosas a menudo se ven diferentes si te tomas el tiempo de revisar las instrucciones como si fueras el usuario final.

5. Asegúrate de hacer un `git rebase -i` sobre tu rama para:

- Fusionar commits pequeños o relacionados (`squash`).
- Reescribir los mensajes de commit para que sean claros y descriptivos.

6. Abre un `pull request` hacia la rama `main`:

- Asegúrate de que los cambios estén bien documentados y formateados con claridad.
- Da una descripción clara de los cambios en el pull request.
- Referencia cualquier fuente externa si aplica.

   > **Tip**: si usas VS Code con la extensión [`GitHub Pull Requests`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github), puedes crear, revisar y fusionar pull requests directamente desde el editor, sin necesidad de abrir el navegador.

### Flujo simplificado: cuando aún no sabes qué contendrá la rama

Con **Squash and Merge**, los mensajes de los commits de tu rama no llegan a `main`: todos se combinan en un único commit cuyo título, por defecto, es el título de la PR, y que puedes editar en el momento de fusionar. Esto permite trabajar sin decidir de antemano el nombre de la rama ni cuidar cada mensaje de commit.

1. **Crear una rama temporal** con tu usuario, la fecha y una descripción breve en inglés, en minúsculas y separada por guiones:

   ```bash
   git checkout -b wip/<usuario>/$(date +%Y%m%d)-short-description
   ```

   Por ejemplo: `wip/jesus/20260416-update-docs`.

2. **Hacer commits libremente** mientras trabajas: la calidad de los mensajes no importa aquí, porque se combinarán en uno.

3. **Subir la rama** al remoto cuando esté lista.

4. **Crear la PR** y usar el botón ✨ para que Copilot sugiera el título. Ese título será el mensaje del único commit que llegue a `main`.

5. **Fusionar con Squash and Merge**: revisa y edita el mensaje del commit si hace falta y confirma.

El nombre de la rama y los commits intermedios desaparecen tras la fusión. En `main` solo queda el commit resultante, con el título de la PR.

## Parte 3 — Autor: abrir la pull request

Estos pasos los realiza la persona que ha hecho los cambios y quiere que se revisen.

1. **Iniciar sesión en GitHub**: abre el menú **Accounts** (abajo a la izquierda de VS Code) e inicia sesión con tu cuenta de GitHub si aún no lo has hecho.

2. **Subir la rama al remoto**: asegúrate de que la rama está publicada y actualizada en el repositorio remoto. Desde el panel **Source Control** puedes usar **Publish Branch** la primera vez y **Sync Changes** en las siguientes.

3. **Crear la pull request**: en el panel **GitHub Pull Requests** (Activity Bar, a la izquierda), pulsa **Create Pull Request**. Se abre un formulario dentro de VS Code.

4. **Completar los datos**: indica la rama destino (`main`), escribe un título y una descripción, y pulsa **Create**.

   > **Consejo**: pulsa el botón ✨ junto al campo del título para que GitHub Copilot sugiera uno. La sugerencia seguirá la convención Conventional Commits configurada en `.vscode/settings.json`.
   >
   > El campo de descripción se rellenará con la plantilla del proyecto, `.github/pull_request_template.md`, una vez que esté fusionada en `main`.

## Parte 3 — Revisor: revisar la pull request

Estos pasos los realiza la persona responsable de aprobar los cambios.

5. **Abrir la PR**: en el panel **GitHub Pull Requests**, localiza la PR y haz clic en ella. La vista de la PR se abre en el editor.

6. **Revisar los cambios**: en el panel **CHANGES IN PULL REQUEST**, haz clic en cualquier fichero para abrir su diff e inspeccionar los cambios. Marcarlos como vistos (**Viewed**) es opcional y solo sirve para llevar la cuenta de lo revisado.

   Si quieres comentar una línea concreta, pasa el ratón sobre el margen del diff y pulsa el icono **+** que aparece.

7. **Enviar la revisión**: en el panel **REVIEW PULL REQUEST** (a la izquierda, debajo de la lista de ficheros), escribe un comentario si lo necesitas y elige el resultado de la revisión:

   - **Approve**: aprueba los cambios. Es lo que habilita al autor para fusionar la PR.
   - **Request Changes**: pide correcciones antes de fusionar. El autor sube nuevos commits a la misma rama y la PR se actualiza sola.
   - **Comment**: deja observaciones sin aprobar ni bloquear.

## Parte 4 — Autor: fusionar y limpiar

Una vez aprobada la PR, el autor la fusiona.

8. **Fusionar la pull request**: se puede hacer desde dos sitios:

   - **Panel izquierdo** (REVIEW PULL REQUEST): pulsa la flecha del desplegable junto a **Create Merge Commit**, selecciona **Squash and Merge** y pulsa **Merge Pull Request**.
   - **Panel derecho** (desplazándote hacia abajo): localiza la sección **Merge Pull Request**, cambia el método a **Squash and Merge** y pulsa **Merge Pull Request**.

   En ambos casos aparece un paso de confirmación en el que puedes revisar y editar el mensaje y la descripción del commit. Cuando esté listo, pulsa **Squash and Merge** para confirmar. El resultado es un único commit en `main`.

9. **Limpiar**: tras la fusión, pulsa **Delete Branch...** en la parte inferior del panel izquierdo de la vista **GitHub Pull Requests**. Ofrecerá borrar tanto la rama local como la remota: confirma ambas. Después, actualiza tu `main` local:

   ```bash
   git checkout main
   git pull origin main
   ```

---
