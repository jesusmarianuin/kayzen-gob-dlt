# Orden de las transacciones

Una blockchain impone a sus registros una secuencia única que todos los nodos comparten y pueden verificar. Esa secuencia es el orden en que las transacciones entraron en el *ledger*, que no tiene por qué coincidir con el orden en que se enviaron ni con el orden en que ocurrieron los hechos que describen. La pregunta de diseño no es si la red ordena, porque siempre lo hace, sino qué orden necesita cada operación y quién lo decide en realidad.

## Tres órdenes distintos

Conviene separar tres secuencias que a menudo se dan por iguales:

- Orden de los hechos: cuándo ocurrió lo que se registra, por ejemplo cuándo se resolvió un expediente. Está fuera de la red, y la red no puede comprobarlo por sí misma.
- Orden de llegada: cuándo recibió cada nodo la transacción. Cada nodo tiene el suyo, y no queda guardado en el *ledger*.
- Orden del *ledger*: el número de bloque y la posición dentro del bloque. Es único, verificable por cualquier participante y, con la finalidad inmediata de QBFT, definitivo una vez confirmado el bloque.

La red solo garantiza el tercero. Los otros dos solo se reflejan en él si el diseño lo procura.

## Qué garantiza Besu

Lo que sigue describe la [documentación del *pool* de transacciones](https://docs.besu-eth.org/public-networks/concepts/transactions/pool) y el código de la rama principal de Besu en noviembre de 2026. Los criterios del *pool* no forman parte del protocolo y pueden cambiar entre versiones.

### Entre transacciones de un mismo remitente

El orden es estricto y es una regla de consenso. Cada cuenta tiene un contador, el *nonce*, y [una transacción solo es válida si su *nonce* coincide con el de la cuenta](https://github.com/hyperledger/besu/blob/main/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/mainnet/MainnetTransactionValidator.java). Un bloque que altere esa secuencia se rechaza, lo decida quien lo decida.

### Entre remitentes distintos

El protocolo no fija ningún orden. Los [validadores se turnan para proponer el bloque](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft), y el proponente de cada turno elige qué transacciones incluye y en qué posición. Los demás comprueban que el bloque sea válido, no que su orden sea el que ellos habrían elegido. Un proponente también puede omitir una transacción válida, pero eso normalmente solo la retrasa: como los validadores se turnan, el siguiente puede incluirla si le ha llegado.

### Cómo ordena el proponente

El orden sale del *pool* del nodo proponente. Besu procede de Ethereum, donde cada transacción ofrece un precio por procesarla y ese precio influye en su orden. En una red de la Administración suele fijarse en cero, de modo que no interviene ningún factor económico, pero el software conserva el criterio y por eso importa qué implementación se elige:

- *Layered*: es la predeterminada de Besu y está pensada para redes abiertas como Ethereum. Ordena por ese precio, que con valor cero deja de distinguir entre transacciones.
- *Sequenced*: es la recomendada para redes privadas y la predeterminada con el perfil *enterprise*. Funciona como una cola en la que se atiende primero a quien llega primero.

Esa cola no equivale a un orden justo entre organismos, por tres motivos:

- Algunas transacciones se saltan la cola. [Por defecto, cada nodo da prioridad](https://github.com/hyperledger/besu/blob/main/ethereum/eth/src/main/java/org/hyperledger/besu/ethereum/eth/transactions/TransactionPool.java) a las que le envían directamente, no a las que le reenvían otros nodos, y también a las de los remitentes que tenga configurados en una lista. El [criterio del *pool* secuenciado](https://github.com/hyperledger/besu/blob/main/ethereum/eth/src/main/java/org/hyperledger/besu/ethereum/eth/transactions/sorter/GasPricePendingTransactionsSorter.java) atiende primero a estas, después mira el precio y deja la llegada como desempate. Con [precio cero para todos](https://docs.besu-eth.org/private-networks/how-to/configure/free-gas), lo habitual en estas redes, solo cuentan la prioridad y la llegada. Así, en su turno, un validador adelanta las transacciones de su organismo a otras más antiguas, salvo que se desactive esa prioridad.
- La llegada es la del nodo proponente. Dos transacciones enviadas casi a la vez a nodos distintos pueden llegarle invertidas, y una transacción firmada antes puede entrar después.
- El *pool* es configuración local, no consenso. Un validador con otros criterios produce bloques igual de válidos, y como la llegada no se guarda en el *ledger*, la cadena por sí sola no permite demostrar que el orden se alteró.

### La marca de tiempo del bloque

Cada bloque lleva la hora que le pone el validador que lo propone, según su propio reloj. Esa hora indica aproximadamente cuándo se registró el bloque, no cuándo ocurrieron los hechos. Además, todas las transacciones del bloque comparten la misma hora, así que tampoco dice cuál fue antes.

## Cuándo importa el orden

Si dos organismos envían una transacción casi a la vez, la que se envió primero puede quedar registrada después, y la red no lo impide. A veces eso es un problema y a veces no.

No es un problema si las operaciones no se afectan entre sí. Si dos universidades registran los títulos de dos personas distintas, da igual cuál entre antes, porque el resultado es el mismo.

Sí es un problema en estos casos:

- Una operación depende de otra. Un título no se puede revocar antes de haberse emitido, así que la emisión tiene que quedar antes.
- Varias solicitudes compiten por algo limitado, como plazas o ayudas que se conceden por orden de presentación. Quien queda delante la obtiene, así que el orden tiene efectos jurídicos. La Ley 39/2015 establece como regla general respetar el [orden de recepción en los registros](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a16) y el [orden de inicio de los expedientes](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a71) similares.

Los plazos son otra cuestión: no cuenta quién va antes, sino si se llegó a tiempo. La hora del bloque es aproximada, así que por sí sola no acredita la hora exacta.

## Decisiones de diseño

Como la red no garantiza el orden entre organismos, hay que diseñar el sistema para que eso no cause problemas. Estas son las medidas:

**Envío correcto**:

Enviar cada operación cuando la anterior de la que depende ya esté registrada. Antes de revocar un título, el sistema comprueba en el ledger que consta como emitido. Con QBFT esa comprobación es fiable, porque un bloque confirmado no se revierte.

**Comprobación vs tratado posterior**:

Existen dos opciones de diseño, una que el contrato compruebe el orden. El contrato sabe en qué situación está cada título, como emitido o revocado, y rechaza lo que no tenga sentido, como revocar un título que no se ha emitido. La transacción rechazada no cambia nada, pero queda en el bloque como fallida, así que se ve que llegó fuera de orden.

La optra opcion es aceptar también lo que llegue fuera de orden y ordenarlo por la fecha del hecho, no por la de registro. Si llega la revocación de un título cuya emisión aún no consta, se guarda como pendiente y se aplica cuando llegue la emisión. Si esta no llega nunca, un responsable tiene que revisarlo.

**Información contable para el smart contract**:

Si queremos que un smart contract pueda realizar una validación determinista de un estado, debe tener la mínima información necesaria en la blockchain, o mejor dicho en el estado de cuenta e igualmente en la información de la transacción.

Es tendencia en los diseños de la Administración para respetar las reglas de [protección de datos](data-protection.md) poner información como hashes o de conocimiento cero, pero esto debe ser cotejado con lo que realmente es un ledger, un registro contable y sin nada que contar se convierte en algo inútil.

**Fecha del hecho y fecha de registro**:

Son dos fechas distintas y hay que guardarlas por separado. La del hecho viaja en una atestación, una declaración firmada por el organismo competente. La de registro es la del bloque. El contrato comprueba quién firma, pero no puede saber si la fecha es cierta.

**Un único remitente**:

Si todas las operaciones salen de la misma cuenta, el *nonce* ya garantiza su orden. El inconveniente es que, si una transacción se atasca, todas las siguientes de esa cuenta quedan esperando. Por eso solo conviene cuando haga falta un orden estricto.

Esto también afecta a un organismo que opere con una sola cuenta y una sola clave privada: el *nonce* no se agotaría en la práctica, pero todas sus operaciones dependerían de una misma cola y una transacción atascada detendría las demás.

**Orden con efectos jurídicos**:

Cuando el orden tiene efectos jurídicos, no debe depender de lo que ocurra dentro de la red. Existen dos opciones de diseño.

Una es fijar el orden antes de enviar a la red, con un registro electrónico o con un sello de tiempo cualificado. Este sello es una fecha y hora certificadas por un prestador de confianza. La transacción lleva esa prueba.

La otra es no atender por orden de llegada. Se reciben las solicitudes hasta una fecha límite y el organismo las ordena con una regla pública, fuera de la blockchain. En el *ledger* solo se registra el resultado.

**Configuración del *pool***:

Si cada validador configura su *pool* de forma distinta, el orden dependerá de a quién le toque proponer el bloque. Por eso los organismos deben acordar en la [gobernanza](network-governance.md) una misma configuración, en la que ningún nodo dé prioridad a sus propias transacciones salvo que se haya pactado.

De todas formas, no se puede demostrar que todos los nodos tengan la misma configuración, así que el orden del ledger no demuestra que las transacciones se atendieran por orden de llegada.

**Corrección de errores**:

Lo registrado no se puede cambiar. Si dos operaciones quedan en un orden equivocado, se registra otra nueva que lo rectifica, y todas permanecen en el *ledger*.

**Pruebas**:

En la [red local de pruebas](besu-design-challenges.md) se envían transacciones a la vez a nodos distintos, para comprobar que el resultado es correcto sea cual sea el orden en que queden registradas.

## Qué dice eIDAS 2 sobre el orden

eIDAS 2 regula un servicio llamado libro mayor electrónico cualificado, creado y gestionado por prestadores cualificados de servicios de confianza. Para los datos registrados en él, presume un orden cronológico secuencial único y exacto, y su integridad ([artículos 45 duodecies y 45 terdecies del Reglamento (UE) 910/2014, modificado por el Reglamento (UE) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/spa)).

En realidad, eIDAS2 solo habla de garantozar el orden y la integridad de cuándo se anotó el dato en el libro, no el orden real del hecho que ese dato describe.
