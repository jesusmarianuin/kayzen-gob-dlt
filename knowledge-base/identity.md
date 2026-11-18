# Identidad Web3

## Desambiguación de términos

Antes de continuar, debemos aclarar los términos técnicos que la identidad maneja para que no exista ambigüedad sobre lo que hablamos, porque solemos confundirlos o, sobre todo, tratarlos como si fueran lo mismo.

Un **identificador** es un código único que te representa en el sistema. Tu DNI, con su número y letra de control (12345678Z), funciona como tu identificador ante la Administración, un código que permite a los sistemas localizarte y comunicarse contigo. Este es un ejemplo simple, existen otros identificadores como el [DID (Decentralized Identifier)](https://www.w3.org/TR/did-core/). Lo importante es que un identificador no es una identidad, lo es según las relaciones que establecemos con él.

Un **certificado** en un ámbito mas general, se le conoce a aquel soporte físico o digital donde un hecho o afirmación de un sujeto existe, respaldado por una entidad de confianza para permitir su verificación. La idea general con la que podemos quedarnos es que el certificado es ese documento o archivo que, teniéndolo, nos da esa seguridad de validar ese hecho.
En el ámbito digital, **certificado electrónico** (término formal regulatorio) y **certificado digital** (término de uso común) suelen usarse como sinónimos. Su función principal es vincular una clave pública con la **identidad** de una persona física o jurídica mediante una Autoridad de Certificación (CA).

En su sentido más amplio, una **credencial** es cualquier prueba o artefacto (físico o digital) otorgado por una autoridad para que un tercero pueda confiar en quién eres o en qué derechos/atributos posees. Los participantes estáticos de una credencial son su emisor (issuer), el poseedor (holder) y el verificador (verifier); como procesos dinámicos sobre esa credencial tenemos la autenticación y la verificación.

La **autenticación** es el proceso de demostrar que controlas una credencial, el cual tiene **tres factores** o métodos para comprobarlo: algo que sabes, algo que tienes y algo que eres.

El primer factor, **algo que sabes**, son secretos como password, PINs o la frase semilla de una wallet. El password es el método de autenticación: el servidor verifica que conoces el secreto asociado a tu cuenta. La debilidad estructural de este factor es que el secreto puede robarse, filtrarse o adivinarse.

El segundo factor, **algo que tienes**, es el objeto físico o criptográfico que custodias. Ejemplos conocidos son el DNIe o, más significativo como factor adicional, las llaves Yubico. Aunque el ejemplo más ilustrativo de este factor es la evolución directa del password: las [passkeys](https://fidoalliance.org/passkeys/).

El tercer factor, **algo que eres**, son rasgos biométricos como huella dactilar, reconocimiento facial o iris. Es el factor más difícil de delegar, pero también el más difícil de revocar si se compromete: una contraseña se cambia, los dedos no. En la práctica su papel habitual es desbloquear localmente el segundo factor —la huella que libera la passkey en el smartphone, el reconocimiento facial que da acceso a la hardware wallet—, no actuar como credencial directa.

La **verificación**, en cambio, no la hace quien se autentica sino el *verifier*: es la comprobación de que la credencial en sí es válida —firma correcta, emisor de confianza, no revocada— con independencia de si quien la presenta ha demostrado controlarla. Autenticación y verificación son procesos complementarios: uno confirma a la persona, el otro confirma el documento.

Una **identidad** es la representación reconocible y significativa de quién eres en un contexto social. Conviene subrayarlo porque la identidad siempre depende del marco en el que se interpreta: en el ámbito legal, un identificador como el DNI puede operar como identidad por decisión institucional. También intervienen elementos de *marca personal* y la reputación que los demás asocian contigo. En muchos contextos no eres solo una persona, sino "la doctora X" o "el auditor Y". Por eso decimos que la identidad se construye y se verifica a partir de una o varias credenciales.

Una **Credencial Verificable (VC)** es el modelo de datos que W3C estandariza en su [Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/) para expresar afirmaciones (*claims*) sobre un sujeto, de forma que cualquiera pueda comprobar criptográficamente quién las emitió y que no se han alterado. Mantiene los mismos participantes estáticos de una credencial tradicional (*issuer*, *holder* y *verifier*), pero desacoplados: el *holder* custodia la credencial en su wallet y la presenta sin que el *issuer* intervenga en cada uso, aunque este conserva el control sobre su validez porque puede revocarla. Para comprobarla sin contactar con el *issuer*, el *verifier* se apoya en un cuarto rol, el [VDR (Verifiable Data Registry)](#vdr-verifiable-data-registry). Cuando el *holder* comparte una o varias credenciales, no las envía tal cual, sino que genera con ellas una Verifiable Presentation (VP). El intercambio de credenciales y presentaciones suele apoyarse en [OpenID4VC](https://openid.net/sg/openid4vc/), la familia de protocolos de la OpenID Foundation construida sobre OAuth 2.0, que define la emisión con [OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) y la presentación con [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html).

Una **Verifiable Presentation** (VP) es la otra pieza del mismo modelo de datos de W3C, la [estructura](https://www.w3.org/TR/vc-data-model/#verifiable-presentations) con la que el *holder* comparte con un *verifier* una o varias credenciales verificables, o solo datos derivados de ellas. Se distingue de la VC por quién la firma y para qué. La VC la firma el *issuer* y sirve mientras no caduque o se revoque, mientras que la VP la firma el *holder* para una presentación concreta ante un *verifier* concreto. Por eso no reenvía la credencial tal cual, sino que la envuelve, incluye solo los atributos que le piden cuando el formato lo permite (divulgación selectiva) y firma el conjunto con su propia clave junto a un valor de un solo uso (*nonce*) que fija el *verifier*, para que esa presentación no pueda reutilizarse. OpenID4VP usa el término en sentido amplio para cualquier formato, aunque en SD-JWT VC o mdoc esa estructura recibe otro nombre. Así, en una misma operación se resuelven los dos procesos dinámicos vistos antes: el *verifier* comprueba la firma del *issuer* sobre la credencial (verificación) y la firma del *holder* sobre la presentación (autenticación, porque demuestra que controla la clave a la que se emitió la credencial). El intercambio se hace habitualmente con [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html), la parte de OpenID4VC dedicada a las presentaciones.

Una **atestación** es un término conocido en la informática como el proceso por el que un sistema demuestra de forma verificable su estado o su integridad ante otro, aunque en identidad es una manifestación firmada de atributos que pueden ser verificados. En términos simples, es cuando un emisor —una universidad, un empleador, una organización o una administración pública— confirma algo sobre ti de forma verificable, por ejemplo, una universidad puede atestiguar que has completado un grado académico, o el Servicio Público de Empleo puede atestiguar que estás inscrito como demandante de empleo.

El concepto de atestación parece similar al de certificado electrónico, pero la diferencia es clara: con el principio de minimización de datos, la atestación surge como necesidad para acreditar atributos o hechos específicos (como la mayoría de edad o la posesión de un título), a diferencia del certificado electrónico, que acredita la identidad general del titular (nombre, NIF).

Es importante recalcar que una atestación se parece mucho a una credencial verificable (VC). Uno se pregunta por qué no usaron el término. Tanto eIDAS como EAS (en Web3) necesitaban representar atributos firmados, pero se encontraron con que el formato clásico de W3C (basado en JSON-LD) no era conveniente. Para eIDAS, el motivo de más peso es que no tenía un mecanismo estándar de divulgación selectiva, y además es más complejo de implementar. A esto se suma que eIDAS es tecnológicamente neutro, así que su término legal no podía depender de un estándar concreto. Por eso una atestación de eIDAS se codifica sobre todo en formatos más pragmáticos como SD-JWT VC (IETF) o mdoc (ISO), aunque el ARF también admite la versión 2.0 del modelo de W3C.

### La wallet

Una wallet es la aplicación con la que custodias y usas tus claves privadas para firmar, y esa firma es lo que demuestra que eres tú quien actúa. La wallet no siempre guarda la clave: puede estar en la propia aplicación, en el chip seguro del móvil, en un dispositivo físico como una Ledger o en manos de un tercero, y la wallet solo pide la firma. En identidad, además, la wallet guarda tus credenciales verificables para presentarlas cuando te las pidan.

**Custodia de claves en Wallet**:

Una **wallet custodial** delega la custodia de las claves privadas a un tercero. Tú accedes con usuario y contraseña, pero las claves que firman tus transacciones las guarda la plataforma. Ejemplos típicos son para Web3 en exchanges como [Coinbase](https://www.coinbase.com/) o [Binance](https://www.binance.com/). Si la plataforma cierra, te bloquea la cuenta o es hackeada, pierdes el acceso a tu identidad y fondos porque nunca tuviste las claves. Es el modelo más próximo a la banca tradicional.

Una **wallet self-custodial** (o *autocustodial*) es aquella en la que tú —y solo tú— controlas las claves privadas. La frase canónica del ecosistema es "not your keys, not your coins", y aplica igual a tu identidad: si no controlas las claves, no controlas el identificador. La [EUDI Wallet](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet) es un ejemplo, en Web3 [MetaMask](https://metamask.io/) es el ejemplo más representativo.

Una **wallet non-custodial** es una alternativa intermedia entre la wallet custodial y la autocustodia: ninguna entidad central guarda tu clave privada completa, sino que el control se reparte entre varias partes y ninguna lo tiene por sí sola. Así no dependes de un custodio, pero tampoco cargas con todo el riesgo de la autocustodia, como perder la única copia de la clave. La forma habitual de implementarla es [MPC (*Multi-Party Computation*)](https://en.wikipedia.org/wiki/Secure_multi-party_computation), una técnica criptográfica en la que la clave se reparte en fragmentos entre el usuario y uno o varios proveedores, de forma que ninguna parte puede firmar transacciones ni reconstruir la clave por sí sola: necesita la colaboración de las demás o de un número mínimo de ellas.

El modelo non-custodial no surge solo de una motivación técnica o de seguridad: tiene también una dimensión legal deliberada. Al distribuir el control entre varias partes sin que ninguna lo posea completamente, se elimina la figura del custodio —una entidad jurídicamente responsable a la que un regulador pueda señalar, reclamar o sancionar—.

## Identidad descentralizada

Uno de los objetivos declarados de [eIDAS 2.0 (Reglamento (UE) 2024/1183)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) es dar a los ciudadanos más control sobre su identidad digital y sus datos, hoy concentrados en buena parte en grandes plataformas, no solo por una busqueda de soberania estrategica, sino porque concentrar este control en manos de terceros genera vulnerabilidades sistémicas de seguridad y dependencia de las grandes plataformas.

El objetivo es que cada persona pueda poseer y gestionar su propia identidad bajo su control, vincular a ella credenciales de terceros que acrediten sus atributos y presentarlas a quien necesite verificarlas. En la práctica, esta visión no difiere radicalmente de lo que ya conocemos en el mundo físico con un pasaporte que te pertenece, del cual eres custodio, y donde acumulas sellos y validaciones que acreditan tus accesos.

La idea no nace con eIDAS 2.0. Procede de la [Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana, un principio que establece que los individuos deben tener control completo sobre sus credenciales y datos personales, y decidir cómo se comparten, sin depender de autoridades centrales para su validación o almacenamiento. El término lo popularizó Christopher Allen en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/).

eIDAS 2.0 recoge de SSI el control del usuario sobre sus credenciales, pero no la autosoberanía completa. El legislador europeo adopta la [identidad descentralizada](https://www.entrust.com/blog/2023/06/decentralized-identity) como infraestructura técnica, y mantiene bajo control institucional la confianza: emisores cualificados, certificación de wallets y listas de confianza gestionadas por los Estados miembros.

Ese estándar técnico fue definido por [W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, mediante dos especificaciones complementarias: los [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) definen cómo se componen y resuelven los identificadores descentralizados, y el modelo de [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) establece cómo estructurar credenciales que acrediten atributos de la identidad y, con las [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations), cómo presentarlas ante un verificador. Esta tecnología maximiza la privacidad mediante el control del usuario: las credenciales viven en su wallet y solo él decide cuándo y a quién mostrarlas.

En la EUDI Wallet, el [Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/) concreta estos conceptos con estándares ya existentes: SD-JWT VC e ISO/IEC 18013-5 (mdoc) para las atestaciones, con divulgación selectiva de atributos, y OpenID4VCI y OpenID4VP para su emisión y presentación. Los DIDs no son obligatorios, y las [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) se estudian como mejora para evitar que un verificador pueda correlacionar presentaciones.

### EUDI Wallet

La EUDI Wallet (European Digital Identity Wallet, Cartera Europea de Identidad Digital) es la wallet de identidad que introduce eIDAS 2.0. Es una aplicación bajo el control del usuario con la que guarda sus datos de identidad y sus credenciales y las presenta ante servicios públicos y privados de cualquier Estado miembro. También sirve para firmar con firma electrónica cualificada.

Nace porque la primera versión de eIDAS solo aseguraba el reconocimiento mutuo de los sistemas nacionales de identificación electrónica, como el DNIe, y cada uno funcionaba a su manera. Con la EUDI Wallet cada Estado ofrece al menos una cartera, pero todas siguen las mismas reglas y son interoperables en toda la UE. El reglamento fija los requisitos, y el ARF y los [actos de ejecución](eIDAS/implementing-acts.md) concretan formatos, protocolos y certificación.

> [Más detalle sobre la EUDI Wallet en eIDAS](eIDAS/README.md#cartera-europea-de-identidad-digital-eudi-wallet).

En la cartera, eIDAS distingue cuatro tipos de datos que se pueden guardar y presentar:

- PID (Person Identification Data, datos de identificación de la persona): los datos que permiten establecer la identidad de una persona física o jurídica, o de quien la representa. Es el equivalente digital del DNI, y la emite el Estado miembro o la entidad que este designe
- QEAA (atestación electrónica cualificada de atributos): la emite un prestador cualificado de servicios de confianza (QTSP) y tiene el mismo efecto jurídico que una atestación en papel emitida legalmente
- PuB-EAA (atestación electrónica de atributos del sector público): la emite un organismo público responsable de una fuente auténtica, como un registro oficial, o designado por el Estado miembro. Tiene el mismo efecto jurídico que la cualificada
- EAA no cualificada: la emite cualquier otro emisor. No se le puede negar efecto jurídico por ser electrónica, pero no tiene garantizado el mismo efecto que una atestación en papel

Entre las tres atestaciones, lo que las distingue es quién las emite, no el formato. Un mismo título universitario es una QEAA si lo emite un prestador cualificado y una EAA no cualificada si no lo es. El formato lo fija el [ARF](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/), que en su apartado 5.3.1 enumera tres para la wallet, ISO/IEC 18013-5 (mdoc), SD-JWT VC y W3C VCDM 2.0.

### Triángulo de confianza (credential trust triangle)

Patrón básico de las credenciales verificables, con tres roles:

- Emisor (issuer): firma y entrega la credencial
- Titular (holder): la guarda y la presenta
- Verificador (verifier): comprueba la firma y la validez de la credencial sin tener que contactar con el emisor

Para comprobar la credencial sin preguntar al emisor, el verificador necesita un sitio de confianza donde consultar con qué clave se firmó, si el emisor es de confianza y si la credencial sigue siendo válida. Cada marco lo resuelve a su manera: W3C con un Verifiable Data Registry (VDR), que se explica a continuación, y eIDAS con las [listas de confianza](eIDAS/trusted-lists.md) de los Estados miembros.

### VDR (Verifiable Data Registry)

En el triángulo de confianza, el verificador comprueba la credencial sin llamar al emisor. Para poder hacerlo necesita consultar información pública en algún sitio de referencia. Ese sitio es el VDR, un rol definido en el [modelo de credenciales verificables del W3C](https://www.w3.org/TR/vc-data-model/#roles).

El mundo físico ofrece una analogía: el banco que recibe un poder notarial no necesita contactar con el notario que lo autorizó. Le basta con consultar el registro de notarios para confirmar que está en activo, cotejar su firma con la registrada y comprobar que el poder no se ha revocado. Un VDR desempeña ese papel con las credenciales digitales: el verificador obtiene de él la clave pública del emisor y el estado de revocación, sin contactar con el emisor.

El verificador consulta el VDR para responder a cuatro preguntas:

- ¿Con qué clave compruebo la firma? El VDR asocia el identificador del emisor (por ejemplo, su DID) con su clave pública
- ¿Es un emisor de confianza? El VDR mantiene el registro de emisores autorizados a expedir cada tipo de credencial
- ¿Tiene la credencial la estructura correcta? El VDR publica los esquemas, es decir, qué campos debe contener cada tipo de credencial
- ¿Sigue siendo válida? El VDR publica las listas de revocación o suspensión

Un ejemplo completo: una universidad emite un título digital a una alumna, que lo guarda en su wallet. Años después lo presenta a una empresa. La empresa lee en el título el DID de la universidad, busca en el VDR su clave pública y verifica la firma; confirma en el registro de emisores que es una universidad acreditada; y comprueba en la lista de revocación que el título no se ha anulado. En ningún momento contacta con la universidad, que así no sabe quién, cuándo ni dónde ha usado su título la alumna.

El VDR nunca guarda las credenciales ni datos personales del titular, solo la información pública necesaria para verificarlas. Por eso puede ser compartido y consultable por cualquiera.

El W3C define qué función cumple el VDR, pero no cómo se implementa: puede ser una base de datos, una infraestructura de clave pública (PKI) o una blockchain. La blockchain aporta que ningún actor puede alterar el registro por su cuenta y que queda constancia de cada cambio. En el ecosistema europeo, la blockchain de [EBSI](eIDAS/ebsi.md) cumple este rol.

### TIR (Trusted Issuers Registry)

La firma de una credencial dice quién la emitió, pero no si ese emisor es de confianza. Para eso el verificador necesita un registro de emisores autorizados, la segunda de las preguntas que resuelve el VDR.

Como concepto, un registro de emisores de confianza no depende de la tecnología: puede ser una base de datos, un servicio web o una blockchain. El TIR (Trusted Issuers Registry) es el de EBSI, que lo implementa sobre su blockchain. No guarda credenciales, sino quién puede emitirlas: por cada emisor anota su DID y los tipos de credencial que está autorizado a emitir.

EBSI reparte el rol de VDR en varios registros, y el TIR es solo uno de ellos. El DID del emisor y sus claves públicas están en el registro de DIDs (DID Registry), y los esquemas de las credenciales, en el registro de esquemas (Trusted Schemas Registry). El DID es el nexo entre registros: el verificador lo lee en la credencial, obtiene la clave en el registro de DIDs para comprobar la firma y busca ese mismo DID en el TIR para saber si el emisor estaba acreditado.

La acreditación la da otra entidad ya acreditada (por ejemplo, un ministerio a una universidad), y así sucesivamente hasta una raíz reconocida por la gobernanza de EBSI. El resultado es una cadena de confianza que el verificador puede recorrer.

El TIR no es un término de eIDAS. En eIDAS el papel legal de decir qué emisores son de confianza lo cumplen las [listas de confianza](eIDAS/trusted-lists.md), basadas en certificados X.509 y no en DIDs. Que un emisor esté en el TIR de EBSI no da a sus credenciales el valor legal de una atestación cualificada de eIDAS.

Referencias:

- [modelo de confianza de EBSI (EBSI Hub)](https://hub.ebsi.eu/vc-framework/trust-model)
- [API del registro de emisores de confianza (EBSI Hub)](https://hub.ebsi.eu/api/core/issuers-registry)

## Contexto actual del ecosistema de identidad

Podemos ahora ver quién está construyendo en este espacio y desde qué posición.

**Las BigTech en web2: Siloed/Traditional**:

Por una parte, las grandes tecnológicas (*Big Tech*), dominadoras de la [Web2](https://ethereum.org/en/developers/docs/web2-vs-web3/) en plataformas centralizadas como redes sociales y servicios cloud, gestionan una identidad digital que no te pertenece realmente. Cuando creas una cuenta en Facebook, Google o cualquier plataforma digital, la empresa almacena tu información, controla el acceso a ella y puede modificarla, censurarla o eliminarla sin tu consentimiento previo. Esta fragmentación de identidad entre múltiples plataformas que no se comunican entre sí es lo que técnicamente se conoce como [siloed identity](hhttps://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186), donde cada servicio mantiene tu información aislada en su propio silo.

Este modelo centralizado genera varios problemas fundamentales. Primero, existe un riesgo de seguridad significativo porque todas tus credenciales están almacenadas en servidores centralizados que se convierten en objetivos atractivos para cyber criminales. Segundo, no tienes portabilidad: tu reputación en Amazon no sirve en eBay, tu historial profesional en LinkedIn no se transfiere a otras plataformas. Tercero, dependes completamente de la plataforma: si deciden cerrar tu cuenta, pierdes años de datos, conexiones y reputación acumulada. Esta dependencia crea lo que se denomina [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), donde quedas atrapado en el ecosistema de un proveedor específico sin capacidad real de migrar tu identidad y datos a alternativas.

Además, el modelo centralizado crea problemas de privacidad. Para usar la mayoría de servicios digitales, debes revelar más información de la necesaria. Si quieres entrar a un sitio para mayores de edad, tienes que proporcionar tu fecha de nacimiento completa cuando en realidad solo necesitan saber que eres mayor de 18 años.

**Identidad federada: cuando BigTech se convierte en el intermediario**:

La industria reconoció tempranamente que obligar a usuarios a crear cuentas separadas en cada sitio web era insostenible. La solución que emergió fue el modelo de identidad federada: permite que un proveedor de identidad externo actúe como intermediario de confianza. Cuando hoy encuentras botones de "Sign in with Google", "Sign in with Apple" o "Sign in with Facebook" en prácticamente cualquier aplicación o servicio digital, estás usando este modelo basado principalmente en [OpenID Connect (OIDC)](https://openid.net/connect/), una capa de identidad construida sobre [OAuth 2.0](https://oauth.net/2/) que extiende su framework de autorización con capacidades de autenticación. [SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) es un protocolo alternativo más antiguo que todavía se usa en contextos empresariales.

Este enfoque resolvió problemas prácticos significativos: ya no necesitas recordar docenas de contraseñas diferentes, ni repetir procesos de registro tediosos en cada sitio. Sin embargo, simplemente trasladó la centralización a un nivel superior. En lugar de tener tu identidad fragmentada en múltiples silos, ahora depende de un puñado de gigantes tecnológicos que actúan como guardianes. Google, Apple, Facebook y Microsoft se han convertido en los IDPs dominantes, intermediando la mayoría de relaciones digitales en Internet. Si una de estas compañías cierra tu cuenta o decide que no cumples sus términos de servicio, pierdes acceso simultáneamente a docenas o cientos de servicios que dependen de esa identidad federada.

En 2026, este modelo no solo persiste sino que se ha convertido en el método de autenticación más usado globalmente en aplicaciones Web.

**DID en Gobiernos y reguladores**:

La identidad descentralizada ha sido la opción adoptada por reguladores y gobiernos como marco normativo. La regulación [eIDAS 2.0](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) y su implementación mediante la European Digital Identity Wallet (EUDI Wallet) ofrecen un equilibrio entre el control institucional y la autonomía del usuario, materializando las tecnologías Decentralized Identifiers (DIDs), Verifiable Credentials (VCs) y Verifiable Presentations (VP) en un sistema con respaldo legal.

Respondiendo a las carencias del modelo Web2, la normativa europea eIDAS 2.0 establece que los Estados miembros deberán ofrecer la EUDI Wallet a finales de 2026, y a partir de finales de 2027 las plataformas de gran tamaño —Meta, Amazon, Apple, Booking.com, TikTok, Zalando y otras— estarán obligadas por ley a aceptarla como método válido de autenticación e identificación.»

El uso de la cartera digital europea es voluntario para los ciudadanos: los Estados miembros deben ofrecer métodos alternativos de identificación para quienes no deseen adoptarla. Sin embargo, la regulación cubre sectores tan amplios —banca, transporte, energía, seguridad social, sanidad, suministro de agua, infraestructura postal, infraestructura digital, educación y telecomunicaciones— que en la práctica se convierte en un estándar de facto para la identidad digital en Europa.

**DID soberano fuera de Europa: Bután y Buenos Aires**:

El modelo DID/VC no es exclusivo de Europa ni requiere el paraguas regulatorio de eIDAS para funcionar. Dos casos reales demuestran que gobiernos pueden adoptar identidad descentralizada con una filosofía más cercana a la visión SSI original, donde el protocolo es abierto y el Estado actúa como emisor de credenciales pero sin ser propietario ni intermediario permanente.

El [Sistema de Identidad Digital Nacional de Bután (NDI)](https://www.bhutanndi.com/) migró en octubre de 2025 desde Polygon a Ethereum mainnet, convirtiéndose en uno de los primeros sistemas de identidad nacional anclados directamente en la L1 de Ethereum. El sistema emite credenciales de ciudadanía, pasaporte e identidad oficial como Verifiable Credentials firmadas digitalmente en la wallet personal del ciudadano. La privacidad se implementa mediante Zero-Knowledge Proofs: un ciudadano puede demostrar que es mayor de edad o que es residente sin revelar su fecha de nacimiento exacta ni su número de identificación. Al anclar las pruebas criptográficas en Ethereum, cualquier parte puede verificar la autenticidad de las credenciales sin consultar a ninguna autoridad central butanesa, algo que eIDAS no permite porque mantiene listas de confianza gubernamentales como requisito de verificación.

[QuarkID](https://www.digitalpublicgoods.net/r/quarkid), desarrollado por la Secretaría de Innovación de la Ciudad de Buenos Aires, introduce un matiz arquitectónico especialmente relevante: el gobierno no es propietario del protocolo, sino un usuario más de él. Cuando el Gobierno de la Ciudad de Buenos Aires integró QuarkID en su aplicación oficial `miBA` en 2024, los más de 3,6 millones de usuarios recibieron identidades digitales descentralizadas para gestionar documentos civiles —certificados de nacimiento, matrimonio, defunción, registros fiscales, vacunación— como VCs en ZKSync Era, la L2 de Ethereum basada en ZK-proofs. La consecuencia de que el Gobierno de Buenos Aires sea "usuario del protocolo" y no su propietario es que ningún tercero, ni siquiera el propio gobierno, puede rastrear cuándo o para qué usa un ciudadano sus credenciales. QuarkID es open source y ha sido reconocido como [Bien Público Digital](https://www.digitalpublicgoods.net/) en el marco de los Objetivos de Desarrollo Sostenible de la ONU, lo que lo convierte en infraestructura reutilizable por cualquier gobierno sin licencias ni dependencia de un proveedor.

La diferencia estructural con eIDAS es precisamente esa: eIDAS impone un anillo de control institucional alrededor de la tecnología DID/VC mediante listas de emisores cualificados y certificación de wallets, lo que garantiza reconocimiento legal pero a costa de recentralizar la confianza en los estados. Bután y Buenos Aires demuestran que es posible emitir credenciales con validez real sin ese anillo, dejando la verificación criptográfica en manos del protocolo abierto.

**OpenID4VC: cuando los IDPs se transforman en emisores de credenciales**:

Por otra parte, el estándar [OpenID4VC (OpenID for Verifiable Credentials)](https://openid.net/sg/openid4vc/) está transformando el panorama al convertir IDPs (proveedores de identidad) tradicionales en VC (emisores de credenciales verificables). Esto significa que Google o Apple pueden emitir VCs que el usuario guarda en su wallet Web3 o [EUDI Wallet europeo](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet), creando un puente entre la identidad federada Web2 y las credenciales autosoberanas.

La diferencia fundamental con la federación tradicional es arquitectónica: en lugar de que Google intermedie cada login manteniendo control perpetuo, ahora Google puede emitir una credencial verificable una vez que tú guardas en tu wallet y presentas donde quieras sin su participación posterior. El IDP sigue siendo el emisor inicial, pero pierde el rol de intermediario permanente que caracteriza a la federación clásica.

Eso no significa que desaparezcan los intermediarios. La cartera elimina el intermediario técnico de cada autenticación, pero no el económico. Las plataformas dejan de competir por el inicio de sesión y pasan a competir por la interfaz en la que se guardan y presentan las credenciales. Entre la cartera y las partes usuarias aparecen además nuevos actores que ofrecen la verificación como servicio. La intermediación no desaparece, cambia de sitio.

La distinción crucial es que eIDAS 2.0 establece dos niveles de confianza: **credenciales cualificadas**, emitidas por Qualified Trust Service Providers (QTSPs) certificados bajo eIDAS con reconocimiento legal pleno en toda la UE, y **credenciales no cualificadas**, emitidas por proveedores privados, técnicamente compatibles con EUDI Wallet pero sin el mismo peso legal que las gubernamentales. Para casos críticos como identidad oficial o edad legal, predominarán las credenciales cualificadas; para casos de uso menos regulados como membresías o reputación, las credenciales privadas seguirán siendo válidas y útiles.

**Web3**:

Web3 es un ecosistema permissionless, abierto a cualquier persona y economía, que ya está tokenizando activos financieros de EEUU, como los bonos del Tesoro. En él, la identidad sigue varias vías.

La primera suelen ser las rampas de salida o entrada o salida donde la identidad se basa en cualquier identidad federada de Web2 tradicional, y es así por obligación legal de [KYC](https://en.wikipedia.org/wiki/Know_your_customer) (Know Your Customer) y [AML](https://en.wikipedia.org/wiki/Money_laundering#Anti-money_laundering) (Anti-Money Laundering) donde exigen adicionalmente documento de identidad y, según el riesgo e importe, prueba de domicilio y justificación del origen de los fondos, datos que quedan almacenados en los servidores del proveedor. Es así porque en la UE, los proveedores autorizados bajo [MiCA (Reglamento (UE) 2023/1114)](https://eur-lex.europa.eu/eli/reg/2023/1114/oj) son sujetos obligados de prevención del blanqueo, y la Travel Rule del [Reglamento (UE) 2023/1113](https://eur-lex.europa.eu/eli/reg/2023/1113/oj) les obliga a identificar a ordenante y beneficiario en cada transferencia de criptoactivos.

De manera más marginal existe un modelo de identificación Web3 mas institucional, siendo descentralizado, basada en DID con Verifiable Credentials (VCs) custodiadas por el propio usuario fuera de la cadena, que se presentan selectivamente mediante Zero-Knowledge Proofs. Proyectos como Privado ID (antes Polygon ID) son el mejor ejemplo, mientras que emisores VC como Fractal ID o Civic actúan como puente pragmático entre identidad legal y ecosistema descentralizado, mejorando la experiencia de usuario, pero sin eliminar la centralización de fondo.

La identificación más habitual en Web3 y usada en mayor parte para DeFi, que son las financias abiertas y sin pedir permiso, son mediante la [wallet Web3](https://ethereum.org/wallets/find-wallet/), donde la identidad no la emite nadie. La identidad se basa también en la reputación que se acumula como un rastro verificable on-chain en las DAOs a las que se pertenece, los eventos a los que se asiste, las votaciones de gobernanza o los protocolos que se usan. Es la idea que Vitalik Buterin, E. Glen Weyl y Puja Ohlhaver plantearon en el paper [DeSoc (Decentralized Society)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) de 2022, con tokens intransferibles (Soulbound Tokens) para representarla. A esa idea se suman piezas como los [POAPs](https://poap.xyz/) (NFTs, transferibles, que acreditan la asistencia a un evento), las [atestaciones EAS](https://attest.org/) o protocolos sociales como [Lens](https://www.lens.xyz/) y [Farcaster](https://www.farcaster.xyz/). La capa de nombres la aporta [ENS (Ethereum Name Service)](https://docs.ens.domains/), que asocia a la dirección un nombre legible (ejemplo alice.eth). Toda esa identidad queda atada a una dirección y perderla era perderlo todo, motivo que surgen las smart contract wallets, donde la identidad vive on-chain facilitando la experiencia de usuario y permitiendo el on-boarding, es decir, acceso mediante Wallets non-custodial donde incluso el login puede ser mediante tú cuenta de Google o Apple y donde tienes recuperación social de claves.

## Seudónimos y seudonimato

Muchas operaciones no necesitan saber quién eres, solo que eres la misma persona que la última vez o que cumples un requisito, como ser mayor de edad. Para eso existen los seudónimos, y eIDAS 2.0 los incorpora de forma expresa.

El seudónimo es el punto intermedio entre la identificación y el anonimato. Al identificarte, la acción queda ligada a tu identidad real, como al firmar con certificado electrónico o iniciar un trámite. En el anonimato no queda ligada a nada, y nadie puede saber quién eres ni que dos acciones son de la misma persona. Con un seudónimo, la acción queda ligada a un identificador estable que no revela quién eres pero permite reconocerte, y por eso sirve para mantener una cuenta, una reputación o un historial. No es anonimato, porque alguien puede tener la información para volver a vincularlo con la persona (reidentificación), y confundirlos lleva a errores técnicos y legales.

No todos protegen igual. La diferencia está en cuántos servicios ven el mismo seudónimo:

- Global: el mismo en todos los servicios, lo que permite cruzar información y construir un perfil. Una dirección de wallet Web3 es el ejemplo típico
- Por relación (*pairwise*): uno distinto por servicio, así que dos servicios no pueden saber que tratan con la misma persona. OpenID Connect lo contempla con los [identificadores de sujeto por pares (pairwise subject identifiers)](https://openid.net/specs/openid-connect-core-1_0.html#PairwiseAlg) y es el modelo de las [passkeys](https://fidoalliance.org/passkeys/), que generan una clave para cada sitio
- De un solo uso: uno nuevo en cada operación. Se acerca al anonimato, pero no sirve para mantener una cuenta, y quien lo genera puede conservar la relación con la persona

### Seudónimos en eIDAS 2.0

[eIDAS 2.0 (Reglamento (UE) 2024/1183)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) trata los seudónimos en tres niveles:

- Derecho del usuario (artículo 5): puede usar seudónimos salvo que una ley europea o nacional le obligue a identificarse, y cada Estado decide qué validez legal tienen. El seudónimo es la regla y la identificación, la excepción que necesita base legal
- Función de la wallet (artículo 5 bis): la EUDI Wallet debe generar seudónimos y guardarlos cifrados en local. Su marco técnico no puede permitir a emisores ni a terceros rastrear, vincular o correlacionar las operaciones del usuario cuando la atestación no requiera identificarle (no vinculabilidad, *unlinkability*)
- Obligación de las partes usuarias (artículo 5 ter): los servicios que piden datos a la wallet (*relying parties*) no pueden rechazar un seudónimo si la ley no exige identificar al usuario. Además deben registrarse en su Estado declarando qué datos piden y para qué, y la wallet se lo muestra al usuario antes de compartir nada

Las excepciones más relevantes para la Administración y para DLT son:

- Procedimiento administrativo: la [Ley 39/2015](https://www.boe.es/eli/es/l/2015/10/01/39/con) regula en su artículo 9 cómo se identifica a los interesados, porque un trámite con efectos jurídicos requiere saber quién es
- Prevención del blanqueo: el KYC y la Travel Rule del [Reglamento (UE) 2023/1113](https://eur-lex.europa.eu/eli/reg/2023/1113/oj), vistos en el apartado de Web3
- Firma electrónica cualificada: su valor legal está precisamente en vincular el documento con una persona identificada

Fuera de estos casos, pedir la identidad completa cuando basta un seudónimo o un atributo choca con el artículo 5 ter de eIDAS y con el principio de minimización del RGPD (artículo 5.1.c).

En la práctica, el [Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/) plantea implementar estos seudónimos sobre WebAuthn, el estándar de las passkeys: uno por servicio, generado por la wallet sin intervención de ningún emisor. Para la verificación de edad, la Comisión Europea publicó en 2025 una solución de referencia (*blueprint*) compatible con la EUDI Wallet, en cuyo piloto participa España, que permite demostrar la mayoría de edad sin revelar nombre ni fecha de nacimiento. Es la minimización de datos vista en la definición de [atestación](#desambiguación-de-términos): se acredita el atributo, no la identidad.

### Seudonimización en el RGPD

El [RGPD (Reglamento (UE) 2016/679)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) no habla de seudónimos elegidos por el usuario, sino de seudonimización, una técnica de tratamiento por la que los datos ya no pueden atribuirse a una persona sin información adicional guardada por separado y protegida (artículo 4.5). Es una medida recomendada de protección desde el diseño (artículo 25) y de seguridad (artículo 32), pero los datos seudonimizados siguen siendo datos personales (considerando 26). Solo los anónimos, que no permiten identificar a nadie por medios razonables, quedan fuera del RGPD.

El Comité Europeo de Protección de Datos (CEPD) publicó en enero de 2025 sus directrices 01/2025 sobre seudonimización, y el Tribunal de Justicia de la UE matizó el criterio en el asunto C-413/23 P (SEPD contra SRB, septiembre de 2025): los datos seudonimizados pueden no ser datos personales para un destinatario sin medios razonables para reidentificar. Depende, por tanto, de quién los tiene.

### Seudónimos en Web3

En Web3 el seudonimato es el modelo por defecto, pero con un seudónimo global y un historial público y permanente. Basta con vincular la dirección a una persona una vez, por ejemplo al pasar por un exchange con KYC, para asociarle todo su historial pasado y futuro, y hay empresas especializadas en ese análisis de cadena (*chain analysis*). Por eso el CEPD, en sus directrices 02/2025 sobre blockchain (abril de 2025), considera que las direcciones pueden ser datos personales. Como eso choca con la inmutabilidad de la cadena y con el derecho de supresión, recomienda no registrar datos personales on-chain, ni siquiera seudonimizados, cuando pueda evitarse. eIDAS hace lo contrario: identidad fuerte cuando la ley la exige y seudónimos por servicio, sin rastro público, para todo lo demás.

### Retos

- Vinculabilidad de los formatos: SD-JWT VC y mdoc permiten la divulgación selectiva, pero al presentar varias veces la misma credencial se repiten su firma y sus valores, y varios verificadores de acuerdo pueden correlacionar al usuario. El ARF lo mitiga emitiendo credenciales en lotes de un solo uso, y se estudian firmas compatibles con Zero-Knowledge Proofs (como BBS+) que lo eviten de raíz
- Reidentificación por combinación: varios atributos juntos (código postal, edad, profesión) pueden identificar aunque ninguno lo haga por sí solo. Minimizar no es solo ocultar el nombre
- Partes usuarias que piden de más: el registro obligatorio y lo que muestra la wallet buscan frenarlo, pero su eficacia depende de la supervisión de cada Estado
- Financiación sin observación: si se cobra por operación, alguien tiene que contar las presentaciones, y eso choca con que nadie pueda rastrear ni correlacionar las operaciones del usuario
- Responsabilidad y abuso: un seudónimo también puede amparar fraudes o acoso, y sigue abierto el equilibrio entre privacidad y reidentificación con orden legal
- DLT en la Administración: en una red pública o de consorcio, un hash o identificador seudonimizado registrado on-chain sigue siendo dato personal si alguien puede reidentificarlo, y no se podrá borrar

Referencias:

- [eIDAS 2.0, Reglamento (UE) 2024/1183 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [RGPD, Reglamento (UE) 2016/679 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [marco de arquitectura y referencia de la EUDI Wallet (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/)
- [directrices del CEPD (EDPB)](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en)

## Identidad de los agentes de IA

Un agente de IA es software que usa un modelo de lenguaje para decidir y ejecutar acciones con cierta autonomía, como llamar a APIs, usar herramientas, leer y escribir datos o comunicarse con otros agentes, normalmente en nombre de una persona u organización. Plantea las mismas preguntas que el resto del documento, pero sin una persona física detrás de cada acción: quién actúa, en nombre de quién, con qué permisos y quién responde. Es un área que evoluciona rápido, y lo que sigue refleja el estado a mediados de 2026, distinguiendo lo que ya es estándar de lo que todavía es propuesta.

Al hablar de la identidad de un agente se suelen mezclar tres identidades:

- Del modelo: qué modelo es y quién lo desarrolla (por ejemplo, Claude, de Anthropic). Es una identidad de producto, no criptográfica, y el modelo no tiene claves, credenciales ni memoria entre sesiones salvo que el despliegue se las dé
- De la instancia o despliegue: el software concreto que ejecuta el modelo con su configuración, sus herramientas y sus permisos. Es la que se autentica ante otros servicios, como cualquier aplicación
- Del principal: la persona física o jurídica en cuyo nombre actúa el agente, que le delega los permisos y responde jurídicamente de lo que hace

Funciona como un poder notarial para firmar la venta de un piso: el agente es el apoderado y el principal, el titular. El apoderado solo puede hacer lo que el poder le permite y el titular puede retirárselo cuando quiera. Por eso quien recibe una petición de un agente necesita comprobar qué agente la hace y en nombre de quién.

El marco europeo todavía no da identidad propia a los agentes. El [Reglamento de Inteligencia Artificial (Reglamento (UE) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) obliga en su artículo 50 a que los sistemas de IA que interactúan con personas físicas les hagan saber que hablan con una IA, salvo que sea evidente, pero es una obligación de transparencia, no un sistema de identificación. [eIDAS 2.0](eIDAS/README.md#eidas2) emite la EUDI Wallet y los certificados cualificados a personas físicas y jurídicas, así que un agente solo puede apoyarse en las credenciales de la persona u organización a la que representa, y la responsabilidad recae en ella.

### Delegación frente a suplantación

Lo más sencillo, y lo más peligroso, es entregar al agente las credenciales del usuario (su contraseña, su API key o su clave privada). El agente pasa a suplantarle: el servicio no distingue quién actúa, los permisos no se pueden acotar y revocar al agente obliga a cambiar la credencial del usuario.

La alternativa es la delegación, en la que el agente recibe una credencial propia, limitada a lo que necesita (mínimo privilegio), de caducidad corta y revocable sin afectar al usuario. OAuth ya lo expresa con [OAuth 2.0 Token Exchange (RFC 8693)](https://www.rfc-editor.org/rfc/rfc8693), cuya claim `act` (actor) indica a la vez el sujeto en cuyo nombre se actúa y el actor que hace la petición. En Web3 la identidad del agente es la de la dirección y la cadena no distingue si firma un humano o un agente, así que las smart contract wallets delegan con claves de sesión, claves secundarias con permisos, importes y caducidad limitados por el propio contrato que el agente recibe sin la clave principal.

La delegación también limita el daño de la inyección de instrucciones (*prompt injection*), en la que un agente que lee contenido de terceros es manipulado por instrucciones escondidas en él. El atacante hereda los permisos del agente, y cuanto más acotados estén, menos daño puede hacer.

### Estándares y propuestas en marcha

Los más relevantes, de los protocolos entre agentes a la identidad on-chain:

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/): protocolo abierto que Anthropic publicó en noviembre de 2024 para conectar agentes con herramientas y fuentes de datos, transferido en diciembre de 2025 a la Agentic AI Foundation, bajo la Linux Foundation. Su [especificación de autorización](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) se apoya en OAuth 2.1, con el servidor MCP como servidor de recursos
- [Agent2Agent (A2A)](https://github.com/a2aproject/A2A): protocolo que Google presentó en abril de 2025 para que se comuniquen agentes de distintos proveedores, transferido a la Linux Foundation en junio de 2025. Cada agente publica una Agent Card, un JSON con sus capacidades, su punto de acceso y la autenticación que exige
- [SPIFFE](https://spiffe.io/): estándar de la CNCF (la fundación que mantiene Kubernetes) que da a cada carga de trabajo (*workload*), sea un servicio, un contenedor o un proceso, un identificador y un certificado de corta duración que se renueva solo, en lugar de una contraseña o API key fija. En agentes permite identificar cada instancia sin darle secretos que puedan filtrarse
- Web Bot Auth: propuesta de Cloudflare presentada en el IETF en 2025 para que bots y agentes firmen sus peticiones HTTP con [HTTP Message Signatures (RFC 9421)](https://www.rfc-editor.org/rfc/rfc9421), de modo que el sitio sepa qué agente le visita sin deducirlo de la IP o del user agent
- IdPs empresariales: empiezan a tratar a los agentes como un tipo de identidad propio, distinto de usuarios y aplicaciones, como Microsoft Entra Agent ID, anunciado en 2025
- Credenciales verificables: el principal puede emitir al agente una credencial que acredite qué puede hacer en su nombre. Agent Payments Protocol (AP2), presentado por Google en septiembre de 2025, lo aplica a pagos firmando la instrucción del usuario como un mandato verificable que el agente presenta al comercio
- [ERC-8004 (Trustless Agents)](https://eips.ethereum.org/EIPS/eip-8004): propuesta de Ethereum en borrador (agosto de 2025) que complementa protocolos como A2A con tres registros on-chain, de identidad (un identificador que apunta a la descripción del agente), de reputación (valoraciones de quienes han interactuado con él) y de validación (verificación independiente de su trabajo). Recuerda al [TIR de EBSI](#tir-trusted-issuers-registry) aplicado a agentes, pero en un entorno permissionless donde cualquiera se registra y la confianza se apoya en la reputación y la validación, no en la acreditación institucional

La OpenID Foundation, que mantiene OpenID Connect, concluye en su informe "Identity Management for Agentic AI" (octubre de 2025) que OAuth y OpenID Connect ya sirven para buena parte de los usos de agentes, pero no resuelven tres de los [problemas abiertos](#problemas-abiertos): las cadenas de delegación, el consentimiento y la revocación.

### Problemas abiertos

- Cadenas de delegación: cuando un agente delega en otro, el último de la cadena debe conservar la referencia al principal original y no puede tener más permisos que quien le delegó
- Revocación: retirar los permisos de un agente en todos los servicios en los que actúa, de forma inmediata
- Consentimiento: el usuario no puede aprobar cada acción, pero tampoco debería firmar permisos en blanco
- Distinguir humano y agente: los servicios necesitan saberlo para aplicar límites, cumplir obligaciones de transparencia y atribuir responsabilidades
- Responsabilidad: quién responde cuando un agente con permisos legítimos causa un daño, si el principal, el desarrollador del modelo o quien lo despliega

Referencias:

- [principios con los que Anthropic entrena a Claude (Anthropic)](https://www.anthropic.com/news/claudes-constitution)
- [autorización en MCP (especificación)](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- [ERC-8004: Trustless Agents (EIPs de Ethereum)](https://eips.ethereum.org/EIPS/eip-8004)

---
