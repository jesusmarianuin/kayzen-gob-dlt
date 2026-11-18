# DLT en la Administración

Los conceptos de base (qué es una DLT y un *ledger*, qué distingue lo distribuido de lo descentralizado y qué es la lógica *on-chain*) están en [blockchain](../../knowledge-base/blockchain.md). De las distintas familias de DLT, estos documentos se centran en blockchain para la administración basado en la tecnología de Hyperledger Besu, la solución elegida en la infraestructura europea EBSI (European Blockchain Services Infrastructure).

Un DLT no debe presentarse en la Administración como una mera pieza tecnológica que el departamento de sistemas instala y pone a disposición del resto. Esa visión resulta reduccionista. Una DLT es, ante todo, una infraestructura compartida entre organizaciones autónomas. Cada participante opera su nodo, forma parte activa de la red, consume recursos y aporta capacidad de validación. El sistema evoluciona mediante acuerdos de gobernanza, requiere estándares semánticos comunes y puede precisar esquemas de ponderación interna para coordinar el uso de los recursos.

La tecnología del *ledger* es la capa técnica; la dificultad real reside en la gobernanza: lograr que múltiples organizaciones independientes adopten reglas comunes, mantengan sus nodos, coordinen la evolución del software y asuman la responsabilidad compartida de la red. Ese reto organizativo es, al mismo tiempo, la razón de ser de la tecnología DLT: permitir la construcción de una infraestructura pública común sin obligar a los participantes a someterse a un dominio técnico centralizado.

En este documentos veremos en diferentes partes:

//todo: **ISO 23257:2022:** arquitectura de referencia para tecnologías blockchain y de registros distribuidos.
//todo: **ISO/TS 23635:2022:** directrices de gobernanza para tecnologías blockchain y de registros distribuidos.

- [Cuándo es interesante una DLT](when-to-use-dlt.md): condiciones en las que una DLT aporta valor y casos en los que basta una base de datos convencional
- [Gobernanza de la red](network-governance.md): modelo federado, el nodo como infraestructura propia y compartida, estándares abiertos, resiliencia y economía interna
- [Coste del gas](gas-cost.md): si el gas debe costar cero, qué se pierde y qué permitiría un coste
- [Identidad en la red](identity.md): quién firma cada transacción, cómo se une una dirección con un órgano y qué ocurre cuando cambia una clave
- [Protección de datos en la red](data-protection.md): qué es dato personal en una blockchain, quién responde y qué estrategias permiten escribir en la cadena
- [Retos de diseño con Besu](besu-design-challenges.md): crecimiento del estado, indexación, determinismo, disponibilidad del consenso y pruebas
- [Orden de las transacciones](transaction-ordering.md): qué orden garantiza Besu, quién lo decide, cuándo importa y cómo diseñar para no depender de la llegada
- [Inmutabilidad y evolución de los smart contracts](smart-contract-upgradeability.md): *proxies*, paradas de emergencia y *time locks*

---
