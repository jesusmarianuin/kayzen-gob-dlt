# Protección de datos en la red

Guardar solo *hashes* no saca los datos personales de la red. Las [directrices del Comité Europeo de Protección de Datos (EDPB)](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf), de julio de 2026, tratan esos *hashes* como datos personales, igual que las direcciones de personas físicas. Por eso hay que decidir desde el diseño qué se escribe, quién responde y cómo se dejará de identificar a una persona cuando corresponda.

Salvo que se indique otra cosa, los párrafos citados son los de esas directrices.

## Qué es un dato personal en la red

Un dato es personal si permite identificar a una persona, directa o indirectamente, con medios razonables. Los [datos seudonimizados siguen siéndolo](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807) si se pueden atribuir a alguien con información adicional. En una blockchain esto alcanza a:

- Direcciones y claves públicas: si el usuario es una persona física identificable (párrafo 26). Para la AEPD, [la dirección de una persona física es un dato personal](https://www.aepd.es/guias/nota-tecnica-blockchain.pdf). La dirección de un órgano no apunta a una persona, pero la de un [empleado sí](identity.md).
- Metadatos: identificadores de transacción, eventos, recibos, cambios de estado y almacenamiento de contratos, cuando permitan identificar a alguien (nota 12).
- *Hashes* con secreto: el *hash* se considera dato personal (párrafo 52), incluso con un secreto guardado fuera de la cadena.
- Datos cifrados: siguen siendo datos personales (párrafo 51).
- Datos fuera de la cadena: el almacén externo sigue sujeto al RGPD (párrafo 52), y también los *indexers*, las copias de seguridad y los almacenamientos temporales de cada nodo.

## Quién responde

El responsable del tratamiento es quien decide para qué y cómo se tratan los datos. El EDPB no asigna este papel por tecnología: exige analizar los hechos de cada red, y la [gobernanza](network-governance.md) suele ser el elemento clave (párrafos 38 y 39). Favorece las redes permisionadas porque permiten repartir mejor las responsabilidades (párrafo 40).

Un nodo que solo aplica comprobaciones técnicas, sin interés ni beneficio en elegir transacciones, podría no ser responsable (párrafo 42). Un validador que [prioriza las transacciones de su organismo](transaction-ordering.md) no encaja del todo en esa descripción, así que el caso debe analizarse. Los organismos que decidan juntos serán [corresponsables](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807) y deben acordar cómo se atiende a los interesados. El reparto debe quedar escrito antes de desplegar.

## El derecho de supresión en la Administración

El derecho de supresión no es absoluto. [No se aplica](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807) cuando el tratamiento es necesario para cumplir una obligación legal o una misión de interés público. Muchos registros de la Administración pueden entrar en esta excepción, pero eso no permite conservar los datos para siempre:

- La vida de la cadena no sirve como plazo de conservación (párrafo 78). Cada dato necesita el suyo, también las direcciones (párrafo 80).
- Al acabar el plazo, el dato debe borrarse o anonimizarse (párrafo 80). Si no hay una solución técnica para ello, no debe escribirse en la cadena (párrafo 120).
- La imposibilidad técnica no justifica incumplir (párrafo 50).
- El consentimiento es una mala base jurídica para este tipo de registro, porque quien lo retira tiene que poder dejar de ser identificable (párrafo 116).

## Qué se escribe en la cadena

La recomendación general es [guardar fuera de la cadena los datos personales](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf), más allá de los identificadores que ya exige la propia transacción (párrafo 109). A partir de ahí hay varias opciones, que se distinguen por lo que el contrato puede comprobar y por cómo se deja de identificar a la persona.

### Datos sin referencia a personas

La cadena guarda solo datos del órgano o del expediente que no llevan a nadie. Es la opción con menos riesgo. Su límite es que un identificador que se pueda relacionar con una persona vuelve a ser un dato personal mientras exista esa relación (párrafo 64).

### Compromiso o *hash* con secreto

Un compromiso criptográfico es un valor que fija un dato sin revelarlo: quien tiene el dato puede demostrar después que coincide, y quien solo ve el valor no aprende nada (párrafo 34). Un *hash* con secreto se usa de forma parecida (párrafo 52). El dato y el secreto se guardan fuera de la cadena.

Para dejar de identificar a la persona se borran el dato y el secreto. Con un compromiso bien construido, lo que queda en la cadena ya no sirve para recuperar ni reconocer el dato (párrafo 53). La transacción pierde su significado, pero sigue sirviendo para comprobar la integridad de la cadena (párrafo 64).

Tiene tres límites:

- Solo prueba que un dato existía. Un contrato no puede comprobar nada sobre un valor que no entiende, lo que lleva al [problema de un *ledger* sin contenido útil](transaction-ordering.md).
- El *hash* sin secreto no se considera, en general, protección suficiente para una red pública (párrafo 52). Y cada registro necesita su propio secreto, porque un secreto común permitiría relacionar registros de la misma persona.
- El borrado ha de ser real en todas las copias, y el almacén externo es otro sistema con sus propios riesgos (párrafo 52).

El EDPB admite estas formas cuando es necesario guardar algo (párrafo 54), pero desaconseja registrar datos personales en claro, cifrados o con *hash*, porque dificulta la rectificación y la supresión (párrafo 104).

### Datos cifrados

Solo quien tiene la clave puede leer el dato, y al destruirla queda ilegible. Sin embargo, sigue siendo un dato personal, y un cifrado actual puede romperse si la cadena se conserva indefinidamente (párrafo 51). Es poco adecuado para datos de larga duración.

### Pruebas de conocimiento cero

Una prueba de conocimiento cero (ZKP) [permite demostrar que se dispone de una información sin exponerla](https://www.aepd.es/prensa-y-comunicacion/blog/cifrado-privacidad-iv-pruebas-conocimiento-cero). Su ventaja frente al *hash* es que un contrato puede verificar que se cumple una regla sin ver el dato, por ejemplo que un título sigue vigente o que una persona cumple un requisito de edad. Así, la cadena conserva capacidad de validación sin contener los datos.

No resuelve por sí sola la protección de datos:

- La AEPD advierte de que [no elimina la información personal](https://www.aepd.es/prensa-y-comunicacion/blog/cifrado-privacidad-iv-pruebas-conocimiento-cero): es una herramienta de seudonimización, ofrece una certeza probabilista y su riesgo depende de cómo se implemente, por lo que exige auditorías.
- Lo que sustituye a un identificador puede seguir siendo un dato personal (párrafo 27).
- El EDPB la considera útil, pero pide probarla y validarla, y combinarla con otras medidas (párrafo 56).
- Verificar la prueba consume [gas](gas-cost.md) dentro de los límites del bloque, y si cambia la regla hay que [cambiar también la lógica de verificación](smart-contract-upgradeability.md).

La cartera europea de identidad la estudia para funciones como la divulgación selectiva, pero la [página de arquitectura de la cartera](https://eudi.dev/latest/discussion-topics/g-zero-knowledge-proof/) la trata como tema de discusión, no como requisito cerrado.

### Borrar en la propia cadena

La AEPD ha demostrado que se puede: su [prueba de concepto](https://www.aepd.es/guias/nota-tecnica-blockchain.pdf) sobrescribe una dirección en todas las estructuras del nodo mediante un *hard fork*, un cambio de reglas que todos los nodos adoptan a la vez. La red asume la inconsistencia resultante en los bloques afectados y sigue funcionando. Por eso la AEPD sostiene que la inmutabilidad es un objetivo acordado entre participantes, no una propiedad física.

Es una vía de último recurso, y requiere procedimientos acordados en la gobernanza y la colaboración de todos los nodos. Además, se [probó con Geth y dos validadores en un entorno de laboratorio](https://www.aepd.es/guias/anexo-tecnico-blockchain.pdf), no con Besu y QBFT.

## Quién puede ver qué

En una red permisionada, todos los participantes siguen viendo por defecto lo que se difunde: el acceso debe limitarse a lo necesario para cada finalidad (párrafo 49). Saber qué organismo registra qué y cuándo puede revelar información aunque no haya datos en claro, de modo que el nivel de publicidad se evalúa también para los metadatos (párrafos 48 y 61).

Son dos capas independientes: los permisos de Besu controlan quién entra en la red, y una capa adicional como [Paladin](https://docs.besu-eth.org/private-networks/concepts/privacy-with-paladin) controla qué ven quienes ya están dentro.

## Qué hacer antes de desplegar

El EDPB y la AEPD [piden abordar esto desde el diseño](https://www.aepd.es/guias/nota-tecnica-blockchain.pdf), porque después es muy difícil corregirlo:

- Justificar por qué hace falta una blockchain y qué alternativas se han descartado (párrafos 46 y 108). Si no se necesita su integridad reforzada, el EDPB recomienda otras herramientas (párrafo 103).
- Hacer la [evaluación de impacto](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807) cuando el riesgo sea alto, incluyendo los riesgos propios de la cadena (párrafo 98).
- Fijar un plazo de conservación para cada tipo de dato, también para las direcciones y los metadatos (párrafos 81 y 119).
- Revisar cada contrato que tome decisiones sobre personas: puede ser una decisión automatizada, con derecho a intervención humana y a impugnarla aunque ya se haya ejecutado (párrafo 107).
- Planificar qué pasa si se rompe un algoritmo criptográfico durante la vida de la red (párrafos 85 y 96).
- Comprobar si hay nodos fuera del Espacio Económico Europeo, porque implicarían transferencias internacionales (párrafo 74).
