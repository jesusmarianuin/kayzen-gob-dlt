# Libro mayor electrónico (electronic ledger)

Un libro mayor electrónico (electronic ledger) es un registro digital en el que los datos se incorporan siguiendo una secuencia cronológica y se utilizan mecanismos que permiten garantizar su integridad y detectar cualquier modificación posterior.

Podemos entenderlo como la evolución digital de un libro de registro tradicional: cada anotación queda incorporada a una secuencia ordenada y debe poder verificarse que no ha sido manipulada. La diferencia es que, en lugar de depender de páginas numeradas o mecanismos físicos de custodia, utiliza técnicas criptográficas para proteger los registros y acreditar su posición dentro de la secuencia.

Como sucede con otros servicios de confianza, eIDAS distingue entre el libro mayor electrónico y el libro mayor electrónico cualificado. La diferencia fundamental está en los requisitos que deben cumplir y en los efectos jurídicos que se les reconocen.

- Libro mayor electrónico: no puede denegarse su efecto jurídico ni su admisibilidad como prueba en procedimientos judiciales por el mero hecho de estar en formato electrónico o de no cumplir los requisitos de un libro mayor cualificado. Esto no significa que cualquier registro tenga automáticamente valor probatorio suficiente: su fiabilidad y fuerza probatoria se valorarán atendiendo a las circunstancias del caso.

- Libro mayor electrónico cualificado: debe cumplir los requisitos específicos del artículo 45 terdecies y estar creado y gestionado por uno o varios prestadores cualificados de servicios de confianza (QTSP). Sus registros gozan de una presunción jurídica de unicidad y exactitud de su orden cronológico secuencial y de integridad.

Esta presunción tiene una consecuencia importante: quien cuestione la integridad de los registros o su orden cronológico deberá aportar elementos para rebatirla. No obstante, no significa que el contenido registrado sea necesariamente verdadero. Por ejemplo, si una empresa registra que ha entregado una mercancía, el libro mayor puede acreditar la integridad y la posición cronológica de ese registro, pero no demuestra por sí mismo que la entrega se haya producido realmente.

También conviene distinguir dos conceptos: **la procedencia de un registro y la veracidad de su contenido**. El libro mayor cualificado debe establecer el origen de los datos, pero eso no equivale a garantizar que la información aportada por su autor sea cierta.

Los efectos jurídicos de ambas modalidades se encuentran en el artículo 45 duodecies del Reglamento eIDAS.

## Reglamento de Ejecución (UE) 2025/2531: requisitos técnicos

El [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj) fija las normas de referencia de los libros mayores electrónicos cualificados y concreta cómo garantizar técnicamente la procedencia, la integridad y el orden cronológico de los registros. Se adoptó el 16 de diciembre de 2025, tras una [consulta pública](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14752-Qualified-electronic-ledgers_en) en septiembre, y se publicó en el DOUE al día siguiente.

Los requisitos se dividen entre los comunes a cualquier prestador cualificado y los propios del libro mayor electrónico.

Para un prestador cualificado en general, como el servicio lo presta un QTSP, la referencia es la norma [ETSI EN 319 401 v3.1.1](https://www.etsi.org/deliver/etsi_en/319400_319499/319401/), con los requisitos generales de política y seguridad de los prestadores y adaptaciones para este servicio. Le aplican además los actos horizontales de los servicios de confianza cualificados:

- [Reglamento de Ejecución (UE) 2025/2530](https://eur-lex.europa.eu/eli/reg_impl/2025/2530/oj): requisitos de cumplimiento y seguridad de los prestadores cualificados.
- [Reglamento de Ejecución (UE) 2025/1572](https://eur-lex.europa.eu/eli/reg_impl/2025/1572/oj): inicio de la prestación de servicios de confianza cualificados.
- [Reglamento de Ejecución (UE) 2025/2162](https://eur-lex.europa.eu/eli/reg_impl/2025/2162/oj): acreditación de los organismos de evaluación de la conformidad; su anexo II reúne las normas con las que se evalúa cada servicio cualificado.

Para el libro mayor electrónico, el reglamento concreta, entre otras cuestiones, los mecanismos para:

- Autenticar el origen de los registros con firmas o sellos electrónicos avanzados basados en certificados cualificados, creados por los usuarios del servicio.
- Garantizar la secuencia cronológica con vínculos criptográficos basados en listas o árboles hash (SHA-256 o superior, o SHA3-256 o superior). También admite sellos de tiempo cualificados como alternativa para garantizar la unicidad de ese orden.
- Garantizar la integridad con firmas o sellos electrónicos avanzados basados en certificados cualificados.
- Detectar inmediatamente cualquier modificación posterior de los datos.
- Proteger las claves criptográficas del prestador.

El prestador debe además documentar estos mecanismos en la declaración de prácticas del servicio, para que usuarios y partes que confían en él sepan cómo se garantizan la procedencia, la integridad y la ordenación de los registros.

En los [libros mayores distribuidos](#libro-mayor-electrónico-distribuido-cualificado-qdlt) se añaden especificaciones sobre la arquitectura DLT, la gobernanza de la red y los mecanismos de consenso.

[CEN](standardization-bodies.md#cen-y-cenelec) ha publicado también la especificación técnica [CEN/TS 18264:2026](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/issues/646) sobre libros mayores electrónicos, posterior al reglamento y no citada en él.

## Libro mayor electrónico distribuido cualificado (qDLT)

El Reglamento eIDAS no obliga a utilizar blockchain para implementar un libro mayor electrónico. Puede construirse mediante una arquitectura centralizada o distribuida, siempre que se cumplan los requisitos establecidos.

Cuando es distribuido, el libro mayor se comparte entre diferentes nodos que mantienen sus registros sincronizados mediante un mecanismo de consenso. El [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj) llama a esta variante "libro mayor electrónico distribuido cualificado", también conocida como qDLT, y le añade especificaciones técnicas propias.

El reglamento introduce varios conceptos específicos:

- Nodo: dispositivo o proceso que forma parte de la red y almacena una copia completa o parcial de los registros.
- Red distribuida: conjunto de nodos que forman el sistema de registro distribuido.
- Consenso: acuerdo entre los nodos sobre la validez de las transacciones y el mantenimiento de un conjunto coherente y ordenado de transacciones validadas.
- Mecanismo de consenso: conjunto de reglas y procedimientos mediante los cuales se alcanza ese acuerdo.
- Carácter definitivo (finality): estado de un registro que se ha vuelto irreversible y no puede modificarse ni suprimirse.

Este último concepto es especialmente relevante. En una red distribuida no basta con que una transacción haya sido aceptada por un nodo: debe existir un mecanismo que permita determinar cuándo alcanza el carácter definitivo y puede considerarse incorporada de forma irreversible al libro mayor.

Para la arquitectura y la gobernanza de la red, el reglamento incorpora dos referencias técnicas adicionales:

- [ISO 23257:2022](https://www.iso.org/standard/75093.html): arquitectura de referencia para tecnologías blockchain y de registros distribuidos.
- [ISO/TS 23635:2022](https://www.iso.org/standard/76480.html): directrices de gobernanza para tecnologías blockchain y de registros distribuidos.

## ¿Qué aporta en la práctica?

La incorporación de este servicio permite disponer de registros electrónicos con garantías técnicas y jurídicas armonizadas en toda la Unión Europea.

Algunos ejemplos de aplicación son:

- Cadena de suministro: registrar acontecimientos relacionados con la fabricación, transporte y entrega de mercancías.
- Propiedad intelectual: registrar evidencias de la existencia de determinados contenidos en una secuencia temporal.
- Trazabilidad documental: mantener un historial verificable de documentos y operaciones.
- Transacciones empresariales: registrar operaciones y acontecimientos entre diferentes organizaciones.
- Auditoría: conservar secuencias de registros cuya integridad y orden cronológico puedan verificarse posteriormente.

La principal aportación no consiste simplemente en almacenar información, sino en proporcionar garantías verificables sobre su procedencia, integridad y orden cronológico, respaldadas por una presunción jurídica cuando el servicio está cualificado.

En definitiva, eIDAS2 permite que un libro mayor electrónico, incluida una infraestructura blockchain, pueda funcionar como un servicio de confianza cualificado y beneficiarse de un reconocimiento jurídico armonizado en la Unión Europea. La tecnología utilizada es secundaria: lo determinante es el cumplimiento de los requisitos normativos y la cualificación del servicio.

## Referencias

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj).
- [Reglamento (UE) n.º 910/2014 (eIDAS), texto consolidado](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018).
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj).
- [ETSI EN 319 401](https://www.etsi.org/deliver/etsi_en/319400_319499/319401/): requisitos generales de política y seguridad para prestadores de servicios de confianza.
- [ISO 23257:2022](https://www.iso.org/standard/75093.html): arquitectura de referencia para tecnologías blockchain y DLT.
- [ISO/TS 23635:2022](https://www.iso.org/standard/76480.html): directrices de gobernanza para tecnologías blockchain y DLT.
- [De la conservación cualificada de firmas y sellos a los servicios cualificados de archivo con orden cronológico (qDLT)](../inza.blog/2026/09/18-de-la-conservacion-cualificada-de-firmas-y-sellos-a-los-servicios-cualificados-de-archivo-con-orden-cronologico-qdlt.md)
- [De las tablillas cuneiformes al Cartulario: historia de la contabilidad y origen de las RJT](../inza.blog/2026/10/23-de-las-tablillas-cuneiformes-al-cartulario-historia-de-la-contabilidad-y-origen-de-las-rjt.md)
