# Especificación spaced-repetition-app

## Concepto

### Qué es la repetición espaciada

Una técnica para memorizar con tarjetas de pregunta y respuesta.

En lugar de repasarlo todo cada día, cada tarjeta se repasa justo antes de que se te olvide. Lo que recuerdas bien vuelve cada vez más tarde; lo que fallas vuelve pronto. Así el tiempo de estudio se gasta en lo que todavía no sabes.

### Cómo es un repaso

1. Ves la pregunta.
2. Intentas recordar la respuesta.
3. Ves la respuesta y dices cómo te ha ido: fallé, me costó, bien o fácil.
4. Según lo que digas, la tarjeta vuelve en unos minutos (si fallaste) o dentro de días o semanas (si acertaste). Como máximo, una tarjeta vuelve a los 21 días, aunque se sepa muy bien.

Cada tarjeta lleva su propio calendario, independiente de las demás.

El estudio se reparte en días: una tarjeta acertada no vuelve a salir el mismo día. Si no se abre la aplicación el día que tocaba, la tarjeta no se pierde: sale con retraso la siguiente vez.

### Modelos de tarjeta

Existen los siguientes modelos:

Básico: Ves el frente de la tarjeta (Ej: Dog), piensas mentalmente la respuesta ("Perro"), revelas el reverso y evalúas tu propia memoria indicando si te ha costado recordarlo o no.

Básico con tarjeta invertida: Introduces un dato una sola vez y el sistema genera dos tarjetas independientes para estudiar en ambas direcciones. Un día te preguntará Dog (piensas "Perro") y otro día te preguntará Perro (piensas "Dog").

Básico de teclear la respuesta: ves la pregunta acompañada de un cuadro de texto en blanco. Debes escribir la respuesta con el teclado. Al revelar la solución, el programa compara lo que escribiste con la respuesta correcta.

Huecos (Cloze): Introduces una frase completa y ocultas los fragmentos que quieras memorizar. De la frase "La capital de Francia es París", creas una tarjeta que muestra "La capital de [...] es París". El contexto siempre está visible.

### Modelos elegidos

Son 2 modelos elegidos.

Para temas conceptuales complejos, el modelo es: Básico con tarjeta invertida.
De esta forma me evalúo a mí mismo sin complejidad técnica, y además para evitar memorizar lo hago en 2 direcciones.

Pero hay muchas veces en temas de términos y vocabulario que necesito precisión, no solo entender la idea, por eso para esos casos elijo: Básico teclear la respuesta, porque saber en concreto unas iniciales o nombre propio es necesario también.

En el modelo 1 puntuar es fácil, ves la respuesta y pulsas uno de los cuatro botones (fallé, me costó, bien, fácil).

En el modelo 2 la app compara lo que escribiste y decide en parte, si fallas, cuenta como "fallé" sin preguntar. Si aciertas, solo eliges entre me costó, bien o fácil, porque lo rápido que respondiste solo lo sabes tú.

Al comparar se toleran diferencias de forma: mayúsculas, espacios sobrantes, un punto final y tildes. La ñ sí cuenta. Cada tarjeta puede tener además respuestas alternativas que también se aceptan.

## Casos de uso

Para desambiguar la solución se enumeran casos de uso que la aplicación debe recoger:

### Usuario inicia aplicación

Usuario ejecuta script, se abre el navegador e inicia las pruebas. Se entiende es un usuario único, el contexto es que es un repositorio personal o como mucho el que se baja el repo y ejecuta es una única persona, no existe complejidad multi-usuario.

El usuario continua su progreso de preguntas, es decir, no inicia el set de preguntas de cera cada vez, el programa le recuerda donde estaba según su progreso de aprendizaje espaciado o si es la primera vez, claro inicia por primera vez.

### Tarjetas de diferentes tipos

Hemos visto que hay 2 modelos elegidos: básico con tarjeta invertida y básico para teclear la respuesta. Simplemente el set de preguntas que se le muestra serán ambas, la duda es ¿primero de un tipo y luego otro o entremezcladas? Lo mejor es dejar eso al proceso de creación de la base de datos de preguntas, es decir, existirá tarjeta 1, luego 2, 3.. cada tarjeta en su creación será de tipo 1 o 2 según fue creada. Pero sabemos que no es tan simple, porque qué se pregunta en un sistema de repetición espaciada se basa en formular las preguntas según sea necesario en lo aprendido, pero para el programa simplemente, a groso modo, evalúa tarjeta 1, ve que se sabe, la omite y va a tarjeta 2, etc. Y tarjeta 1 podría ser de tipo 1 y tarjeta 2 de tipo 2 y tarjeta 3 de tipo 1 otra vez..

## Usuario accede y responde en tarjeta

Tiene una pantalla bonita, que pueda ver la tarjeta que puede ser de tipo 1 o 2, la imagen de fondo y los botones de evaluar. Si es tipo 2 debe esperar completar la respuesta. Claro cuando quiera acabar la sesión tendrá un botón "ya vale por hoy" para cerrar todo. De todas formas el progreso en base de datos se debe guardar en cada acción del navegador, no sea que lo cierre en cualquier momento.

### Usuario consulta su progreso

Desde cualquier pantalla puede abrir una pantalla de progreso que resume, sin decir qué tarjetas son, cuántas tiene con buen progreso, cuántas a medias y cuántas no sabe. También indica cuántas respuestas y cuántos días faltan como mínimo para acabar de aprenderlas todas. Así sabe si le queda trabajo por delante.

### Usuario consulta la ayuda

La aplicación incluye un manual de ayuda que explica cómo trabajar con ella: qué hace cada botón, por qué el estudio se reparte en días, qué pasa si no se abre la aplicación durante un tiempo, cuándo se puede parar y cómo leer el progreso. Se abre solo la primera vez que se usa la aplicación y después está siempre accesible.

### Usuario hace estudio libre

Puede repasar todas las tarjetas cuando quiera, por ejemplo antes de un examen, sin que esas respuestas cuenten para el calendario ni para el progreso.

## Solución técnica

A nivel técnico:

Será una solución standalone python que se ejecuta al bajarse este repo de github, donde CONTRIBUTING.md ayuda a iniciar el entorno y la ejecución de un script inicia un navegador de la app web con framework flask.

La base de datos que será un simple archivo de base de datos, formato json o el que se vea necesario, con los campos necesarios con pregunta, respuesta en su caso (o respuestas para dar versatilidad a errores gramaticales). A modo debug, esta base de datos se inicia con preguntas básicas de ejemplo para depurar la creación de la aplicación.

Como bonus, y para hacer una aplicación menos aburrida, a cada tarjeta se le puede asociar una imagen de fondo. Pero iniciar esta información, aunque no objeto del diseño, si debe considerar que sea fácil obtener, si existe un recurso en línea donde se pueda buscar un concepto y te de una imagen, entonces este bonus se pude cumplir, sino descartar. La prueba de fuego será al crear los datos de prueba, se deberá hacer usando este recurso en línea.

Como bonus 2: que el formato de texto de la base de datos sea compatible con Anki para trasladarlo si fuera el caso a dicho programa, será bien visto, solo si no aporta excesiva complejidad técnica.

## Entregables necesarios previos a la construcción

Previo a la constrcción para validar la solución aportada por el constructor, En esta carpeta `learning/spaced-repetition-app` existirán según la norma y los estándares correctos en estructura de carpeta y buenas prácticas la estructura de carpetas, archivos, scripts sin contenido como esbozo de la solución a aplicar, si es posible inicialmente con comentarios de lo que se espera en cada uno.

Debe existir correspondiente archivos README.md básico, pero no recargado ni verborrea, solo un resumen, ejemplos para iniciar y ejecutar el programa y lo que los estándares definen para este documento pero sin sobre-cargar, solo lo básico. Esto sirve para validar previamente la forma de ejecución y de alguna forma, sirve para verificar que ha entendido el constructor que es necesario.

Igualmente se espera un DESIGN.md esquemático que sirva para resumir la solución técnica, no recargado, conciso pero preciso.

Como documento y como documento de acuerdo, existirá un TEST-PLAN.md con un documento que recoja a modo de ejemplo una lista de casos de prueba simple que contemplen todos los casos de uso que se abordan en la aplicación, siempre orientado a ejemplos simples representativos reales.

---
