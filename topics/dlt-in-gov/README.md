# DLT en la Administración

Lo primero que se debe aclarar es qué es una DLT, porque seamos honestos: existen demasiado pocas definiciones rigurosas y demasiadas imprecisiones.

Primero vamos a aclarar qué es un *ledger*. Encontramos aquí una buena definición sobre [qué es un ledger](https://www.hosteltur.com/hosteltur-responde/ledger), donde se aclara algo no trivial: es un registro contable, se genera de forma cronológica y refleja transacciones. Por ello se le denomina tradicionalmente como el registro de verdad o la «fuente única de verdad» (*single source of truth*).

Para este contexto de DLT, no es correcto pensar en el *ledger* como una base de datos convencional; es más bien un registro append-only (solo lectura y escritura al final) que sirve para identificar, auditar y validar una transacción junto con su estado final.

Cuando decimos que es distribuido, encontramos otra buena explicación sobre [distribuido vs. descentralizado](https://blockandcapital.com/es/distribuido-vs-descentralizado/). Un registro está distribuido porque varios actores, en forma de nodos, son responsables de mantener la misma copia del *ledger*. Esos nodos deben llegar a un acuerdo sobre el estado único de la red, y es aquí donde aparecen los **grados** de descentralización: si el estado depende únicamente de un coordinador central, no hay descentralización; si alcanza un estado común mediante un protocolo de consenso entre pares, existe cierto grado de descentralización; si además son nodos en una red sin restricciones de acceso ni necesidad de confianza (*trustless* y *permissionless*), es completamente descentralizado. Que un sistema sea distribuido no lo convierte automáticamente en descentralizado: la descentralización depende del grado de subordinación a una entidad central.

> En el ámbito de Web3 ha sido habitual utilizar este registro para validar el estado final de un saldo (ya sea mediante el modelo UTXO o mediante el control de cuentas). No obstante, esa es solo una decisión de diseño específica. La idea subyacente es más simple: la DLT sirve como registro inmutable de un estado final, que no tiene por qué ser un saldo financiero, sino cualquier concepto o hecho jurídico/administrativo. Mientras que en Web3 el saldo es necesario para la composabilidad financiera, la Administración pública quizás solo necesita un registro incontestable sobre un hecho objetivo que ha sucedido en un momento determinado.

Conociendo que existe una red de nodos que mantiene un *ledger* distribuido con mayor o menor grado de descentralización, podemos explicar mejor qué es la tecnología DLT. Dentro de las diversas familias existentes, nos centraremos en el modelo de *blockchain*, no porque sea el único, sino porque es la tecnología sobre la que se apoya Hyperledger Besu, que es la solución técnica elegida en la infraestructura europea EBSI (European Blockchain Services Infrastructure).

Cuando concretamos que existe una red de nodos que mantiene una DLT mediante tecnología blockchain, podemos definir una nueva lógica de negocio denominada «on-chain», que constituye la capa de validación, anclaje y consolidación de la información.»

## Qué es y qué no es una DLT

Esta contextualización es fundamental porque nos ofrece una demarcación muy clara de lo que es y lo que no es una DLT.

Cuando se aborda el uso de DLT en la Administración Pública, existe una tendencia a tratarla como una tecnología más dentro del catálogo de sistemas tradicionales: una nueva base de datos, una plataforma adicional o, en el peor de los casos, un elemento novedoso que incorporar a la arquitectura por mera tendencia. Ese enfoque es el primer error sistemático que conviene evitar. Una DLT carece de sentido entendida como una pieza aislada o como una simple sustitución de un sistema de bases de datos. Su valor emerge cuando articula una red de nodos operados por organizaciones independientes que necesitan colaborar, compartir un estado inalterable y operar sin depender de un único proveedor u organismo central (por ejemplo, nodos distribuidos entre universidades, ministerios, comunidades autónomas y entidades locales).

La diferencia es estructural. Una base de datos distribuida puede estar replicada en varios centros de datos y seguir perteneciendo, técnica y organizativamente, a una única entidad central que la coordina. Esa entidad decide el modelo de datos, controla las actualizaciones, administra los servidores, gestiona los permisos y determina qué versión del sistema es válida.

Por el contrario, la Administración puede optar por un modelo con separación entre lo común y lo particular. Aparece así el concepto de **gobernanza**: la capacidad que se otorga a los participantes de la red para decidir sobre la evolución del *ledger*. En el marco europeo, el modelo dominante es el federado, donde se acuerda un marco tecnológico y normativo común manteniendo al mismo tiempo la autonomía operativa de cada organismo.

Desde la perspectiva de una Administración pública, esto modifica sustancialmente la arquitectura de integración. Ya no se trata únicamente de consumir una API REST expuesta por otro organismo. La Administración despliega y opera su propio nodo, utilizándolo para consultar, registrar transacciones, validar evidencias y comunicarse con el resto de la red. Ese nodo es una pieza de infraestructura propia y, simultáneamente, un componente de una infraestructura compartida. La organización deja de ser un mero cliente para convertirse en proveedor y participante de la red.

Esta es, en realidad, una de las ideas centrales de una arquitectura DLT con tecnología blockchain: los participantes actúan como pares (*peers*). Cada nodo consume y aporta capacidad, disponibilidad y validación al conjunto mediante un protocolo de consenso como QBFT (*Quorum Byzantine Fault Tolerant*) en Hyperledger Besu.

Es evidente que en la Administración el grado de descentralización será menor, articulándose mediante redes permisionadas o de consorcio, con participantes identificados, identidades institucionales vinculadas y mecanismos normativos de incorporación. No obstante, aunque la descentralización sea acotada, la autonomía de los participantes sigue siendo relevante: el sistema deja de depender técnicamente de un único punto de control o de fallo. De lo contrario, no tendría sentido asumir el coste que supone mantener este tipo de redes.

Junto a la infraestructura técnica emerge la gobernanza. Una DLT resuelve la sincronización criptográfica del *ledger*, pero no determina por sí misma quién tiene derecho a desplegar un nodo, qué versión del cliente es la oficial, qué contratos inteligentes (*smart contracts*) se despliegan, qué modelos de datos son los estándares, cómo se gestiona el alta o baja de un participante ni cómo se responde ante la detección de un fallo de seguridad. Todas estas cuestiones pertenecen al plano de la gobernanza y, en una red administrativa, su resolución requiere mayor esfuerzo organizativo que el despliegue técnico de los nodos.

La gobernanza es vital porque una red DLT es un sistema dinámico. El software se actualiza, los esquemas de datos evolucionan y los contratos inteligentes requieren parches. En un entorno centralizado, la entidad propietaria aplica la actualización de forma unilateral. En una red federada de organismos independientes, es imprescindible la coordinación para evitar discrepancias en las reglas de validación que originen bifurcaciones de la red (*forks*).

Esta necesidad de alineamiento exige el uso de estándares abiertos. La red puede compartir la misma capa de consenso y, sin embargo, resultar inoperativa si cada organismo interpreta la información de forma divergente. Por ello, una DLT en la administración requiere acuerdos sobre modelos de datos, ontologías (es decir vocabulario común sin ambigüedad), sentido semántico, identificadores y esquemas de contratos inteligentes. Es en esta capa de estandarización donde la DLT actúa como una verdadera infraestructura de interoperabilidad.

Otro factor determinante es la resiliencia. Dado que múltiples nodos mantienen una copia idéntica del *ledger*, se genera una redundancia estructural de la información. La caída temporal de un nodo no compromete la disponibilidad de los datos ni la continuidad del registro en la red.

Conviene, sin embargo, distinguir entre redundancia de datos y redundancia de servicio. Que otros nodos posean la misma información no significa que automáticamente puedan sustituir a nuestro nodo cuando éste falla. Para que eso ocurra es necesario diseñar mecanismos de acceso, autenticación, autorización y reparto de carga. Si una Administración quiere utilizar temporalmente el nodo de otra porque el suyo está saturado o fuera de servicio, la red debe haber previsto esa posibilidad. Debe estar definido qué operaciones pueden delegarse, qué garantías existen, cómo se contabiliza el consumo y quién asume la responsabilidad.

En ese punto aparece otra consecuencia interesante: una red colaborativa necesita alguna forma de economía interna. Mantener nodos tiene coste. Se consume almacenamiento, cómputo, ancho de banda, monitorización, soporte y trabajo operativo. Si algunos participantes aportan mucha capacidad y otros utilizan más recursos de los que proporcionan, puede ser conveniente establecer mecanismos de compensación. Eso no implica necesariamente dinero ni criptomonedas. Puede tratarse de simples créditos internos, unidades de servicio o balances de aportación y consumo. Una organización puede acumular capacidad disponible ayudando a otros participantes y consumirla posteriormente cuando lo necesite.

> El siguiente [caso hipotético de mundo ideal](../../idea-sandbox/brave-new-world-ideas.md), desarrolla esta idea posible sobre como la economía es un también relevante en una red de nodos, pero se asume que en la administración sería algo anecdótico.

Incluso podrían utilizarse tokens para representar esas unidades, pero el token no sería el objetivo del sistema. Sería únicamente una herramienta contable para coordinar recursos. Esta distinción es importante porque durante años se ha asociado DLT casi exclusivamente con criptomonedas, cuando en una infraestructura de la administración el uso más razonable de un token puede ser mucho más prosaico: representar derechos, capacidad, autorizaciones o unidades de consumo.

La gestión de la identidad es otro pilar crítico. Una red de la administración exige la identificación fehaciente de cada nodo y de cada actor que firma una transacción. Esto requiere la integración con esquemas de PKI (*Public Key Infrastructure*), certificados electrónicos cualificados y marcos de Identidad Digital Descentralizada (mediante *Verifiable Credentials* y *Decentralized Identifiers* - DIDs, alineados con el reglamento eIDAS2 y las listas de confianza TSL). La custodia y gestión del ciclo de vida de las claves privadas institucionales se convierte en un requisito de alta seguridad, dado que la firma criptográfica vincula jurídicamente a la organización en el *ledger*.

> Resumen temprano y donde realmente este repositorio DLT tiene un trabajo importante en concretar.

Por último, la arquitectura debe ser plenamente respetuosa con la normativa de protección de datos (RGPD). Una DLT inmutable no debe utilizarse como almacenamiento primario de datos de carácter personal o confidencial, ya que la replicación masiva y la imposibilidad de alteración entran en conflicto directo con los derechos de supresión («derecho al olvido») y rectificación. El patrón arquitectónico correcto consiste en registrar *on-chain* exclusivamente *hashes*, evidencias criptográficas, estados o compromisos (*commitments*), manteniendo los datos personales *off-chain* en los sistemas de gestión tradicionales sujetos a sus correspondientes controles de acceso y políticas de borrado.

De este modo, la DLT actúa como un notario digital distribuido: permite demostrar la existencia, la integridad y la secuencia temporal de un documento o evento sin necesidad de exponer información subyacente.

## Cuándo es interesante una DLT

Una DLT tiene sentido únicamente bajo condiciones de diseño muy concretas. Resulta relevante cuando concurren los siguientes factores:

- Existen múltiples organizaciones normativamente autónomas.
- Todos los participantes necesitan compartir y confiar en un estado común de la información.
- Ninguna entidad debe o puede asumir el control centralizado de la infraestructura.
- Existe un valor claro en la verificación independiente y auditable de los registros.
- La trazabilidad, la inmutabilidad y la resiliencia interorganitativa son requisitos del sistema.

En cambio, si existe una única autoridad competente, todos los participantes aceptan que dicho organismo administre la base de datos centralizada y no aporta valor distribuir la gobernanza, una base de datos convencional será una solución infinitamente más eficiente, económica y sencilla de mantener. Ocurre lo mismo cuando el sistema requiere un rendimiento extremo en transacciones por segundo (TPS), latencias de milisegundos o procesamiento analítico masivo (OLAP). Una DLT introduce mecanismos de replicación y consenso que conllevan inevitablemente una penalización en rendimiento.

Una prueba rápida es evaluar si por mantener un registro central surgen conflictos de autonomía, gobernanza, auditoría independiente, trazabilidad o puntos únicos de fallo. Si fuera el caso, entonces tendríamos que considerar un DLT.

## Qué no debemos olvidar en una DLT

Las bases de datos relacionales acumulan décadas de madurez en archivado y retención, escalado, indexación y lenguajes de consulta como SQL. Una DLT renuncia a parte de esas capacidades a cambio de un estado compartido que cualquier participante puede verificar por sí mismo. Esa renuncia debe asumirse en la fase de diseño, no descubrirse en producción.

Estos son los retos que con más frecuencia condicionan una red de la Administración basada en Hyperledger Besu.

> Por cierto, son los retos críticos que precisamente son de interés para este repositorio de estudio.

### Crecimiento del *ledger* y del estado

Un nodo guarda dos cosas distintas, y las dos ocupan cada vez más espacio. Para verlo, sirve de ejemplo un registro de títulos universitarios sobre DLT:

- El historial es la lista de todo lo que ha pasado: cada título emitido, cada corrección y cada revocación, desde el primer día. Nunca se borra nada, así que solo puede crecer. Y crece incluso sin actividad, porque QBFT genera un bloque nuevo cada pocos segundos aunque nadie haya registrado nada.
- El estado es la foto del momento actual: qué títulos son válidos hoy. Es lo que el nodo consulta para validar cada operación nueva. Si esa foto se hace demasiado grande, el nodo se vuelve lento. A ese problema se le llama *[state bloat](https://superex.medium.com/superex-educational-series-understanding-state-size-and-state-bloat-f331bcaeb62b)*.

Besu ofrece [distintos formatos de almacenamiento](https://besu.hyperledger.org/public-networks/concepts/data-storage-formats): Bonsai conserva solo el estado reciente y ocupa mucho menos disco, mientras que Forest permite conservar los estados históricos. La elección no es solo técnica. Si la red debe responder a una auditoría sobre el estado en una fecha pasada, al menos algunos participantes tendrán que operar nodos de archivo y asumir su coste de almacenamiento. El dimensionamiento debe partir del volumen de transacciones previsto, del periodo de bloque y de la política de retención que exija la normativa de archivo.

### Indexación y consulta

Las estructuras internas del *ledger* (árboles Merkle Patricia) están optimizadas para generar pruebas de integridad y alcanzar consenso, no para consultas analíticas. La API JSON-RPC del nodo sirve para lecturas puntuales, pero no para búsquedas complejas ni informes.

El patrón habitual es que los *smart contracts* emitan eventos y que un *indexer* los lea y los cargue en una base de datos relacional o en un motor de búsqueda. Este patrón tiene tres consecuencias de diseño:

- Lo que un contrato no emite como evento es muy costoso de reconstruir después, así que los eventos se diseñan junto con el contrato, no al final.
- El *indexer* es una vista derivada, no la fuente de verdad. Las decisiones con efectos jurídicos deben poder verificarse contra el nodo.
- La finalidad inmediata de QBFT (un bloque confirmado no se revierte) simplifica el *indexer*, porque no tiene que gestionar reorganizaciones de la cadena como ocurre en redes públicas.

### Determinismo de la lógica *on-chain*

Cada nodo vuelve a ejecutar todas las transacciones, y todos deben llegar exactamente al mismo estado. Por eso un *smart contract* no puede llamar a APIs externas, leer el reloj del sistema ni generar números aleatorios. La única referencia temporal es la marca de tiempo del bloque, que fija el validador que lo propone y que solo es fiable dentro del margen que admite el consenso.

Esta restricción confirma que la capa *on-chain* es una capa aislada, no solo conceptualmente. El contrato no sale a buscar nada fuera: valida, ancla y consolida lo que le llega en cada transacción. Toda la lógica que depende del exterior se queda *off-chain*.

La respuesta habitual en las redes públicas para introducir datos externos son los oráculos (*oracles*): un intermediario consulta una fuente y escribe el dato en la cadena. En la Administración suele ser mejor evitarlos, porque existe una alternativa más directa: las atestaciones. El organismo competente, que es la fuente auténtica del dato, emite una declaración firmada (por ejemplo, una credencial verificable que acredita que una persona tiene un título). Esa atestación viaja dentro de la transacción, y el contrato solo comprueba la firma y que el emisor figura en un registro de emisores de confianza, como el que mantiene EBSI.

La diferencia es de confianza. Con un oráculo hay que fiarse del intermediario que transporta el dato; con una atestación se confía directamente en quien tiene la competencia legal para afirmarlo, y el contrato no necesita conocer ninguna fuente externa. Los oráculos solo compensan cuando el dato cambia de forma continua y nadie lo firma como hecho jurídico, como un índice de precios, y ese caso es poco frecuente en la Administración.

### Inmutabilidad y evolución de los *smart contracts*

El código de un contrato desplegado no se puede modificar. Es la misma propiedad que da valor al *ledger*, pero un error en un contrato queda en producción para siempre, y una norma que cambia obliga a cambiar las reglas que el contrato aplica.

Hay que distinguir dos inmutabilidades. La del historial no se negocia: lo registrado no se altera. La de la lógica sí puede relajarse, siempre que el cambio sea visible, esté gobernado y quede registrado *on-chain*. Para ello existen tres mecanismos que se diseñan desde el principio, porque no se pueden añadir a un contrato ya desplegado.

#### Proxies

Un *proxy* es un contrato que conserva la dirección y los datos, y delega la ejecución en un contrato de implementación que puede sustituirse. Quien interactúa con el sistema siempre usa la misma dirección, aunque la lógica haya cambiado por debajo.

Los patrones más extendidos son:

- *Proxy* transparente: la lógica de actualización vive en el *proxy* y solo puede invocarla un administrador.
- UUPS ([ERC-1822](https://eips.ethereum.org/EIPS/eip-1822)): la lógica de actualización vive en la implementación, lo que abarata el *proxy*, pero una implementación sin esa función bloquea para siempre futuras actualizaciones.
- *Beacon*: muchos *proxies* apuntan a un mismo contrato que indica la implementación vigente, útil cuando cada organismo tiene su propia instancia del mismo contrato y todas deben actualizarse a la vez.

#### Paradas de emergencia

Una parada de emergencia (*circuit breaker*, patrón *pausable*) permite suspender las operaciones de un contrato ante un incidente de seguridad o un error grave, sin esperar a tener una corrección. Los datos no se tocan: solo se bloquean las funciones marcadas como pausables.

Su diseño plantea tres preguntas que corresponden a la gobernanza:

- Quién puede pausar: debe ser rápido, así que suele bastar con un único rol de guardián o una firma múltiple.
- Qué se pausa: las escrituras críticas, pero conviene mantener las consultas para que la información siga siendo verificable.
- Quién reanuda: reanudar debe exigir más acuerdo que pausar, para que el guardián no pueda abusar del mecanismo.

El rol que pausa no debe ser el mismo que actualiza. Pausar es una medida defensiva y acotada; actualizar cambia las reglas.

#### Time locks

Un *time lock* introduce un retardo obligatorio entre la aprobación de una operación sensible (una actualización, un cambio de parámetros, un cambio de roles) y su ejecución. Durante ese plazo, la operación es pública y cualquier participante puede revisar el nuevo código, objetar por los cauces acordados o preparar sus sistemas.

En una red de la Administración el *time lock* es la traducción técnica de un plazo de información previa: ningún organismo puede cambiar las reglas comunes de un día para otro.

#### Cómo se combinan

El esquema habitual reparte los poderes según su urgencia y su impacto:

- Actualizar la implementación exige firma múltiple de varios organismos y pasa siempre por el *time lock*.
- Pausar queda en manos de un guardián con efecto inmediato, pero sin capacidad de actualizar ni de reanudar por sí solo.
- Todo cambio deja rastro *on-chain*, de modo que la evolución de la lógica es tan auditable como los datos.

Cada contrato debe documentar qué es actualizable, quién tiene cada rol y qué plazos aplican. Un contrato actualizable sin esas reglas explícitas ofrece menos garantías que una base de datos centralizada, porque aparenta una inmutabilidad que no tiene.

### Disponibilidad del consenso

QBFT sigue funcionando mientras no fallen más de f validadores de un total de n = 3f + 1. Con 4 validadores se tolera la caída de uno; si caen dos, la red deja de producir bloques. No se pierden datos, pero no se pueden registrar nuevas transacciones hasta que se recupere el quórum.

En consecuencia, el número de validadores y su reparto entre organismos es una decisión de diseño, no un detalle de despliegue. Que un organismo detenga su nodo validador afecta a todos, y el alta o baja de validadores se decide por votación entre los existentes, otra vez en el plano de la gobernanza. La [documentación de QBFT en Besu](https://besu.hyperledger.org/private-networks/how-to/configure/consensus/qbft) detalla estos parámetros.

### Pruebas y entornos

Probar sobre una DLT exige más capas que en un desarrollo tradicional:

- Pruebas unitarias de los *smart contracts* con *frameworks* como Hardhat o Foundry.
- Una red QBFT local con varios nodos Besu en contenedores, para reproducir caídas de validadores, latencias y particiones de red.
- Un entorno de preproducción compartido que replique también la gobernanza: el mismo proceso de despliegue de contratos y de actualización de versión del cliente que se seguirá en producción.

Las actualizaciones de Besu deben coordinarse entre todos los organismos, porque nodos con reglas de validación distintas pueden bifurcar la red. Ensayarlas en preproducción forma parte del ciclo de CI/CD tanto como las pruebas del código.

## Resumen

En definitiva, una DLT no debe presentarse en la Administración como una mera pieza tecnológica que el departamento de sistemas instala y pone a disposición del resto. Esa visión resulta reduccionista. Una DLT es, ante todo, una infraestructura compartida entre organizaciones autónomas. Cada participante opera su nodo, forma parte activa de la red, consume recursos y aporta capacidad de validación. El sistema evoluciona mediante acuerdos de gobernanza, requiere estándares semánticos comunes y puede precisar esquemas de ponderación interna para coordinar el uso de los recursos.

La tecnología del *ledger* es la capa técnica; la dificultad real reside en la gobernanza: lograr que múltiples organizaciones independientes adopten reglas comunes, mantengan sus nodos, coordinen la evolución del software y asuman la responsabilidad compartida de la red. Ese reto organizativo es, al mismo tiempo, la razón de ser de la tecnología DLT: permitir la construcción de una infraestructura pública común sin obligar a los participantes a someterse a un dominio técnico centralizado.

---
