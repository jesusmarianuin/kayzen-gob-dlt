# Gobernanza de la red

Frente a una base de datos distribuida, que pertenece técnica y organizativamente a una única entidad central (véase [distribución versus descentralización](../../knowledge-base/blockchain.md)), la Administración puede optar por un modelo con separación entre lo común y lo particular. Aparece así el concepto de gobernanza: la capacidad que se otorga a los participantes de la red para decidir sobre la evolución del *ledger*. En el marco europeo, el modelo dominante es el federado, donde se acuerda un marco tecnológico y normativo común manteniendo al mismo tiempo la autonomía operativa de cada organismo.

## El nodo como infraestructura propia y compartida

Desde la perspectiva de una Administración pública, esto modifica sustancialmente la arquitectura de integración. Ya no se trata únicamente de consumir una API REST expuesta por otro organismo. La Administración despliega y opera su propio nodo, utilizándolo para consultar, registrar transacciones, validar evidencias y comunicarse con el resto de la red. Ese nodo es una pieza de infraestructura propia y, simultáneamente, un componente de una infraestructura compartida. La organización deja de ser un mero cliente para convertirse en proveedor y participante de la red.

Esta es, en realidad, una de las ideas centrales de una arquitectura DLT con tecnología blockchain: los participantes actúan como pares (*peers*). Cada nodo consume y aporta capacidad, disponibilidad y validación al conjunto mediante un protocolo de consenso como QBFT (*Quorum Byzantine Fault Tolerant*) en Hyperledger Besu.

Es evidente que en la Administración el grado de descentralización será menor, articulándose mediante redes permisionadas o de consorcio, con participantes identificados, identidades institucionales vinculadas y mecanismos normativos de incorporación. No obstante, aunque la descentralización sea acotada, la autonomía de los participantes sigue siendo relevante: el sistema deja de depender técnicamente de un único punto de control o de fallo. De lo contrario, no tendría sentido asumir el coste que supone mantener este tipo de redes.

## Qué decide la gobernanza

Junto a la infraestructura técnica emerge la gobernanza. Una DLT resuelve la sincronización criptográfica del *ledger*, pero no determina por sí misma quién tiene derecho a desplegar un nodo, qué versión del cliente es la oficial, qué contratos inteligentes (*smart contracts*) se despliegan, qué modelos de datos son los estándares, cómo se gestiona el alta o baja de un participante ni cómo se responde ante la detección de un fallo de seguridad. Todas estas cuestiones pertenecen al plano de la gobernanza y, en una red administrativa, su resolución requiere mayor esfuerzo organizativo que el despliegue técnico de los nodos.

La gobernanza es vital porque una red DLT es un sistema dinámico. El software se actualiza, los esquemas de datos evolucionan y los contratos inteligentes requieren parches. En un entorno centralizado, la entidad propietaria aplica la actualización de forma unilateral. En una red federada de organismos independientes, es imprescindible la coordinación para evitar discrepancias en las reglas de validación que originen bifurcaciones de la red (*forks*).

## Estándares abiertos

Esta necesidad de alineamiento exige el uso de estándares abiertos. La red puede compartir la misma capa de consenso y, sin embargo, resultar inoperativa si cada organismo interpreta la información de forma divergente. Por ello, una DLT en la administración requiere acuerdos sobre modelos de datos, ontologías (es decir, vocabulario común sin ambigüedad), sentido semántico, identificadores y esquemas de contratos inteligentes. Es en esta capa de estandarización donde la DLT actúa como una verdadera infraestructura de interoperabilidad.

## Resiliencia

Otro factor determinante es la resiliencia. Dado que múltiples nodos mantienen una copia idéntica del *ledger*, se genera una redundancia estructural de la información. La caída temporal de un nodo no compromete la disponibilidad de los datos ni la continuidad del registro en la red.

Conviene, sin embargo, distinguir entre redundancia de datos y redundancia de servicio. Que otros nodos posean la misma información no significa que automáticamente puedan sustituir a nuestro nodo cuando este falla. Para que eso ocurra es necesario diseñar mecanismos de acceso, autenticación, autorización y reparto de carga. Si una Administración quiere utilizar temporalmente el nodo de otra porque el suyo está saturado o fuera de servicio, la red debe haber previsto esa posibilidad. Debe estar definido qué operaciones pueden delegarse, qué garantías existen, cómo se contabiliza el consumo y quién asume la responsabilidad.

## Economía interna

En ese punto aparece otra consecuencia interesante: una red colaborativa necesita alguna forma de economía interna. Mantener nodos tiene coste. Se consume almacenamiento, cómputo, ancho de banda, monitorización, soporte y trabajo operativo. Si algunos participantes aportan mucha capacidad y otros utilizan más recursos de los que proporcionan, puede ser conveniente establecer mecanismos de compensación. Eso no implica necesariamente dinero ni criptomonedas. Puede tratarse de simples créditos internos, unidades de servicio o balances de aportación y consumo. Una organización puede acumular capacidad disponible ayudando a otros participantes y consumirla posteriormente cuando lo necesite.

> El siguiente [caso hipotético de mundo ideal](../../idea-sandbox/brave-new-world-ideas.md) desarrolla la idea de que la economía también es relevante en una red de nodos, aunque se asume que en la Administración sería algo anecdótico.

Incluso podrían utilizarse tokens para representar esas unidades, pero el token no sería el objetivo del sistema. Sería únicamente una herramienta contable para coordinar recursos. Esta distinción es importante porque durante años se ha asociado blockchain casi exclusivamente con criptomonedas, cuando en una infraestructura de la administración el uso más razonable de un token puede ser mucho más prosaico: representar derechos, capacidad, autorizaciones o unidades de consumo.
