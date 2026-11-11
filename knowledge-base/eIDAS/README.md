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

La ventaja del servicio cualificado es la presunción legal automática en toda la UE de su integridad, origen o fecha, según el servicio: ante un juez se da por cierto de entrada y la carga de probar lo contrario recae en quien lo impugna. Aunque un servicio puede ser no cualificado, como un certificado TLS, siendo perfecto para la mayoría de operaciones comerciales cotidianas de riesgo bajo o medio donde prima la rapidez, pero el proveedor asume el riesgo probatorio si el asunto acaba en los tribunales.

**Aclaraciones**:

Una **firma electrónica cualificada** tiene, conforme al artículo 25 de eIDAS, un efecto jurídico equivalente al de una firma manuscrita.

"Cualificado" es un atributo que se aplica a diferentes elementos en distintos contextos, en este documento se menciona para los servicios y proveedores. Por ejemplo, pueden ser cualificados un prestador o un servicio de confianza, pero también pueden serlo un certificado electrónico, que solo expide un prestador cualificado, o un dispositivo de creación de firma, que se certifica como cualificado.

**Actos de ejecución**:

Un acto de ejecución es una norma que adopta la Comisión Europea para concretar cómo se aplica un reglamento en todos los Estados miembros. Es decir es una forma de entregar de forma periodica normas sin necesidad de modificar el reglamento.

eIDAS como reglamente, cuenta con sus propios [actos de ejecución](https://commission.europa.eu/law/law-making-process/adopting-eu-law/implementing-and-delegated-acts_es), pero no se cubren en este documento.

### Referencias de eIDAS

- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)

## eIDAS2

eIDAS2 es la reforma de eIDAS aprobada por el Reglamento (UE) 2024/1183. Añade la Cartera Europea de Identidad Digital (EUDI Wallet) y nuevos servicios de confianza, como la declaración electrónica de atributos, el archivo electrónico y los libros mayores electrónicos.

> Se puede valorar que existe un [cambio de paradigma](../../idea-sandbox/decentralization-paradox-idea.md).

Su objetivo principal es evolucionar desde un sistema centrado en el reconocimiento mutuo de sistemas nacionales de identificación electrónica hacia un ecosistema europeo de identidad digital interoperable, donde los ciudadanos y organizaciones puedan utilizar una identidad digital reconocida en toda la Unión Europea.

La principal novedad es la creación de la Cartera Europea de Identidad Digital (European Digital Identity Wallet, EUDI Wallet).

El reglamento define la cartera y los servicios de confianza y fija sus requisitos, pero no todos sus detalles técnicos. Por ejemplo, establece que debe existir una cartera europea de identidad digital (EUDI Wallet), pero no define por sí solo todos los formatos de datos, protocolos de comunicación, mecanismos de seguridad o procedimientos de certificación que debe utilizar.

Como explicamos, esos detalles se concretan en los [actos de ejecución](implementing-acts.md), que redacta la [DG CONNECT](dg-connect.md), la dirección general de la Comisión Europea responsable de eIDAS. Así pueden actualizarse sin modificar el reglamento.

### Nuevos servicios de confianza

eIDAS2 amplía la lista de servicios de confianza regulados, incorporando:

[**Declaración electrónica de atributos (*Electronic Attestation of Attributes, EAA*)**](electronic-attestation-of-attributes.md):

Permite emitir y verificar atributos electrónicos sobre una persona o entidad. Un atributo es una información asociada a una identidad como edad, titulación académica, permiso profesional, condición de estudiante, etc.

Permite que estos datos puedan ser utilizados de forma confiable en transacciones electrónicas.

[**Archivo electrónico (*Electronic Archiving*)**](electronic-archiving.md):

Introduce el servicio de archivo electrónico. Su finalidad es garantizar la conservación de documentos electrónicos durante largos periodos asegurando: integridad, autenticidad, origen, disponibilidad.

Está orientado a conservar evidencias digitales con valor jurídico.

[**Libros mayores electrónicos (*Electronic Ledger*)**](electronic-ledger.md):

Introduce los libros mayores electrónicos como servicio de confianza.

Un libro mayor electrónico es una secuencia de registros de datos que garantiza su integridad y la exactitud de su orden cronológico. El reglamento no exige una tecnología concreta: puede implementarse con o sin blockchain.

### Plazos de aplicación de la cartera europea

- 24 de diciembre de 2026: cada Estado miembro debe poner a disposición al menos una cartera europea, y las administraciones públicas deben aceptarla como medio de identificación. Es el plazo de emisión y aceptación por el sector público, no de adopción generalizada
- 24 de diciembre de 2027: el sector privado regulado (banca, telecomunicaciones, energía, transporte, sanidad, seguros, educación e infraestructura digital) debe aceptarla cuando la normativa le exija autenticación reforzada

### Referencias de eIDAS2

- [Reglamento (UE) 910/2014 (eIDAS) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)
- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)

## Cartera Europea de Identidad Digital (EUDI Wallet)

La IDUE (Identidad Digital de la Unión Europea) conocida como [la Cartera Europea de Identidad Digital (EUDI Wallet)](eudi-wallet.md) es una aplicación digital segura y controlada por el usuario que permite gestionar, almacenar y utilizar su identidad digital y otras credenciales electrónicas verificables en sus interacciones con servicios públicos y privados, tanto a nivel nacional como transfronterizo dentro de la Unión Europea.

La cartera forma parte de un ecosistema europeo de identidad digital en el que intervienen diferentes actores, entre ellos los usuarios, los proveedores que emiten datos de identidad y credenciales electrónicas, los proveedores de la cartera y las entidades que solicitan y verifican dichas credenciales. Este ecosistema se basa en mecanismos comunes de interoperabilidad, seguridad y confianza.

Entre sus principales capacidades se encuentran:

- Identificación y autenticación electrónica frente a servicios públicos y privados.
- Almacenamiento y gestión de datos de identidad y credenciales digitales verificables.
- Presentación de credenciales para demostrar determinados atributos ante terceros.
- Interoperabilidad transfronteriza, permitiendo utilizar la identidad y las credenciales en diferentes Estados miembros.
- Firma electrónica, como [firma cualificada (QES)](https://www.e-signature.eu/en/eidas-2-electronic-signature/#:~:text=*%20QES%20via%20smartphone%20(software%20QSCD)%20becomes,and%20compliant%20during%20and%20after%20the%20transition.), en los casos y condiciones previstos por el marco europeo.
- Control por parte del usuario sobre la información que comparte, permitiendo proporcionar únicamente los datos necesarios para una determinada operación.

Para que su titular pueda identificarse, la cartera guarda los datos que acreditan quién es, como el nombre, los apellidos o la fecha de nacimiento, lo mismo que hoy recoge el DNI. Son los datos de identificación personal (Person Identification Data, PID) y los emite un proveedor designado por cada Estado miembro. Emitir el PID no es un servicio de confianza, así que estos proveedores no figuran en las listas de QTSP, sino en otra lista de emisores, la [lista de entidades de confianza (LoTE)](trusted-lists.md#en-la-eudi-wallet).

Además del PID, la cartera guarda credenciales que acreditan otros atributos de personas físicas o jurídicas, como permisos de conducción, titulaciones académicas o cualificaciones profesionales. Las emiten autoridades públicas y entidades privadas y adoptan la forma de [declaraciones electrónicas de atributos](electronic-attestation-of-attributes.md) cualificadas o no cualificadas, sujetas a distintos requisitos y efectos jurídicos conforme al Reglamento eIDAS. Los casos de uso incluyen el acceso a servicios públicos y privados, la apertura de cuentas bancarias, los pagos, la firma de contratos, los viajes, la educación y la seguridad social, de acuerdo con la normativa aplicable.

Un principio especialmente relevante de la EUDI Wallet es la **minimización de datos**. Por ejemplo, para demostrar que una persona cumple un requisito de edad, no necesariamente tendría que revelar su fecha de nacimiento completa: podría presentar una prueba verificable de que **es mayor de 18 años**, evitando revelar información adicional que no sea necesaria para la operación.

Por tanto, la EUDI Wallet no debe entenderse simplemente como una versión digital de un documento de identidad, sino como una **infraestructura de identidad y credenciales digitales controlada por el usuario**, diseñada para permitir que diferentes entidades puedan emitir, solicitar y verificar información digital de forma segura e interoperable en toda la Unión Europea.

Su arquitectura y requisitos técnicos se definen en el **European Digital Identity Wallet Architecture and Reference Framework (ARF)**, desarrollado en el marco del Reglamento Europeo de Identidad Digital. El ARF establece la arquitectura, los componentes, las interacciones y los mecanismos de confianza necesarios para que las diferentes implementaciones nacionales sean interoperables.

### Referencias EUDI

- [European Digital Identity Wallet — Architecture and Reference Framework](https://eudi.dev/latest/main/01-introduction/?utm_source=chatgpt.com#11-eudi-wallet-ecosystem)
- [Comisión Europea — Aplicación de la cartera de identidad digital de la UE](https://digital-strategy.ec.europa.eu/es/policies/eudi-wallet-implementation)

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

### Referencias European Business Wallet

- [Propuesta de reglamento sobre las carteras empresariales europeas, COM(2025) 838, en EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=celex:52025PC0838)
- [Cartera empresarial europea en el tren legislativo del Parlamento Europeo](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-european-business-wallet)
- [Posición del Consejo sobre las carteras empresariales europeas](https://www.consilium.europa.eu/es/press/press-releases/2026/06/09/european-business-wallets-council-adopts-negotiating-position/)

---
