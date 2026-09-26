# Estándares generales de código del proyecto

## Documentación en Markdown

Normas para cualquier fichero `.md` de documentación del proyecto.

### Idioma

- Escribe las explicaciones en español
- Mantén en inglés los términos técnicos de uso habitual en el sector (por ejemplo, "smart contract", "blockchain", "stack"), y úsalos siempre igual
- Los nombres de ficheros y carpetas van en inglés y en kebab-case (por ejemplo, `smart-contracts-guide.md`)

### Formato

- No uses negrita
- Respeta la jerarquía de encabezados (`#`, `##`, `###`, `####`) y deja una línea en blanco después de cada uno
- Deja una línea en blanco entre un texto introductorio y la lista que le sigue
- Usa guiones para las listas
- No uses tabulaciones en ningún sitio
- Los bloques de código no van sangrados, llevan identificador de lenguaje (`bash`, `json`, `solidity`...) y van rodeados de líneas en blanco
- Cumple las reglas de markdownlint

### Estructura según el tipo de documento

- Guías de instalación: explica qué hace cada herramienta antes de instalarla, da comandos para Ubuntu y añade un comando de verificación de versión tras cada instalación
- Buenas prácticas: explica el porqué de cada recomendación, céntrate en sus implicaciones de seguridad, acompáñala de código concreto y cita los estándares oficiales (ERC-20, ERC-721...) cuando apliquen
- Añade una sección de resolución de problemas cuando haya fallos habituales

### Ejemplos de código

- Indica dónde se ejecuta cada comando o fragmento
- Incluye la ruta del fichero cuando muestres configuración
- Da secuencias de comandos completas y ajustadas al stack del proyecto
- Indica la versión de una herramienta cuando el procedimiento dependa de ella

### Enlaces

- Usa rutas relativas para enlazar documentación interna
- Enlaza a documentación oficial antes que a tutoriales de terceros
- Escribe el texto del enlace en español aunque el destino esté en inglés

### Mantenimiento

- Si un cambio afecta a una herramienta o a la estructura del proyecto, actualiza la documentación relacionada en la misma tarea
- Marca las prácticas obsoletas e indica cómo migrar

## Convenciones de nombres

- Usa PascalCase para nombres de componentes, interfaces y alias de tipos
- Usa camelCase para variables, funciones y métodos
- Usa kebab-case para nombres de archivos de texto y documentación, carpetas y ramas
- Los archivos y carpetas de código siguen la convención de su lenguaje, para que se puedan importar (por ejemplo, snake_case en Python: `answer_checker.py`)
- Antepón un guion bajo (_) a los miembros privados de una clase
- Usa ALL_CAPS para las constantes
- Todos los nombres de archivo, clase, método y tipo deben estar en inglés, aunque los comentarios pueden estar en español

## Guía de mensajes de commit

Todos los mensajes de commit deben seguir la especificación [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). Esto garantiza claridad y consistencia en el historial del proyecto.

**Tipos:**

- feat: una nueva funcionalidad
- fix: una corrección de error
- docs: cambios solo en documentación
- style: cambios que no afectan al significado del código (espacios en blanco, formato, punto y coma, etc.)
- refactor: un cambio de código que ni corrige un error ni añade una funcionalidad
- perf: un cambio de código que mejora el rendimiento
- test: añadir pruebas que faltaban o corregir pruebas existentes
- build: cambios que afectan al sistema de build o a dependencias externas
- ci: cambios en los archivos y scripts de configuración de CI
- chore: otros cambios que no modifican archivos de código o de pruebas
- revert: revierte un commit anterior

**Ejemplos:**

```plaintest
feat(auth): add login functionality

fix(api): handle null response from server

docs: update README with setup instructions
```

**Reglas:**

- Usa el modo imperativo en la descripción ("add" en vez de "added" o "adds").
- Limita la línea de asunto a 72 caracteres.
- Solo asunto, como los ejemplos, sin cuerpo.
- Referencia issues y pull requests cuando sea relevante.

## Convención de nombres de rama

Sigue la metodología Git Flow con estos tipos de rama:

- **Feature branches**: para nuevas funcionalidades. Ejemplo: `feature/chapter-1-ipfs` o `feature/install-proxy`
- **Bugfix branches**: para corregir errores. Ejemplo: `bugfix/issue-123` o `bugfix/review-inconsistent-steps`
- **Documentation branches**: para cambios en la documentación del repositorio. Ejemplo: `docs/initial-documentation`
- **Experiment branches**: para probar ideas que podrían no incluirse finalmente. Ejemplo: `experiment/test-alternative-installation`

Los nombres de rama deben usar palabras clave en inglés en `kebab-case`, con las secciones separadas únicamente por `-`.

## Operativa respecto a git

Una tarea solicitada nunca puede contener operaciones git. Ni para añadir o hacer commit o traer o subir porque es algo exclusivo del propietario del repositorio, nunca podrá ser ejecutado o gestionado por un agente de IA.

## Asistencia en operaciones git

No puedes hacer realizar operaciones git, pero puedes asistir cuando se pida, en la petición se indicará algo como "ayúdame con git".

A continuación se crea un resumen para asistir:

### Autor: iniciar rama de trabajo simplificada

Las ramas para simplificar se crean de forma simplificada de la siguiente forma:

```bash
git checkout -b wip/<usuario>/$(date +%Y%m%d)-short-description
```

Por ejemplo: `wip/jesus/20260416-update-docs`.

Cuando pidan crear una rama, pregunta el usuario de git, pregunta sobre los cambios realizados y asiste con las instrucciones que el usuario debe lanzar en terminal.

### Autor: realizar commits

Cuando el usuario pida instrucciones para crear el commit, pregunta más o menos sobre los cambios realizados, pero en este caso, si puedes hacer un status de git, diciendo al usuario que realize un "git add ." para que puedas proponer un mensaje de commit coherente.

## Contexto del prompt frente a contenido del documento

- Lo que el usuario te cuenta en el prompt es contexto para que decidas bien. No es
  contenido del documento.
- Ese contexto se usa para elegir, priorizar y descartar. Se refleja en la decisión,
  nunca en el texto que escribes.
- No trasladar al documento las circunstancias personales del usuario, sus dudas, su
  forma de trabajar ni el motivo por el que pide algo, aunque lo haya explicado y
  aunque justifique la decisión. Se reformula como criterio objetivo o se omite.
- El documento solo contiene lo que necesita quien lo lea sin haber visto la
  conversación.
- Tampoco se vuelca en el documento el razonamiento que has seguido para decidir. Va
  la decisión y lo que la sostiene desde el propio material, no el recorrido.
- Si dudas de si algo es contexto o contenido, pregunta antes de escribirlo.

## Lectura de contexto del repositorio

- Solo puedes leer los ficheros que el usuario comparta en el prompt o cuya ruta aparezca
  explícitamente en él.
- Cualquier otra lectura está prohibida, incluido el intento, y con independencia de que
  fuera a ser aprobada.
- Nada es implícito. Si el prompt no comparte el fichero ni da su ruta, no existe.
- Si falta información, pregunta. Nunca la busques.

---
