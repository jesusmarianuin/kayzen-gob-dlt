# Coste del gas

En una red de la Administración tiene sentido que el gas cueste cero, siempre que se siga midiendo y limitando lo que consume cada organismo. Ponerle un precio real solo aporta algo propio en un caso: cuando participan terceros que deben costear su uso.

## Qué es el gas

El gas es la unidad que [mide el trabajo de cómputo](https://ethereum.org/en/developers/docs/gas/) que exige cada operación en una red basada en Ethereum, como Besu. Hay que separar tres cosas:

- Consumo: las unidades de gas que gasta una transacción, según lo que haga.
- Límite: el máximo de unidades que admiten una transacción y un bloque.
- Precio: lo que se paga por cada unidad. La comisión de una transacción es su consumo multiplicado por el precio.

Una [red de gas gratuito](https://docs.besu-eth.org/private-networks/how-to/configure/free-gas) solo elimina el precio. Las transacciones siguen consumiendo gas y los límites siguen vigentes. Además, es una decisión de toda la red: un nodo que exija un precio mínimo descarta sin avisar las transacciones de precio cero.

## Qué cambia con el precio a cero

En Ethereum, la comisión cumple tres funciones, y cada una corre una suerte distinta:

- [Frenar el abuso](https://ethereum.org/en/developers/docs/gas/): enviar muchas transacciones cuesta dinero. Con precio cero este freno desaparece, y hay que sustituirlo por otro.
- [Pagar a quien valida](https://ethereum.org/en/developers/docs/gas/): en una red de la Administración no hace falta, porque cada organismo costea su nodo. La red sigue teniendo [costes reales](network-governance.md), pero no se pagan transacción a transacción.
- Influir en el orden: el precio ofrecido [afecta a la posición de la transacción](transaction-ordering.md). Con precio cero, ningún organismo puede pagar por pasar delante.

Un bucle infinito se sigue deteniendo con precio cero, porque lo corta el límite de gas. Por eso el límite de bloque no debe subirse hasta dejarlo sin efecto: Besu recomienda [acercarlo a lo que los validadores pueden procesar](https://docs.besu-eth.org/private-networks/how-to/configure/free-gas) en cada bloque.

También desaparece un incentivo: nadie paga por escribir de más, y lo escrito [hace crecer el estado de la red](besu-design-challenges.md).

## Por qué el precio cero suele ser correcto

Las comisiones protegen a una red abierta de participantes desconocidos. En una red permisionada, el freno puede ser otro: se puede [restringir qué cuentas operan y suspenderlas](https://docs.besu-eth.org/private-networks/concepts/permissioning), y quien abusa está identificado.

El riesgo pasa a ser sobre todo el fallo, no el ataque de un desconocido: una aplicación que repite envíos, un contrato mal diseñado o una clave robada. Un precio solo pararía estos fallos al agotarse el saldo, y entonces el organismo tampoco podría registrar sus operaciones legítimas.

Cobrar también crea trabajo nuevo: alguien tiene que emitir la unidad de pago, repartirla y controlar los saldos.

El precio cero deja un hueco. La [documentación de Besu](https://docs.besu-eth.org/public-networks/concepts/transactions/pool) describe límites a las transacciones pendientes de cada remitente, pero no un límite de consumo por cuenta u organismo a lo largo del tiempo. Sin una medida adicional, el fallo de un organismo puede llenar los bloques hasta que alguien lo detecte y lo suspenda.

## Qué permitiría un coste

Un coste abriría cuatro posibilidades, pero solo la última necesita de verdad un precio real.

### Repartir los costes según el uso

Quien más usa la red, más aporta. No hace falta precio, porque [cada transacción registra su remitente y su consumo de gas](https://ethereum.org/en/developers/docs/apis/json-rpc/). Basta con sumar el consumo de cada organismo.

### Frenar los excesos de forma automática

Un saldo que se agota detiene a quien consume demasiado. Una cuota de gas consigue lo mismo sin dinero y puede renovarse sola.

### Dar prioridad a lo urgente

Pagar más para pasar delante solo funciona con precio, pero sustituye la neutralidad entre organismos por una ventaja de quien más gasta. Una prioridad acordada en la [gobernanza](network-governance.md) no tiene ese efecto.

### Financiar la participación de terceros

Si la red se abre a entidades que no aportan nodos, como empresas que registran datos, un precio permite que costeen lo que usan. Si las unidades de pago se pudieran transferir y tuvieran valor económico, habría que analizar además si les aplica MiCA, el reglamento europeo de criptoactivos.

## Opciones de diseño

### Precio cero con límites generales

Se fija el precio a cero, se ajustan los límites de transacción y de bloque y se restringen las cuentas permitidas. Es lo más sencillo y no requiere desarrollo propio. Un organismo con un fallo puede ocupar la capacidad de los demás hasta que alguien intervenga, así que encaja en redes con pocos participantes y monitorización activa.

### Precio cero con cuotas por organismo

Cada organismo recibe una cantidad de gas por bloque. LACNet, una red permisionada basada en Besu, tiene un [modelo documentado](https://github.com/lacchain/gas-management/blob/master/docs/OVERVIEW.md):

- El gas se asigna a los nodos que escriben, no a los usuarios finales.
- Un contrato lleva la cuenta de lo que tiene cada nodo por bloque. Los límites van desde 500 000 unidades hasta un reparto de lo que queda disponible, según el tipo de miembro.
- Quien supera su cuota queda fuera de la lista de permitidos y debe explicar lo ocurrido para volver.

Protege a cada organismo del fallo de otro, pero añade contratos y cambia el camino de las transacciones, porque pasan por un intermediario que las comprueba. Besu no lo incluye, y el repositorio citado está archivado desde 2022 y remite a [su continuación](https://github.com/LACNetNetworks/gas-management).

### Precio cero con reparto de costes

La red mide el consumo de cada organismo fuera de la cadena y lo usa para repartir los gastos. Si la red se regula por convenio, las [aportaciones no pueden superar los gastos de ejecutarlo](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566#a48) y hay que [fijar el compromiso económico de cada parte](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566#a49). Este reparto no afecta a las transacciones, pero tampoco frena nada: solo contabiliza.

### Precio real con unidades internas

Cada transacción paga con una unidad interna que un órgano común reparte. Es el único modelo con freno económico directo, y el más costoso de operar: si un organismo se queda sin saldo, deja de registrar, y el precio vuelve a influir en el orden.

## Cómo elegir

Las tres primeras opciones se pueden combinar:

- Red con pocos organismos: límites generales y, si los costes son desiguales, reparto de costes.
- Red con muchos participantes o con cargas muy distintas: añadir cuotas.
- Red con terceros que no aportan nodos: valorar un precio solo para ellos.
