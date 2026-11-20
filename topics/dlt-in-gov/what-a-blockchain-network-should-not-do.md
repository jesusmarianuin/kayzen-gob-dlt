# Lo que una red blockchain no debería hacer

Montar una red blockchain en la Administración no consiste solo en levantar nodos. Hay decisiones que parecen razonables al principio y que, con el tiempo, dejan la red expuesta o le quitan el sentido. Casi nunca se toman de forma intencionada: aparecen por comodidad, por prisa o porque la organización que arranca el proyecto se ocupa de todo y nadie más lo cuestiona.

Este documento recoge lo que una red blockchain no debería hacer y los errores que una organización debería evitar al crearla. Cada uno se explica por separado, con casos reales cuando los hay.

## Definir sola las reglas y el software

Un error frecuente es que la misma organización escriba las reglas de la red, programe el software que las aplica y sea la única que entiende cómo funciona. En ese caso las reglas no son un acuerdo, son lo que haga ese software, y nadie más está en condiciones de revisarlas.

Ethereum muestra el camino contrario. Sus reglas están escritas en una especificación pública, el conocido Yellow Paper y las especificaciones que lo han sucedido, y distintos equipos independientes construyen su propio cliente a partir de ella. Gracias a eso existe variedad: si un cliente tiene un fallo grave, caen los nodos que lo usan, pero el resto sigue funcionando. Ya ha pasado varias veces; en enero de 2024 un fallo en uno de los clientes de Ethereum dejó parados a los nodos que lo ejecutaban mientras la red seguía adelante con los demás. Ethereum lo explica en su página sobre la [diversidad de clientes](https://ethereum.org/es/developers/docs/nodes-and-clients/client-diversity/).

En una red de la Administración no siempre habrá varios clientes distintos, pero la idea se mantiene: las reglas de la red (qué datos se guardan, qué contratos hay, cómo se valida) deben estar escritas y publicadas como un acuerdo común, comprensible por todos los participantes. Si mañana el equipo que las escribió desaparece, la red tiene que poder seguir.

## Operar todos los nodos igual y desde el mismo sitio

Seguir unas reglas comunes de seguridad está bien. Lo que no debe ocurrir es que todos los nodos se operen de la misma forma, con la misma infraestructura y por el mismo equipo. Cada organización debería operar su nodo de manera independiente: en su propio centro de datos o proveedor, con su propio personal y sus propios procedimientos.

Si todos los nodos viven en la misma nube, comparten configuración y los administra la misma gente, un único problema los afecta a todos a la vez: una caída del proveedor, un error de configuración, una credencial robada o una vulnerabilidad en una pieza común. Si cada uno sigue su propio camino, un fallo derriba algunos nodos pero los demás continúan.

Hay un caso real que lo ilustra. Un proveedor de alojamiento decidió expulsar de sus servidores a los nodos de una conocida red pública y, de golpe, una parte importante de sus validadores se desconectó. La red sobrevivió porque no estaban todos allí, pero quedó claro el riesgo de concentrarlos.

## Acumular demasiado peso en el consenso

Las redes de la Administración suelen usar un consenso en el que un grupo de nodos validadores aprueba cada bloque. Ese mecanismo tolera que algunos validadores fallen o se comporten mal, siempre que no sean demasiados. Si una sola organización controla una parte grande de los validadores, puede bloquear la red por sí misma, y si controla la mayoría, puede decidir sola qué entra en ella.

Por eso no basta con contar nodos, hay que contar quién está detrás de cada uno. Diez validadores operados por la misma entidad equivalen, a efectos de confianza, a uno solo.

## Guardar las claves en las mismas manos

Cada validador firma con su propia clave. Si las claves de varios validadores las guarda la misma organización, o si una organización deja que otra firme en su nombre para simplificar, el reparto desaparece aunque los nodos sean de entidades distintas.

El robo al puente de la red Ronin en 2022, uno de los mayores de la historia de blockchain, sucedió así: la mayoría de las claves necesarias estaban en manos de la misma empresa, y otra participante le había autorizado a firmar en su nombre. Al comprometer a esa única empresa, el atacante tuvo todo lo que necesitaba. Cada participante debe custodiar sus claves y no delegarlas. Cómo se vincula cada clave con su organismo se trata en [identidad en la red](identity.md).

## Dar acceso a la red por una única puerta

Puede que la red esté bien repartida y, sin embargo, que todas las aplicaciones se conecten a ella a través del nodo de una sola organización o de un único punto de acceso. Si esa puerta se cierra, la red sigue funcionando, pero nadie puede usarla.

Ocurrió en Ethereum en 2020. Un proveedor muy usado para acceder a la red se quedó desalineado tras un fallo y muchas aplicaciones dejaron de funcionar, aunque la red seguía operativa. Dependían de un intermediario, no de la red. Cada organismo debería acceder a través de su propio nodo, y si se comparte el acceso, debe ser una decisión prevista y no un hábito, como se explica en [gobernanza de la red](network-governance.md).

## Dejar los contratos con un único dueño

Los smart contracts de la red a menudo se pueden actualizar o pausar. Si ese permiso lo tiene una sola cuenta, quien la controle puede cambiar las reglas sin preguntar a nadie, y si le roban la clave, el atacante también. Lo mismo vale para los contratos que deciden quién puede entrar en la red.

Estos permisos deberían requerir el acuerdo de varios participantes y dar tiempo a los demás para reaccionar antes de que un cambio se aplique. Las técnicas para hacerlo se describen en [inmutabilidad y evolución de los smart contracts](smart-contract-upgradeability.md).

## Actualizar todos los nodos a la vez desde un solo punto

Cuando una organización gestiona un sistema que despliega automáticamente cada nueva versión en todos los nodos, cualquier error en esa versión llega a toda la red a la vez. Fuera de blockchain hay un ejemplo muy conocido: en 2024 una actualización defectuosa de un producto de seguridad, instalada a la vez en millones de equipos, los dejó inservibles en todo el mundo en cuestión de horas.

En una red federada, cada organización debería decidir cuándo actualiza su nodo, dentro de los plazos acordados. Ir a distintas velocidades parece menos eficiente, pero es lo que permite detectar un problema en unos pocos nodos antes de que afecte a todos.

## Guardar fuera de la red los datos importantes en un solo sitio

Es habitual guardar en la cadena solo una huella o una referencia, y dejar el documento real en otro sistema. Es una buena práctica, sobre todo por [protección de datos](data-protection.md), pero si ese otro sistema es un único servidor de una única organización, la red certifica algo que depende por completo de ella. Si ese servidor cae o se pierde, la referencia en la cadena apunta a la nada.

Cuando los datos externos son necesarios para que la red cumpla su función, conviene que estén replicados o custodiados por más de un participante, o al menos que cada interesado pueda guardar su propia copia.

## Una pregunta para revisar el diseño

Antes de dar por bueno un diseño conviene hacerse una pregunta: si una sola organización desaparece, se equivoca o es atacada, ¿la red sigue funcionando y los demás pueden seguir usándola? Si la respuesta es no, alguno de estos errores está presente.
