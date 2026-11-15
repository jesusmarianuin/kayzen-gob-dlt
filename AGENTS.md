# Estándares generales de código del proyecto

## Lectura de contexto del repositorio

- Solo puedes leer los ficheros o directorios que el usuario comparta en el prompt o cuya ruta aparezca explícitamente en él (el fichero abierto en el editor cuenta como compartido). Se puede compartir una ruta de archivo o una ruta de directorio lo que implícitamente es también autorizar a sus ficheros contenidos.
- Cualquier otra lectura está prohibida, incluido el intento, y con independencia de que fuera a ser aprobada.
- Siempre tienes acceso completo a la carpeta de skills ".claude"
- Si falta información, pregunta. Nunca la busques.

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
- No usar tablas, prefiere usar listas o texto.
- Cumple las reglas de markdownlint

### Redacción

El lenguaje expresado debe ser natural, técnico cuando es necesario, con ejemplos simples si ayudan a entender el concepto, orientado a un nivel promedio de desarrollador de software.

### Síntesis y nivel de detalle

Antes de escribir, fija la idea central del documento y la de cada sección. Si tienes duda pregunta para que quede claro el objetivo del documento y el perfil del lector.

### Ejemplos de código

Sólo pon ejemplos de código cuando tenga sentido, una documentación conceptual no debería tenerlo, solo puede distraer, en cualquier caso, si tienes duda pregunta.

### Enlaces

- Usa rutas relativas para enlazar documentación interna
- Enlaza a documentación oficial antes que a tutoriales de terceros
- Escribe el texto del enlace en español aunque el destino esté en inglés

### Contexto del prompt frente a contenido del documento

Lo que el usuario te cuenta en el prompt es contexto para que decidas bien. No es contenido del documento. Siempre son documentos educativos para terceros, por lo tanto, el documento siempre tiene que servir para la perspectiva del lector, en conclusión: ninguna circusntancia o debate o análisis previo que se hable en el chat cuando se plantea el promtp debe quedar reflejado en el documento.

## Lenguaje de programación

- Sigue la convención de nombres estándar de cada lenguaje (PEP 8 en Python, la habitual en TypeScript...)
- Los nombres de archivo, clase, método, variable y tipo van en inglés; los comentarios pueden ir en español
- Python 3.x, dependencias con <uv/pip>, formato y lint según `<ruta de configuración>`
- No añadas dependencias nuevas sin preguntar
- Tests solo cuando se pidan

## Código fuente (git)

### Convención de nombres de rama

Sigue la metodología Git Flow con estos tipos de rama:

- **Feature branches**: para nuevas funcionalidades. Ejemplo: `feature/chapter-1-ipfs` o `feature/install-proxy`
- **Bugfix branches**: para corregir errores. Ejemplo: `bugfix/issue-123` o `bugfix/review-inconsistent-steps`
- **Documentation branches**: para cambios en la documentación del repositorio. Ejemplo: `docs/initial-documentation`
- **Experiment branches**: para probar ideas que podrían no incluirse finalmente. Ejemplo: `experiment/test-alternative-installation`

Los nombres de rama deben usar palabras clave en inglés en `kebab-case`, con las secciones separadas únicamente por `-`.

### Guía de mensajes de commit

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

### Asistencia en operaciones git

Una tarea solicitada nunca puede contener operaciones git. Ni para añadir o hacer commit o traer o subir porque es algo exclusivo del propietario del repositorio, nunca podrá ser ejecutado o gestionado por un agente de IA.

No puedes hacer realizar operaciones git, pero puedes asistir cuando se pida, en la petición se indicará algo como "ayúdame con git".

A continuación se crea un resumen para asistir:

#### Autor: iniciar rama de trabajo simplificada

Las ramas para simplificar se crean de forma simplificada de la siguiente forma:

```bash
git checkout -b wip/<usuario>/$(date +%Y%m%d)-short-description
```

Por ejemplo: `wip/jesus/20260416-update-docs`.

Cuando pidan crear una rama, pregunta el usuario de git, pregunta sobre los cambios realizados y asiste con las instrucciones que el usuario debe lanzar en terminal.

#### Autor: realizar commits

Cuando el usuario pida instrucciones para crear el commit, pregunta más o menos sobre los cambios realizados, pero en este caso, si puedes hacer un status de git, diciendo al usuario que realize un "git add ." para que puedas proponer un mensaje de commit coherente.

---
