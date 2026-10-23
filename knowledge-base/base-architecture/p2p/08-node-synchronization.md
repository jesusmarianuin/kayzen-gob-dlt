# Sincronización de nodos

La sincronización es el proceso por el que un nodo nuevo, o uno que ha estado desconectado, obtiene el estado actual de la red y se pone al día con sus pares. En redes con estado global, como las blockchain, es la operación más costosa de la vida de un nodo y la que más condiciona los requisitos de disco, ancho de banda y tiempo de puesta en marcha.

La sincronización se apoya en mecanismos ya vistos:

- Necesita pares a los que pedir datos, que obtiene en la [conexión inicial y el descubrimiento de nodos](04-bootstrap-and-node-discovery.md).
- Es la forma en que un nodo recupera las copias que la red mantiene mediante las [técnicas de replicación](07-replication-and-consistency.md#técnicas-de-replicación).
- Determina qué [clase de nodo](08-node-roles.md#clasificación-por-capacidad) resulta: completo, podado, archive o ligero.
- Es la respuesta al [churn](02-challenges-and-vulnerabilities.md#problema-de-disponibilidad-o-rotación-churn): cada nodo que vuelve a la red tiene que recuperar lo que se perdió mientras estaba fuera.

## Fases de una sincronización

Aunque cada cliente tiene su implementación, la mayoría sigue un esquema parecido. Bitcoin Core lo llama headers-first:

1. Conexión a pares: el nodo arranca con los nodos semilla y amplía su lista de pares.
2. Descarga de cabeceras: descarga primero la cadena de cabeceras de bloque, que es ligera, y comprueba que es válida (en Bitcoin, que acumula la mayor prueba de trabajo).
3. Descarga de bloques: con la cadena de cabeceras ya validada, pide los bloques completos en paralelo a varios pares.
4. Validación y construcción del estado: ejecuta o comprueba las transacciones de cada bloque y actualiza el estado local (en Bitcoin, el conjunto de UTXO; en Ethereum, el world state).
5. Seguimiento de la cabeza de la cadena: una vez alcanzada la cabeza, el nodo deja de sincronizar en bloque y pasa a recibir los bloques nuevos según se [propagan](05-routing-and-diffusion.md#propagación-de-transacciones-y-bloques).

Descargar primero las cabeceras tiene una implicación de seguridad: el nodo sabe qué cadena está siguiendo antes de gastar recursos en bajar los bloques, y un par que envíe bloques que no encajan con esas cabeceras queda en evidencia.

## Modos de sincronización

Los modos se diferencian en cuánto historial descargan y en cuánto verifican por sí mismos. Cuanto menos verifica el nodo, antes termina, pero más depende de que otros le hayan dado datos correctos.

### Sincronización completa (full sync)

El nodo descarga todos los bloques desde el génesis y reconstruye el estado ejecutando cada uno de ellos. Es el modo más seguro, porque el nodo no confía en nadie para conocer el estado, y también el más lento: en redes grandes puede tardar días o semanas.

El resultado depende de qué guarde el nodo después de validar:

- Nodo archive: conserva todos los estados históricos, lo que permite consultar el estado en cualquier bloque pasado.
- Nodo podado (pruned): valida igual, pero descarta los datos antiguos que ya no necesita para seguir validando (véase pruning en [estrategias de almacenamiento](01-characteristics.md#estrategias-de-almacenamiento-en-redes-p2p)).

### Snap sync

En lugar de reconstruir el estado ejecutando todo el historial, el nodo elige un bloque reciente de referencia (pivot block) y descarga directamente el estado en ese punto. Según la [documentación de Besu](https://besu.hyperledger.org/public-networks/concepts/node-sync), descarga tantas hojas del árbol de estado como puede y reconstruye el árbol localmente.

El estado descargado se comprueba contra la raíz de estado (state root) que figura en la cabecera del pivot block, de modo que un estado falso enviado por un par no cuadraría con esa raíz. Lo que el nodo no hace es ejecutar el historial anterior al pivot: confía en que la cadena de cabeceras que sigue es la correcta.

Es el modo por defecto en la red principal de Ethereum, y [ethereum.org](https://ethereum.org/en/developers/docs/nodes-and-clients/) lo describe como la estrategia de sincronización más rápida.

> El antiguo fast sync, que descargaba el estado nodo a nodo del árbol, está obsoleto en los clientes actuales y ha sido sustituido por snap sync.

### Sincronización ligera (light sync)

El nodo descarga solo las cabeceras y pide a nodos completos los datos concretos que necesita, que verifica con pruebas de Merkle contra esas cabeceras. Es el modelo de los nodos ligeros y del SPV (Simplified Payment Verification) que describe el whitepaper de Bitcoin.

Consume muy pocos recursos, pero depende de nodos completos para obtener datos y no valida las transacciones por sí mismo. Según [ethereum.org](https://ethereum.org/en/developers/docs/nodes-and-clients/), la sincronización ligera todavía no funciona en el Ethereum actual con proof of stake.

### Checkpoint sync en la capa de consenso

En Ethereum con proof of stake, el cliente de consenso puede arrancar desde un checkpoint reciente en lugar de desde el génesis de la Beacon Chain. Se conoce también como weak subjectivity sync: un nodo que llega nuevo, o que lleva mucho tiempo desconectado, necesita un punto de partida reciente de confianza, porque en proof of stake la cadena por sí sola no le permite distinguir la cadena correcta de una alternativa construida con claves de validadores antiguos.

La implicación de seguridad es directa: quien proporciona el checkpoint es un tercero de confianza y, como advierte [ethereum.org](https://ethereum.org/en/developers/docs/nodes-and-clients/), hay que elegirlo con cuidado. Lo recomendable es contrastarlo con más de una fuente.

## Atajos de confianza

Varios clientes ofrecen atajos que aceleran la sincronización a cambio de una suposición de confianza explícita:

- assumevalid (Bitcoin Core): el nodo omite la comprobación de firmas de los bloques anteriores a un bloque conocido que viene fijado en el software, aunque sigue validando el resto de reglas.
- assumeutxo (Bitcoin Core): el nodo carga una instantánea del conjunto de UTXO, empieza a funcionar desde ella y valida el historial completo en segundo plano hasta confirmar que la instantánea era correcta.
- Checkpoint sync en la capa de consenso de Ethereum, descrito en el apartado anterior.

La diferencia con confiar sin más es que estas suposiciones son acotadas y, en el caso de assumeutxo, se terminan comprobando.

## Sincronización en Besu

Hyperledger Besu es un cliente de ejecución de Ethereum que también se usa en redes privadas con consenso QBFT. El modo se elige con la opción `--sync-mode`. Lo que sigue corresponde a Besu 26.9 y está contrastado con su [código fuente](../../besu-eth/besu/app/src/main/java/org/hyperledger/besu/cli/BesuCommand.java), su [CHANGELOG](../../besu-eth/besu/CHANGELOG.md) y su documentación para [redes públicas](https://besu.hyperledger.org/public-networks/concepts/node-sync) y [redes privadas](https://besu.hyperledger.org/private-networks/concepts/node-sync-private):

- `FULL`: descarga y verifica la cadena desde el génesis.
- `SNAP`: snap sync, descrito más arriba. Para servir datos de snap sync a otros nodos hace falta almacenamiento Bonsai, que es el formato por defecto (`--data-storage-format`), y activar `--snapsync-server-enabled`, que por defecto está desactivado.

Si no se indica `--sync-mode`, Besu usa `SNAP` solo cuando se conecta a una red pública con nombre (opción `--network`) sin fichero génesis propio. En cualquier otro caso, y por tanto en toda red privada que arranca con `--genesis-file`, el valor por defecto es `FULL`.

Modos obsoletos:

- Fast sync dejó de estar soportado en Besu 26.2.0. Se sustituye por snap sync.
- `CHECKPOINT` ya no es un modo propio. Si se pasa `--sync-mode=CHECKPOINT`, Besu muestra un aviso y realiza snap sync, usando el checkpoint configurado en el génesis. Desde Besu 26.8.0, la opción `--checkpoint=<hash>:<number>:<totalDifficulty>` permite fijar ese punto de confianza por línea de comandos; solo la usa snap sync y se ignora, con un aviso, en modo `FULL`.

Para migrar una configuración antigua, sustituye `FAST` o `CHECKPOINT` por `SNAP`.

La documentación de redes privadas recomienda full sync para los nodos iniciales de la red y siempre que los pares no puedan servir datos de snap sync.

Para que un nodo nuevo de una red privada pueda sincronizar en modo snap, al menos uno de los nodos existentes tiene que servir esos datos. En el host de un nodo existente, con almacenamiento Bonsai:

```bash
besu --genesis-file=genesis.json \
  --data-storage-format=BONSAI \
  --snapsync-server-enabled=true
```

En el host del nodo que se incorpora a la red:

```bash
besu --genesis-file=genesis.json \
  --bootnodes=<enode-del-bootnode> \
  --sync-mode=SNAP
```

Ambos nodos usan el mismo fichero génesis de la red. El resto de opciones (identificador de red, permisos, puertos) dependen de la configuración concreta de cada red.

## Desafíos

- Ancho de banda y disco: sincronizar desde cero implica descargar cientos de GB en las redes públicas grandes.
- Coste de validación: ejecutar y verificar millones de transacciones exige mucha CPU y E/S de disco.
- Crecimiento del estado: el estado global crece de forma continua, lo que encarece cada nueva sincronización y obliga a aplicar pruning.
- Pares maliciosos o lentos: un par puede enviar datos falsos o servirlos despacio para retrasar al nodo. Las cabeceras y las raíces de estado permiten detectar los datos falsos, pero un nodo rodeado solo de pares maliciosos (ataque [Eclipse](02-challenges-and-vulnerabilities.md#ataques-a-la-seguridad)) puede acabar siguiendo una cadena equivocada. Por eso importa la [selección de peers](04-bootstrap-and-node-discovery.md#selección-de-peers).

## Resolución de problemas

- Un nodo Besu en una red privada no avanza con `--sync-mode=SNAP`: ningún par sirve datos de snap sync. Comprueba que al menos un nodo existente use almacenamiento Bonsai y tenga `--snapsync-server-enabled=true`, o sincroniza el nodo nuevo con `--sync-mode=FULL`.
- Al arrancar aparece el aviso "CHECKPOINT sync mode is deprecated and has been removed": la configuración usa `--sync-mode=CHECKPOINT`, que Besu ya trata como snap sync. Cambia el valor a `SNAP` para que la configuración refleje lo que hace realmente.
- Un nodo configurado con `--sync-mode=FAST` deja de arrancar tras actualizar a Besu 26.2.0 o posterior: ese modo ya no existe. Cambia el valor a `SNAP`.
