# ¿Qué son las declaraciones electrónicas de atributos? EAA, QEAA y las del sector público Pub-EAA en eIDAS2

Post: <https://inza.blog/2026/09/20/que-son-las-declaraciones-electronicas-de-atributos-eaa-qeaa-y-las-del-sector-publico-pub-eaa-en-eidas2/>

Fecha: 2026-09-20

Una declaración electrónica de atributos (EAA) es una manifestación firmada que acredita que un atributo de una persona física o jurídica es cierto (su edad, su titulación, que administra una sociedad, que tiene un permiso) sin necesidad de identificarla por completo. No responde a "¿quién eres?", sino a "¿es cierto este dato sobre ti?". Es el complemento de la EUDI Wallet: la cartera guarda el PID y, sobre él, acumula declaraciones emitidas por terceros de confianza. El término oficial en español es "declaración", no "atestación"; también se ha usado "testimonio".

Separar la identidad de los atributos permite la divulgación selectiva: demostrar que se tienen más de 18 años sin revelar la fecha de nacimiento.

eIDAS2 distingue tres tipos:

- DEA (EAA), no cualificada: la emite cualquier prestador, no exige verificación contra fuente auténtica y solo goza del principio de no discriminación como prueba
- DECA (QEAA), cualificada: la emite un prestador cualificado supervisado y auditado; si el atributo está en el anexo VI (domicilio, edad, sexo, estado civil, nacionalidad, títulos, permisos o datos registrales de personas jurídicas), se verifica contra la fuente auténtica; equivale a la declaración en papel y se reconoce en toda la UE
- DEA-AAPP (Pub-EAA): la emite el organismo público responsable de la fuente auténtica, o alguien en su nombre, con la misma fuerza que la cualificada en su ámbito

Una fuente auténtica es el repositorio reconocido como origen primario del atributo: registro civil, registro mercantil, registro de títulos o DGT. La declaración no inventa el dato, lo transporta con garantías desde donde se gestiona.

El régimen está en los artículos 45 ter a 45 nonies del Reglamento 910/2014 modificado (efectos jurídicos, uso en servicios públicos, requisitos de las cualificadas en el anexo V, verificación contra fuentes auténticas en el anexo VI, declaraciones del sector público en el anexo VII y expedición a la cartera). Se desarrolla con actos de ejecución y normas ETSI y CEN, recogidos en [los actos de ejecución de eIDAS2 al día](../08/30-los-actos-de-ejecucion-de-eidas2-al-dia-y-las-normas-etsi-y-cen-que-citan-the-eidas2-implementing-acts-up-to-date-and-the-etsi-and-cen-standards-they-cite.md). El ARF admite dos formatos: SD-JWT VC e ISO/IEC 18013-5 mdoc.

Casos de uso: mayoría de edad, titulación o colegiación, representación de una empresa o titularidad de un permiso. Los atributos societarios enlazan con la futura European Business Wallet.

Calendario:

- 24 de diciembre de 2026: cartera disponible y aceptación por el sector público
- 24 de diciembre de 2027: aceptación por el sector privado regulado cuando se exija autenticación reforzada

La categoría cualificada aún está poco poblada en las listas de confianza, pero ya aparecen prestadores: [DigitalSign](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls/tl/PT/tsp/7) (Portugal), [Microsec](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls/tl/HU/tsp/2) (Hungría) e [IDnow Trust Services](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls/tl/SE/tsp/4) (Suecia). Cierra con el contacto de EADTrust ([web](http://www.eadtrust.eu)).

En una frase: eIDAS2 define tres tipos de declaraciones de atributos con distinto emisor y valor jurídico, que viajan en la cartera y se presentan de forma selectiva.

---
