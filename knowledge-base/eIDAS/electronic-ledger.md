# Libro mayor electrónico (electronic ledger)

Un libro mayor electrónico es un registro de datos en el que cada entrada queda en orden y no se puede modificar sin que se note. La idea es la de un libro de registro de entradas en papel, con las páginas numeradas, pero en formato digital.

eIDAS 2 (Reglamento (UE) 2024/1183) lo incorpora como un nuevo servicio de confianza, junto a la firma, el sello o el sello de tiempo. Lo define como "una secuencia de registros electrónicos de datos que garantiza la integridad de dichos registros y la exactitud de su orden cronológico" (artículo 3).

Como en el resto de servicios de confianza, hay dos niveles:

- Libro mayor electrónico: un juez no puede rechazarlo como prueba solo por ser electrónico o por no ser cualificado.
- Libro mayor electrónico cualificado: lo presta un prestador cualificado de servicios de confianza supervisado, y la ley presume que los datos son auténticos, que su fecha y su orden son exactos y que no se han alterado. Quien quiera negarlo tiene que demostrarlo.

El reglamento no menciona la tecnología: un libro mayor puede implementarse con o sin blockchain. La relación con las tecnologías de registro distribuido (DLT) se concreta en su desarrollo técnico. El Reglamento de Ejecución (UE) 2025/2531 fija las normas de referencia para los libros mayores cualificados, y uno de sus anexos se dedica a los "libros mayores electrónicos distribuidos cualificados", con definiciones de nodo, consenso, mecanismo de consenso y carácter definitivo de los registros. Ese reglamento exige a todos los libros mayores cualificados la norma ETSI EN 319 401, y a los distribuidos además ISO 23257:2022 (arquitectura DLT) e ISO/TS 23635:2022 (gobernanza).

En la práctica, esto significa que una red blockchain puede ofrecer un servicio con valor probatorio reconocido en toda la UE, siempre que la opere un prestador cualificado y cumpla esas normas. Que una red sea blockchain no le da por sí mismo esa presunción legal.

Por ejemplo, [EBSI](ebsi.md) es una infraestructura concreta para verificar credenciales y no es por sí misma un libro mayor electrónico cualificado.

ISBE, en cambio, una de las [redes públicas permisionadas que buscan ser institucionales](permissioned-public-networks.md), está diseñada para llegar a serlo, aunque es un objetivo y no una condición ya reconocida por el organismo de supervisión.

El término oficial en español es "libro mayor electrónico cualificado" (qualified electronic ledger). Sus efectos y requisitos están en los artículos 45 duodecies y 45 terdecies del Reglamento eIDAS modificado.

Referencias:

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj)

## Efectos jurídicos e implementación

Un libro mayor electrónico (electronic ledger) es un registro digital en el que los datos se incorporan siguiendo una secuencia cronológica y se utilizan mecanismos que permiten garantizar su integridad y detectar cualquier modificación posterior.

Podemos entenderlo como la evolución digital de un libro de registro tradicional: cada anotación queda incorporada a una secuencia ordenada y debe poder verificarse que no ha sido manipulada. La diferencia es que, en lugar de depender de páginas numeradas o mecanismos físicos de custodia, utiliza técnicas criptográficas para proteger los registros y acreditar su posición dentro de la secuencia.

Como sucede con otros servicios de confianza, eIDAS distingue entre el libro mayor electrónico y el libro mayor electrónico cualificado. La diferencia fundamental está en los requisitos que deben cumplir y en los efectos jurídicos que se les reconocen.

- Libro mayor electrónico: no puede denegarse su efecto jurídico ni su admisibilidad como prueba en procedimientos judiciales por el mero hecho de estar en formato electrónico o de no cumplir los requisitos de un libro mayor cualificado. Esto no significa que cualquier registro tenga automáticamente valor probatorio suficiente: su fiabilidad y fuerza probatoria se valorarán atendiendo a las circunstancias del caso.

- Libro mayor electrónico cualificado: debe cumplir los requisitos específicos del artículo 45 terdecies y estar creado y gestionado por uno o varios prestadores cualificados de servicios de confianza (QTSP). Sus registros gozan de una presunción jurídica de unicidad y exactitud de su orden cronológico secuencial y de integridad.

Esta presunción tiene una consecuencia importante: quien cuestione la integridad de los registros o su orden cronológico deberá aportar elementos para rebatirla. No obstante, no significa que el contenido registrado sea necesariamente verdadero. Por ejemplo, si una empresa registra que ha entregado una mercancía, el libro mayor puede acreditar la integridad y la posición cronológica de ese registro, pero no demuestra por sí mismo que la entrega se haya producido realmente.

También conviene distinguir dos conceptos: **la procedencia de un registro y la veracidad de su contenido**. El libro mayor cualificado debe establecer el origen de los datos, pero eso no equivale a garantizar que la información aportada por su autor sea cierta.

Los efectos jurídicos de ambas modalidades se encuentran en el artículo 45 duodecies del Reglamento eIDAS.

**Implementación del libro mayor**:

El Reglamento eIDAS no obliga a utilizar blockchain para implementar un libro mayor electrónico. Puede construirse mediante una arquitectura centralizada o distribuida, siempre que se cumplan los requisitos establecidos.

La relación con las tecnologías de registro distribuido (DLT) se concreta en el Reglamento de Ejecución (UE) 2025/2531, que contempla expresamente los libros mayores electrónicos distribuidos cualificados y establece especificaciones técnicas adicionales para ellos.

Un libro mayor distribuido es aquel que se comparte entre diferentes nodos y mantiene sus registros sincronizados mediante un mecanismo de consenso.

El Reglamento introduce varios conceptos específicos:

- **Nodo:** dispositivo o proceso que forma parte de la red y almacena una copia completa o parcial de los registros.
- **Red distribuida:** conjunto de nodos que forman el sistema de registro distribuido.
- **Consenso:** acuerdo entre los nodos sobre la validez de las transacciones y el mantenimiento de un conjunto coherente y ordenado de transacciones validadas.
- **Mecanismo de consenso:** conjunto de reglas y procedimientos mediante los cuales se alcanza ese acuerdo.
- **Carácter definitivo (finality):** estado de un registro que se ha vuelto irreversible y no puede modificarse ni suprimirse.

Este último concepto es especialmente relevante. En una red distribuida no basta con que una transacción haya sido aceptada por un nodo: debe existir un mecanismo que permita determinar cuándo alcanza el carácter definitivo y puede considerarse incorporada de forma irreversible al libro mayor.

Para estos sistemas de libro mayor, el Reglamento 2025/2531 incorpora dos referencias técnicas adicionales:

- **ISO 23257:2022:** arquitectura de referencia para tecnologías blockchain y de registros distribuidos.
- **ISO/TS 23635:2022:** directrices de gobernanza para tecnologías blockchain y de registros distribuidos.

## Reglamento de Ejecución (UE) 2025/2531: requisitos técnicos

El Reglamento de Ejecución (UE) 2025/2531 desarrolla las normas y especificaciones de referencia para los libros mayores electrónicos cualificados. Su objetivo es concretar cómo deben garantizarse técnicamente la procedencia, la integridad y el orden cronológico de los registros.

Establece como referencia general la norma **ETSI EN 319 401 v3.1.1**, relativa a los requisitos generales de política y seguridad de los prestadores de servicios de confianza, con adaptaciones específicas para este servicio.

Entre otras cuestiones, concreta los mecanismos utilizados para:

- Autenticar el origen de los registros mediante firmas electrónicas avanzadas o sellos electrónicos avanzados basados en certificados cualificados, creados por los usuarios del servicio.
- Garantizar la secuencia cronológica mediante vínculos criptográficos basados en listas o árboles hash, utilizando funciones hash SHA-256 o superiores, o SHA3-256 o superiores.
- Garantizar la integridad de los registros mediante firmas electrónicas avanzadas o sellos electrónicos avanzados basados en certificados cualificados.
- Detectar inmediatamente cualquier modificación posterior de los datos.
- Proteger las claves criptográficas utilizadas por el prestador.

También contempla la utilización de sellos de tiempo cualificados como alternativa para garantizar la unicidad del orden cronológico secuencial.

En el caso de los libros mayores distribuidos, se añaden las especificaciones relacionadas con la arquitectura DLT, la gobernanza de la red y los mecanismos de consenso.

El Reglamento exige, además, que el prestador documente los mecanismos técnicos utilizados en su declaración de prácticas del servicio. De esta forma, los usuarios y las partes que confían en él pueden conocer cómo se garantiza la procedencia, la integridad y la ordenación de los registros.

## ¿Qué aporta en la práctica?

La incorporación de este servicio permite disponer de registros electrónicos con garantías técnicas y jurídicas armonizadas en toda la Unión Europea.

Algunos ejemplos de aplicación son:

- Cadena de suministro: registrar acontecimientos relacionados con la fabricación, transporte y entrega de mercancías.
- Propiedad intelectual: registrar evidencias de la existencia de determinados contenidos en una secuencia temporal.
- Trazabilidad documental: mantener un historial verificable de documentos y operaciones.
- Transacciones empresariales: registrar operaciones y acontecimientos entre diferentes organizaciones.
- Auditoría: conservar secuencias de registros cuya integridad y orden cronológico puedan verificarse posteriormente.

La principal aportación no consiste simplemente en almacenar información, sino en proporcionar garantías verificables sobre su procedencia, integridad y orden cronológico, respaldadas por una presunción jurídica cuando el servicio está cualificado.

En definitiva, eIDAS 2 permite que un libro mayor electrónico, incluida una infraestructura blockchain, pueda funcionar como un servicio de confianza cualificado y beneficiarse de un reconocimiento jurídico armonizado en la Unión Europea. La tecnología utilizada es secundaria: lo determinante es el cumplimiento de los requisitos normativos y la cualificación del servicio.

## Referencias

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj).
- [Reglamento (UE) n.º 910/2014 (eIDAS), texto consolidado](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018).
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj).
- ETSI EN 319 401 v3.1.1: requisitos generales de política y seguridad para prestadores de servicios de confianza.
- ISO 23257:2022: arquitectura de referencia para tecnologías blockchain y DLT.
- ISO/TS 23635:2022: directrices de gobernanza para tecnologías blockchain y DLT.
