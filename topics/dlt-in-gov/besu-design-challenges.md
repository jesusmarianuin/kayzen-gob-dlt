# Retos de diseño con Besu

Las bases de datos relacionales acumulan décadas de madurez en archivado y retención, escalado, indexación y lenguajes de consulta como SQL. Una DLT renuncia a parte de esas capacidades a cambio de un estado compartido que cualquier participante puede verificar por sí mismo. Esa renuncia debe asumirse en la fase de diseño, no descubrirse en producción.

Estos son los retos que con más frecuencia condicionan una red de la Administración basada en Hyperledger Besu. La inmutabilidad y evolución de los *smart contracts* se trata aparte, en [inmutabilidad y evolución de los smart contracts](smart-contract-upgradeability.md).

## Crecimiento del *ledger* y del estado

Un nodo guarda dos cosas distintas, y las dos ocupan cada vez más espacio. Para verlo, sirve de ejemplo un registro de títulos universitarios sobre DLT:

- El historial es la lista de todo lo que ha pasado: cada título emitido, cada corrección y cada revocación, desde el primer día. Nunca se borra nada, así que solo puede crecer. Y crece incluso sin actividad, porque QBFT genera un bloque nuevo cada pocos segundos aunque nadie haya registrado nada.
- El estado es la foto del momento actual: qué títulos son válidos hoy. Es lo que el nodo consulta para validar cada operación nueva. Si esa foto se hace demasiado grande, el nodo se vuelve lento. A ese problema se le llama *[state bloat](https://superex.medium.com/superex-educational-series-understanding-state-size-and-state-bloat-f331bcaeb62b)*.

Besu ofrece [distintos formatos de almacenamiento](https://besu.hyperledger.org/public-networks/concepts/data-storage-formats): Bonsai conserva solo el estado reciente y ocupa mucho menos disco, mientras que Forest permite conservar los estados históricos. La elección no es solo técnica. Si la red debe responder a una auditoría sobre el estado en una fecha pasada, al menos algunos participantes tendrán que operar nodos de archivo y asumir su coste de almacenamiento. El dimensionamiento debe partir del volumen de transacciones previsto, del periodo de bloque y de la política de retención que exija la normativa de archivo.

## Indexación y consulta

Las estructuras internas del *ledger* (árboles Merkle Patricia) están optimizadas para generar pruebas de integridad y alcanzar consenso, no para consultas analíticas. La API JSON-RPC del nodo sirve para lecturas puntuales, pero no para búsquedas complejas ni informes.

El patrón habitual es que los *smart contracts* emitan eventos y que un *indexer* los lea y los cargue en una base de datos relacional o en un motor de búsqueda. Este patrón tiene tres consecuencias de diseño:

- Lo que un contrato no emite como evento es muy costoso de reconstruir después, así que los eventos se diseñan junto con el contrato, no al final.
- El *indexer* es una vista derivada, no la fuente de verdad. Las decisiones con efectos jurídicos deben poder verificarse contra el nodo.
- La finalidad inmediata de QBFT (un bloque confirmado no se revierte) simplifica el *indexer*, porque no tiene que gestionar reorganizaciones de la cadena como ocurre en redes públicas.

## Determinismo de la lógica *on-chain*

Cada nodo vuelve a ejecutar todas las transacciones, y todos deben llegar exactamente al mismo estado. Por eso un *smart contract* no puede llamar a APIs externas, leer el reloj del sistema ni generar números aleatorios. La única referencia temporal es la marca de tiempo del bloque, que fija el validador que lo propone y que solo es fiable dentro del margen que admite el consenso.

Esta restricción confirma que la capa *on-chain* es una capa aislada, no solo conceptualmente. El contrato no sale a buscar nada fuera: valida, ancla y consolida lo que le llega en cada transacción. Toda la lógica que depende del exterior se queda *off-chain*.

La respuesta habitual en las redes públicas para introducir datos externos son los oráculos (*oracles*): un intermediario consulta una fuente y escribe el dato en la cadena. En la Administración suele ser mejor evitarlos, porque existe una alternativa más directa: las atestaciones. El organismo competente, que es la fuente auténtica del dato, emite una declaración firmada (por ejemplo, una credencial verificable que acredita que una persona tiene un título). Esa atestación viaja dentro de la transacción, y el contrato solo comprueba la firma y que el emisor figura en un registro de emisores de confianza, como el que mantiene EBSI.

La diferencia es de confianza. Con un oráculo hay que fiarse del intermediario que transporta el dato; con una atestación se confía directamente en quien tiene la competencia legal para afirmarlo, y el contrato no necesita conocer ninguna fuente externa. Los oráculos solo compensan cuando el dato cambia de forma continua y nadie lo firma como hecho jurídico, como un índice de precios, y ese caso es poco frecuente en la Administración.

## Disponibilidad del consenso

QBFT sigue funcionando mientras no fallen más de f validadores de un total de n = 3f + 1. Con 4 validadores se tolera la caída de uno; si caen dos, la red deja de producir bloques. No se pierden datos, pero no se pueden registrar nuevas transacciones hasta que se recupere el quórum.

En consecuencia, el número de validadores y su reparto entre organismos es una decisión de diseño, no un detalle de despliegue. Que un organismo detenga su nodo validador afecta a todos, y el alta o baja de validadores se decide por votación entre los existentes, otra vez en el plano de la [gobernanza](network-governance.md). La [documentación de QBFT en Besu](https://besu.hyperledger.org/private-networks/how-to/configure/consensus/qbft) detalla estos parámetros.

## Pruebas y entornos

Probar sobre una DLT exige más capas que en un desarrollo tradicional:

- Pruebas unitarias de los *smart contracts* con *frameworks* como Hardhat o Foundry.
- Una red QBFT local con varios nodos Besu en contenedores, para reproducir caídas de validadores, latencias y particiones de red.
- Un entorno de preproducción compartido que replique también la gobernanza: el mismo proceso de despliegue de contratos y de actualización de versión del cliente que se seguirá en producción.

Las actualizaciones de Besu deben coordinarse entre todos los organismos, porque nodos con reglas de validación distintas pueden bifurcar la red (véase [gobernanza de la red](network-governance.md)). Ensayarlas en preproducción forma parte del ciclo de CI/CD tanto como las pruebas del código.
