# datos.gob.es

Noticia: <https://administracionelectronica.gob.es/pae_Home/pae_Actualidad/pae_Noticias/2026/Julio/noticia-2026-07-27-Datos-abiertos-preparados-para-la-IA-buenas-practicas-para-publicadores.html>

Partiendo de las conclusiones del ejercicio práctico [Análisis de precios de carburantes con GenAI como copiloto](https://datos.gob.es/es/conocimiento/analisis-de-precios-de-carburantes-con-genai-como-copiloto), el artículo repasa qué deben tener en cuenta los publicadores de datos abiertos ahora que modelos de IA y agentes autónomos consultan catálogos, interpretan columnas y cruzan fuentes sin intervención humana. Propone organizar las buenas prácticas en tres dimensiones: formatos y mecanismos de acceso, contexto semántico y privacidad.

En cuanto a formatos, recomienda priorizar CSV, JSON o [Parquet](https://datos.gob.es/es/blog/por-que-deberias-de-usar-ficheros-parquet-si-procesas-muchos-datos) frente a los ficheros Excel sobre-formateados, que generan "ruido" para los modelos. A nivel de acceso, defiende combinar API REST bien documentadas —que permiten a los modelos hacer "Function Calling" y protocolos emergentes como MCP— con la descarga masiva (bulk download), especialmente necesaria para los conjuntos de [datos de alto valor](https://datos.gob.es/sites/default/files/blog/file/conjunto-datos-alto-valor-es.pdf), y con mecanismos de descarga incremental o delta que reducen la carga sobre los servidores del publicador.

Sobre el contexto semántico, subraya que un modelo no puede inferir por sí solo el significado de una columna: cada conjunto de datos debería ir acompañado de un [diccionario de datos](https://datos.gob.es/es/blog/que-es-un-diccionario-de-datos-y-por-que-es-importante) explícito, ya sea mediante JSON Schema, ficheros sidecar de metadatos siguiendo el estándar CSV on the Web, o aprovechando el esquema integrado de Parquet, además de usar nombres de columna semánticos y consistentes entre conjuntos de datos.

En materia de privacidad, el artículo insiste en que la eliminación o el enmascaramiento de datos de carácter personal no es una recomendación sino una obligación previa a la publicación, y advierte del riesgo de subir información sensible a modelos comerciales que pueden reutilizarla para su reentrenamiento; la respuesta pasa por una [gobernanza](https://datos.gob.es/es/blog/recomendaciones-para-abordar-la-gobernanza-de-los-datos) clara sobre qué información puede procesarse con IA y en qué condiciones.

En una frase: preparar los datos abiertos para la IA y los agentes autónomos exige formatos limpios combinados con API, descarga masiva e incremental, contexto semántico explícito mediante diccionarios de datos, y un filtro de privacidad y gobernanza aplicado siempre en origen.

---
