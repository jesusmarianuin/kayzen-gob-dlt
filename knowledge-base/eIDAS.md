# Glosario de términos relacionado con eIDAS

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

### Referencias de eIDAS

- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)

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

### Referencias de eIDAS2

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

## Libro mayor electrónico (electronic ledger)

Un libro mayor electrónico es un registro de datos en el que cada entrada queda en orden y no se puede modificar sin que se note. La idea es la de un libro de registro de entradas en papel, con las páginas numeradas, pero en formato digital.

eIDAS 2 (Reglamento (UE) 2024/1183) lo incorpora como un nuevo servicio de confianza, junto a la firma, el sello o el sello de tiempo. Lo define como "una secuencia de registros electrónicos de datos que garantiza la integridad de dichos registros y la exactitud de su orden cronológico" (artículo 3).

Como en el resto de servicios de confianza, hay dos niveles:

- Libro mayor electrónico: un juez no puede rechazarlo como prueba solo por ser electrónico o por no ser cualificado (artículo 45 duodecies)
- Libro mayor electrónico cualificado: lo presta un prestador cualificado de servicios de confianza supervisado, y la ley presume que los datos son auténticos, que su fecha y su orden son exactos y que no se han alterado. Quien quiera negarlo tiene que demostrarlo (artículos 45 duodecies y 45 terdecies)

El reglamento no menciona la tecnología: un libro mayor puede implementarse con o sin blockchain. La relación con las tecnologías de registro distribuido (DLT) se concreta en su desarrollo técnico. El Reglamento de Ejecución (UE) 2025/2531 fija las normas de referencia para los libros mayores cualificados, y su anexo se dedica a los "libros mayores electrónicos distribuidos cualificados", con definiciones de nodo, consenso, mecanismo de consenso y carácter definitivo de los registros.

En la práctica, esto significa que una red blockchain puede ofrecer un servicio con valor probatorio reconocido en toda la UE, siempre que la opere un prestador cualificado y cumpla esas normas. Que una red sea blockchain no le da por sí mismo esa presunción legal.

Referencias:

- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj)

## EBSI (European Blockchain Services Infrastructure)

Infraestructura blockchain impulsada por la Comisión Europea y la European Blockchain Partnership (EBP). Se describe como "pública y permisionada", dos términos que responden a preguntas distintas:

- Pública: cualquiera puede leer los datos, porque los verificadores de credenciales tienen que poder consultarlos sin pedir permiso
- Permisionada: solo pueden operar nodos las entidades autorizadas, en la práctica los Estados miembros y la Comisión. Y solo escriben quienes han sido acreditados para ello, por ejemplo un emisor de confianza que registra su DID

Una persona o empresa cualquiera puede consultar EBSI, pero no puede montar un nodo propio.

Además, sigue un [modelo de gobernanza federado](blockchain.md#modelo-gobernanza-federado): ningún actor la controla en solitario. Cada Estado miembro opera sus propios nodos, y todos se someten a reglas comunes que se deciden de forma conjunta.

Su uso principal es actuar como registro de confianza para credenciales verificables (títulos académicos, identidad de entidades, documentos), además de otros casos como la notarización de documentos.

EBSI y el libro mayor electrónico de eIDAS son cosas distintas, aunque ambos usan DLT:

- El libro mayor electrónico es una categoría legal: un servicio de confianza que cualquier prestador puede ofrecer y que, si es cualificado, tiene valor probatorio reconocido
- EBSI es una infraestructura concreta, construida para guardar la información pública con la que se verifican credenciales: identificadores de emisores, sus claves públicas, emisores de confianza y estado de revocación. Es decir, cumple el rol de VDR

La condición de cualificado no depende de la tecnología, sino de quién presta el servicio y cómo: la otorga el organismo de supervisión a un prestador cualificado de servicios de confianza que cumple eIDAS y el Reglamento de Ejecución (UE) 2025/2531, y el servicio aparece en las listas de confianza. Por eso EBSI no es un libro mayor electrónico cualificado por sí misma. Podría serlo un servicio que un prestador cualificado ofreciera sobre ella. Donde más se acercan es en la notarización de documentos, que consiste precisamente en dejar constancia fechada e inalterable de unos datos.

Referencia: [EBSI (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/display/EBSI/Home)

## EDIC (European Digital Infrastructure Consortium) y Europeum

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

## Espacio de datos (data space)

Un espacio común europeo de datos (common European data space) es un concepto de la Unión Europea, introducido por la Comisión en la Estrategia Europea de Datos (2020), para que empresas y administraciones de un mismo sector económico compartan datos entre ellas sin cederlos a una plataforma que los centralice. Nace porque esas organizaciones apenas compartían datos, por miedo a perder el control sobre ellos, y su valor lo concentraban unas pocas plataformas, mayoritariamente no europeas.

Cada espacio corresponde a un sector: salud, movilidad, energía, agricultura, industria, finanzas, administración pública, Pacto Verde, entre otros. Lo forman las organizaciones de ese sector que aceptan unas reglas comunes:

- Legales: el Data Governance Act (Reglamento (UE) 2022/868), que prevé estos espacios por sectores, y el Data Act (Reglamento (UE) 2023/2854), cuyo artículo 33 fija requisitos de interoperabilidad para quienes ofrecen datos en ellos. Algunos sectores tienen además ley propia: el primero es el Espacio Europeo de Datos Sanitarios (Reglamento (UE) 2025/327)
- Técnicas: cada organización conserva sus datos en sus sistemas y los intercambia directamente con otra, normalmente mediante un software llamado conector, junto con unas condiciones de uso legibles por máquinas
- De gobernanza: una entidad del espacio decide quién entra, verifica su identidad y fija las reglas

El término "espacio de datos" también se usa fuera de este marco oficial para iniciativas privadas que siguen el mismo modelo. La más conocida es Catena-X, del sector del automóvil, impulsada desde 2020 por empresas como BMW, Bosch, SAP o Siemens. En ella, un fabricante pide a sus proveedores los datos de huella de CO2 de las piezas y cada proveedor se los envía directamente desde su conector, con la condición de que solo se usen para calcular CO2. Ningún dato pasa por un servidor central.

Los términos de este ámbito son de tipos muy distintos y conviene separarlos:

- Piezas técnicas, que explican cómo se intercambian los datos: conector, DSP, ODRL y el marco de confianza de Gaia-X
- Organizaciones que definen esas piezas: IDSA, Gaia-X, W3C y, como normalizadores oficiales, [CEN y CENELEC](#cen-y-cenelec)
- Iniciativas de la Comisión Europea que reúnen esas piezas para los espacios comunes europeos: DSSC y Simpl
- Otros actores del ecosistema: BDVA

Referencia: [espacios comunes europeos de datos (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/data-spaces)

### Cómo funciona un intercambio de datos

Siguiendo el ejemplo de Catena-X, cuando un fabricante pide a un proveedor los datos de huella de CO2 de una pieza:

- Cada empresa tiene instalado en sus sistemas un conector, el software que se comunica con los conectores de los demás participantes
- Antes de intercambiar nada, cada parte comprueba la identidad de la otra y que cumple las reglas del espacio, mediante credenciales verificables (ver [Gaia-X](#gaia-x))
- El conector del fabricante consulta el catálogo del proveedor, negocia un contrato de uso y recibe los datos. Las reglas de esa comunicación entre conectores las fija el [DSP](#dsp-dataspace-protocol)
- La condición "solo para calcular CO2" viaja escrita en un formato legible por máquinas, [ODRL](#odrl-open-digital-rights-language)

#### DSP (Dataspace Protocol)

Protocolo que define cómo se comunican los conectores de un espacio de datos: cómo publican un catálogo con los datos que ofrecen, cómo negocian el contrato de uso y cómo gestionan la transferencia. Las condiciones de uso se expresan en ODRL.

Lo creó IDSA, que en 2024 trasladó su mantenimiento al Eclipse Dataspace Working Group de la Eclipse Foundation, con el objetivo de convertirlo en estándar ISO/IEC.

Referencia: [versión estable del Dataspace Protocol (IDSA)](https://internationaldataspaces.org/idsa-releases-stable-version-of-the-dataspace-protocol/)

#### ODRL (Open Digital Rights Language)

Recomendación del W3C para expresar políticas de uso (permisos, prohibiciones y obligaciones) de forma legible por máquinas. En un espacio de datos es el formato en el que se escriben las condiciones de uso de un conjunto de datos, por ejemplo "uso permitido solo para calcular CO2, durante un año".

Referencia: [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)

### Organizaciones que definen las piezas

#### IDSA (International Data Spaces Association)

Asociación fundada en 2016 que creó el modelo técnico en el que se basan la mayoría de espacios de datos: la arquitectura de referencia (IDS-RAM), el modelo de conectores y su certificación, y el Dataspace Protocol. Catena-X, por ejemplo, se basa en este modelo. También mantiene el Data Spaces Radar, un mapa de las iniciativas de espacios de datos existentes en Europa.

Referencia: [web de IDSA](https://internationaldataspaces.org/)

#### Gaia-X

Asociación europea sin ánimo de lucro que define un marco de confianza (Trust Framework) para servicios de datos y nube: qué reglas deben cumplir los participantes y cómo se comprueba, de forma automatizada, mediante credenciales verificables. En un espacio de datos aporta la respuesta a la pregunta "¿cómo sé que la otra parte es quien dice ser y cumple las reglas?".

Referencia: [web de Gaia-X](https://gaia-x.eu/)

### Iniciativas de la Comisión Europea

#### DSSC (Data Spaces Support Centre)

Proyecto financiado por la Comisión Europea, dentro del programa Europa Digital, que actúa como centro de apoyo de los espacios comunes europeos de datos. Recoge el trabajo de IDSA, Gaia-X, FIWARE y otras iniciativas y lo ordena en un marco común, para que los espacios de cada sector usen las mismas piezas en lugar de desarrollar soluciones incompatibles. Publica:

- DSSC Blueprint: guía de cómo construir un espacio de datos, organizada en building blocks legales, técnicos y de gobernanza
- DSSC Toolbox: catálogo de componentes software que implementan esos building blocks
- Glosario: vocabulario común para que todas las iniciativas nombren igual los mismos conceptos

Referencia: [web del DSSC](https://dssc.eu/)

#### Simpl

Software open source financiado por la Comisión Europea que reúne las piezas técnicas (gestión de identidades, catálogos, contratos e intercambio de datos) listas para usar en los espacios comunes europeos de datos, para que cada uno no tenga que desarrollar las suyas. DSSC dice cómo construir un espacio de datos; Simpl es software con el que construirlo.

Referencia: [Simpl (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/simpl)

### Otros actores

#### BDVA (Big Data Value Association)

Asociación industrial europea que representa al sector privado en la colaboración público-privada con la Comisión Europea en materia de datos e inteligencia artificial. Influye en la agenda europea de investigación e innovación sobre espacios de datos, pero no aporta piezas técnicas.

Referencia: [web de BDVA](https://bdva.eu/)

## ETSI (European Telecommunications Standards Institute)

Instituto Europeo de Normas de Telecomunicaciones, con sede en Sophia Antipolis (Francia). Es uno de los tres organismos europeos de normalización reconocidos por el Reglamento (UE) 1025/2012, junto con CEN y CENELEC. Su comité ESI (Electronic Signatures and Infrastructures) elabora las normas técnicas que desarrollan eIDAS (firmas, certificados, prestadores de servicios de confianza, listas de confianza).

Referencias:

- [web de ETSI](https://www.etsi.org/)
- [comité ESI de ETSI](https://www.etsi.org/committee/esi)

## CEN y CENELEC

Comité Europeo de Normalización (CEN) y Comité Europeo de Normalización Electrotécnica (CENELEC), con sede en Bruselas. Junto con ETSI son los tres organismos europeos de normalización reconocidos oficialmente por la UE (Reglamento (UE) 1025/2012). Elaboran las normas europeas formales (EN), que los organismos nacionales (UNE en España) adoptan como propias.

Su papel en la regulación europea es este: una ley de la UE fija requisitos generales, la Comisión encarga a estos organismos las normas técnicas que los concretan, y quien cumple esas normas se presume que cumple la ley. Por eso aparecen en los tres ámbitos de este glosario, cada uno a través de un comité técnico distinto:

- eIDAS: el comité CEN/TC 224 elabora la serie de normas EN 419, que fija los requisitos de seguridad de los dispositivos de firma y sello (tarjetas, módulos criptográficos de los prestadores, firma en servidor). La mayoría de las normas de los servicios de confianza las elabora ETSI, no CEN
- Blockchain: el comité conjunto CEN/CENELEC JTC 19 (Blockchain and Distributed Ledger Technologies) adapta al ámbito europeo las normas internacionales de ISO/TC 307 y trabaja en normas propias, como la protección de datos personales en DLT
- Espacios de datos: el comité conjunto CEN/CENELEC JTC 25 (Data management, Dataspaces, Cloud and Edge), creado en septiembre de 2024, elabora las normas que concretan los requisitos de interoperabilidad del artículo 33 del Data Act, por encargo de la Comisión (mandato M/614, aceptado en julio de 2025). Lo preside un representante de IDSA

Referencias:

- [web de CEN y CENELEC](https://www.cencenelec.eu/)
- [creación del comité JTC 25 (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2024/brief-news/2024-09-25-jtc-25/)
- [aceptación del mandato del Data Act (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2025/brief-news/2025-07-11-data-act-standardization-request/)

---
