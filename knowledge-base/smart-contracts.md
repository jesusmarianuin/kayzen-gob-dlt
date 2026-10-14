# Smart contracts

## Origen: de Bitcoin a Ethereum

La idea es anterior a la blockchain. Nick Szabo acuñó el término "smart contract" en 1994 para describir acuerdos cuyas cláusulas se incorporan a un sistema informático que las hace cumplir sin depender de un intermediario. Durante casi dos décadas fue un concepto teórico, porque faltaba un entorno compartido en el que nadie pudiera alterar ni el programa ni su resultado.

Bitcoin introdujo la solución pionera de blockchain, enfocada en la simplicidad, la seguridad y la inmutabilidad, con una capacidad de programación limitada mediante Bitcoin Script. Aunque esta funcionalidad se ha ampliado con propuestas como [Taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) y otras [BIP (Bitcoin Improvement Proposals)](https://github.com/bitcoin/bips), su diseño deliberadamente restrictivo prioriza la seguridad y la resistencia a la censura sobre la flexibilidad. Esta limitación no es un defecto, sino una elección de diseño.

Por eso, para los casos que requieren una lógica de ejecución compleja, surgieron los smart contracts en la red Ethereum (2015) y, después, en otras redes de propósito similar. Se ejecutan sobre una máquina virtual [Turing-completa](https://es.wikipedia.org/wiki/Turing_completo), orientada a la programabilidad general pero limitada en la práctica por el coste de ejecución, el gas. En el ecosistema Ethereum esa máquina se llama [EVM (Ethereum Virtual Machine)](https://ethereum.org/es/developers/docs/evm/), y es también la que usan las redes compatibles, incluidas las redes permisionadas basadas en Hyperledger Besu. Existen alternativas equivalentes basadas en WebAssembly (WASM) en redes más recientes, como Polkadot, NEAR o las cadenas de Cosmos con CosmWasm. Ethereum exploró esa vía con [eWASM](https://ewasm.readthedocs.io/en/mkdocs/), pero la propuesta se abandonó y la EVM sigue siendo su única máquina virtual.

## Qué es un smart contract

El término "contrato inteligente" puede parecer una etiqueta comercial, pero en realidad describe un [programa informático desplegado en una blockchain](https://ethereum.org/es/developers/docs/smart-contracts/) que define reglas de negocio y se ejecuta al recibir una transacción. Tiene su propia dirección en la red, igual que una cuenta, y en ella guarda su código y su estado. Cada nodo reproduce la ejecución de la transacción y, mediante el consenso, la red acuerda el bloque válido, quedando su resultado registrado de forma inmutable en la blockchain.

Conviene distinguir dos formas de invocarlo:

- Transacción: va firmada por una cuenta, puede modificar el estado, la ejecutan todos los nodos, cuesta gas y queda registrada en un bloque
- Consulta (llamada de solo lectura, como `eth_call` en JSON-RPC): la resuelve únicamente el nodo al que se pregunta, no modifica el estado, no pasa por consenso, no cuesta gas y no deja rastro en la blockchain

Para quienes vienen del mundo de las bases de datos relacionales, la analogía más cercana sería un [procedimiento almacenado](https://es.wikipedia.org/wiki/Procedimiento_almacenado) con una interfaz similar a una API RPC, es decir, procedural.

> Ambos residen en un entorno persistente (blockchain o base de datos), gestionan su propio estado y exponen funciones. Sin embargo, a diferencia de los procedimientos tradicionales, los smart contracts operan de forma descentralizada, siguiendo las reglas de inmutabilidad y consenso de la red.

La analogía tiene un límite importante: en una blockchain pública todo lo que guarda el contrato es legible por cualquiera, aunque una variable se declare `private` en Solidity. Esa palabra solo impide que otros contratos la lean, no que un nodo inspeccione el almacenamiento. Por eso no se deben guardar en un smart contract datos personales ni secretos, algo especialmente relevante en la administración por el RGPD.

Tampoco es un contrato en sentido jurídico. Puede ejecutar de forma automática lo pactado en un acuerdo legal, pero por sí mismo es solo código: su validez y sus efectos legales dependen del marco jurídico, no de la blockchain.

## La blockchain como máquina de estados

Una forma útil de entender los smart contracts es ver la blockchain como una máquina de estados replicada. El estado global de la red (saldos, código y datos de cada contrato) cambia únicamente mediante transacciones, y cada bloque representa la transición de un estado al siguiente.

De ahí se deriva una propiedad clave: como las transacciones se conservan ordenadas, cualquier nodo puede reconstruir el estado de la red en cualquier momento de su historia partiendo del bloque génesis y repitiéndolas. La blockchain no guarda solo la foto actual, sino el histórico completo de cómo se llegó a ella.

Para que esto funcione, la ejecución debe ser determinista: la misma transacción sobre el mismo estado tiene que producir exactamente el mismo resultado en todos los nodos. Por eso un smart contract no puede consultar una API externa, leer la hora del sistema operativo ni generar números aleatorios de forma fiable; cada nodo obtendría un valor distinto y la red no llegaría a un consenso.

Además del estado, los contratos emiten eventos (logs). No los puede leer otro contrato, pero quedan en el registro de la transacción y las aplicaciones externas los usan para enterarse de lo que ha ocurrido sin tener que consultar el estado una y otra vez.

## El gas: coste de ejecución y protección frente a abusos

Ethereum introduce el [gas](https://ethereum.org/es/developers/docs/gas/) como unidad del coste computacional: cada operación de la EVM consume una cantidad fija de gas, y quien envía la transacción paga por el gas consumido. Esto cumple dos funciones:

- Remunera a quienes validan y ejecutan las transacciones
- Protege la red frente a ataques de denegación de servicio (DoS): como cada transacción fija un límite máximo de gas, un bucle infinito acaba agotándolo y la ejecución se detiene

Esta segunda función es la que hace compatible una máquina Turing-completa con una red compartida. Sin gas, un solo contrato malicioso podría bloquear a todos los nodos. En las redes permisionadas el precio del gas puede ser cero, pero el límite de gas por transacción y por bloque se mantiene, precisamente para conservar esa protección.

## Un smart contract no se autoejecuta

A pesar de lo que sugiere la palabra "automático", un smart contract no actúa por iniciativa propia. Permanece inactivo hasta que algo lo invoca: una transacción de un usuario, una llamada desde otro contrato o un servicio off-chain que envía la transacción cuando se cumple una condición, como un temporizador o un proceso de la organización.

Lo mismo ocurre con la información del mundo exterior. Si el contrato necesita un dato que no está en la blockchain, como un tipo de cambio o el resultado de un trámite, alguien tiene que escribirlo en ella mediante una transacción. Esa pieza se llama [oráculo](https://ethereum.org/es/developers/docs/oracles/), y es un punto de confianza: el contrato solo es tan fiable como el dato que recibe.

## Inmutabilidad: garantía y riesgo

Como hemos visto, una de las características fundamentales de los smart contracts es la inmutabilidad: una vez desplegados en la blockchain, su código y su lógica no pueden modificarse. Esta propiedad garantiza transparencia y confianza, ya que todos los participantes pueden verificar que las reglas no cambiarán arbitrariamente.

Sin embargo, la inmutabilidad también implica un riesgo importante: si el contrato contiene errores o vulnerabilidades, corregirlos resulta extremadamente difícil, ya que no es posible actualizar el código directamente. Y como el contrato suele gestionar activos o derechos, un error no es solo un fallo de software, sino una puerta abierta que cualquiera puede explotar.

## Patrones para gestionar el riesgo

Para mitigar este riesgo se han desarrollado varios patrones:

- Contratos proxy: separan los datos de la lógica. El proxy conserva el estado y delega las llamadas, mediante `delegatecall`, a un contrato de implementación cuya dirección se puede cambiar. Así, el contrato con el que interactúan los usuarios permanece inmutable, pero la lógica puede evolucionar sustituyendo la implementación. El estándar [ERC-1967](https://eips.ethereum.org/EIPS/eip-1967) fija dónde guarda el proxy esa dirección
- Interruptores de emergencia (circuit breakers): permiten pausar la ejecución del contrato al detectar un problema grave, evitando daños mayores mientras se implementa una solución
- Timelocks: programan un retraso antes de aplicar cambios importantes, dando tiempo a los participantes para revisar, auditar y actuar en consecuencia, incluso para retirarse si no están de acuerdo
- Gobernanza: otorga a los participantes la capacidad de votar las propuestas de actualización o migración. Aunque el contrato sea inmutable, se puede desplegar otro que corrija el problema y migrar a él, siempre que la comunidad esté de acuerdo. En una red pública esa comunidad suelen ser los poseedores de un token; en una red permisionada, los miembros del consorcio según sus reglas de gobierno

Todos estos mecanismos tienen un precio: reintroducen un poder de modificación. Quien controla el proxy, la pausa o el voto puede cambiar las reglas, así que la confianza ya no descansa solo en el código, sino también en quién tiene esas claves y en cómo se protegen. La clave de administración de un proxy es uno de los activos más sensibles de un despliegue, y debería estar en una cartera multifirma o en un HSM y no en una cuenta personal.

Estos patrones ayudan, en definitiva, a equilibrar la flexibilidad para corregir errores con la necesidad de mantener la confianza y la transparencia. Elegir cuánto de cada una es una decisión de diseño, igual que lo fue la sencillez de Bitcoin.

---
