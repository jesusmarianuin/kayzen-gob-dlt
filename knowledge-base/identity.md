# Identidad Web3

## Desambiguación de términos

Antes de continuar, debemos aclarar los términos técnicos que la identidad maneja para que no exista ambigüedad sobre lo que hablamos, porque solemos confundirlos o, sobre todo, tratarlos como si fueran lo mismo.

Los conceptos parten de una idea fundamental que todos podemos relacionar con el mundo real. Sin embargo, debemos distinguir entre lo que conocemos con su definición digital, formal o regulatoria. Cada institución, norma o regulador puede adoptar un término general y delimitar su significado en función de sus objetivos y necesidades. Por tanto, una definición no es necesariamente ambigua en sí misma, sino que puede resultar ambigua cuando no se especifica el contexto en el que se utiliza.
Para evitarlo, estableceremos primero el contexto y después definiremos cada concepto. Esto es especialmente importante en el ámbito de la identidad electrónica, donde términos como certificado, credencial, firma y atestación tienen significados que pueden diferir de su interpretación general y de los utilizados en otros ámbitos técnicos o jurídicos.

Un **identificador** es un código único que te representa en el sistema. Tu DNI, con su número y letra de control (12345678Z), funciona como tu identificador ante la Administración, un código que permite a los sistemas localizarte y comunicarse contigo. Este es un ejemplo simple, existen otros identificadores como el [DID (Decentralized Identifier)](https://www.w3.org/TR/did-core/). Lo importante es que un identificador no es una identidad, lo es según las relaciones que establecemos con él.

Una **atestación**, o más concretamente, una atestación electrónica, no nace de un único marco, sino que converge desde el regulatorio (eIDAS, con la “Electronic Attestation of Attributes”), el técnico (client attestation en OAuth y OpenID4VC) y, en paralelo, Web3 (EAS).
En términos simples, es cuando un emisor —una universidad, un empleador, una organización o una administración pública— confirma algo sobre ti de forma verificable. Por ejemplo, una universidad puede atestiguar que has completado un grado académico, o el Servicio Público de Empleo puede atestiguar que estás inscrito como demandante de empleo.
En esta definición no hablamos de su formato ni de su implementación técnica, sino de qué es y qué finalidad tiene. La forma de representarla, firmarla, almacenarla o verificarla corresponde a su implementación técnica. Además, aunque es habitual utilizar firmas o sellos electrónicos para garantizar su autenticidad e integridad, no conviene definir toda atestación como necesariamente firmada digitalmente.

Un **certificado** en un ámbito mas general, se le conoce a aquel soporte físico o digital donde un hecho o afirmación de un sujeto existe, respaldado por una entidad de confianza para permitir su verificación. La idea general con la que podemos quedarnos es que el certificado es ese documento o archivo que, teniéndolo, nos da esa seguridad de validar ese hecho.
En el ámbito digital, **certificado electrónico** (término formal regulatorio) y **certificado digital** (término de uso común) suelen usarse como sinónimos. Su función principal es vincular una clave pública con la **identidad** de una persona física o jurídica mediante una Autoridad de Certificación (CA).
El concepto de atestación parece similar al de certificado electrónico, pero la diferencia es clara: con el principio de minimización de datos, la atestación surge como necesidad para acreditar atributos o hechos específicos (como la mayoría de edad o la posesión de un título), a diferencia del certificado electrónico, que acredita la identidad general del titular (nombre, NIF).

En su sentido más amplio, una **credencial** es cualquier prueba o artefacto (físico o digital) otorgado por una autoridad para que un tercero pueda confiar en quién eres o en qué derechos/atributos posees. Los participantes estáticos de una credencial son su emisor (issuer), el poseedor (holder) y el verificador (verifier); como procesos dinámicos sobre esa credencial tenemos la autenticación y la verificación.

La **autenticación** es el proceso de demostrar que controlas una credencial, el cual tiene **tres factores** o métodos para comprobarlo: algo que sabes, algo que tienes y algo que eres.

El primer factor, **algo que sabes**, son secretos como password, PINs o la frase semilla de una wallet. El password es el método de autenticación: el servidor verifica que conoces el secreto asociado a tu cuenta. Protocolos como [OAuth 2.0](https://oauth.net/2/) y [OpenID Connect](https://openid.net/connect/) construyen sobre este modelo mecanismos de federación de identidad ("Sign in with Google"), delegando la autenticación en un tercero —sea cual sea el factor que ese tercero use para autenticarte—. La debilidad estructural de este factor es que el secreto puede robarse, filtrarse o adivinarse.

El segundo factor, **algo que tienes**, es el objeto físico o criptográfico que custodias. Ejemplos conocidos son el DNIe o, más significativo como factor adicional, las llaves Yubico. Aunque el ejemplo más ilustrativo de este factor es la evolución directa del password: las [passkeys](https://fidoalliance.org/passkeys/).

El tercer factor, **algo que eres**, son rasgos biométricos como huella dactilar, reconocimiento facial o iris. Es el factor más difícil de delegar, pero también el más difícil de revocar si se compromete: una contraseña se cambia, los dedos no. En la práctica su papel habitual es desbloquear localmente el segundo factor —la huella que libera la passkey en el smartphone, el reconocimiento facial que da acceso a la hardware wallet—, no actuar como credencial directa.

La **verificación**, en cambio, no la hace quien se autentica sino el *verifier*: es la comprobación de que la credencial en sí es válida —firma correcta, emisor de confianza, no revocada— con independencia de si quien la presenta ha demostrado controlarla. Autenticación y verificación son procesos complementarios: uno confirma a la persona, el otro confirma el documento.

Como aclaraciones, en el sentido amplio empleado aquí: un certificado digital y atestación es un tipo de credencial.

Una **identidad** es la representación reconocible y significativa de quién eres en un contexto social. Conviene subrayarlo porque la identidad siempre depende del marco en el que se interpreta: en el ámbito legal, un identificador como el DNI puede operar como identidad por decisión institucional. También intervienen elementos de *marca personal* y la reputación que los demás asocian contigo. En muchos contextos no eres solo una persona, sino "la doctora X" o "el auditor Y". Por eso decimos que la identidad se construye y se verifica a partir de una o varias credenciales.

Una **Credencial Verificable** (VC) surge cuando W3C necesita definir un estándar para una credencial más descentralizada, autoverificable y con la mínima información posible. Aunque mantiene los mismos participantes estáticos de una credencial tradicional (*issuer*, *holder* y *verifier*), estos actúan de forma desacoplada: el *holder* custodia la credencial en su billetera sin depender del *issuer* para gestionar su identidad. Como proceso dinámico de uso sobre esa credencial tenemos la **Verifiable Presentation** (VP). Adicionalmente las **OpenID4VC** como el puente entre OpenID y las credenciales verificables.

Una **Verifiable Presentation** (VP) es el paquete que el *holder* construye para mostrar una o varias credenciales verificables a un *verifier*. No reenvía la credencial tal cual: la envuelve, incluye solo los atributos que le piden cuando el formato lo permite (divulgación selectiva) y, normalmente, firma el conjunto con su propia clave junto a un valor de un solo uso (*nonce*) que fija el *verifier*, para que esa presentación no pueda reutilizarse. Así, en una misma operación se resuelven los dos procesos dinámicos vistos antes: el *verifier* comprueba la firma del *issuer* sobre la credencial (verificación) y la firma del *holder* sobre la presentación (autenticación, porque demuestra que controla la clave a la que se emitió la credencial). El intercambio se hace habitualmente con [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html), la parte de OpenID4VC dedicada a las presentaciones.

La relación con la atestación es de capas: la atestación es lo que el emisor afirma sobre ti (que tienes un grado, que eres mayor de edad), la VC es una forma técnica de representar esa afirmación de manera firmada y verificable, y la VP es el acto de mostrarla a quien la pide. Por ejemplo, la universidad emite la atestación de tu grado como VC a tu wallet y, cuando una empresa la solicita, tu wallet genera una VP con solo el título y la fecha, firmada por ti. En eIDAS 2.0 ocurre lo mismo con las atestaciones electrónicas de atributos que guarda la EUDI Wallet, aunque allí no se usa solo el modelo W3C: también se emplean los formatos SD-JWT VC y mdoc (ISO/IEC 18013-5).

**La wallet**:

Una wallet es la aplicación con la que custodias y usas tus claves privadas para firmar, y esa firma es lo que demuestra que eres tú quien actúa. La wallet no siempre guarda la clave: puede estar en la propia aplicación, en el chip seguro del móvil, en un dispositivo físico como una Ledger o en manos de un tercero, y la wallet solo pide la firma. En identidad, además, la wallet guarda tus credenciales verificables para presentarlas cuando te las pidan.

**Custodia de claves en Wallet**:

Una **wallet custodial** delega la custodia de las claves privadas a un tercero. Tú accedes con usuario y contraseña, pero las claves que firman tus transacciones las guarda la plataforma. Ejemplos típicos son para Web3 en exchanges como [Coinbase](https://www.coinbase.com/) o [Binance](https://www.binance.com/). Si la plataforma cierra, te bloquea la cuenta o es hackeada, pierdes el acceso a tu identidad y fondos porque nunca tuviste las claves. Es el modelo más próximo a la banca tradicional.

Una **wallet self-custodial** (o *autocustodial*) es aquella en la que tú —y solo tú— controlas las claves privadas. La frase canónica del ecosistema es "not your keys, not your coins", y aplica igual a tu identidad: si no controlas las claves, no controlas el identificador. La [EUDI Wallet](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet) es un ejemplo, en Web3 [MetaMask](https://metamask.io/) es el ejemplo más representativo.

Una **wallet non-custodial** es una alternativa intermedia entre la wallet custodial y la autocustodia: ninguna entidad central guarda tu clave privada completa, sino que el control se reparte entre varias partes y ninguna lo tiene por sí sola. Así no dependes de un custodio, pero tampoco cargas con todo el riesgo de la autocustodia, como perder la única copia de la clave. La forma habitual de implementarla es [MPC (*Multi-Party Computation*)](https://en.wikipedia.org/wiki/Secure_multi-party_computation), una técnica criptográfica en la que la clave se reparte en fragmentos entre el usuario y uno o varios proveedores, de forma que ninguna parte puede firmar transacciones ni reconstruir la clave por sí sola: necesita la colaboración de las demás o de un número mínimo de ellas.

El modelo non-custodial no surge solo de una motivación técnica o de seguridad: tiene también una dimensión legal deliberada. Al distribuir el control entre varias partes sin que ninguna lo posea completamente, se elimina la figura del custodio —una entidad jurídicamente responsable a la que un regulador pueda señalar, reclamar o sancionar—.

## Identidad descentralizada

Uno de los objetivos fundamentales de [eIDAS 2.0 (Reglamento (UE) 2024/1183)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) es devolver a los ciudadanos el control de su identidad digital y de sus datos, no solo por soberanía personal, sino porque concentrar este control en manos de terceros genera vulnerabilidades sistémicas de seguridad y dependencia de las grandes plataformas.

El objetivo es que cada persona pueda poseer y gestionar su propia identidad bajo su control, vincular a ella credenciales de terceros que acrediten sus atributos y presentarlas a quien necesite verificarlas. En la práctica, esta visión no difiere radicalmente de lo que ya conocemos en el mundo físico: posees un DNI en España o un pasaporte que te pertenece, del cual eres custodio, y donde acumulas sellos y validaciones que acreditan tus accesos.

La idea no nace con eIDAS 2.0. Procede de la [Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana, un principio que establece que los individuos deben tener control completo sobre sus credenciales y datos personales, y decidir cómo se comparten, sin depender de autoridades centrales para su validación o almacenamiento. El término lo popularizó Christopher Allen en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/).

eIDAS 2.0 recoge de SSI el control del usuario sobre sus credenciales, pero no la autosoberanía completa. El legislador europeo adopta la [identidad descentralizada](https://www.entrust.com/blog/2023/06/decentralized-identity) como infraestructura técnica, y mantiene bajo control institucional la confianza: emisores cualificados, certificación de wallets y listas de confianza gestionadas por los Estados miembros.

Ese estándar técnico fue definido por [W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, mediante tres especificaciones complementarias: los [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) definen cómo se componen y resuelven los identificadores descentralizados, las [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) establecen cómo estructurar credenciales que acrediten atributos de la identidad, y las [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations) definen cómo presentarlas selectivamente ante un verificador. Esta tecnología maximiza la privacidad mediante el control del usuario: las credenciales viven en su wallet, solo él decide cuándo y a quién mostrarlas, y puede revelar únicamente los atributos necesarios.

En la EUDI Wallet, el [Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/) concreta estos conceptos con formatos y protocolos propios: SD-JWT VC e ISO/IEC 18013-5 (mdoc) para las credenciales, con divulgación selectiva de atributos, y OpenID4VCI y OpenID4VP para su emisión y presentación. Los DIDs no son obligatorios, y las [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) se estudian como mejora para evitar que un verificador pueda correlacionar presentaciones.

### Triángulo de confianza (credential trust triangle)

Patrón básico de las credenciales verificables, con tres roles:

- Emisor (issuer): firma y entrega la credencial
- Titular (holder): la guarda y la presenta
- Verificador (verifier): comprueba la firma y la validez de la credencial sin tener que contactar con el emisor

Los tres se apoyan en un Verifiable Data Registry para resolver claves públicas, esquemas y estado de revocación.

### VDR (Verifiable Data Registry)

En el triángulo de confianza, el verificador comprueba la credencial sin llamar al emisor. Para poder hacerlo necesita consultar información pública en algún sitio de referencia. Ese sitio es el VDR, un rol definido en el [modelo de credenciales verificables del W3C](https://www.w3.org/TR/vc-data-model/#roles).

Una analogía del mundo físico: un banco recibe un poder notarial. No llama al notario, pero sí consulta el registro de notarios para saber si ese notario existe y está en activo, compara la firma con la registrada y comprueba que el poder no se ha revocado. El VDR cumple la misma función con las credenciales digitales.

El verificador consulta el VDR para responder a cuatro preguntas:

- ¿Con qué clave compruebo la firma? El VDR asocia el identificador del emisor (por ejemplo, su DID) con su clave pública
- ¿Es un emisor de confianza? El VDR mantiene el registro de emisores autorizados a expedir cada tipo de credencial
- ¿Tiene la credencial la estructura correcta? El VDR publica los esquemas, es decir, qué campos debe contener cada tipo de credencial
- ¿Sigue siendo válida? El VDR publica las listas de revocación o suspensión

Un ejemplo completo: una universidad emite un título digital a una alumna, que lo guarda en su wallet. Años después lo presenta a una empresa. La empresa lee en el título el DID de la universidad, busca en el VDR su clave pública y verifica la firma; confirma en el registro de emisores que es una universidad acreditada; y comprueba en la lista de revocación que el título no se ha anulado. En ningún momento contacta con la universidad, que así no sabe quién, cuándo ni dónde ha usado su título la alumna.

El VDR nunca guarda las credenciales ni datos personales del titular, solo la información pública necesaria para verificarlas. Por eso puede ser compartido y consultable por cualquiera.

El W3C define qué función cumple el VDR, pero no cómo se implementa: puede ser una base de datos, una infraestructura de clave pública (PKI) o una blockchain. La blockchain aporta que ningún actor puede alterar el registro por su cuenta y que queda constancia de cada cambio. En el ecosistema europeo, la blockchain de EBSI cumple este rol.

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

La distinción crucial es que eIDAS 2.0 establece dos niveles de confianza: **credenciales cualificadas**, emitidas por Qualified Trust Service Providers (QTSPs) certificados bajo eIDAS con reconocimiento legal pleno en toda la UE, y **credenciales no cualificadas**, emitidas por proveedores privados, técnicamente compatibles con EUDI Wallet pero sin el mismo peso legal que las gubernamentales. Para casos críticos como identidad oficial o edad legal, predominarán las credenciales cualificadas; para casos de uso menos regulados como membresías o reputación, las credenciales privadas seguirán siendo válidas y útiles.

**Web3**:

Web3 es un ecosistema permissionless, abierto a cualquier persona y economía, que ya está tokenizando activos financieros de EEUU, como los bonos del Tesoro. En él, la identidad sigue varias vías.

La primera suelen ser las rampas de salida o entrada o salida donde la identidad se basa en cualquier identidad federada de Web2 tradicional, y es así por obligación legal de [KYC](https://en.wikipedia.org/wiki/Know_your_customer) (Know Your Customer) y [AML](https://en.wikipedia.org/wiki/Money_laundering#Anti-money_laundering) (Anti-Money Laundering) donde exigen adicionalmente documento de identidad y, según el riesgo e importe, prueba de domicilio y justificación del origen de los fondos, datos que quedan almacenados en los servidores del proveedor. Es así porque en la UE, los proveedores autorizados bajo [MiCA (Reglamento (UE) 2023/1114)](https://eur-lex.europa.eu/eli/reg/2023/1114/oj) son sujetos obligados de prevención del blanqueo, y la Travel Rule del [Reglamento (UE) 2023/1113](https://eur-lex.europa.eu/eli/reg/2023/1113/oj) les obliga a identificar a ordenante y beneficiario en cada transferencia de criptoactivos.

De manera más marginal existe un modelo de identificación Web3 mas institucional, siendo descentralizado, basada en DID con Verifiable Credentials (VCs) custodiadas por el propio usuario fuera de la cadena, que se presentan selectivamente mediante Zero-Knowledge Proofs. Proyectos como Privado ID (antes Polygon ID) son el mejor ejemplo, mientras que emisores VC como Fractal ID o Civic actúan como puente pragmático entre identidad legal y ecosistema descentralizado, mejorando la experiencia de usuario, pero sin eliminar la centralización de fondo.

La identificación más habitual en Web3 y usada en mayor parte para DeFi, que son las financias abiertas y sin pedir permiso, son mediante la [wallet Web3](https://ethereum.org/wallets/find-wallet/), donde la identidad no la emite nadie. La identidad se basa también en la reputación que se acumula como un rastro verificable on-chain en las DAOs a las que se pertenece, los eventos a los que se asiste, las votaciones de gobernanza o los protocolos que se usan. Es la idea que Vitalik Buterin, E. Glen Weyl y Puja Ohlhaver plantearon en el paper [DeSoc (Decentralized Society)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) de 2022, con tokens intransferibles (Soulbound Tokens) para representarla. A esa idea se suman piezas como los [POAPs](https://poap.xyz/) (NFTs, transferibles, que acreditan la asistencia a un evento), las [atestaciones EAS](https://attest.org/) o protocolos sociales como [Lens](https://www.lens.xyz/) y [Farcaster](https://www.farcaster.xyz/). La capa de nombres la aporta [ENS (Ethereum Name Service)](https://docs.ens.domains/), que asocia a la dirección un nombre legible (ejemplo alice.eth). Toda esa identidad queda atada a una dirección y perderla era perderlo todo, motivo que surgen las smart contract wallets, donde la identidad vive on-chain facilitando la experiencia de usuario y permitiendo el on-boarding, es decir, acceso mediante Wallets non-custodial donde incluso el login puede ser mediante tú cuenta de Google o Apple y donde tienes recuperación social de claves.

---
