# Glosario de términos

//todo: faltan referencias

## eIDAS (electronic IDentification, Authentication and trust Services)

Reglamento (UE) relativo a la identificación electrónica, autenticación y los servicios de confianza para las transacciones electrónicas en el mercado interior (de los estados miembro como personas, bienes, servicios o capitales). Se aplica en toda la UE desde el 1 de julio de 2016.

Por una parte, permite el reconocimiento de sistemas nacionales de identificación electrónica (eID), incluyendo los procesos de autenticación asociados, notificados por los Estados miembros. Por ejemplo, DNI electrónico es reconocido como sistema de identificación electrónica.

Define que existen los **servicios de confianza**, que es un servicio electrónico que permite realizar determinadas operaciones relacionadas con la confianza en transacciones electrónicas y que está regulado, como puede ser la firma, sello y sello de tiempo electrónicos, entrega electrónica certificada y certificados de autenticación de sitios web.

Un servicio de confianza, tiene un **Prestador de Servicios de Confianza** (TSP Trust Service Provider) que es la entidad que presta dichos servicios.

Los prestadores de servicios de confianza pueden ser **Prestador cualificado de servicios de confianza** (*Qualified Trust Service Provider*, QTSP), que es un prestador que cumple los requisitos establecidos por eIDAS y que ha sido reconocidos por el organismo de supervisión correspondiente incluyéndolo en la **lista de confianza** (TL Trusted List).

Los prestadores de servicios de confianza pueden ser **Prestadores cualificados de servicios de confianza** (*Qualified Trust Service Provider*, QTSP), que son prestadores que cumplen los requisitos establecidos por eIDAS y han sido reconocidos como cualificados por el organismo de supervisión correspondiente, figurando como tales en la **lista de confianza** (*Trusted List*, TL) del Estado miembro correspondiente.

Los prestadores de servicios de confianza pueden obtener la categoría de **Prestadores Cualificados de Servicios de Confianza** (*Qualified Trust Service Provider*, QTSP). Para ello, deben cumplir los requisitos previstos en el Reglamento eIDAS y contar con el reconocimiento formal del órgano de supervisión competente de su país, el cual los incluye en la **lista de confianza** del Estado miembro correspondiente (*Trusted List*, TL, especificada técnicamente como *Trust Service Status List*, TSL).

A su vez, las listas de cada Estado miembro (TL/TSL) se engloban centralmente en la *List of Trusted Lists* (LOTL). Al respecto, *EUTL (EU Trusted List)* es la denominación funcional y divulgativa habitual para referirse a esta infraestructura europea, mientras que la terminología técnica oficial bajo eIDAS y los estándares ETSI utiliza la sigla **LOTL**.

Estos servicios pueden ser **servicios cualificados**, es decir, servicios que cumplen los requisitos establecidos por eIDAS para una determinada categoría y que son prestados por un prestador cualificado (QTSP).

**Aclaraciones**:

Un TSP puede prestar servicios a ciudadanos, empresas, organizaciones o administraciones públicas.

Una **firma electrónica cualificada** tiene, conforme al artículo 25 de eIDAS, un efecto jurídico equivalente al de una firma manuscrita.

"Cualificado" es un atributo que se aplica a diferentes elementos en distintos contextos. Por ejemplo, pueden ser cualificados un prestador o un servicio de confianza, un certificado electrónico o un dispositivo de creación de firma. En el caso de una firma electrónica, existen distintos niveles (simple, avanzada y cualificada), siendo la firma cualificada aquella que cumple los requisitos adicionales de eIDAS, incluyendo el uso de un certificado cualificado y un dispositivo cualificado de creación de firma.

### eIDAS 2.0

eIDAS 2.0 establece un nuevo marco europeo de identidad digital.

> Se puede valorar que existe un [cambio de paradigma](../idea-sandbox/decentralization-paradox-idea.md).

Su objetivo principal es evolucionar desde un sistema centrado en el reconocimiento mutuo de sistemas nacionales de identificación electrónica hacia un ecosistema europeo de identidad digital interoperable, donde los ciudadanos y organizaciones puedan utilizar una identidad digital reconocida en toda la Unión Europea.

La principal novedad es la creación de la Cartera Europea de Identidad Digital (European Digital Identity Wallet, EUDI Wallet).

#### Nuevos servicios de confianza

eIDAS 2.0 amplía la lista de servicios de confianza regulados, incorporando:

**Declaración electrónica de atributos (*Electronic Attestation of Attributes, EAA*)**:

Permite emitir y verificar atributos electrónicos sobre una persona o entidad. Un atributo es una información asociada a una identidad como edad, titulación académica, permiso profesional, condición de estudiante, etc.

La declaración electrónica de atributos permite que estos datos puedan ser utilizados de forma confiable en transacciones electrónicas.

**Archivo electrónico (*Electronic Archiving*)**:

Introduce el servicio de archivo electrónico cualificado. Su finalidad es garantizar la conservación de documentos electrónicos durante largos periodos asegurando: integridad, autenticidad, origen, disponibilidad.

Está orientado a conservar evidencias digitales con valor jurídico.

**Libros mayores electrónicos (*Electronic Ledgers*)**:

Introduce los libros mayores electrónicos como servicio de confianza.

Un libro mayor electrónico permite registrar datos de forma distribuida o compartida garantizando: integridad de los registros, orden cronológico, trazabilidad de las operaciones.

> No significa que eIDAS regule blockchain como tecnología concreta, sino que establece requisitos para determinados sistemas de registro electrónico.

### Referencias de eIDAS

- [Reglamento (UE) 910/2014 (eIDAS) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)
- [buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)

## Cartera Europea de Identidad Digital (EUDI Wallet)

La **Cartera Europea de Identidad Digital (EUDI Wallet)** es una aplicación digital segura y controlada por el usuario que permite **gestionar, almacenar y utilizar su identidad digital y otras credenciales electrónicas verificables** en sus interacciones con servicios públicos y privados, tanto a nivel nacional como transfronterizo dentro de la Unión Europea.

La cartera forma parte de un **ecosistema europeo de identidad digital** en el que intervienen diferentes actores, entre ellos los usuarios, los proveedores que emiten datos de identidad y credenciales electrónicas, los proveedores de la cartera y las entidades que solicitan y verifican dichas credenciales. Este ecosistema se basa en mecanismos comunes de interoperabilidad, seguridad y confianza.

Entre sus principales capacidades se encuentran:

- **Identificación y autenticación electrónica** frente a servicios públicos y privados.
- **Almacenamiento y gestión** de datos de identidad y credenciales digitales verificables.
- **Presentación de credenciales** para demostrar determinados atributos ante terceros.
- **Interoperabilidad transfronteriza**, permitiendo utilizar la identidad y las credenciales en diferentes Estados miembros.
- **Firma electrónica**, en los casos y condiciones previstos por el marco europeo.
- **Control por parte del usuario sobre la información que comparte**, permitiendo proporcionar únicamente los datos necesarios para una determinada operación.

Las credenciales pueden proceder tanto de **autoridades públicas como de entidades privadas** y pueden representar diferentes tipos de información, como datos de identidad, permisos de conducción, títulos académicos, información profesional u otros atributos verificables. Los casos de uso previstos incluyen, entre otros, el acceso a servicios públicos, apertura de cuentas bancarias, pagos, firma de contratos, viajes, educación y servicios de seguridad social.

Un principio especialmente relevante de la EUDI Wallet es la **minimización de datos**. Por ejemplo, para demostrar que una persona cumple un requisito de edad, no necesariamente tendría que revelar su fecha de nacimiento completa: podría presentar una prueba verificable de que **es mayor de 18 años**, evitando revelar información adicional que no sea necesaria para la operación.

Por tanto, la EUDI Wallet no debe entenderse simplemente como una versión digital de un documento de identidad, sino como una **infraestructura de identidad y credenciales digitales controlada por el usuario**, diseñada para permitir que diferentes entidades puedan emitir, solicitar y verificar información digital de forma segura e interoperable en toda la Unión Europea.

Su arquitectura y requisitos técnicos se definen en el **European Digital Identity Wallet Architecture and Reference Framework (ARF)**, desarrollado en el marco del Reglamento Europeo de Identidad Digital. El ARF establece la arquitectura, los componentes, las interacciones y los mecanismos de confianza necesarios para que las diferentes implementaciones nacionales sean interoperables.

### Referencias

- [European Digital Identity Wallet — Architecture and Reference Framework](https://eudi.dev/latest/main/01-introduction/?utm_source=chatgpt.com#11-eudi-wallet-ecosystem)
- [Comisión Europea — Aplicación de la cartera de identidad digital de la UE](https://digital-strategy.ec.europa.eu/es/policies/eudi-wallet-implementation?utm_source=chatgpt.com)

## SSI (Self-Sovereign Identity)

Identidad autosoberana: modelo de identidad digital en el que el titular controla sus propios identificadores (DIDs) y credenciales verificables, las guarda en su cartera y decide qué presenta y a quién, sin depender de un proveedor de identidad central que intermedie cada verificación.

## Triángulo de confianza (credential trust triangle)

Patrón básico de las credenciales verificables, con tres roles:

- Emisor (issuer): firma y entrega la credencial
- Titular (holder): la guarda y la presenta
- Verificador (verifier): comprueba la firma y la validez de la credencial sin tener que contactar con el emisor

Los tres se apoyan en un Verifiable Data Registry para resolver claves públicas, esquemas y estado de revocación.

Referencia: [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)

## VDR (Verifiable Data Registry)

Rol definido en el modelo de credenciales verificables del W3C: sistema que publica y mantiene los datos necesarios para verificar credenciales, como identificadores (DIDs) y sus claves públicas, esquemas, listas de revocación y registros de emisores de confianza. Puede implementarse con una base de datos, una infraestructura de clave pública o una blockchain. En arquitecturas SSI para espacios de datos, la blockchain de EBSI es la implementación habitual de este rol.

Referencias:

- [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [artículo sobre identidad autosoberana en espacios de datos (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2352340926002210)

## Libro mayor electrónico (electronic ledger)

Servicio de confianza introducido por eIDAS 2: una secuencia de registros electrónicos de datos que garantiza su integridad y la exactitud de su orden cronológico. En su versión cualificada goza de presunción legal de esa integridad y ese orden. Es la figura que da encaje jurídico a blockchain y a las tecnologías de registro distribuido (DLT) dentro de eIDAS, y el Blueprint del DSSC lo recoge como uno de los building blocks posibles para la capa de confianza de un espacio de datos.

Referencia: [Reglamento (UE) 2024/1183 en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)

## EBSI (European Blockchain Services Infrastructure)

Infraestructura blockchain pública y permisionada impulsada por la Comisión Europea y la Asociación Europea de Blockchain (EBP), con nodos operados por los Estados miembros bajo un modelo federado. Su uso principal es actuar como registro de confianza para credenciales verificables (títulos académicos, identidad de entidades, documentos), además de otros casos como la notarización de documentos.

Referencia: [EBSI (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/display/EBSI/Home)

## EDIC (European Digital Infrastructure Consortium) y Europeum

Figura jurídica creada por la Comisión Europea para que varios Estados miembros implementen conjuntamente proyectos digitales transfronterizos. Europeum es el EDIC constituido específicamente para el desarrollo y despliegue de infraestructura blockchain europea, y toma el relevo de EBSI.

Referencia: [creación del EDIC Europeum (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/news/blockchain-creation-europeum-edic)

## Espacio de datos (data space)

Infraestructura y conjunto de reglas comunes (legales, técnicas y de gobernanza) que permiten a empresas y administraciones de un sector compartir datos de forma soberana, interoperable y de confianza: cada participante conserva el control sobre quién usa sus datos y en qué condiciones. La Estrategia Europea de Datos (2020) prevé espacios comunes europeos de datos por sectores (salud, agricultura, movilidad, energía, Pacto Verde...).

Varias iniciativas avanzan en paralelo en este ámbito, a veces solapándose en alcance y resultados: Gaia-X, IDSA, FIWARE, BDVA, DSSC, Simpl y EBSI, entre otras.

Referencia: [espacios comunes europeos de datos (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/data-spaces)

## DSSC (Data Spaces Support Centre)

Proyecto financiado por la Comisión Europea, dentro del programa Europa Digital, que actúa como secretaría técnica de los espacios comunes europeos de datos. Recoge el trabajo técnico de IDSA, Gaia-X, FIWARE y otras iniciativas y lo convierte en un marco común de referencia, para que los espacios de datos sectoriales usen las mismas piezas en lugar de desarrollar soluciones incompatibles. Publica:

- DSSC Blueprint: guía de cómo construir un espacio de datos, organizada en building blocks legales, técnicos y de gobernanza
- DSSC Toolbox: catálogo de componentes software que implementan esos building blocks
- Glosario: vocabulario común para que todas las iniciativas nombren igual los mismos conceptos

El Blueprint recomienda el Dataspace Protocol de IDSA, con ODRL como lenguaje de políticas, para el intercambio de datos entre participantes.

Referencia: [web del DSSC](https://dssc.eu/)

## IDSA (International Data Spaces Association)

Asociación fundada en 2016 que mantiene el estándar técnico de facto de los espacios de datos, con independencia de la financiación europea puntual. Sus aportaciones principales son el modelo de arquitectura de referencia (IDS-RAM), el Dataspace Protocol y la certificación de conectores. También mantiene el Data Spaces Radar, un mapa de las iniciativas de espacios de datos existentes en Europa, con contribuciones de la comunidad del DSSC.

Referencia: [web de IDSA](https://internationaldataspaces.org/)

## DSP (Dataspace Protocol)

Protocolo, originado en IDSA, que define cómo los participantes de un espacio de datos publican catálogos, negocian contratos de uso y gestionan la transferencia de datos entre conectores. Las condiciones de uso se expresan en ODRL.

Referencia: [web de IDSA](https://internationaldataspaces.org/)

## ODRL (Open Digital Rights Language)

Recomendación del W3C para expresar políticas de uso de contenidos y datos (permisos, prohibiciones y obligaciones) de forma legible por máquinas. En los espacios de datos se usa para describir en qué condiciones se puede usar un conjunto de datos.

Referencia: [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)

## Gaia-X

Asociación europea sin ánimo de lucro que define un marco de confianza (Trust Framework) para servicios de datos y nube federados: reglas, etiquetas de conformidad y servicios de verificación basados en credenciales verificables, para que los participantes puedan comprobar de forma automatizada que los demás cumplen requisitos comunes.

Referencia: [web de Gaia-X](https://gaia-x.eu/)

## FIWARE

Fundación que mantiene un conjunto de componentes open source para gestionar datos de contexto (por ejemplo, el Orion Context Broker), basados en la especificación NGSI-LD de ETSI. Es muy usado en ciudades inteligentes y aporta conectores e implementaciones de referencia a los espacios de datos.

Referencia: [web de FIWARE](https://www.fiware.org/)

## BDVA (Big Data Value Association)

Asociación industrial europea que representa al sector privado en la colaboración público-privada con la Comisión Europea en materia de datos e inteligencia artificial, y que contribuye a definir la agenda de investigación e innovación sobre espacios de datos.

Referencia: [web de BDVA](https://bdva.eu/)

## Simpl

Middleware open source financiado por la Comisión Europea para dar a los espacios comunes europeos de datos una base técnica compartida (gestión de identidades, catálogos, contratos e intercambio de datos), de modo que no cada espacio desarrolle la suya.

Referencia: [Simpl (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/simpl)

## ETSI (European Telecommunications Standards Institute)

Instituto Europeo de Normas de Telecomunicaciones, con sede en Sophia Antipolis (Francia). Es uno de los tres organismos europeos de normalización reconocidos por el Reglamento (UE) 1025/2012, junto con CEN y CENELEC. Su comité ESI (Electronic Signatures and Infrastructures) elabora las normas técnicas que desarrollan eIDAS (firmas, certificados, prestadores de servicios de confianza, listas de confianza).

Referencias:

- [web de ETSI](https://www.etsi.org/)
- [comité ESI de ETSI](https://www.etsi.org/committee/esi)

## CEN y CENELEC

Comité Europeo de Normalización (CEN) y Comité Europeo de Normalización Electrotécnica (CENELEC), con sede en Bruselas. Elaboran las normas europeas formales (EN), que los organismos nacionales (UNE en España) adoptan como propias. Trabajan de forma conjunta en ámbitos como blockchain y DLT, a través del comité técnico conjunto CEN/CENELEC JTC 19.

Referencia: [web de CEN y CENELEC](https://www.cencenelec.eu/)

## QBFT (Quorum Byzantine Fault Tolerant)

Algoritmo de consenso de tolerancia a fallos bizantinos (BFT) basado en Proof of Authority (PoA), utilizado en redes blockchain permisionadas (por ejemplo, Hyperledger Besu). Un conjunto de validadores conocidos propone y valida bloques mediante rondas de votación; la red tolera hasta *f* validadores maliciosos o caídos de un total de *3f+1*.

Referencia: [documentación de Hyperledger Besu sobre QBFT](https://besu.hyperledger.org/private-networks/how-to/configure/consensus/qbft)

## IBFT 2.0 (Istanbul Byzantine Fault Tolerant 2.0)

Predecesor de QBFT, también basado en PoA y con propiedades de tolerancia a fallos bizantinos. Se especificó originalmente en el EIP-650. Ambos algoritmos (QBFT e IBFT 2.0) garantizan finalidad inmediata de los bloques (a diferencia de Proof of Work), lo que los hace habituales en consorcios y redes gubernamentales o empresariales.

Referencia: [EIP-650: Istanbul Byzantine Fault Tolerance](https://github.com/ethereum/EIPs/issues/650)

### Modelo gobernanza federado

Modelo de gobernanza que combina supervisión centralizada con ejecución descentralizada. Un órgano común (comité o consejo) fija las normas compartidas de seguridad, cumplimiento e interoperabilidad, y cada organización participante gestiona su parte con autonomía, adaptándola a sus necesidades siempre que respete esas normas. Frente a un modelo centralizado, en el que un único equipo u operador lo gestiona todo.

En redes blockchain permisionadas entre administraciones, cada organización opera sus propios nodos y todas se someten a reglas comunes acordadas (requisitos de adhesión, políticas de seguridad, toma de decisiones). Es el modelo de EBSI: cada Estado miembro aporta y opera nodos, y la gobernanza se ejerce de forma conjunta.

Referencia: [gobernanza federada de datos (Actian)](https://www.actian.com/es/blog/data-governance/federated-data-governance-explained/)

## OSCAL (Open Security Controls Assessment Language)

Lenguaje estándar desarrollado por el NIST (National Institute of Standards and Technology) para representar de forma estructurada (JSON, XML o YAML) controles de seguridad, catálogos de cumplimiento, planes de seguridad (SSP) y evaluaciones de riesgo. Su objetivo es que la información de cumplimiento normativo se pueda leer, validar y transformar de forma automatizada, en lugar de mantenerla en documentos manuales (PDF o Word).

Herramientas que lo soportan:

- NIST OSCAL CLI: herramienta oficial que convierte entre JSON, XML y YAML y valida documentos contra el esquema oficial
- Trestle (compliance-trestle): la herramienta más usada para trabajar con catálogos OSCAL en Python y generar SSP (System Security Plan), profiles, etc.
- OpenControl y GovReady-Q: también consumen documentos OSCAL
- Cualquier parser genérico (Python, `jq`, JavaScript...), al ser JSON, XML o YAML estándar, si solo se quieren extraer datos

Referencia: [documentación de OSCAL (NIST)](https://pages.nist.gov/OSCAL/)

---
