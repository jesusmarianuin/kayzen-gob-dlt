
# Blockchain

## ¿Qué es una blockchain?

Blockchain es el diseño para un registro contable cronológicamente ordenada que tiene que operar en una red de nodos distribuido, normalmente una red P2P, que tienen que llegar a un consenso y por lo tanto, debe ser inmutable.

> La relación entre blockchain, los nodos y el consenso es clave para comprender su diseño y funcionamiento.

Cada bloque contiene un conjunto de transacciones validadas y está enlazado criptográficamente al bloque anterior mediante funciones hash, formando una estructura de datos que garantiza la integridad histórica de la información registrada.

El concepto fue introducido por primera vez en el [whitepaper de Bitcoin](https://bitcoin.org/bitcoin.pdf) de Satoshi Nakamoto en 2008, donde se propuso como la estructura de datos fundamental para mantener un registro de transacciones sin necesidad de una autoridad central. Desde entonces, la tecnología ha evolucionado más allá de las criptomonedas, encontrando aplicaciones en contratos inteligentes, tokenización, trazabilidad de activos (cadena de suministro), gestión de identidad digital y sistemas de gobernanza descentralizada (DAO).

Esta tecnología representa un modelo de base de datos descentralizada donde la seguridad se logra mediante protocolos de consenso que permiten a múltiples participantes acordar el estado del sistema sin confiar en una entidad central. Las características fundamentales que proporciona son resilencia, transparencia verificable y auditabilidad completa del histórico de transacciones.

Si analizamos las decisiones de diseño de esta estructura de datos, podemos concluir que:

* Debe ser un registro inmutable; de lo contrario, cualquier alteración comprometería la integridad del historial, haciendo imposible verificar si ha sido manipulado.

  > La inmutabilidad es un pilar clave de la resilencia del registro y del resistencia a la censura: impide que otros actores borren o modifiquen información registrada, garantizando transparencia y permanencia.

* Para el conjunto de nodos de la red, la información de las transacciones debe ser verificable, de lo contrario no podrán llegar a un consenso sobre el estado único de la red.

  > Aunque existen opciones para mejorar la privacidad, como las pruebas de conocimiento cero (ZK proofs), que permiten a los nodos validar transacciones sin revelar información, su implementación sigue siendo compleja y representa un desafío técnico importante en la actualidad.

* Como existe un coste para llegar al consenso, las transacciones se agrupan en bloques. Imagina lo inviable que sería que cientos o miles de nodos tengan que llegar a un acuerdo por cada transacción individual que reciben.
* Agrupar las transacciones en bloques y, además, incluir el hash del bloque anterior —que resume y valida todas las transacciones previas— facilita la validación de nuevos bloques por parte de los nodos. Sin este mecanismo, los nodos tendrían que validar millones de transacciones previas, lo que sería inviable.
* Según el modelo de confianza, una red puede ser trustless (sin confianza previa entre participantes) o trusted (con participantes identificados y autorizados). En ambos casos, los nodos necesitan generar unas evidencias criptográficas mínimas, incluso en redes permisionadas como Hyperledger Besu con protocolos de consenso como QBFT o BFT 2.0, donde cada bloque lleva las firmas de los validadores que lo aprueban. Ejemplos de estas evidencias son los árboles de Merkle, que permiten validar grandes volúmenes de datos de forma eficiente, y las zero-knowledge proofs (pruebas de conocimiento cero), que se usan en redes y soluciones más recientes, como los ZK-Rollups, para mejorar la privacidad y la escalabilidad.

En las redes blockchain, las decisiones por consenso suelen seguir tres enfoques principales que equilibran de forma progresiva la seguridad, la descentralización y la escalabilidad. Dependiendo del contexto, puede ser necesario realizar un trabajo (Proof of Work), demostrar la participación (Proof of Stake) o, si el participante se identifica correctamente y tiene suficiente autoridad en un ámbito concreto, basta con considerar su participación como confiable (Proof of Authority). QBFT e IBFT 2.0, los protocolos de consenso de Hyperledger Besu para redes permisionadas o consorcio, son de este último tipo: un conjunto de validadores autorizados propone y firma los bloques por turnos.

> Es decir, se generan evidencias (proof, en inglés) que demuestran el trabajo realizado ([PoW, Proof of Work](https://academy.bit2me.com/que-es-proof-of-work-pow/)), o la participación ([PoS, Proof of Stake](https://academy.bit2me.com/que-es-proof-of-stake-pos/)) o la autoridad ([PoA, Proof of Authority](https://academy.bit2me.com/que-es-proof-of-authority-poa/)).

Cada enfoque es relevante para cada necesidad, bitcoin como sistema resiliente necesita PoW, el trabajo realizado es lo que realmente asegura la red, pero otras redes con PoS es suficiente como demuestra Ethereum, donde cualquiera que deposite el stake mínimo puede ser validador. Una variante es DPoS (Delegated Proof of Stake), usada por IOTA, donde los poseedores de tokens no validan, sino que votan con su stake a un grupo reducido y fijo de delegados, que son los únicos que producen bloques (Se gana velocidad a cambio de concentrar el consenso en pocos actores). Por último, hay redes, muchas veces privadas, consorcio o permisionadas, donde demostrar la pertenencia a la red con PoA es suficiente, porque los validadores están identificados y responden de su comportamiento. Aun así, protocolos PoA como QBFT o IBFT 2.0 siguen siendo tolerantes a [fallas bizantinas](https://academy.bit2me.com/que-es-falla-bizantina/) (BFT, Byzantine Fault Tolerant): la red funciona correctamente mientras los validadores caídos o maliciosos sean menos de un tercio del total (n ≥ 3f + 1), y cada bloque es definitivo en cuanto se añade, sin forks.

## Distributed Ledger Technology (DLT)

Es importante distinguir que blockchain es una implementación específica dentro de un concepto más amplio conocido como [Distributed Ledger Technology (DLT)](https://research.ibm.com/projects/privacy-preserving-and-interoperable-digital-assets). Mientras que todas las blockchains son DLTs, no todas las DLTs utilizan bloques encadenados.

Existen otras implementaciones de DLT que emplean estructuras de datos alternativas:

**Tangle (IOTA):**

El protocolo [Tangle](https://www.iota.org/) utiliza un grafo acíclico dirigido (DAG) en lugar de bloques lineales. En este sistema, cada nueva transacción debe validar dos transacciones anteriores, creando una red de validaciones interconectadas. Este diseño elimina la necesidad de mineros y teóricamente mejora la escalabilidad, ya que el throughput aumenta con el número de transacciones.

**Hashgraph:**

[Hashgraph](https://hedera.com/learning/hashgraph/what-is-hashgraph) emplea un algoritmo de consenso basado en "gossip about gossip" y "virtual voting". Las transacciones se estructuran en un DAG donde los nodos comparten información sobre el orden de los eventos, logrando consenso sin necesidad de bloques tradicionales. Este mecanismo promete alta eficiencia y rapidez en la confirmación de transacciones.

**Holochain:**

[Holochain](https://www.Holochain.org/) adopta un enfoque radicalmente diferente: no utiliza bloques ni busca consenso global. Cada agente mantiene su propia cadena de datos y las interacciones se gestionan de forma descentralizada mediante validación por pares. Este diseño se enfoca en la autonomía de los nodos y la escalabilidad horizontal.

## Distribución versus descentralización

Los términos "distributed" y "decentralized" frecuentemente se confunden, pero representan conceptos distintos que es crucial diferenciar en el contexto de blockchain y sistemas distribuidos.

**Sistema distribuido:**

Se refiere a que los datos o procesos están replicados en múltiples ubicaciones geográficas o lógicas. Un sistema puede ser distribuido pero mantener control centralizado, como ocurre con los servidores replicados de una empresa que operan en diferentes regiones para mejorar la disponibilidad y el rendimiento, pero donde una única organización mantiene el control total sobre la infraestructura.

**Sistema descentralizado:**

Implica que no existe una autoridad central que controle completamente el sistema. Las decisiones, el control y la gobernanza están distribuidos entre múltiples participantes que operan de forma autónoma. La descentralización fomenta la resistencia a la censura y reduce los puntos únicos de fallo tanto técnicos como de gobernanza.

Ethereum con su diseño de sharding ilustra bien esta distinción. Es un sistema tanto distribuido como descentralizado, pero con matices importantes. La carga de datos y procesamiento se distribuye entre los nodos y, con [sharding](https://ethereum.org/en/roadmap/danksharding/), cada shard procesa un subconjunto de transacciones aumentando la escalabilidad. Sin embargo, la gobernanza y la seguridad se mantienen descentralizadas mediante la Beacon Chain, donde los validadores se distribuyen entre shards y participan en el consenso global.

Es crucial entender que el término DLT se refiere a un libro mayor distribuido, pero no implica necesariamente descentralización completa. Una DLT siempre es distribuida, pero su control puede estar centralizado, descentralizado o repartido en parte, según su diseño y su modelo de gobernanza. Dicho de otro modo, la distribución responde a dónde están los datos (cuántos nodos guardan una copia del registro), mientras que la descentralización responde a quién controla el sistema y toma las decisiones. Blockchain, en su concepción original, está diseñada principalmente para sistemas descentralizados, aunque existen implementaciones permisionadas con diferentes grados de centralización.

## Tipos de blockchain según autorización

Las blockchains se pueden clasificar según el modelo de acceso y permisos que implementan, determinando quién puede participar en el consenso y acceder a los datos:

**Blockchain pública:**

Cualquier persona puede unirse a la red, participar en el proceso de consenso y leer todas las transacciones. Bitcoin y Ethereum son ejemplos prominentes. La seguridad se basa en incentivos criptoeconómicos y la transparencia total. Son ideales para casos de uso que requieren máxima descentralización y resistencia a la censura.

**Blockchain privada:**

El acceso está restringido a participantes autorizados por una entidad u organización. Típicamente las emplean empresas y administraciones públicas que necesitan las propiedades de inmutabilidad y trazabilidad de blockchain, pero requieren control sobre quién puede participar. [Hyperledger Fabric](https://www.hyperledger.org/use/fabric) y [Hyperledger Besu](https://besu.hyperledger.org/) (cliente Ethereum con soporte de redes permisionadas) son frameworks habituales para implementar blockchains privadas.

**Blockchain consorcio:**

Un modelo intermedio en el que un grupo predefinido de organizaciones controla el proceso de consenso. Combina elementos de descentralización con requisitos de gobernanza específicos. Útil para industrias donde múltiples entidades necesitan colaborar manteniendo cierto control, como en cadenas de suministro, consorcios bancarios o redes entre administraciones públicas.

**Blockchain híbrida:**

Combina una parte privada y una parte pública. Parte de los datos se mantiene en un entorno de acceso restringido y parte se hace pública o se puede verificar públicamente. Útil cuando algunos datos deben ser confidenciales pero otros, o su integridad, tienen que poder comprobarse desde fuera.

**Blockchain permisionada:**

La participación está permitida a nodos verificados y aprobados; es una red que puede ser pública o privada que se abre a más participantes bajo unas condiciones. Además define roles o permisos específicos, por ejemplo, unos nodos pueden leer solamente y otros escribir o mas típicamente es pública porque cualquiera puede consultar pero permisionada para participar como nodo.

## Forks y evolución de la blockchain

Durante la operación de una blockchain, pueden surgir situaciones donde la cadena se bifurca, creando caminos alternativos. Comprender estos escenarios es fundamental para entender la evolución y gobernanza de redes blockchain.

**Fork nativo:**

Ocurre temporalmente cuando dos nodos encuentran bloques válidos casi simultáneamente (como en PoW), creando dos versiones competidoras de la cadena. La mayoría de los nodos eventualmente convergen hacia una de las cadenas siguiendo las reglas del protocolo de consenso, típicamente la cadena más larga o la que representa más trabajo acumulado, quedando la cadena del **fork huérfano**.  (orphaned chain) abandonada.

**Soft fork:**

Una actualización del protocolo que es retrocompatible. Los nodos que no actualicen su software pueden seguir validando transacciones, aunque no podrán aprovechar las nuevas características. Un ejemplo significativo es [SegWit (Segregated Witness)](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki) en Bitcoin, que optimizó el uso del espacio en bloques sin requerir que todos los nodos actualizaran simultáneamente.

**Hard fork:**

Representa un cambio significativo en las reglas del protocolo que rompe la compatibilidad con versiones anteriores. Los nodos deben actualizar su software para continuar participando en la red actualizada. Si parte de la comunidad no acepta los cambios, puede resultar en dos blockchains separadas que comparten historia hasta el punto de bifurcación. Ejemplos notables son [Bitcoin Cash](https://bitcoincash.org/) (fork de Bitcoin) y [Ethereum Classic](https://ethereumclassic.org/) (fork de Ethereum tras el incidente de The DAO).

## Regla de la cadena canónica

Un principio fundamental en blockchain es la determinación de cuál es la cadena válida cuando existen múltiples versiones. La regla general es que la cadena con mayor "peso" es considerada la cadena canónica.

En Bitcoin, el peso se calcula según el trabajo computacional acumulado (Proof of Work), siguiendo la regla de la cadena más larga en términos de dificultad acumulada, no simplemente el número de bloques. Los mineros invierten recursos computacionales para resolver puzzles criptográficos, y la cadena que representa más trabajo acumulado se considera la válida.

En Ethereum post-merge, el peso viene determinado por el stake acumulado respaldando una cadena particular. Los validadores depositan ETH como garantía y participan en el consenso mediante [Proof of Stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/). La cadena respaldada por más stake y que sigue las reglas del protocolo Gasper (combinación de Casper FFG y LMD GHOST) se considera canónica.

Este mecanismo de selección de cadena es crucial para la seguridad y funcionalidad de la red, proporcionando una forma objetiva de resolver disputas sobre el estado del sistema sin requerir coordinación centralizada.

Algunos protocolos de consenso, como QBFT o IBFT 2.0, no necesitan esta regla porque tienen finalidad inmediata: un bloque solo se añade a la cadena cuando lo aprueban más de dos tercios de los validadores, y a partir de ese momento ya no puede revertirse.

## Escalabilidad y sidechains

A medida que las blockchains principales enfrentan limitaciones de escalabilidad, han surgido diversas soluciones para procesar más transacciones sin comprometer la descentralización o seguridad.

**Sidechains:**

Son blockchains independientes que se conectan a la blockchain principal mediante un puente bidireccional, permitiendo transferir activos entre ambas cadenas. Las sidechains pueden implementar reglas de consenso diferentes, optimizadas para casos de uso específicos, mientras aprovechan la seguridad de la cadena principal para el asentamiento final de transacciones. Ejemplos incluyen [Polygon](https://polygon.technology/) (anteriormente Matic Network) para Ethereum.

**Layer 2:**

Son protocolos construidos sobre la blockchain principal que procesan transacciones fuera de la cadena principal pero heredan sus garantías de seguridad. Tecnologías como [Lightning Network](https://lightning.network/) para Bitcoin y [Optimistic Rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/) o [ZK-Rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/) para Ethereum permiten throughput significativamente mayor mientras mantienen la finalidad en la blockchain base.

**Sharding:**

Particiona la blockchain en múltiples fragmentos (shards) que procesan transacciones en paralelo. Cada shard mantiene un subconjunto del estado global, y los validadores rotan entre shards para garantizar seguridad. Ethereum está implementando sharding como parte de su roadmap de escalabilidad, coordinado por la Beacon Chain.

Estas soluciones representan diferentes compromisos en el trilema blockchain de escalabilidad, seguridad y descentralización, buscando optimizar el rendimiento sin sacrificar las propiedades fundamentales que hacen valiosa la tecnología blockchain.

## QBFT (Quorum Byzantine Fault Tolerant)

Algoritmo de consenso de tolerancia a fallos bizantinos (BFT) basado en Proof of Authority (PoA), utilizado en redes blockchain permisionadas (por ejemplo, Hyperledger Besu). Un conjunto de validadores conocidos propone y valida bloques mediante rondas de votación; la red tolera hasta *f* validadores maliciosos o caídos de un total de *3f+1*.

Referencia: [documentación de Hyperledger Besu sobre QBFT](https://besu.hyperledger.org/private-networks/how-to/configure/consensus/qbft)

## IBFT 2.0 (Istanbul Byzantine Fault Tolerant 2.0)

Predecesor de QBFT, también basado en PoA y con propiedades de tolerancia a fallos bizantinos. Se especificó originalmente en el EIP-650. Ambos algoritmos (QBFT e IBFT 2.0) garantizan finalidad inmediata de los bloques (a diferencia de Proof of Work), lo que los hace habituales en consorcios y redes gubernamentales o empresariales.

Referencia: [EIP-650: Istanbul Byzantine Fault Tolerance](https://github.com/ethereum/EIPs/issues/650)

## Gobernanza de la red

La gobernanza define las reglas que permiten coordinar a los participantes de una red, gestionar su evolución y resolver los conflictos que puedan surgir. Es uno de los aspectos fundamentales de cualquier sistema distribuido, especialmente en redes blockchain donde diferentes organizaciones deben colaborar sin depender necesariamente de una autoridad central.

La gobernanza abarca aspectos como la admisión y expulsión de participantes, la gestión de identidades y permisos, las políticas de seguridad, las actualizaciones del protocolo, la resolución de conflictos y los mecanismos de toma de decisiones. También determina cómo se distribuye el poder entre los participantes y qué procedimientos deben seguirse para modificar las reglas que rigen el funcionamiento de la red.

Como vemos en [características de las redes P2P](base-architecture/p2p/01-characteristics.md), los principales modelos de gobernanza son la gobernanza centralizada, en la que una entidad controla las decisiones y la evolución del sistema; la gobernanza federada, en la que varias organizaciones comparten la responsabilidad de gestionar la red mediante acuerdos y procedimientos comunes; la gobernanza descentralizada, en la que los participantes intervienen en las decisiones mediante mecanismos distribuidos; la gobernanza mediante organizaciones autónomas descentralizadas (DAO), que puede utilizar contratos inteligentes y mecanismos de votación para gestionar propuestas y recursos; y la gobernanza híbrida, que combina elementos de distintos modelos para adaptarse a las necesidades de la red.

La criptoeconomía constituye una dimensión complementaria de la gobernanza, especialmente en las redes públicas que utilizan tokens nativos. Con ella es posible el diseño de incentivos y penalizaciones económicas destinados a alinear el comportamiento de los participantes con los objetivos de la red. Las recompensas por validar transacciones, los mecanismos de staking y las penalizaciones económicas, como el slashing, pueden contribuir a la seguridad del protocolo y desincentivar comportamientos maliciosos. La criptoeconomía también puede influir en la gobernanza cuando los tokens incorporan derechos de voto o cuando los incentivos económicos condicionan la participación en las decisiones colectivas.

Es importante distinguir la gobernanza del mecanismo de consenso. El consenso permite que los nodos acuerden el estado válido de la blockchain y el orden de las transacciones, mientras que la gobernanza determina cómo se establecen, interpretan y modifican las reglas que rigen la red. Ambos mecanismos están relacionados, pero cumplen funciones diferentes: el consenso proporciona coordinación técnica y la gobernanza establece los procedimientos de decisión y evolución del sistema.

En las redes permisionadas, utilizadas habitualmente en entornos empresariales e institucionales, la gobernanza suele basarse en acuerdos entre las organizaciones participantes, políticas de acceso, responsabilidades definidas y procedimientos formales para aprobar cambios. En estos entornos, la confianza puede sustentarse en mecanismos jurídicos, organizativos y técnicos, sin necesidad de utilizar tokens ni incentivos económicos integrados en el protocolo.

En conclusión, el modelo de gobernanza determina quién puede modificar el protocolo, cómo se aprueban esos cambios y qué ocurre cuando los participantes no están de acuerdo. En las redes públicas que utilizan tokens, también importa quién los posee y qué derechos confieren, ya que la concentración de tokens puede permitir que unos pocos participantes controlen las votaciones. En las redes permisionadas, estas decisiones suelen depender de los acuerdos entre las organizaciones que forman parte de la red, sin necesidad de utilizar tokens ni mecanismos de votación basados en ellos.

### Modelo de gobernanza federado

La gobernanza federada resulta especialmente adecuada cuando varias entidades independientes necesitan compartir una infraestructura y mantener una distribución acordada de responsabilidades y autoridad.

Es un modelo de gobernanza que combina supervisión centralizada con ejecución descentralizada. Un órgano común (comité o consejo) fija las normas compartidas de seguridad, cumplimiento e interoperabilidad, y cada organización participante gestiona su parte con autonomía, adaptándola a sus necesidades siempre que respete esas normas. Frente a un modelo centralizado, en el que un único equipo u operador lo gestiona todo.

En redes blockchain permisionadas entre administraciones, cada organización opera sus propios nodos y todas se someten a reglas comunes acordadas: requisitos de adhesión, alta de validadores, gestión de claves, resolución de conflictos y mayorías para cambiar el protocolo. Es el modelo de EBSI: cada Estado miembro aporta y opera nodos, y la gobernanza se ejerce de forma conjunta.

Para que el modelo funcione, las responsabilidades de cada organización deben estar claramente definidas, los mecanismos de decisión deben ser transparentes y debe existir un procedimiento acordado para resolver conflictos y evolucionar la red.

Referencia: [gobernanza federada de datos (Actian)](https://www.actian.com/es/blog/data-governance/federated-data-governance-explained/)

---
