---
name: review-comments-selected-text
description: Revisa el texto seleccionado y lo corrige según los comentarios indicados entre corchetes con "//todo:". Usar cuando se pida resolver, aplicar o revisar comentarios "//todo:" de un documento.
---

# Revisar comentarios del texto seleccionado

Te seleccionaré un texto del documento y el objetivo es que revises los comentarios como si fueran prompts que te estoy haciendo sobre el texto seleccionado.

Para saber qué es un comentario, es muy explícito, está entre corchetes y tiene un "//todo:", por ejemplo: "[//todo: no se entiende la explicación anterior]".

En muchos casos te marco un texto y es solo ese texto el que quiero que revises, pero a veces puedo ser confuso y el comentario hacer referencia a todo un apartado o subapartado o al documento. En ese caso, haz caso al comentario, no solo afecta al texto seleccionado.

## Permisos de lectura

Invocar esta skill autoriza a leer completo el documento que contiene el texto seleccionado.

Cualquier otra lectura sigue las normas de AGENTS.md: si falta información, pregunta.

## Comportamiento general

Como pasa con los prompts, los comentarios pueden ser peticiones explícitas y ahí simplemente se hace la tarea concreta, sin interpretaciones, y como cualquier prompt si hay dudas se pregunta. Pero el comentario, aparte de la tarea, puede incluir una frase o afirmar un hecho, es decir, incluir un borrador del resultado esperado. En ese caso puede tener errores que debes corregir en base a tu criterio, pero ojo, aunque el borrador pueda tener errores, la tarea no se interpreta, se acata.

Tiendes mucho a realizar cambios cosméticos de redacción, a corregir el texto respondiendo a la pregunta planteada o a usar tu criterio respecto a la tarea ignorando lo solicitado, y ese enfoque es erróneo. Ahora vamos a aclarar esto:

- Si el comentario a revisar es una queja de que cierto texto no se entiende, quiero que evites cambios cosméticos. Debes reescribir el texto seleccionado y, si hace falta y así lo dice el comentario, reescribir el apartado completo que está siendo criticado. Por supuesto, todo manteniendo el hilo narrativo del documento.
- Si el comentario refleja una duda o pregunta, no respondas a la pregunta, sino que reescribe el texto seleccionado para que el lector entienda lo que se está explicando y no tenga dudas.
- No estás autorizado a realizar una tarea diferente a la solicitada. Es decir, si al hacer la tarea ves un texto escrito con anterioridad, aunque esté seleccionado, si no es objeto del comentario no se modifica nunca, aunque pienses que está mal; como mucho se te permite comentar otros errores al finalizar la tarea. El comentario puede ser un borrador y en ese caso, claro que debes revisar el texto del borrador, pero si la tarea pide algo concreto se acata, no se interpreta; igualmente puedes comentar después el error.

## Revisar coherencia después de corregir un comentario

Una vez repasado el o los comentarios, debes volver a leer el documento completo para asegurarte de que lo que has añadido tiene coherencia narrativa con el resto del documento. Si no es así, debes corregir el texto que has añadido y como mucho hacer retoques cosméticos en el resto del documento para que tenga coherencia narrativa, pero nunca modificar el texto que no es objeto del comentario.

Recuerda que cuando propongas un texto que corrige lo que indica el comentario, también debes eliminar el comentario para dejar el apartado limpio.

## Fallos comunes que cometes y que debes evitar

Aunque está explícito en las instrucciones, estos son fallos u olvidos comunes que sueles cometer y a los que debes prestar atención:

- Debes crear un texto que sea coherente con el documento, con el apartado marcado o con el apartado anterior, por lo tanto, no olvides que tienes que leer el documento. Si no quieres leerlo todo, por lo menos lee el texto anterior. Es buena idea que, cuando tengas el texto elegido, leas el texto anterior que no ha sido modificado y, si no tiene coherencia narrativa, lo corrijas.
- Si te hago revisar varios comentarios, cuando completes uno, no olvides volver a leer el documento entero para que el siguiente comentario que revises tenga coherencia narrativa con el documento completo.
- No olvides que el comentario pide algo concreto, eso no te da derecho a realizar otras correcciones que veas oportunas que no son objeto del comentario; como mucho puedes hacer comentarios al final de la tarea.
