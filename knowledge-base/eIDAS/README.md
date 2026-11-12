# Regulación: conceptos relacioandos con eIDAS

## eIDAS

eIDAS: Electronic IDentification, Authentication and trust Services.
eIDAS es un [reglamento](https://eur-lex.europa.eu/ES/legal-content/summary/european-union-regulations.html) de la UE relativo a la identificación electrónica, la autenticación y los servicios de confianza para las transacciones electrónicas en el mercado interior (donde circulan libremente personas, bienes, servicios y capitales). Se aplica en toda la UE desde el 1 de julio de 2016.

Por una parte, permite el reconocimiento de sistemas nacionales de identificación electrónica (eID), incluyendo los procesos de autenticación asociados, notificados por los Estados miembros. Por ejemplo, DNI electrónico es reconocido como sistema de identificación electrónica.

Por otra parte, regula los **servicios de confianza** (TS, Trust Service). Un servicio de confianza es un servicio electrónico que permite realizar determinadas operaciones relacionadas con la confianza en transacciones electrónicas (a ciudadanos, empresas, organizaciones o administraciones públicas) y que está regulado, como puede ser la firma, sello de tiempo electrónicos (TSA), entrega electrónica cualificada (ERDS o Qualified Electronic Registered Delivery Service) y certificados de autenticación de sitios web.

Un servicio de confianza, tiene un **Prestador de Servicios de Confianza** (TSP Trust Service Provider) que es la entidad que presta dichos servicios, bajo la supervisión del Estado miembro correspondiente. Un prestador puede estar sujeto a requisitos nacionales que limiten a quién presta el servicio.

Los prestadores de servicios de confianza pueden obtener la categoría de **Prestadores Cualificados de Servicios de Confianza** (*Qualified Trust Service Provider*, QTSP). Para ello, deben cumplir los requisitos previstos en el Reglamento eIDAS y contar con el reconocimiento formal del órgano de supervisión competente de su país.

Estos prestadores, si son cualificados, se incluyen en la [**lista de confianza**](trusted-lists.md) del Estado miembro correspondiente (*Trusted List*, TL, especificada técnicamente como *Trust Service Status List*, TSL); los no cualificados, solo si el Estado lo decide.

Ser prestador cualificado de servicios (QTSP) es lo que habilita a poder ofrecer **servicios cualificados** (QTS, Qualified Trust Service). Pero aún existen requisitos descritos en eIDAS, que tienen que ser aprobados por el órgano de supervisión nacional (según sede legal del proveedor).

La ventaja del servicio cualificado es la **presunción legal** automática en toda la UE de su integridad, origen o fecha, según el servicio: ante un juez se da por cierto de entrada y la carga de probar lo contrario recae en quien lo impugna. Aunque un servicio puede ser no cualificado, como un certificado TLS, siendo perfecto para la mayoría de operaciones comerciales cotidianas de riesgo bajo o medio donde prima la rapidez, pero el proveedor asume el riesgo probatorio si el asunto acaba en los tribunales.

**Aclaraciones**:

Una **firma electrónica cualificada** tiene, conforme al artículo 25 de eIDAS, un efecto jurídico equivalente al de una firma manuscrita.

"Cualificado" es un atributo que se aplica a diferentes elementos en distintos contextos, en este documento se menciona para los servicios y proveedores. Por ejemplo, pueden ser cualificados un prestador o un servicio de confianza, pero también pueden serlo un certificado electrónico, que solo expide un prestador cualificado, o un dispositivo de creación de firma, que se certifica como cualificado.

**Actos de ejecución**:

Un acto de ejecución es una norma que adopta la Comisión Europea para concretar cómo se aplica un reglamento en todos los Estados miembros. Es decir es una forma de entregar de forma periodica normas sin necesidad de modificar el reglamento.

eIDAS como reglamente, cuenta con sus propios [actos de ejecución](https://commission.europa.eu/law/law-making-process/adopting-eu-law/implementing-and-delegated-acts_es), pero no se cubren en este documento.

## eIDAS2

eIDAS2 es la reforma de eIDAS aprobada por el Reglamento (UE) 2024/1183. Añade la Cartera Europea de Identidad Digital (EUDI Wallet) y nuevos servicios de confianza, como la declaración electrónica de atributos, el archivo electrónico y los libros mayores electrónicos.

> Se puede valorar que existe un [cambio de paradigma](../../idea-sandbox/decentralization-paradox-idea.md).

Su objetivo principal es evolucionar desde un sistema centrado en el reconocimiento mutuo de sistemas nacionales de identificación electrónica hacia un ecosistema europeo de identidad digital interoperable, donde los ciudadanos y organizaciones puedan utilizar una identidad digital reconocida en toda la Unión Europea.

La principal novedad es la creación de la Cartera Europea de Identidad Digital (European Digital Identity Wallet, EUDI Wallet).

El reglamento define la cartera y los servicios de confianza y fija sus requisitos, pero no todos sus detalles técnicos. Por ejemplo, establece que debe existir una cartera europea de identidad digital (EUDI Wallet), pero no define por sí solo todos los formatos de datos, protocolos de comunicación, mecanismos de seguridad o procedimientos de certificación que debe utilizar.

Como explicamos, esos detalles se concretan en los [actos de ejecución](implementing-acts.md), que redacta la [DG CONNECT](dg-connect.md), la dirección general de la Comisión Europea responsable de eIDAS. Así pueden actualizarse sin modificar el reglamento.

### Cartera Europea de Identidad Digital (EUDI Wallet)

La IDUE (Identidad Digital de la Unión Europea) se gestiona con [la Cartera Europea de Identidad Digital (EUDI Wallet)](eudi-wallet.md), es una aplicación digital segura y controlada por el usuario que permite gestionar, almacenar y utilizar su identidad digital y otras credenciales electrónicas verificables en sus interacciones con servicios públicos y privados, tanto a nivel nacional como transfronterizo dentro de la Unión Europea. Se puede relacionar con la idea del pasaporte, pero en formato digital. Lo custodias tú mismo, no un tercero, y en él acumulas credenciales que acreditan datos sobre ti.

Entre sus principales capacidades se encuentran:

- Identificación y autenticación electrónica frente a servicios públicos y privados.
- Almacenamiento y gestión de datos de identidad (PID) y credenciales digitales verificables (EAA, QEAA y PuB-EAA).
- Interoperabilidad transfronteriza, permitiendo utilizar la identidad y las credenciales en diferentes Estados miembros.
- Firma electrónica, como [firma cualificada (QES)](https://www.e-signature.eu/en/eidas-2-electronic-signature/#:~:text=*%20QES%20via%20smartphone%20(software%20QSCD)%20becomes,and%20compliant%20during%20and%20after%20the%20transition.), en los casos y condiciones previstos por el marco europeo.
- Control por parte del usuario sobre la información que comparte, permitiendo proporcionar únicamente los datos necesarios para una determinada operación.

La cartera forma parte de un ecosistema que permite un mecanismo común de interoperabilidad entre los Estados miembros.

En primer lugar están los proveedores de la cartera (*wallet providers*), es decir, quienes ponen a disposición el programa informático que se instala en el dispositivo. Puede proporcionarla el propio Estado miembro, una organización a la que este se lo encarga o una entidad independiente a la que el Estado reconoce.

En la cartera se cargan los datos de identificación de la persona (PID), que son los datos que acreditan quién es, como el nombre, los apellidos o la fecha de nacimiento, lo mismo que hoy recoge el DNI. Lo emite el proveedor de PID que designa cada Estado miembro; España emite el PID de sus ciudadanos a través de los organismos que ella misma designe (presumiblemente la Agencia Estatal de Administración Digital, AEAD).

Como comentábamos, existen además declaraciones de atributos que emite el organismo público responsable de la fuente auténtica de ese dato, como un certificado de empadronamiento (en ese caso, el ayuntamiento, que gestiona el padrón). Ese organismo puede ser de cualquier nivel de la Administración, estatal, autonómica o local, o actuar otra entidad en su nombre. Son las PuB-EAA, y tienen el mismo efecto jurídico que un documento en papel expedido legalmente.

Estos tres elementos (cartera, PID y PuB-EAA) forman parte del ecosistema de la Cartera EUDI, regulado en el propio eIDAS2 y en sus reglamentos de ejecución. Pero ninguno es un servicio de confianza ni aparece en las listas de confianza (TL) nacionales, que en la cartera quedan reservadas a las QEAA. En su lugar, cada Estado miembro notifica sus proveedores a la Comisión, que los publica en las [listas de entidades de confianza (LoTE)](trusted-lists.md#en-la-eudi-wallet): una lista firmada por tipo de entidad, válida para toda la Unión.

La cartera permite incorporar la emisión y validación de otras [declaraciones de atributos](electronic-attestation-of-attributes.md) del ámbito público o privado, como títulos académicos, que son proporcionadas por [servicios de confianza de eIDAS2](#nuevos-servicios-de-confianza) y por lo tanto por prestadores de servicios de confianza. Si son cualificadas (QEAA), su prestador figura en la [lista de confianza (TL)](trusted-lists.md).

Un principio especialmente relevante de la EUDI Wallet es la **minimización de datos**. Por ejemplo, para demostrar que una persona cumple un requisito de edad, no necesariamente tendría que revelar su fecha de nacimiento completa: podría presentar una prueba verificable de que **es mayor de 18 años**, evitando revelar información adicional que no sea necesaria para la operación.

Por tanto, la EUDI Wallet no debe entenderse simplemente como una versión digital de un documento de identidad, sino como una **infraestructura de identidad y credenciales digitales controlada por el usuario**, diseñada para permitir que diferentes entidades puedan emitir, solicitar y verificar información digital de forma segura e interoperable en toda la Unión Europea.

Sus requisitos técnicos se definen en los [actos de ejecución](implementing-acts.md), donde la dirección general encargada, la [DG CONNECT](dg-connect.md), elabora con los Estados miembros guías como el **European Digital Identity Wallet Architecture and Reference Framework (ARF)**, desarrollado en el marco del Reglamento Europeo de Identidad Digital. El ARF no es obligatorio, pero describe la arquitectura, los componentes y los mecanismos de confianza que necesitan las carteras nacionales para ser interoperables.

**Plazos de aplicación de la cartera europea**:

- 24 de diciembre de 2026: cada Estado miembro debe poner a disposición al menos una cartera europea, y las administraciones públicas deben aceptarla como medio de identificación. Es el plazo de emisión y aceptación por el sector público, no de adopción generalizada.
- 24 de diciembre de 2027: el sector privado regulado (banca, telecomunicaciones, energía, transporte, sanidad, seguros, educación e infraestructura digital) debe aceptarla cuando la normativa le exija autenticación reforzada.

### Nuevos servicios de confianza

eIDAS2 amplía la lista de servicios de confianza regulados, incorporando:

[**Declaración electrónica de atributos (*Electronic Attestation of Attributes, EAA*)**](electronic-attestation-of-attributes.md):

Realmente utiles para la EUDI Wallet, permite emitir y verificar atributos electrónicos sobre una persona o entidad. Un atributo es una información asociada a una identidad como edad, titulación académica, permiso profesional, condición de estudiante, etc.

Permite que estos datos puedan ser utilizados de forma confiable en transacciones electrónicas con el principio de minimizar los datos.

Sobre quién puede prestar el servicio y cómo, existen excepciones explciadas en el [documento relacionado sobre quién puede emitirlas](electronic-attestation-of-attributes.md#quién-la-emite-y-qué-valor-tiene).

[**Archivo electrónico (*Electronic Archiving*)**](electronic-archiving.md):

Introduce el servicio de archivo electrónico. Su finalidad es garantizar la conservación de documentos electrónicos durante largos periodos asegurando: integridad, autenticidad, origen, disponibilidad.

Está orientado a conservar evidencias digitales con valor jurídico.

Para la administración ya estaba habilitado que terceros le ofrezacan ese servicio, como plataformas como SIAVAL, lo que habilita es el status legal cuando es un servicio cualificado, con una presunción legal de integridad en toda la UE.

[**Libros mayores electrónicos (*Electronic Ledger*)**](electronic-ledger.md):

Introduce los libros mayores electrónicos como servicio de confianza.

Un libro mayor electrónico es una secuencia de registros de datos que garantiza su integridad y la exactitud de su orden cronológico.

El reglamento no exige una tecnología concreta: puede implementarse con o sin blockchain. De hecho muchos proveedores tradicionales de QTS comentan como algo perfectamente funcional siendo centralizados.

## Iniciativas blockchain

Aunque es un documento sobre eIDAS, es casi obligado aclarar el hecho de que no se ha mencionado iniciativas blockchaim como [EBSI](https://ebsi.eu/) o [ISBE](isbe.md) pero son por motivos diferentes.

EBSI es una iniciativa ahora de la [EUROPEUM-EDIC](https://europeum.eu/), que es una entidad jurídica aparte de eIDAS que gestiona una red blockchain que actúa como ancla de una infraestructura DID de W3C para un consorcio de países. Seamos honestos, es un juguete roto, el RGPD la frustró, no fue lo que podría ser. Hoy muchos se preguntan ¿esto para qué es? Yo me sigo preguntando.

ISBE aspira a ser QTSP del servicio de libro mayor electrónico de eIDAS2 sobre una blockchain público-permisionada. Para cumplir la [directriz 02/2025 del EDPB](https://www.edpb.europa.eu/documents/guideline/guidelines-022025-on-processing-of-personal-data-through-blockchain_en), en la cadena solo guarda una huella del dato, que sin una clave secreta guardada fuera no lleva a nadie. Para borrar se destruye esa clave. La duda es si ese borrado es fiable cuando depende de que cada participante lo haga bien.

## Cartera Empresarial Europea (European Business Wallet)

La Cartera Empresarial Europea es una herramienta digital pensada para que empresas y administraciones públicas se identifiquen e intercambien documentos con validez jurídica en toda la UE. Es a las organizaciones lo que la [Cartera Europea de Identidad Digital (EUDI Wallet)](README.md#cartera-europea-de-identidad-digital-eudi-wallet) es a los ciudadanos.

No forma parte de eIDAS2, sino que es un reglamento propio que se apoya en él. Reutiliza sus servicios de confianza (firma, sello y entrega electrónica certificada) y su organización, ya que la supervisarían los mismos organismos nacionales que supervisan la identidad digital.

En la práctica, la EUDI Wallet identifica a una persona y la Cartera Empresarial Europea identifica a una organización. Ambas comparten el mismo marco de confianza europeo.

Todavía no es una norma aplicable. La Comisión Europea la presentó el 19 de noviembre de 2025 como propuesta de reglamento y sigue en negociación.

Según la propuesta, sus funciones básicas son:

- Identificar y autenticar a la empresa frente a otras empresas y administraciones.
- Firmar y sellar documentos electrónicamente.
- Enviar y recibir documentos y datos verificados con constancia de entrega, mediante el servicio de confianza de eIDAS entrega electrónica certificada cualificada.

Las actuaciones hechas con la cartera tendrían el mismo efecto jurídico que hacerlas en papel o en persona.

Su uso sería voluntario para las empresas, pero las administraciones públicas estarían obligadas a aceptarla para esas funciones básicas.

A noviembre de 2026 la propuesta está en negociación entre el Parlamento Europeo y el Consejo:

- 19 de noviembre de 2025: la Comisión publica la propuesta.
- 9 de junio de 2026: el Consejo fija su posición.
- 10 de septiembre de 2026: la comisión ITRE del Parlamento aprueba su informe y se abren las negociaciones con el Consejo.

Cuando se apruebe hará falta además publicar sus actos de ejecución, igual que ocurre con eIDAS2, así que no se esperan carteras en funcionamiento a corto plazo.

## Referencias

- [Reglamento (UE) n.º 910/2014 (eIDAS)](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32014R0910)
- [Reglamento (UE) 2024/1183 (eIDAS2)](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1183)
- [Marco de arquitectura y referencia de la EUDI Wallet (ARF)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework)

---
