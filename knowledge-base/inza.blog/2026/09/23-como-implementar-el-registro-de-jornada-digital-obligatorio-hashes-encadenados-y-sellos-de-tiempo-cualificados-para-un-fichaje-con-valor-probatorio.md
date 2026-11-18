# Cómo implementar el registro de jornada digital: hashes encadenados y sellos de tiempo cualificados para un fichaje con valor probatorio

Post: <https://inza.blog/2026/09/23/como-implementar-el-registro-de-jornada-digital-obligatorio-hashes-encadenados-y-sellos-de-tiempo-cualificados-para-un-fichaje-con-valor-probatorio/>

Fecha: 2026-09-23

El borrador de real decreto de registro de jornada, de octubre de 2025, exige un registro digital objetivo, fiable y accesible, con un contenido mínimo amplio, modificaciones que dejen huella y autoría, conservación durante cuatro años y acceso remoto de la Inspección. El Consejo de Estado emitió un dictamen desfavorable el 23 de marzo de 2026, entre otras razones por el rango normativo, el coste y la protección de datos, y la tramitación se retomó en septiembre. El borrador no impone ninguna técnica concreta.

La propuesta del autor es un diario append-only:

- Cada asiento se canonicaliza y se calcula hash1(n); después, hash2(n) = H(hash2(n-1) || hash1(n)), de modo que cualquier cambio rompe la cadena
- Las correcciones se añaden como asientos nuevos, nunca se reescriben
- Al cierre del día, el último hash2 recibe un sello de tiempo cualificado (RFC 3161 / ETSI EN 319 422), que según el artículo 41.2 de eIDAS presume la fecha y la integridad, pero no la hora de cada fichaje
- Un informe mensual sellado se deposita en un archivo electrónico ([EADTrust](https://www.eadtrust.eu))

El autor llama RJT (Replicated Journal Technology) a este diario replicado e incluye una lista de verificación del borrador.

En una frase: hashes encadenados y un sello cualificado diario dan al registro de jornada una integridad demostrable.

---
