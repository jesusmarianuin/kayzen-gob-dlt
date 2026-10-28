# DLT en la Administración

Los conceptos de base (qué es una DLT y un *ledger*, qué distingue lo distribuido de lo descentralizado y qué es la lógica *on-chain*) están en [blockchain](../../knowledge-base/blockchain.md). De las distintas familias de DLT, estos documentos se centran en blockchain para la administración basado en la tecnología de Hyperledger Besu, la solución elegida en la infraestructura europea EBSI (European Blockchain Services Infrastructure).

Un DLT no debe presentarse en la Administración como una mera pieza tecnológica que el departamento de sistemas instala y pone a disposición del resto. Esa visión resulta reduccionista. Una DLT es, ante todo, una infraestructura compartida entre organizaciones autónomas. Cada participante opera su nodo, forma parte activa de la red, consume recursos y aporta capacidad de validación. El sistema evoluciona mediante acuerdos de gobernanza, requiere estándares semánticos comunes y puede precisar esquemas de ponderación interna para coordinar el uso de los recursos.

La tecnología del *ledger* es la capa técnica; la dificultad real reside en la gobernanza: lograr que múltiples organizaciones independientes adopten reglas comunes, mantengan sus nodos, coordinen la evolución del software y asuman la responsabilidad compartida de la red. Ese reto organizativo es, al mismo tiempo, la razón de ser de la tecnología DLT: permitir la construcción de una infraestructura pública común sin obligar a los participantes a someterse a un dominio técnico centralizado.

En este documentos veremos en diferentes partes:

- [Cuándo es interesante una DLT](when-to-use-dlt.md): condiciones en las que una DLT aporta valor y casos en los que basta una base de datos convencional
- [Gobernanza de la red](network-governance.md): modelo federado, el nodo como infraestructura propia y compartida, estándares abiertos, resiliencia y economía interna
- [Identidad y protección de datos](identity-and-data-protection.md): identificación de nodos y firmantes, custodia de claves y encaje con el RGPD
- [Retos de diseño con Besu](besu-design-challenges.md): crecimiento del estado, indexación, determinismo, disponibilidad del consenso y pruebas
- [Inmutabilidad y evolución de los smart contracts](smart-contract-upgradeability.md): *proxies*, paradas de emergencia y *time locks*

> La identidad y los retos técnicos de Besu y de los *smart contracts* son las partes en las que este repositorio tiene más trabajo por concretar.

---
