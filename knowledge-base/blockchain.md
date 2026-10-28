
# Blockchain

## ¿Qué es una blockchain?

Blockchain es un tipo de registro distribuido (DLT) de solo añadir (append-only), en el que las transacciones se agrupan en bloques y cada bloque incluye el hash del anterior, formando una cadena. El registro se replica en una red de nodos, normalmente P2P, que acuerdan mediante un mecanismo de consenso qué bloques se añaden y en qué orden. Gracias a esto, se obtiene un registro contable ordenado cronológicamente.

Por el encadenamiento de hashes, cualquier cambio en un bloque anterior se detecta, y el consenso hace que reescribir el historial sea muy costoso o exija que se pongan de acuerdo la mayoría de los nodos; por eso se considera inmutable. Esa inmutabilidad se refiere al historial, no al estado, por ejemplo, el saldo de una cuenta cambia con cada nueva transacción, pero el cambio se hace añadiendo transacciones, nunca editando las anteriores, de modo que cada modificación queda registrada y se puede trazar.

Este diseño no es arbitrario, es una solución de diseño que responde al problema de mantener las mismas transacciones replicadas en un conjunto de nodos que tienen que llegar a un acuerdo, cuando no hay una autoridad central que decida qué es válido y en qué orden.

Su primer caso de uso real llegó con el [whitepaper de Bitcoin](https://bitcoin.org/bitcoin.pdf) de Satoshi Nakamoto en 2008, donde se propuso como la estructura de datos fundamental para mantener un registro de transacciones sin necesidad de una autoridad central. Desde entonces, la tecnología ha evolucionado más allá de las criptomonedas, encontrando aplicaciones en contratos inteligentes, tokenización, trazabilidad de activos (cadena de suministro), gestión de identidad digital y sistemas de gobernanza descentralizada (DAO).

Las características fundamentales que proporciona este diseño son la resiliencia, la transparencia verificable y la auditabilidad completa del histórico de transacciones.

Si analizamos las decisiones de diseño de blockchain, podemos concluir que:

* Para la red que considera esa cadena como correcta, debe ser un registro inmutable; de lo contrario, cualquier alteración comprometería la integridad del historial, haciendo imposible verificar si ha sido manipulado.

  > La inmutabilidad es un pilar clave de la resilencia del registro y del resistencia a la censura: impide que otros actores borren o modifiquen información registrada, garantizando transparencia y permanencia. No debemos confundir con un ataque del 51% o un fork, eso es posible, pero entonces no es para lo que la red considera como la cadena correcta.

* Para el conjunto de nodos de la red, la información de las transacciones debe ser verificable, de lo contrario no podrán llegar a un consenso sobre el estado único de la red.

  > Aunque existen opciones para mejorar la privacidad, como las pruebas de conocimiento cero (ZK proofs), que permiten a los nodos validar transacciones sin revelar información, su implementación sigue siendo compleja y representa un desafío técnico importante en la actualidad.

* Como existe un coste para llegar al consenso, las transacciones se agrupan en bloques.

  > Imagina lo inviable que sería que cientos o miles de nodos tengan que llegar a un acuerdo por cada transacción individual que reciben.

* Agrupar las transacciones en bloques y, además, incluir el hash del bloque anterior —que resume y valida todas las transacciones previas— facilita la validación de nuevos bloques por parte de los nodos. 

  > Sin este mecanismo, los nodos tendrían que validar millones de transacciones previas, lo que sería inviable.

* Según el modelo de confianza, una red puede ser trustless (sin confianza previa entre participantes) o trusted (con participantes identificados y autorizados). En ambos casos, los nodos necesitan generar unas evidencias criptográficas mínimas, incluso en redes permisionadas como Hyperledger Besu con protocolos de consenso como QBFT o BFT 2.0, donde cada bloque lleva las firmas de los validadores que lo aprueban.

  > Ejemplos de estas evidencias son los árboles de Merkle, que permiten validar grandes volúmenes de datos de forma eficiente, y las zero-knowledge proofs (pruebas de conocimiento cero), que se usan en redes y soluciones más recientes, como los ZK-Rollups, para mejorar la privacidad y la escalabilidad.

En las redes blockchain, las decisiones por consenso suelen seguir tres enfoques principales, donde se generan evidencias (proof en ingles). Dependiendo de la necesidad y contexto, puede ser necesario realizar evidencias de un trabajo (Proof of Work), evidenciar la participación (Proof of Stake) o considerar su participación como confiable (Proof of Authority).

Cada enfoque es relevante para cada necesidad, bitcoin como sistema resiliente necesita PoW, el trabajo realizado es lo que realmente asegura la red, pero otras redes con PoS es suficiente como demuestra Ethereum, donde cualquiera que deposite el stake mínimo puede ser validador. Una variante es DPoS (Delegated Proof of Stake), usada por IOTA, donde los poseedores de tokens no validan, sino que votan con su stake a un grupo reducido y fijo de delegados, que son los únicos que producen bloques (Se gana velocidad a cambio de concentrar el consenso en pocos actores). Por último, hay redes, muchas veces privadas, consorcio o permisionadas, donde demostrar la pertenencia a la red con PoA es suficiente, porque los validadores están identificados y responden de su comportamiento. Aun así, protocolos PoA como QBFT o IBFT 2.0 siguen siendo tolerantes a [fallas bizantinas](https://academy.bit2me.com/que-es-falla-bizantina/) (BFT, Byzantine Fault Tolerant).

## Distributed Ledger Technology (DLT)

Es importante distinguir que blockchain es una implementación específica dentro de un concepto más amplio conocido como [Distributed Ledger Technology (DLT)](https://research.ibm.com/projects/privacy-preserving-and-interoperable-digital-assets). Mientras que todas las blockchains son DLTs, no todas las DLTs utilizan bloques encadenados.

El término ledger viene de la contabilidad, donde es el libro mayor: agrupa los movimientos por cuenta y da el saldo de cada una. El que anota los movimientos en orden cronológico, tal como se producen, es el journal (libro diario), y el mayor se obtiene a partir de él. Por estructura, una blockchain se parece más al diario, porque es un registro cronológico de transacciones. Aun así, el término asentado es ledger, y la norma [ISO 22739:2024](https://www.iso.org/standard/82208.html) lo define como un almacén de información que guarda registros de transacciones pensados para ser finales, definitivos e inmutables. Un distributed ledger es el ledger que se comparte entre los nodos de la red y se mantiene sincronizado mediante un mecanismo de consenso.

Existen otras implementaciones de DLT que emplean estructuras de datos alternativas:

**Corda (R3):**

[Corda](https://docs.r3.com/) no agrupa las transacciones en bloques ni las difunde a toda la red: cada transacción se comparte solo con las partes que intervienen, que comprueban su validez. Un servicio de notaría confirma que los estados de entrada no se han consumido ya, lo que impide gastar dos veces un mismo activo. Así, ningún nodo guarda una copia completa del registro, solo los hechos que le afectan, un diseño pensado para entornos regulados como el financiero.

**Hashgraph:**

[Hashgraph](https://hedera.com/learning/hashgraph/what-is-hashgraph) emplea un algoritmo de consenso basado en "gossip about gossip" y "virtual voting". Las transacciones se estructuran en un DAG donde los nodos comparten información sobre el orden de los eventos, logrando consenso sin necesidad de bloques tradicionales. Este mecanismo promete alta eficiencia y rapidez en la confirmación de transacciones.

**Canton (Digital Asset):**

[Canton](https://docs.canton.network/overview/learn/how-transactions-work) ejecuta contratos escritos en Daml y aplica la privacidad a cada parte de una transacción: cada participante recibe, cifradas, solo las partes que le afectan. Un servicio de sincronización (synchronizer) ordena y reparte esos mensajes sin poder leer su contenido, y los participantes implicados validan y confirman la transacción entre ellos. Este diseño permite que varias organizaciones compartan un registro sin exponer sus datos al resto.

## El estado de la red y el almacenamiento local del nodo

Hasta ahora hemos visto que blockchain proporciona un registro inmutable del historial de transacciones. Sin embargo, para validar una nueva transacción (por ejemplo, comprobar si una cuenta tiene saldo suficiente o si un contrato inteligente cumple una condición), un nodo no puede permitirse el lujo de recorrer todo el historial desde el bloque génesis cada vez. Necesita conocer el estado actual de la red.

El estado es la "fotografía" en tiempo real de todos los saldos, los nonces (contadores de transacciones) y los datos internos de los contratos inteligentes en un momento dado. Cuando un nodo se sincroniza por primera vez, reconstruye este estado procesando cronológicamente cada transacción del historial, aplicando los cambios paso a paso en su almacenamiento local. Una vez sincronizado, el nodo actualiza este estado local con cada nuevo bloque validado.

Para que este mecanismo sea eficiente, verificable y asegure el consenso sin hinchar la cadena de bloques, los nodos recurren a estructuras de datos criptográficas que guardan en local, fuera de los bloques. En las redes compatibles con la Ethereum Virtual Machine (EVM), la estructura fundamental es el Merkle Patricia Trie (MPT), que combina dos conceptos:

**Patricia Trie (o Radix Tree):**

Un árbol de búsqueda eficiente donde los caminos (las ramas) están determinados por las claves de los datos (por ejemplo, las direcciones criptográficas de las cuentas). Permite localizar rápidamente la información de una cuenta específica sin recorrer toda la base de datos.

**Merkle Tree:**

Un árbol criptográfico donde cada nodo padre contiene el hash de sus nodos hijos. Si un solo bit de información cambia en la base del árbol (una "hoja"), el hash de su padre cambia, provocando un efecto dominó que altera todos los hashes hasta llegar al hash único de la cima (la raíz).

La clave de este diseño es que la blockchain en sí misma no almacena el estado completo de la red, sino únicamente la raíz criptográfica del estado (State Root), que se incluye en la cabecera de cada bloque.

Tomando como ejemplo la arquitectura de un nodo Hyperledger Besu, el software no guarda el estado de las cuentas dentro de los bloques físicos. En su lugar, utiliza una base de datos local y muy rápida de tipo clave-valor (habitualmente RocksDB) para almacenar estos árboles. Cuando el nodo recibe un bloque, ejecuta sus transacciones en la EVM, modifica los saldos en su base de datos local y recalcula el árbol. Si el hash de la raíz (State Root) resultante en su máquina coincide con el publicado por el validador, el nodo tiene la garantía criptográfica de que su estado reconstruido es idéntico al del resto de la red.

Para mantener todo organizado y auditable, un nodo típico mantiene varios de estos árboles interconectados:

**State Trie (Árbol de estado global):**

Es el árbol principal. Mapea las direcciones de todas las cuentas de la red con su estado fundamental (saldo, nonce y, si es un contrato, el hash de su código y la raíz de su propio almacenamiento).

**Storage Trie (Árbol de almacenamiento):**

Cada contrato inteligente desplegado en la red tiene su propio árbol individual para guardar sus variables de estado (los datos que gestiona el contrato). La raíz de este árbol se guarda como un dato dentro del State Trie global.

**Transaction Trie y Receipt Trie:**

Por cada bloque, se generan árboles efímeros que contienen las transacciones de ese bloque específico y los recibos de su ejecución (gas consumido, eventos emitidos, éxito o fracaso). Sus respectivas raíces también se incluyen en la cabecera del bloque.

Si analizamos las decisiones de diseño sobre cómo el nodo gestiona y reconstruye el estado, podemos concluir que:

* El diseño separa el almacenamiento masivo de datos de la necesidad de consenso global.

  > El almacenamiento pesado de cuentas y contratos reside en la base de datos local del nodo, mientras que el consenso de la red solo requiere que los nodos acuerden una huella criptográfica de 32 bytes incluida en el bloque.

* La estructura de árbol de hashes facilita enormemente la verificación externa.

  > Permite la existencia de clientes ligeros (light nodes) que pueden verificar criptográficamente el saldo de una cuenta pidiendo a un nodo completo solo la rama específica del árbol (Merkle proof), sin necesidad de descargar ni procesar toda la blockchain.

## Distribución versus descentralización

Los términos "distributed" y "decentralized" frecuentemente se confunden, pero representan conceptos distintos que es crucial diferenciar en el contexto de blockchain y sistemas distribuidos.

**Sistema distribuido:**

Se refiere a que los datos o procesos están replicados en múltiples ubicaciones geográficas o lógicas. Un sistema puede ser distribuido pero mantener control centralizado, como ocurre con los servidores replicados de una empresa que operan en diferentes regiones para mejorar la disponibilidad y el rendimiento, pero donde una única organización mantiene el control total sobre la infraestructura.

**Sistema descentralizado:**

Implica que no existe una autoridad central que controle completamente el sistema. Las decisiones, el control y la gobernanza están distribuidos entre múltiples participantes que operan de forma autónoma. La descentralización fomenta la resistencia a la censura y reduce los puntos únicos de fallo tanto técnicos como de gobernanza.

Es crucial entender que el término DLT se refiere a un libro mayor distribuido, pero no implica necesariamente descentralización completa. Una DLT siempre es distribuida, pero su control puede estar centralizado, descentralizado o repartido en parte, según su diseño y su modelo de gobernanza. Dicho de otro modo, la distribución responde a dónde están los datos (cuántos nodos guardan una copia del registro), mientras que la descentralización responde a quién controla el sistema y toma las decisiones. Blockchain, en su concepción original, está diseñada principalmente para sistemas descentralizados, aunque existen implementaciones permisionadas con diferentes grados de descentralización.

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

La criptoeconomía constituye una dimensión complementaria de la gobernanza, especialmente en las redes públicas trustless que utilizan tokens nativos. Con ella es posible el diseño de incentivos y penalizaciones económicas destinados a alinear el comportamiento de los participantes con los objetivos de la red. Las recompensas por validar transacciones, los mecanismos de staking y las penalizaciones económicas, como el slashing, pueden contribuir a la seguridad del protocolo y desincentivar comportamientos maliciosos. La criptoeconomía también puede influir en la gobernanza cuando los tokens incorporan derechos de voto o cuando los incentivos económicos condicionan la participación en las decisiones colectivas.

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
