# EBSI (European Blockchain Services Infrastructure)

Infraestructura blockchain impulsada por la Comisión Europea y la European Blockchain Partnership (EBP). Se describe como "pública y permisionada", dos términos que responden a preguntas distintas:

- Pública: cualquiera puede leer los datos, porque los verificadores de credenciales tienen que poder consultarlos sin pedir permiso
- Permisionada: solo pueden operar nodos las entidades autorizadas, en la práctica los Estados miembros y la Comisión. Y solo escriben quienes han sido acreditados para ello, por ejemplo un emisor de confianza que registra su DID

Una persona o empresa cualquiera puede consultar EBSI, pero no puede montar un nodo propio.

Además, sigue un [modelo de gobernanza federado](../blockchain.md#modelo-gobernanza-federado): ningún actor la controla en solitario. Cada Estado miembro opera sus propios nodos, y todos se someten a reglas comunes que se deciden de forma conjunta.

Su uso principal es actuar como registro de confianza para credenciales verificables (títulos académicos, identidad de entidades, documentos), además de otros casos como la notarización de documentos.

> Registro de confianza no es que sea el registro de las VC, es que es el registro o ancla. EBSI guarda los identificadores de los emisores y quién los acreditó, el [registro de emisores de confianza (Trusted Issuers Registry)](../identity.md#tir-trusted-issuers-registry)

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

## TIR

//TODO corrige el desastre que has hecho aqui explica que TIR es el registro de emisores de confianza para la infraestructura DID. Ve a https://inza.blog/2026/09/20/que-son-las-declaraciones-electronicas-de-atributos-eaa-qeaa-y-las-del-sector-publico-pub-eaa-en-eidas2/ revisa la gran duda, ¿que articula que u
