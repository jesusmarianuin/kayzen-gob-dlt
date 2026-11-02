# Glosario de términos relacionado con eIDAS

## ETSI (European Telecommunications Standards Institute)

Instituto Europeo de Normas de Telecomunicaciones, con sede en Sophia Antipolis (Francia). Es uno de los tres organismos europeos de normalización reconocidos por el Reglamento (UE) 1025/2012, junto con CEN y CENELEC. Su comité ESI (Electronic Signatures and Infrastructures) elabora las normas técnicas que desarrollan eIDAS (firmas, certificados, prestadores de servicios de confianza, listas de confianza).

Referencias:

- [Web de ETSI](https://www.etsi.org/)
- [Comité ESI de ETSI](https://www.etsi.org/committee/esi)

## CEN y CENELEC

El Comité Europeo de Normalización (CEN) y el Comité Europeo de Normalización Electrotécnica (CENELEC) son, junto con ETSI, los organismos europeos de normalización reconocidos oficialmente por la UE (Reglamento (UE) 1025/2012). Tienen su sede en Bruselas y se encargan de elaborar las normas europeas formales (EN), que posteriormente los organismos nacionales (como [UNE](https://www.une.org/) en España) adoptan como propias.

Su función principal es traducir los requisitos legales generales de la Unión Europea en especificaciones técnicas concretas. Cuando la Comisión Europea aprueba una ley, encarga a estos organismos la creación de la norma técnica correspondiente; si un sistema o servicio cumple con dicha norma, adquiere automáticamente la presunción de conformidad legal. 

Esta labor estandarizadora es clave para la infraestructura digital europea, operando a través de comités técnicos especializados en cada ámbito:

- **eIDAS y EUDI Wallet:** El comité CEN/TC 224 elabora normas como la serie EN 419, que define los requisitos de seguridad de los dispositivos de creación de firma y sello electrónico (tarjetas inteligentes, módulos criptográficos HSM y firmas en servidor). Estas especificaciones son la base técnica ineludible para certificar los esquemas de seguridad de nivel "alto" que exige la arquitectura de la EUDI Wallet y los prestadores de servicios de confianza cualificados.
- **Blockchain, EBSI e ISBE:** El comité conjunto CEN/CENELEC JTC 19 (Blockchain and Distributed Ledger Technologies) adapta los estándares internacionales de ISO al marco europeo y desarrolla normativas propias, especialmente sobre privacidad y protección de datos en redes DLT. Estos estándares son la referencia para las redes públicas permisionadas que buscan validez legal en la UE: [EBSI](#ebsi-european-blockchain-services-infrastructure), la infraestructura de la Comisión y los Estados miembros para verificar credenciales de forma transfronteriza, e ISBE (Infraestructura de Servicios Blockchain de España), la red nacional alineada con EBSI. En ambos casos, cumplirlos es lo que permite garantizar la interoperabilidad, cumplir con el RGPD y articular la integración legal con los servicios eIDAS.
- **Espacios de datos:** El comité conjunto CEN/CENELEC JTC 25 (Data management, Dataspaces, Cloud and Edge), creado en septiembre de 2024, elabora las normas que concretan los requisitos de interoperabilidad del artículo 33 del Data Act por mandato de la Comisión.

Referencias:

- [Web de CEN y CENELEC](https://www.cencenelec.eu/)
- [Creación del comité JTC 25 (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2024/brief-news/2024-09-25-jtc-25/)
- [Aceptación del mandato del Data Act (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2025/brief-news/2025-07-11-data-act-standardization-request/)

## eIDAS (electronic IDentification, Authentication and trust Services)

Reglamento (UE) relativo a la identificación electrónica, autenticación y los servicios de confianza para las transacciones electrónicas en el mercado interior (de los estados miembro como personas, bienes, servicios o capitales). Se aplica en toda la UE desde el 1 de julio de 2016.

Por una parte, permite el reconocimiento de sistemas nacionales de identificación electrónica (eID), incluyendo los procesos de autenticación asociados, notificados por los Estados miembros. Por ejemplo, DNI electrónico es reconocido como sistema de identificación electrónica.

Define que por estado miembro existen los **servicios de confianza**, que es un servicio electrónico que permite realizar determinadas operaciones relacionadas con la confianza en transacciones electrónicas y que está regulado, como puede ser la firma, sello de tiempo electrónicos (TSA), entrega electrónica certificada (ERDS o Qualified Electronic Registered Delivery Service) y certificados de autenticación de sitios web.

Un servicio de confianza, tiene un **Prestador de Servicios de Confianza** (TSP Trust Service Provider) que es la entidad que presta dichos servicios.

Los prestadores de servicios de confianza pueden obtener la categoría de **Prestadores Cualificados de Servicios de Confianza** (*Qualified Trust Service Provider*, QTSP). Para ello, deben cumplir los requisitos previstos en el Reglamento eIDAS y contar con el reconocimiento formal del órgano de supervisión competente de su país, el cual los incluye en la **lista de confianza** del Estado miembro correspondiente (*Trusted List*, TL, especificada técnicamente como *Trust Service Status List*, TSL).

A su vez, las listas de cada Estado miembro (TL/TSL) se engloban centralmente en la *List of Trusted Lists* (LOTL). Al respecto, *EUTL (EU Trusted List)* es la denominación funcional y divulgativa habitual para referirse a esta infraestructura europea, mientras que la terminología técnica oficial bajo eIDAS y los estándares ETSI utiliza la sigla **LOTL**.

Estos servicios pueden ser **servicios cualificados**, es decir, servicios que cumplen los requisitos establecidos por eIDAS para una determinada categoría y que son prestados por un prestador cualificado (QTSP).

**Aclaraciones**:

Un TSP puede prestar servicios a ciudadanos, empresas, organizaciones o administraciones públicas.

Una **firma electrónica cualificada** tiene, conforme al artículo 25 de eIDAS, un efecto jurídico equivalente al de una firma manuscrita.

"Cualificado" es un atributo que se aplica a diferentes elementos en distintos contextos. Por ejemplo, pueden ser cualificados un prestador o un servicio de confianza, un certificado electrónico o un dispositivo de creación de firma. En el caso de una firma electrónica, existen distintos niveles (simple, avanzada y cualificada), siendo la firma cualificada aquella que cumple los requisitos adicionales de eIDAS, incluyendo el uso de un certificado cualificado y un dispositivo cualificado de creación de firma.

### Referencias de eIDAS

- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)

## eIDAS2

eIDAS2 establece un nuevo marco europeo de identidad digital.

> Se puede valorar que existe un [cambio de paradigma](../idea-sandbox/decentralization-paradox-idea.md).

Su objetivo principal es evolucionar desde un sistema centrado en el reconocimiento mutuo de sistemas nacionales de identificación electrónica hacia un ecosistema europeo de identidad digital interoperable, donde los ciudadanos y organizaciones puedan utilizar una identidad digital reconocida en toda la Unión Europea.

La principal novedad es la creación de la Cartera Europea de Identidad Digital (European Digital Identity Wallet, EUDI Wallet).

### Nuevos servicios de confianza

eIDAS2 amplía la lista de servicios de confianza regulados, incorporando:

**Declaración electrónica de atributos (*Electronic Attestation of Attributes, EAA*)**:

Permite emitir y verificar atributos electrónicos sobre una persona o entidad. Un atributo es una información asociada a una identidad como edad, titulación académica, permiso profesional, condición de estudiante, etc.

La declaración electrónica de atributos permite que estos datos puedan ser utilizados de forma confiable en transacciones electrónicas. Sus tipos, efectos y requisitos se explican en la [sección dedicada](#nuevo-servicio-eidas2-declaración-electrónica-de-atributos-eaa).

**Archivo electrónico (*Electronic Archiving*)**:

Introduce el servicio de archivo electrónico cualificado. Su finalidad es garantizar la conservación de documentos electrónicos durante largos periodos asegurando: integridad, autenticidad, origen, disponibilidad.

Está orientado a conservar evidencias digitales con valor jurídico. Sus niveles y requisitos se resumen en la [sección dedicada](#nuevo-servicio-eidas2-archivo-electrónico-electronic-archiving).

**Libros mayores electrónicos (*Electronic Ledger*)**:

Introduce los libros mayores electrónicos como servicio de confianza.

Un libro mayor electrónico es una secuencia de registros de datos que garantiza su integridad y la exactitud de su orden cronológico. El reglamento no exige una tecnología concreta: puede implementarse con o sin blockchain. Sus niveles, efectos y relación con las DLT se explican en la [sección dedicada](#nuevo-servicio-eidas2-libro-mayor-electrónico-electronic-ledger).

### Plazos de aplicación de la cartera europea

- 24 de diciembre de 2026: cada Estado miembro debe poner a disposición al menos una cartera europea, y las administraciones públicas deben aceptarla como medio de identificación. Es el plazo de emisión y aceptación por el sector público, no de adopción generalizada
- 24 de diciembre de 2027: el sector privado regulado (banca, telecomunicaciones, energía, transporte, sanidad, seguros, educación e infraestructura digital) debe aceptarla cuando la normativa le exija autenticación reforzada

### Referencias de eIDAS2

- [Reglamento (UE) 910/2014 (eIDAS) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)
- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)

## Cartera Europea de Identidad Digital (EUDI Wallet)

La **Cartera Europea de Identidad Digital (EUDI Wallet)** es una aplicación digital segura y controlada por el usuario que permite **gestionar, almacenar y utilizar su identidad digital y otras credenciales electrónicas verificables** en sus interacciones con servicios públicos y privados, tanto a nivel nacional como transfronterizo dentro de la Unión Europea.

La cartera forma parte de un **ecosistema europeo de identidad digital** en el que intervienen diferentes actores, entre ellos los usuarios, los proveedores que emiten datos de identidad y credenciales electrónicas, los proveedores de la cartera y las entidades que solicitan y verifican dichas credenciales. Este ecosistema se basa en mecanismos comunes de interoperabilidad, seguridad y confianza.

Entre sus principales capacidades se encuentran:

- **Identificación y autenticación electrónica** frente a servicios públicos y privados.
- **Almacenamiento y gestión** de datos de identidad y credenciales digitales verificables.
- **Presentación de credenciales** para demostrar determinados atributos ante terceros.
- **Interoperabilidad transfronteriza**, permitiendo utilizar la identidad y las credenciales en diferentes Estados miembros.
- **Firma electrónica**, como [firma cualificada (QES)](https://www.e-signature.eu/en/eidas-2-electronic-signature/#:~:text=*%20QES%20via%20smartphone%20(software%20QSCD)%20becomes,and%20compliant%20during%20and%20after%20the%20transition.), en los casos y condiciones previstos por el marco europeo.
- **Control por parte del usuario sobre la información que comparte**, permitiendo proporcionar únicamente los datos necesarios para una determinada operación.

Las credenciales digitales pueden ser emitidas por autoridades públicas y entidades privadas para acreditar atributos de personas físicas o jurídicas, como datos de identidad, permisos de conducción, titulaciones académicas o cualificaciones profesionales. En el marco europeo de identidad digital, pueden adoptar la forma de [declaraciones electrónicas de atributos](#nuevo-servicio-eidas2-declaración-electrónica-de-atributos-eaa) cualificadas o no cualificadas, sujetas a distintos requisitos y efectos jurídicos conforme al Reglamento eIDAS. Los casos de uso incluyen el acceso a servicios públicos y privados, la apertura de cuentas bancarias, los pagos, la firma de contratos, los viajes, la educación y la seguridad social, de acuerdo con la normativa aplicable.

Un principio especialmente relevante de la EUDI Wallet es la **minimización de datos**. Por ejemplo, para demostrar que una persona cumple un requisito de edad, no necesariamente tendría que revelar su fecha de nacimiento completa: podría presentar una prueba verificable de que **es mayor de 18 años**, evitando revelar información adicional que no sea necesaria para la operación.

Por tanto, la EUDI Wallet no debe entenderse simplemente como una versión digital de un documento de identidad, sino como una **infraestructura de identidad y credenciales digitales controlada por el usuario**, diseñada para permitir que diferentes entidades puedan emitir, solicitar y verificar información digital de forma segura e interoperable en toda la Unión Europea.

Su arquitectura y requisitos técnicos se definen en el **European Digital Identity Wallet Architecture and Reference Framework (ARF)**, desarrollado en el marco del Reglamento Europeo de Identidad Digital. El ARF establece la arquitectura, los componentes, las interacciones y los mecanismos de confianza necesarios para que las diferentes implementaciones nacionales sean interoperables.

### Referencias

- [European Digital Identity Wallet — Architecture and Reference Framework](https://eudi.dev/latest/main/01-introduction/?utm_source=chatgpt.com#11-eudi-wallet-ecosystem)
- [Comisión Europea — Aplicación de la cartera de identidad digital de la UE](https://digital-strategy.ec.europa.eu/es/policies/eudi-wallet-implementation)

## Nuevo servicio eIDAS2: Declaración electrónica de atributos (EAA)

Una declaración electrónica de atributos es una manifestación electrónica firmada que acredita que un atributo de una persona física o jurídica es cierto (edad, titulación, permiso, cargo en una sociedad) sin tener que identificarla por completo. El término oficial en español es "declaración", no "atestación".

Hay tres tipos, y lo que los distingue es quién la emite:

- EAA: cualquier prestador de servicios de confianza. No se le puede negar valor como prueba solo por ser electrónica
- QEAA (cualificada): un prestador cualificado (QTSP). Equivale a una declaración en papel y se reconoce en toda la UE. Si el atributo está en el anexo VI (dirección, edad, estado civil, nacionalidad, titulaciones, permisos, datos registrales...), el prestador debe poder comprobarlo en su fuente auténtica, el registro oficial que custodia el dato
- Pub-EAA: un organismo público responsable de una fuente auténtica, o alguien en su nombre. Equivale también a la declaración en papel, y no necesita esa comprobación porque emite la propia fuente

Su régimen está en los artículos 45 ter a 45 nonies del Reglamento eIDAS modificado (45b a 45h en inglés) y en los anexos V a VII. Lo desarrollan los actos de ejecución, como el [Reglamento de Ejecución (UE) 2024/2977](#qué-publica-para-eidas), y las normas de [ETSI](#etsi-european-telecommunications-standards-institute) y [CEN](#cen-y-cenelec). En septiembre de 2026 había todavía pocos prestadores de QEAA en las listas de confianza.

Referencias:

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [Qué son las declaraciones electrónicas de atributos EAA, QEAA y Pub-EAA en eIDAS2 (inza.blog)](https://inza.blog/2026/09/20/que-son-las-declaraciones-electronicas-de-atributos-eaa-qeaa-y-las-del-sector-publico-pub-eaa-en-eidas2/)

## Nuevo servicio eIDAS2: Archivo electrónico (electronic archiving)

El archivo electrónico es un servicio que recibe, almacena, recupera y elimina datos y documentos electrónicos. Su fin es que sigan siendo legibles y conserven su integridad, su confidencialidad y la prueba de su origen durante todo el periodo de conservación (artículo 3).

Antes de eIDAS 2 ya existía un servicio parecido, pero más limitado: la conservación cualificada de firmas y sellos electrónicos cualificados (artículos 34 y 40), que mantiene verificable la firma aunque su tecnología quede obsoleta. El archivo electrónico, en cambio, cubre cualquier dato o documento, esté firmado o no.

Como en el resto de servicios de confianza, hay dos niveles:

- Archivo electrónico: un juez no puede rechazar como prueba los datos y documentos conservados solo por ser electrónicos o por no haberse conservado con un servicio cualificado
- Archivo electrónico cualificado: lo presta un prestador cualificado de servicios de confianza, y la ley presume la integridad y el origen de los datos y documentos durante todo el periodo de conservación

El servicio cualificado debe cumplir estos requisitos:

- Usar procedimientos y tecnologías que garanticen que los datos sigan siendo duraderos y legibles más allá de la vida de la tecnología que los protege, y al menos durante el periodo de conservación legal o contractual
- Proteger los datos frente a pérdidas y alteraciones. Se admiten los cambios de soporte o de formato electrónico, para poder migrar los datos cuando un formato quede obsoleto
- Entregar a las partes usuarias autorizadas, de forma automatizada, un informe que confirme que los datos recuperados mantienen la presunción de integridad desde el inicio de la conservación hasta su recuperación

Sus efectos y requisitos están en los artículos 45 decies y 45 undecies del Reglamento eIDAS modificado (45i y 45j en la versión inglesa).

Referencias:

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)

## Nuevo servicio eIDAS2: Libro mayor electrónico (electronic ledger)

Un libro mayor electrónico es un registro de datos en el que cada entrada queda en orden y no se puede modificar sin que se note. La idea es la de un libro de registro de entradas en papel, con las páginas numeradas, pero en formato digital.

eIDAS 2 (Reglamento (UE) 2024/1183) lo incorpora como un nuevo servicio de confianza, junto a la firma, el sello o el sello de tiempo. Lo define como "una secuencia de registros electrónicos de datos que garantiza la integridad de dichos registros y la exactitud de su orden cronológico" (artículo 3).

Como en el resto de servicios de confianza, hay dos niveles:

- Libro mayor electrónico: un juez no puede rechazarlo como prueba solo por ser electrónico o por no ser cualificado.
- Libro mayor electrónico cualificado: lo presta un prestador cualificado de servicios de confianza supervisado, y la ley presume que los datos son auténticos, que su fecha y su orden son exactos y que no se han alterado. Quien quiera negarlo tiene que demostrarlo.

El reglamento no menciona la tecnología: un libro mayor puede implementarse con o sin blockchain. La relación con las tecnologías de registro distribuido (DLT) se concreta en su desarrollo técnico. El Reglamento de Ejecución (UE) 2025/2531 fija las normas de referencia para los libros mayores cualificados, y uno de sus anexos se dedica a los "libros mayores electrónicos distribuidos cualificados", con definiciones de nodo, consenso, mecanismo de consenso y carácter definitivo de los registros. Ese reglamento exige a todos los libros mayores cualificados la norma ETSI EN 319 401, y a los distribuidos además ISO 23257:2022 (arquitectura DLT) e ISO/TS 23635:2022 (gobernanza).

En la práctica, esto significa que una red blockchain puede ofrecer un servicio con valor probatorio reconocido en toda la UE, siempre que la opere un prestador cualificado y cumpla esas normas. Que una red sea blockchain no le da por sí mismo esa presunción legal.

El término oficial en español es "libro mayor electrónico cualificado" (qualified electronic ledger). Sus efectos y requisitos están en los artículos 45 duodecies y 45 terdecies del Reglamento eIDAS modificado.

Referencias:

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj)

## Nuevo servicio eIDAS2: Libro mayor electrónico (Electronic Ledger)

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


### Reglamento de Ejecución (UE) 2025/2531: requisitos técnicos

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

### ¿Qué aporta en la práctica?

La incorporación de este servicio permite disponer de registros electrónicos con garantías técnicas y jurídicas armonizadas en toda la Unión Europea.

Algunos ejemplos de aplicación son:

- **Cadena de suministro:** registrar acontecimientos relacionados con la fabricación, transporte y entrega de mercancías.
- **Propiedad intelectual:** registrar evidencias de la existencia de determinados contenidos en una secuencia temporal.
- **Trazabilidad documental:** mantener un historial verificable de documentos y operaciones.
- **Transacciones empresariales:** registrar operaciones y acontecimientos entre diferentes organizaciones.
- **Auditoría:** conservar secuencias de registros cuya integridad y orden cronológico puedan verificarse posteriormente.

La principal aportación no consiste simplemente en almacenar información, sino en proporcionar garantías verificables sobre su procedencia, integridad y orden cronológico, respaldadas por una presunción jurídica cuando el servicio está cualificado.

En definitiva, eIDAS 2 permite que un libro mayor electrónico, incluida una infraestructura blockchain, pueda funcionar como un servicio de confianza cualificado y beneficiarse de un reconocimiento jurídico armonizado en la Unión Europea. La tecnología utilizada es secundaria: lo determinante es el cumplimiento de los requisitos normativos y la cualificación del servicio.

### Referencias

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj).
- [Reglamento (UE) n.º 910/2014 (eIDAS), texto consolidado](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018).
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj).
- ETSI EN 319 401 v3.1.1: requisitos generales de política y seguridad para prestadores de servicios de confianza.
- ISO 23257:2022: arquitectura de referencia para tecnologías blockchain y DLT.
- ISO/TS 23635:2022: directrices de gobernanza para tecnologías blockchain y DLT.

### EBSI (European Blockchain Services Infrastructure)

Infraestructura blockchain impulsada por la Comisión Europea y la European Blockchain Partnership (EBP). Se describe como "pública y permisionada", dos términos que responden a preguntas distintas:

- Pública: cualquiera puede leer los datos, porque los verificadores de credenciales tienen que poder consultarlos sin pedir permiso
- Permisionada: solo pueden operar nodos las entidades autorizadas, en la práctica los Estados miembros y la Comisión. Y solo escriben quienes han sido acreditados para ello, por ejemplo un emisor de confianza que registra su DID

Una persona o empresa cualquiera puede consultar EBSI, pero no puede montar un nodo propio.

Además, sigue un [modelo de gobernanza federado](blockchain.md#modelo-gobernanza-federado): ningún actor la controla en solitario. Cada Estado miembro opera sus propios nodos, y todos se someten a reglas comunes que se deciden de forma conjunta.

Su uso principal es actuar como registro de confianza para credenciales verificables (títulos académicos, identidad de entidades, documentos), además de otros casos como la notarización de documentos.

> Registro de confianza no es que sea el registro de las VC, es que es el registro o ancla. EBSI guarda los identificadores de los emisores y quién los acreditó, el [registro de emisores de confianza (Trusted Issuers Registry)](identity.md#tir-trusted-issuers-registry)

EBSI y el libro mayor electrónico de eIDAS son cosas distintas, aunque ambos usan DLT:

- El libro mayor electrónico es una categoría legal: un servicio de confianza que cualquier prestador puede ofrecer y que, si es cualificado, tiene valor probatorio reconocido
- EBSI es una infraestructura concreta, construida para guardar la información pública con la que se verifican credenciales: identificadores de emisores, sus claves públicas, emisores de confianza y estado de revocación. Es decir, cumple el rol de VDR

La condición de cualificado no depende de la tecnología, sino de quién presta el servicio y cómo: la otorga el organismo de supervisión a un prestador cualificado de servicios de confianza que cumple eIDAS y el Reglamento de Ejecución (UE) 2025/2531, y el servicio aparece en las listas de confianza. Por eso EBSI no es un libro mayor electrónico cualificado por sí misma. Podría serlo un servicio que un prestador cualificado ofreciera sobre ella. Donde más se acercan es en la notarización de documentos, que consiste precisamente en dejar constancia fechada e inalterable de unos datos.

Referencia: [EBSI (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/display/EBSI/Home)

### EDIC (European Digital Infrastructure Consortium) y Europeum

Un EDIC (Consorcio Europeo de Infraestructuras Digitales) es una entidad con personalidad jurídica propia que varios Estados miembros crean para llevar adelante juntos un proyecto digital.

EUROPEUM-EDIC es el EDIC dedicado a blockchain, constituido el 21 de mayo de 2024 con sede en Bélgica. Lo fundaron Bélgica, Croacia, Chipre, Eslovenia, Grecia, Italia, Luxemburgo, Portugal y Rumanía.

Su relación con EBSI es la de operador. EBSI nació como proyecto de la Comisión y de la European Blockchain Partnership, sin una entidad jurídica que la explotara. EUROPEUM-EDIC pasa a ser esa entidad. EBSI es la infraestructura y EUROPEUM, la organización que la gestiona.

Según la Comisión, sus funciones son:

- Operar EBSI y ponerla en producción, es decir, que funcione como servicio real y no como piloto
- Ampliarla con más nodos, más países y más servicios
- Coordinar a las administraciones públicas que trabajan con blockchain y tecnologías descentralizadas
- Promover la interoperabilidad de EBSI con otras tecnologías y con el marco europeo de identidad digital

En el día a día, esas funciones implican previsiblemente, aunque la fuente no lo detalla:

- Gobernar la red: fijar las reglas, decidir quién puede operar nodos y qué entidades pueden escribir
- Mantener el software y las especificaciones de EBSI, con equipo propio o contratando a empresas
- Dar soporte a los Estados y organismos que se conectan

Los nodos no los opera EUROPEUM, sino cada Estado miembro (ver la sección de EBSI).

Referencia: [creación del EDIC Europeum (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/news/blockchain-creation-europeum-edic)

### TIR

//TODO corrige el desastre que has hecho aqui explica que TIR es el registro de emisores de confianza para la infraestructura DID. Ve a https://inza.blog/2026/09/20/que-son-las-declaraciones-electronicas-de-atributos-eaa-qeaa-y-las-del-sector-publico-pub-eaa-en-eidas2/ revisa la gran duda, ¿que articula que u

### Redes públicas permisionadas que buscan ser institucionales

ISBE, Alastria y LACChain son redes públicas permisionadas, como EBSI. Buscan lo mismo: que lo registrado en la red tenga validez legal. Para eso los validadores tienen que ser entidades identificadas, porque un regulador solo acepta una red en la que se sabe quién responde de ella y de los datos que trata.

EBSI cubre un uso concreto: la verificación transfronteriza de credenciales, con nodos que solo operan organismos públicos. Estas redes ofrecen una infraestructura de uso general sobre la que empresas y administraciones construyen sus propias aplicaciones.

#### ISBE (Infraestructura de Servicios Blockchain de España)

Red blockchain nacional, pública e interoperable, alineada con EBSI. Es un proyecto de la Comunidad de Madrid, financiado por el Plan de Recuperación, Transformación y Resiliencia (Next Generation EU). Quien la desarrolla es la asociación Alastria, sobre Hyperledger Besu, pero ISBE es una red distinta de las de Alastria.

Su marco regulatorio es el europeo:

- eIDAS 2: está diseñada para llegar a ser un libro mayor electrónico cualificado conforme al Reglamento de Ejecución (UE) 2025/2531. Es un objetivo, no una condición ya reconocida por el organismo de supervisión
- RGPD: el cumplimiento se plantea desde el diseño, tanto en la parte técnica como en la gobernanza

Su finalidad declarada es verificar documentos e identidades con plena validez jurídica sin depender de plataformas privadas de fuera de la UE.

#### Alastria

Asociación española sin ánimo de lucro, creada en 2017, que reúne empresas, universidades y administraciones en torno a redes blockchain permisionadas. Tiene sus propias redes, independientes de ISBE. Además desarrolla ISBE para la Comunidad de Madrid, y lleva a esa red su enfoque regulatorio, centrado en eIDAS y el RGPD.

#### LACChain

Alianza liderada por el BID Lab (Banco Interamericano de Desarrollo), fundada en 2019, que opera una red pública permisionada administrada por sus miembros para América Latina y el Caribe.

No se rige por el marco europeo. Su planteamiento es que la red no sea anónima para que cada país pueda regularla y que cada gobierno la adapte a su propia normativa. Se ha usado, por ejemplo, en compras públicas en Perú y en certificados académicos.

Referencias:

- [proyecto ISBE (Alastria)](https://alastria.io/en/proyectos/isbe-blockchain-services-infrastructure-of-spain/)
- [webinar sobre ISBE como infraestructura conforme a la regulación (LF Decentralized Trust)](https://www.lfdecentralizedtrust.org/learn/webinars/webinar-with-alastria-building-isbe-europes-regulation-compliant-blockchain-infrastructure-on-besu)
- [marco de LACChain para redes públicas permisionadas (BID)](https://publications.iadb.org/en/lacchain-framework-permissioned-public-blockchain-networks-blockchain-technology-blockchain)

## DG CONNECT (Dirección General de Redes de Comunicación, Contenido y Tecnologías)

Departamento de la Comisión Europea responsable de la política digital: redes de telecomunicaciones, datos, inteligencia artificial, ciberseguridad e identidad digital, entre otros ámbitos.

Existe desde el 1 de julio de 2012, cuando la antigua DG INFSO (Sociedad de la Información y Medios) cambió de nombre para reflejar sus nuevas funciones. No la crea una norma propia: las direcciones generales son servicios internos que la Comisión organiza según su Reglamento interno, adoptado en virtud del artículo 249 del [TFUE](https://es.wikipedia.org/wiki/Tratado_de_Funcionamiento_de_la_Uni%C3%B3n_Europea).

Es la dirección general responsable de eIDAS: prepara las propuestas de reglamento, redacta los actos de ejecución y coordina con los Estados miembros el desarrollo de la cartera europea.

### Tipos de documentos que publica y dónde

DG CONNECT no publica canónicamente sino que participa en diferentes tipos de documentos de distinta naturaleza:

**Documentos de planificación estratégica (estrategias y planes)**:

- [Strategic Plans (planes estratégicos)](https://commission.europa.eu/publications/strategic-plan-2025-2029_en): documentos a cinco años que describen la contribución a los objetivos políticos.
- [Management Plans (planes de gestión)](https://commission.europa.eu/publications/management-plans-2016-2019_es): detallan las actividades y recursos anuales previstos.
- [Annual Activity Reports](https://commission.europa.eu/publications/annual-activity-reports-communication_en) (informes anuales): presentan los logros y recursos utilizados el año anterior.

**Documentos políticos y de iniciativa (comunicaciones y libros)**:

- Communications (comunicaciones): el formato oficial para presentar estrategias generales. [Ver Comunicación sobre los objetivos digitales para 2030 (Brújula Digital)](https://espanadigital.gob.es/sites/espanadigital/files/2022-06/Br%C3%BAjula%20Digital%202030.pdf)
- White Papers (libros blancos): contienen propuestas de acción comunitaria en un ámbito específico. [Ver Libro Blanco sobre Inteligencia Artificial](https://commission.europa.eu/publications/white-paper-artificial-intelligence-european-approach-excellence-and-trust_en)
- Green Papers (libros verdes): se publican para estimular la reflexión y lanzar consultas públicas. [Ver portal general de consultas públicas (Have your say)](https://ec.europa.eu/info/law/better-regulation/have-your-say_es)

**Legislación (normas)**:

- Regulations (reglamentos): normas vinculantes de aplicación directa en todos los Estados miembros. [Ver Reglamento de Servicios Digitales (DSA)](https://eur-lex.europa.eu/ES/legal-content/summary/digital-services-act.html)
- Directives (directivas): normas que establecen objetivos de obligado cumplimiento, dejando la forma legislativa a cada país. [Ver Directiva SRI 2 de ciberseguridad](https://digital-strategy.ec.europa.eu/es/policies/nis2-directive)

**Directrices, blueprints y hojas de ruta**:

- Guidelines / Recommendations (directrices): documentos no vinculantes que sugieren líneas de actuación. [Ver Recomendación sobre la ciberseguridad de las redes 5G](https://www.ceoexeuropa.es/comunicaciones/1094/)
- [Blueprints](https://employment-social-affairs.ec.europa.eu/policies-and-activities/skills-and-qualifications/working-together/blueprint-sectoral-cooperation-skills_en): no es una categoría jurídica oficial, sino un término operativo para esquemas, arquitecturas o marcos de trabajo altamente estructurados.
- Roadmaps (hojas de ruta): definen el camino a seguir para desarrollar una tecnología. [Ver Hojas de ruta estratégicas nacionales para la Década Digital](https://digital-strategy.ec.europa.eu/es/policies/national-strategic-roadmaps).

### Qué publica para eIDAS

Las piezas que publica para eIDAS son:

- Actos de ejecución: reglamentos de la Comisión que fijan requisitos técnicos y estándares, por ejemplo el 2024/2977 sobre datos de identificación personal y declaraciones electrónicas de atributos. Son obligatorios. [Ver Reglamento de Ejecución (UE) 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj)
- ARF: la arquitectura de referencia de la cartera europea. Lo elaboran la Comisión y expertos de los Estados miembros, a partir de la caja de herramientas común (toolbox) que pidió la Recomendación (UE) 2021/946. No es obligatorio. [Ver ARF](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/) y [Recomendación (UE) 2021/946](https://eur-lex.europa.eu/eli/reco/2021/946/oj)
- Implementación de referencia: código abierto que muestra cómo construir una cartera conforme al ARF y que los Estados pueden reutilizar. [Ver repositorios de la implementación de referencia](https://github.com/eu-digital-identity-wallet)
- Blueprints: soluciones completas para un caso de uso concreto, explicadas en el [apartado siguiente](#blueprint)

Si dos piezas se contradicen, manda el acto de ejecución.

### Blueprint

Un blueprint es una solución de referencia para un caso de uso concreto: especificaciones técnicas, documentación y una app en código abierto. Un Estado o una empresa la adapta, le pone su marca y la publica. No es una norma, sino una forma de cumplirla ya construida y probada.

Ejemplos:

- Blueprint de verificación de edad: publicado en julio de 2025 para que las plataformas protejan a los menores, como exige el artículo 28 de la Ley de Servicios Digitales (DSA). Permite demostrar que se es mayor de 18 años sin revelar la fecha de nacimiento. Usa las mismas especificaciones que la cartera europea, así que funciona como app independiente o integrado en una cartera nacional. La versión 2, de octubre de 2025, permite obtener la prueba de edad con pasaporte o DNI. Lo desarrolló el consorcio T-Scy (Scytáles y T-Systems) y lo prueban Dinamarca, España, Francia, Grecia e Italia
- Implementación de referencia de la cartera europea: no se llama blueprint, pero cumple la misma función para la cartera completa

> En la UE, "blueprint" también se usa con el sentido de plan de actuación, sin código detrás. Por ejemplo, la Recomendación (UE) 2017/1584, sobre la respuesta coordinada a incidentes de ciberseguridad a gran escala, se conoce como el "blueprint" de ciberseguridad.

Referencias:

- [DG CONNECT (Comisión Europea)](https://commission.europa.eu/about/departments-and-executive-agencies/communications-networks-content-and-technology_es)
- [Recomendación (UE) 2021/946 sobre la caja de herramientas común en EUR-Lex](https://eur-lex.europa.eu/eli/reco/2021/946/oj)
- [blueprint de verificación de edad (Comisión Europea)](https://digital-strategy.ec.europa.eu/en/factpages/blueprint-age-verification-solution-help-protect-minors-online)

---
