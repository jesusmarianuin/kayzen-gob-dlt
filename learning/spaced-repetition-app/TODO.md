# Pendientes spaced-repetition-app

Temas abiertos para próximas sesiones. Cuando uno se resuelva, se marca y, si cambia el diseño, se refleja en [DESIGN.md](DESIGN.md) y [TEST-PLAN.md](TEST-PLAN.md).

## Por comprobar

- [ ] **Importación en Anki (TC-29, TC-30).** No se ha probado. Es la parte del diseño con más incertidumbre: si Anki no acepta las columnas `alternatives` e `image`, hay que ajustar la cabecera o el formato de `cards.tsv`.
- [ ] **Paso de días real.** Los casos que dependen del calendario (TC-03, TC-06, TC-16, TC-17, TC-19 a TC-22, TC-33, TC-34) solo se han comprobado con fechas simuladas. Falta confirmarlos con el uso diario.
- [ ] **Revisión manual en el navegador** de todos los casos de TEST-PLAN.md. Las pruebas automáticas cubren la lógica y las respuestas del servidor, pero no los clics.

## Limitaciones conocidas

- [ ] **Error en `cards.tsv` con la app abierta.** Si se deja un error en el fichero con la app en marcha, aparece una página de error genérica. El mensaje con la línea solo sale al volver a arrancar. Poco probable; no se arregla por ahora.
- [ ] **Estimación de "días que faltan".** No tiene en cuenta que las dos direcciones de una tarjeta invertida no salen el mismo día, así que el número real puede ser algo mayor.
- [ ] **Manual de ayuda automático.** Se abre mientras no exista `progress.json`. Si se cierra la app sin puntuar ninguna tarjeta, vuelve a abrirse en el siguiente arranque.
- [ ] **Anki no recibe todo.** Al importar, se pierden las respuestas alternativas, las imágenes y el progreso.

## Evoluciones de diseño

- [ ] **FSRS en lugar de SM-2.** Motivos del descarte y alcance del cambio en DESIGN.md, "Alternativa descartada: FSRS".
- [ ] **Ignorar palabras de enlace** (`de`, `del`, `la`, `las`, `el`, `los`, `y`) al comparar la respuesta tecleada. Ahora esas variantes se escriben como alternativas en cada nota (por ejemplo, `Organización Naciones Unidas`).
- [ ] **Campo `strict` por nota**, para que las tildes cuenten cuando cambian el significado (`papa` / `papá`).

## Ideas sin decidir

- [ ] **Tarjetas atrasadas en la pantalla de progreso.** Mostrar cuántas tarjetas se debieron repasar y no se hizo, y los días desde la última sesión, para saber de un vistazo si hay trabajo acumulado tras una ausencia.
- [ ] **Aviso al salir con tarjetas pendientes.** Si se pulsa "Ya vale por hoy" con tarjetas por repasar, indicar cuántas quedan ("Te dejas 4 repasos y 3 nuevas").
- [ ] **Recordatorio con la app cerrada.** La app no puede avisar mientras no está en marcha. Haría falta algo externo (por ejemplo, una tarea programada del sistema o un evento de calendario).

## Documentación

- [ ] **Diagrama Mermaid de DESIGN.md.** En la vista previa de VS Code se dibuja y desaparece al momento. Falta saber si es cosa del entorno (otra extensión de vista previa) o del diagrama (el `<br/>` de uno de los nodos).
