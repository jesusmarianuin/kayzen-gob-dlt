# Gestión de pull requests desde VS Code

Esta guía explica cómo crear, revisar y fusionar pull requests (PR) sin salir de VS Code, usando la extensión [`GitHub Pull Requests`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github).

Los nombres de botones y paneles se muestran tal como aparecen en la interfaz de la extensión, en inglés.

## Requisitos previos

- [VS Code](https://code.visualstudio.com/) instalado.
- Extensión [`GitHub Pull Requests`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) instalada.
- El repositorio (o tu fork) clonado en local y una rama con los cambios que quieres proponer.
- La opción **Allow squash merging** habilitada en la configuración del repositorio en GitHub (**Settings → General → Pull Requests**). Sin ella, el método **Squash and Merge** no aparece.

## Parte 1 — Autor: abrir la pull request

Estos pasos los realiza la persona que ha hecho los cambios y quiere que se revisen.

1. **Iniciar sesión en GitHub**: abre el menú **Accounts** (abajo a la izquierda de VS Code) e inicia sesión con tu cuenta de GitHub si aún no lo has hecho.

2. **Subir la rama al remoto**: asegúrate de que la rama está publicada y actualizada en el repositorio remoto. Desde el panel **Source Control** puedes usar **Publish Branch** la primera vez y **Sync Changes** en las siguientes.

3. **Crear la pull request**: en el panel **GitHub Pull Requests** (Activity Bar, a la izquierda), pulsa **Create Pull Request**. Se abre un formulario dentro de VS Code.

4. **Completar los datos**: indica la rama destino (`main`), escribe un título y una descripción, y pulsa **Create**.

   > **Consejo**: pulsa el botón ✨ junto al campo del título para que GitHub Copilot sugiera uno. La sugerencia seguirá la convención Conventional Commits configurada en `.vscode/settings.json`.
   >
   > El campo de descripción se rellenará con la plantilla del proyecto, `.github/pull_request_template.md`, una vez que esté fusionada en `main`.

## Parte 2 — Revisor: revisar la pull request

Estos pasos los realiza la persona responsable de aprobar los cambios.

5. **Abrir la PR**: en el panel **GitHub Pull Requests**, localiza la PR y haz clic en ella. La vista de la PR se abre en el editor.

   El panel REVIEW PULL REQUEST (a la izquierda) solo aparece cuando VS Code está en la rama de la PR. El autor ya está en ella porque la creó. Otro revisor tiene que pulsar Checkout en la vista de la PR, lo que ejecuta `git checkout` a esa rama en su ordenador.

6. **Revisar los cambios**: en el panel **CHANGES IN PULL REQUEST**, haz clic en cualquier fichero para abrir su diff e inspeccionar los cambios. Marcarlos como vistos (**Viewed**) es opcional y solo sirve para llevar la cuenta de lo revisado.

   Si quieres comentar una línea concreta, pasa el ratón sobre el margen del diff y pulsa el icono **+** que aparece.

7. **Enviar la revisión**: en el panel REVIEW PULL REQUEST (a la izquierda, debajo de la lista de ficheros) aparece una caja de texto para escribir un comentario. Los botones que la acompañan dependen de quién revise:

   - Si revisas tu propia PR, solo aparece Comment. GitHub no permite al autor aprobar ni pedir cambios en su propia PR. Debajo aparecen ya los controles de fusión (Create Merge Commit y su desplegable), descritos en la parte 4.
   - Si la revisa otra persona con permisos en el repositorio, puede elegir Approve (aprueba los cambios), Request Changes (pide correcciones; el autor sube nuevos commits a la misma rama y la PR se actualiza sola) o Comment (deja observaciones sin aprobar ni bloquear).

   La aprobación solo es obligatoria para fusionar si la rama `main` tiene una regla de protección que exige revisiones. Sin esa regla, la PR se puede fusionar sin aprobación.

## Parte 3 — Mantenedor: fusionar y limpiar

La fusiona una persona con permiso de escritura en el repositorio, normalmente quien la ha revisado. Si el autor también tiene ese permiso, puede fusionarla él mismo una vez aprobada.

8. **Fusionar la pull request**: antes de fusionar hay que elegir el método:

   - Create Merge Commit: los commits de la rama pasan a `main` tal cual, más un commit adicional que une ambas ramas. Los mensajes provisionales de la rama quedan en el historial de `main`.
   - Squash and Merge: los commits de la rama se combinan en un único commit nuevo en `main`, cuyo mensaje por defecto es el título de la PR. Es el método de este proyecto.

   La fusión se puede hacer desde dos sitios:

   - Panel izquierdo (REVIEW PULL REQUEST): pulsa la flecha del desplegable junto a `Create Merge Commit` y `selecciona Squash and Merge`. El botón pasa a llamarse `Squash and Merge`; al pulsarlo, la PR se fusiona directamente, sin opción de editar el mensaje del commit, que será el título de la PR.
   - Vista de la PR en el editor (desplazándote hacia abajo): localiza la sección `Merge Pull Request`, cambia el método a `Squash and Merge` y pulsa el botón. Aparece un paso de confirmación en el que puedes editar el título y la descripción del commit antes de confirmar.

   Usa el panel izquierdo si el título de la PR ya es un mensaje de commit válido, y la vista de la PR si quieres retocarlo.

9. **Limpiar**: tras la fusión, pulsa **Delete Branch...** en la parte inferior del panel izquierdo de la vista **GitHub Pull Requests**. Ofrecerá borrar tanto la rama local como la remota: confirma ambas. Después, actualiza tu `main` local:

   ```bash
   git checkout main
   git pull origin main
   ```

   El botón Checkout: `main` del panel izquierdo ejecuta `git checkout main`: saca a VS Code de la rama de la PR y lo lleva a `main`. No fusiona la PR; eso solo lo hace Squash and Merge. Tampoco trae la fusión desde GitHub a tu ordenador, por eso después hace falta `git pull origin main`.

## Resolución de problemas

### Aviso "You have uncommitted changes on this pull request branch" al fusionar

Aparece al pulsar Squash and Merge si en tu copia local de la rama de la PR hay cambios sin commit. La fusión se hace en GitHub con lo que ya está subido, así que esos cambios no entran en la PR.

- Si deben formar parte de la PR: cancela, haz commit de los cambios, súbelos con `git push`, espera a que la PR muestre el nuevo commit y vuelve a pulsar Squash and Merge.
- Si van a ir en otra PR: continúa con la fusión. Los cambios locales se conservan.

---
