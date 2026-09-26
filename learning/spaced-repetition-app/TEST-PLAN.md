# Plan de pruebas spaced-repetition-app

Casos de prueba de acuerdo: describen con ejemplos cómo debe comportarse la aplicación. Se validan antes de construirla y se comprueban a mano una vez construida. El detalle técnico está en [DESIGN.md](DESIGN.md).

## Datos de ejemplo

Notas de `data/cards.tsv`, en este orden:

| id | Modelo | Pregunta | Respuesta | Alternativas | Imagen |
| --- | --- | --- | --- | --- | --- |
| `dog` | 1 invertida | Dog | Perro | | sí |
| `boe` | 2 teclear | ¿Qué significa BOE? | Boletín Oficial del Estado | Boletín Oficial | sí |
| `cat` | 1 invertida | Cat | Gato | | sí |
| `onu` | 2 teclear | ¿Qué significa ONU? | Organización de las Naciones Unidas | Naciones Unidas, Organización Naciones Unidas | sí |
| `house` | 1 invertida | House | Casa | | sí |
| `paris` | 2 teclear | ¿Capital de Francia? | París | | sí |
| `tree` | 1 invertida | Tree | Árbol | | sí |
| `spain` | 2 teclear | ¿Qué país tiene por capital Madrid? | España | | sí |
| `book` | 1 invertida | Book | Libro | | no |

Salvo que se indique lo contrario, cada caso parte de estos datos y **sin** `data/progress.json`.

## Inicio y continuidad

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-01 | Primera ejecución | Ejecutar `python learning/spaced-repetition-app/run.py` | Se abre el navegador en `http://127.0.0.1:5000` con el manual de ayuda. Al pulsar "Empezar" sale la tarjeta "Dog". Todavía no existe `progress.json` |
| TC-02 | Primera puntuación | En "Dog", revelar y pulsar "Bien" | Se crea `progress.json` con `dog:forward` y el siguiente repaso para mañana. Aparece "¿Qué significa BOE?" |
| TC-03 | Continuar otro día | Día 1: puntuar "Dog" y "BOE" con "Bien" y cerrar. Día 2: ejecutar de nuevo | Salen primero "Dog" y "BOE" (vencen hoy) y después las nuevas, empezando por "Cat". No se empieza de cero |
| TC-04 | Continuar el mismo día | Puntuar "Dog" con "Bien", cerrar y volver a ejecutar | "Dog" no aparece. La primera tarjeta es "¿Qué significa BOE?" |
| TC-31 | Id duplicado | Añadir al final de `cards.tsv` otra nota con id `dog` y ejecutar | La app no arranca y muestra: `cards.tsv línea 15: id duplicado "dog" (ya usado en la línea 6)`. Con id `dog-verb` arranca con normalidad |
| TC-32 | Id con formato inválido | Añadir una nota con id `tengo una casa` y ejecutar | La app no arranca e indica la línea y que el id no cumple el formato. Lo mismo con `Dog`, `árbol` o `dog_verb` |

## Modelo 1: tarjeta invertida

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-05 | Revelar y puntuar | Ver "Dog" y pulsar "Mostrar respuesta" | Aparece "Perro" y los cuatro botones: Fallé, Me costó, Bien, Fácil |
| TC-06 | Dos direcciones | Jueves 1 oct: "Dog" → Bien. Viernes 2 oct: "Dog" → Bien. Sábado 3 oct: abrir la app | Jueves y viernes no sale "Perro", porque ese día ya se estudia "Dog". El sábado "Dog" no toca (su fecha es el lunes 5) y sale "Perro" como nueva (pregunta "Perro", respuesta "Dog"), con su propio calendario |

## Modelo 2: teclear la respuesta

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-07 | Acierto exacto | En "¿Qué significa BOE?" escribir `Boletín Oficial del Estado` | Se marca como acierto y aparecen solo tres botones: Me costó, Bien, Fácil |
| TC-08 | Tolerancia general | Escribir `boletin oficial  del estado.` con espacios al principio | Acierto: se ignoran mayúsculas, espacios sobrantes, punto final y tildes |
| TC-09 | Alternativa de la nota | Escribir `Boletin oficial` | Acierto por la alternativa `Boletín Oficial` |
| TC-10 | Letras erróneas | Escribir `Boletín Oficial del Estdo` | Fallo: se muestra lo escrito junto a `Boletín Oficial del Estado`, se registra "Fallé" sin preguntar y aparece "Continuar" |
| TC-11 | La ñ cuenta | En "¿Qué país tiene por capital Madrid?" escribir `Espana` | Fallo. `españa` sería acierto |
| TC-12 | Una sola dirección | Puntuar "¿Capital de Francia?" y volver días después | Nunca sale una tarjeta que pregunte "París" |

## Orden de la sesión

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-13 | Modelos mezclados | Primer día, puntuar todo con "Bien" | Orden: Dog, BOE, Cat, ONU, House, París, Tree, España, Book. Los dos modelos se alternan según `cards.tsv` y ninguna tarjeta inversa sale ese día |
| TC-14 | Límite de nuevas | Con 15 notas del modelo 2 sin estudiar, estudiar un día completo | Salen 10 nuevas y después "Has terminado por hoy". Las otras 5 salen al día siguiente |
| TC-15 | Vencidas primero | `progress.json` con "Cat" vencida hace 3 días y "Dog" vencida hoy | Sale "Cat", después "Dog" y después las nuevas |
| TC-16 | Fallo en sesión | Pulsar "Fallé" en "Dog" y seguir con las demás | "Dog" vuelve unos 10 minutos después, intercalada. Si antes no queda nada más, sale en ese momento |
| TC-17 | Fallo y cierre | Día 1: pulsar "Fallé" en "Dog" y cerrar enseguida. Día 2: ejecutar | "Dog" es la primera tarjeta del día 2 |
| TC-18 | Fin de sesión | Responder todas las tarjetas disponibles | Pantalla "Has terminado por hoy" con la fecha del próximo repaso |

## Calendario (SM-2)

Cómo funciona: el usuario abre la app el día que quiere. La app solo muestra las tarjetas cuya fecha de repaso ha llegado. Cada vez que se puntúa una tarjeta, la app le asigna una nueva fecha:

- Si se acierta, la fecha es cada vez más lejana, porque la tarjeta ya se recuerda. Como máximo, 21 días.
- Si se falla, la tarjeta vuelve a los 10 minutos y su calendario empieza de nuevo.

Todos los casos siguen a la tarjeta "Dog", nueva el jueves 1 de octubre de 2026.

### TC-19: aciertos seguidos

| Día en que se abre la app | ¿Sale "Dog"? | Puntuación | Próxima fecha de "Dog" |
| --- | --- | --- | --- |
| Jueves 1 oct | Sí, es nueva | Bien | Viernes 2 oct (1 día después) |
| Viernes 2 oct | Sí, le toca | Bien | Lunes 5 oct (3 días después) |
| Sábado 3 oct | No, aún no le toca | — | — |
| Lunes 5 oct | Sí, le toca | Bien | Martes 13 oct (8 días después) |
| Martes 13 oct | Sí, le toca | Fácil | Martes 3 nov (21 días después: el tope) |

Entre el 13 de octubre y el 3 de noviembre, "Dog" no sale. Durante esos días la app pregunta otras tarjetas.

### TC-34: tope de 21 días

Continúa TC-19.

| Día en que se abre la app | ¿Sale "Dog"? | Puntuación | Próxima fecha de "Dog" |
| --- | --- | --- | --- |
| Martes 3 nov | Sí, le toca | Fácil | Martes 24 nov (21 días después: el tope) |
| Martes 24 nov | Sí, le toca | Bien | Martes 15 dic (21 días después) |

Mientras se acierte, "Dog" sale cada 21 días. Nunca más tarde.

### TC-33: volver tarde

| Día en que se abre la app | ¿Sale "Dog"? | Puntuación | Próxima fecha de "Dog" |
| --- | --- | --- | --- |
| Jueves 1 oct | Sí, es nueva | Bien | Viernes 2 oct |
| Viernes 2 y sábado 3 oct | La app no se abre | — | — |
| Domingo 4 oct | Sí, con retraso, entre las primeras | Bien | Miércoles 7 oct (3 días después) |

La tarjeta no se pierde por no abrir la app el día que tocaba. Sale el primer día que se abre y el calendario sigue desde ese día.

### TC-20: fallo

| Día en que se abre la app | ¿Sale "Dog"? | Puntuación | Próxima fecha de "Dog" |
| --- | --- | --- | --- |
| Jueves 1 oct | Sí, es nueva | Bien | Viernes 2 oct |
| Viernes 2 oct | Sí, le toca | Bien | Lunes 5 oct |
| Lunes 5 oct | Sí, le toca | Fallé | Lunes 5 oct, 10 minutos después |
| Lunes 5 oct, 10 minutos después | Sí, en la misma sesión | Bien | Martes 6 oct (1 día después: vuelve a empezar) |

### TC-21 y TC-22: primera respuesta distinta de "Bien"

| ID | Jueves 1 oct, "Dog" nueva | Próxima fecha de "Dog" |
| --- | --- | --- |
| TC-21 | Fácil | Lunes 5 oct (4 días después) |
| TC-22 | Me costó | Viernes 2 oct (1 día después) |

## Progreso

El progreso se cuenta por tarjetas: los datos de ejemplo tienen 9 notas y 14 tarjetas (5 notas invertidas × 2 + 4 de teclear).

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-35 | Sin estudiar nada | Abrir "Progreso" en la primera ejecución | Buen progreso **0** · Medio **0** · No las sé **14**. "Te faltan al menos 70 respuestas (14 × 5), repartidas en unos 33 días" |
| TC-36 | A mitad de aprendizaje | `progress.json` con "Dog" en 21 días, "Cat" en 8 días (3 aciertos), "BOE" en 1 día (1 acierto) y el resto sin estudiar. Abrir "Progreso" | Buen progreso **1** · Medio **1** · No las sé **12**. "Te faltan al menos 61 respuestas" (Dog 0 + Cat 2 + BOE 4 + 11 nuevas × 5) |
| TC-37 | Sin nombres | Abrir "Progreso" | Solo aparecen cifras y barras, sin preguntas ni respuestas de tarjetas |
| TC-38 | Acceso | Desde el manual, una tarjeta o "Has terminado por hoy", pulsar "Progreso" | Se abre la pantalla de progreso. "Estudiar" vuelve al repaso |

## Ayuda

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-39 | Primera vez | Ejecutar sin `progress.json` | Se abre el manual. Explica que se estudia repartido en días, qué hace cada botón, la historia de "Dog" con el tope de 21 días, qué pasa si no se abre la app, cuándo parar, la pantalla de progreso y el estudio libre |
| TC-40 | Siguientes veces | Ejecutar con `progress.json` | Sale directamente la primera tarjeta. El enlace "Ayuda" abre el manual |

## Estudio libre

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-41 | Repasar todo | Pulsar "Estudio libre" y recorrer todas | Salen las 14 tarjetas, también las nuevas y "Perro", "Gato"…, en orden aleatorio. Siempre visible: "Estudio libre: no cuenta para tu progreso". Al final: "Has repasado 14 tarjetas" |
| TC-42 | Sin puntuación | En "Dog", revelar. En "¿Qué significa BOE?", escribir `Boletin` | Modelo 1: respuesta y botón "Siguiente", sin botones de puntuación. Modelo 2: se indica fallo, se muestra la respuesta correcta y el botón "Siguiente" |
| TC-43 | No cuenta | Anotar las cifras de "Progreso", hacer un estudio libre completo y volver a "Progreso" | Las cifras no cambian. `progress.json` no se modifica |

## Pantalla e imágenes

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-23 | Imagen de fondo | Ver "Dog" | La imagen de un perro ocupa el fondo y el texto de la tarjeta se lee bien sobre ella |
| TC-24 | Sin imagen | Ver "Book" | Fondo neutro. La tarjeta funciona igual |
| TC-25 | Descargar imagen | `python learning/spaced-repetition-app/scripts/fetch_images.py cat "cat"` | Se crea `app/static/images/cat.jpg`, la columna `image` de `cat` pasa a `cat.jpg` y `data/image-credits.md` recoge autor, licencia y URL |

## Cierre y guardado

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-26 | Ya vale por hoy | Pulsar "Ya vale por hoy" a mitad de sesión | Pantalla "Hasta mañana". El script termina y la terminal queda libre |
| TC-27 | Cierre brusco | Puntuar 3 tarjetas y cerrar la pestaña, o parar con Ctrl+C | Al volver a ejecutar, esas 3 tarjetas conservan su calendario |
| TC-28 | Progreso fuera de git | Estudiar y ejecutar `git status` | `progress.json` no aparece como cambio |
| TC-44 | Respuesta repetida | En "Dog" nueva, doble clic en "Bien". En "¿Qué significa BOE?", escribir `Boletín Oficial del Estdo` y recargar la página | "Dog" vuelve mañana (una sola puntuación, no dos). "BOE" registra un solo fallo |

## Compatibilidad con Anki

| ID | Situación | Pasos | Resultado esperado |
| --- | --- | --- | --- |
| TC-29 | Importar en Anki | En Anki, *Archivo → Importar* `data/cards.tsv` | Se crean 9 notas: 5 del tipo "Basic (and reversed card)" (10 tarjetas) y 4 del tipo "Basic (type in the answer)" |
| TC-30 | Reimportar | Cambiar "Perro" por "Perro (animal)" e importar otra vez | Se actualiza la nota `dog`. No se duplica |
