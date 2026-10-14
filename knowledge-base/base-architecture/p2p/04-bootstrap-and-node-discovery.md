# Mecanismos de las redes p2p: conexión inicial, descubrimiento y selección de peers

En una red peer-to-peer (P2P), los nodos se comunican mediante el intercambio de mensajes, que pueden ser peticiones de información (lecturas, R) o entregas (escrituras, W). Un nodo puede iniciar la transacción o actuar como intermediario replicando peticiones hacia otros nodos.

Estas operaciones están reguladas por una serie de mecanismos compuestos por procesos o técnicas o estrategias o modelos, establecidos en el protocolo de la red.

> Este apartado intenta explicar las diferentes soluciones técnicas que podemos encontrarnos.

Se debe considerar que estos mecanismos no están exentos de excepcione según el [grado de descentralización](01-characteristics.md#grado-de-descentralización) o su [estrategia de almacenamiento](01-characteristics.md#estrategias-de-almacenamiento-en-redes-p2p).

Se describen los mecanismos más relevantes, considerando que algunos se aplican específicamente a redes estructuradas y otros a no estructuradas.

## Conexión inicial de nodos (Bootstrapp)

Cuando un nodo se inicia por primera vez, durante el arranque (conocido como bootstrap), se conecta a otros nodos denominados nodos semilla o [nodos bootstrap](https://en.wikipedia.org/wiki/Bootstrapping_node), normalmente preconfigurados en el propio software del nodo. Estos nodos suelen ser confiables y frecuentemente pertenecen a los fundadores o mantenedores del protocolo.

Esta conexión inicial continua con el descubrimiento de nodos que veremos a continuación, pero como simplificación, se puede ver en el siguiente ejemplo:

https://github.com/user-attachments/assets/15d1f200-a030-4278-a5b2-bf88b2e537e2

Inicialmente, el nodo parte de una lista de nodos conocidos, por ejemplo los nodos identificados como 1, 2, 3 y 4 que son nodos semilla, y el proceso consiste en consultar a esos nodos para descubrir otros nuevos, como serían el 10, 14, 25 y 30; así sucesivamente con los nuevos nodos para ampliar y actualizar su red de relaciones.

Además de los nodos semilla, existen diversos mecanismos para el descubrimiento inicial de nodos. Entre ellos se encuentran el uso de [Rendezvous](https://docs.libp2p.io/concepts/discovery-routing/rendezvous/), el DNS seed (que resuelve dominios a direcciones IP de nodos activos), y los servidores de directorio (también llamados *bootstrap servers* o *trackers*), que ofrecen listas centralizadas de nodos disponibles. En redes locales, también se emplea difusión mediante *broadcast* o *multicast*, como [mDNS](https://docs.libp2p.io/concepts/discovery-routing/mdns/), para descubrir nodos cercanos. No obstante, en modelos descentralizados como Web3, predominan los **nodos semilla** para iniciar la conexión a la red.

## Descubrimiento de nodos (Node Discovery)

El descubrimiento de nodos es el mecanismo que permite al nodo encontrar nuevos pares para incluirlos en su lista de confianza.

Ocurre tras el arranque inicial (bootstrap), pero también periódicamente para mantener la red actualizada y de manera reactiva, por ejemplo, cuando se detecta la caída de nodos durante la [comprobación de conectividad](06-connection-and-data-transfer.md#comprobación-de-conectividad).

En redes estructuradas (por ejemplo, DHTs), este proceso sigue protocolos deterministas, mientras que en redes no estructuradas se basa en la propagación de consulta —que es una [técnica de difusión](05-routing-and-diffusion.md#técnicas-de-difusión-en-redes-no-estructurabas)—.

**Redes estructuradas**.

En redes estructuradas, es un mecanismo determinista que establezca con qué nodos debe relacionarse un nodo dado, asegurando que siempre se obtengan resultados consistentes y repetibles.

Tomando como ejemplo la DHT [Kademlia](https://en.wikipedia.org/wiki/Kademlia), en primer lugar, a cada nodo se le asigna un identificador único (ID), y el proceso consiste en la consulta a otros nodos sobre los nodos "más cercanos" que conozcan respecto a su propio ID para guardar esa información en una [tabla de enrutamiento](https://en.wikipedia.org/wiki/Kademlia#Fixed-size_routing_tables).

> Tabla que se usará posteriormente en el proceso [routing](05-routing-and-diffusion.md#enrutamiento-routing-en-redes-estructuradas) que veremos más adelante.

La "cercanía entre nodos" permite que las consultas sean deterministas, es decir, que siempre produzcan el mismo resultado. Esta cercanía se calcula utilizando la [operación binaria XOR](https://es.wikipedia.org/wiki/Puerta_XOR).

En Kademlia, la tabla de enrutamiento almacena contactos de otros nodos organizados según su distancia XOR respecto al nodo local. Estos contactos se agrupan en estructuras llamadas k-buckets (del inglés bucket, que en este contexto equivale a 'cubeta'), donde cada bucket contiene hasta k nodos a una determinada distancia. Por convención, k suele ser 20.

> Los buckets empiezan desde 0, es decir, podemos tener desde Bucket 0 a Bucket 1, 2, 3, etc.

Si quieres entrar en detalle, lo vemos en un ejemplo:

*Ejemplo en primera ronda:*

https://github.com/user-attachments/assets/233bbec8-5ef3-4f68-a160-0fb1db433dfd

- Inicialmente, un nodo local con id 0b0001 (1) conoce al nodo semilla con ID 0b1000 (8) y lo incluye en el Bucket 3 como el único nodo que conoce.

  Si calculamos `0b0001 XOR 0b1000` es `0b1001` (9), siendo posición del bucket 3:

  | 3 ◄ | 2 | 1 | 0 |
  | - | - | - | - |
  | 1 | 0 | 0 | 1 |

  > Si la posición empieza desde 0 y buscamos de izquierda a derecha, 3 es la posición del último bit 1.

- El nodo realiza una consulta a ese nodo semilla mediante el método FIND_NODE, donde indica como ID objetivo el 0b0001 (1), siendo su propio ID de nodo, y además, se especifica k = 3 (a modo de ejemplo, lo normal seria 20) para que el nodo consultado devuelve hasta 3 nodos que conoce y que están más cercanos a 1 (0b0001) según la distancia XOR. El nodo realizará el calculo los nodos que conoce:

  ```text
  0b0001 (1) XOR 0b0011 (3) = 0b0010 (2)
  0b0001 (1) XOR 0b0010 (2) = 0b0011 (3)
  0b0001 (1) XOR 0b0110 (6) = 0b0111 (7)
  0b0001 (1) XOR 0b0111 (7) = 0b0110 (6)
  ```

  Teniendo como resultado, la siguiente lista de 3 nodos ordenados, descartando el más lejano:

  - `0b0011` (ID 3) con resultado XOR `0b0010` (2) en posición del bucket 1.
  - `0b0010` (ID 2) con resultado XOR `0b0011` (3) en posición del bucket 1.
  - `0b0111` (ID 7) con resultado XOR `0b0110` (6) en posición del bucket 2.

  > Por cierto, en el bucket 0 no hay ningún nodo en este ejemplo, pero podría ser, porque recordar que empiezan los buckets desde 0.

  > Aparte de la posición del bucket, como vemos en el ejemplo, en el bucket 1 hay dos nodos y en ese caso el 0b0010 con valor decimal 2 es más cercano que el 0b0011 con valor decimal 3.

- Se debe aclarar que, en esta petición del nodo 1, también el nodo 8 conocen al nodo 1 y lo añaden en su lista de nodos, y esto porque el descubrimiento es reciproco (reciprocal peer discovery).

*Ejemplo en segunda ronda:*

https://github.com/user-attachments/assets/04acbc7a-144a-4528-baea-a587464622d0


- En la segunda ronda, con los nuevos nodos descubiertos, se realiza α (alfa) consultas paralelas para buscar más nodos con FIND_NODE, siendo las consultas a los nodos 0b0011 (3) y 0b0010 (2).

  > El valor de α (alfa) indica el número máximo de consultas concurrentes por ronda, por ejemplo α = 2, con 2 consultas concurrentes. Por defecto en Kademlia α suele ser entre 2 y 3.

- Los nodos consultados responden con los nuevos nodos 0b0100 (4) y 0b0101 (5) y se calcula su posición de Bucket en la Routing table, siendo ambos en el Bucket 2.
- Y se repite otra ronda con el nodo con ID 7...

Esto aunque es una generalización, nos da una idea de lo que se busca, que es:

- Tener un mecanismo para que un nodo se relacione con un conjunto de nodos concretos y se basa en "la cercanía", que no deja de ser una operación simple para tener un mismo criterio y poder descartar finalmente a los nodos más lejanos.
  > En Kademlia, la cantidad total de nodos posibles con los que puede relacionarse un nodo dado, está determinada por el tamaño del identificador: con n bits, hay hasta 2ⁿ nodos posibles. Por ejemplo, con identificadores de 4 bits, los nodos van del 0 al 15, permitiendo disponer en la routing table hasta 16 nodos distintos en la red.
- Agrupar los nodos en buckets facilita y agiliza la búsqueda de nodos cercanos durante el proceso de [enrutamiento](05-routing-and-diffusion.md#enrutamiento-routing-en-redes-estructuradas), como se explicará más adelante.

**Redes no estructuradas**.

En redes no estructuradas, el descubrimiento de nodos se basa en la propagación, no es determinista como en las redes estructuradas, e implica una búsqueda probabilística.

El descubrimiento de nodos es una actividad que ocurre como parte de las [técnicas de difusión](05-routing-and-diffusion.md#técnicas-de-difusión-en-redes-no-estructurabas), como *Gossip* o *Flooding*, aunque inicialmente descubrir nodos no era el objetivo de dichas técnicas. Además, existen otros mecanismos que una red puede emplear, como [Peer Exchange (PEX)](https://en.wikipedia.org/wiki/Peer_exchange), implementado en BitTorrent, entre otros.

Es importante aclarar que, en redes no estructuradas, el descubrimiento de nuevos nodos ocurre principalmente durante la propagación de consultas. Como se verá en [técnicas de difusión](05-routing-and-diffusion.md#técnicas-de-difusión-en-redes-no-estructurabas), cada vez que se realiza una operación de consulta (R), el nodo consultado puede aprovechar para devolver referencias a otros nodos al solicitante. Sin embargo, también este descubrimiento ocurre al arranque inicial (bootstrap) del nodo o periódicamente como se menciono.

A continuación, veremos un ejemplo tomando como referencia Gossip para explicarlo, pero entendiendo que existen muchas particularidades y esto es una generalización:

*Ejemplo en primera ronda:*

https://github.com/user-attachments/assets/384545fe-5b7f-4097-9c9f-be6032c57748


- Inicialmente un nodo consulta a un nodo semilla para conocer otros nodos, y este le responde con los nodos que conoce, por ejemplo, los 6, 2, 3 y 7. Estas consultas pueden ser en paralelo a varios nodos según el fan-out (abanico), que puede se entre 3 y 5, es decir, entre 3 y 5 consultas paralelas.

*Ejemplo en segunda ronda:*

https://github.com/user-attachments/assets/69b61fe2-8088-487d-8047-31e4363c80ac

- El nodo continua consultando a los nodos 6, 2, 3 y 7, y suponiendo que el fan-out es 2, consultaría en una ronda a los nodos 2 y 3, para conocer los nuevos nodos 4 y 5.
- En esta petición, el nodo 1 también es descubierto por los nodos 2 y 3, quienes lo agregan a su lista de nodos conocidos gracias al descubrimiento recíproco (reciprocal peer discovery).
  > Nota: En la representación anterior, cuando el nodo 1 consulta al 8, igualmente existe un descubrimiento reciproco, se ha omitido para simplificar.
- En redes no estructuradas como Gossip, este proceso de descubrimiento reciproco es continuo y se denomina diseminación push-based: por ejemplo, el nodo 2 puede enviar comunicaciones push al nodo 1 cada vez que detecta nuevos nodos, manteniendo así actualizada la topología de la red de forma proactiva.

*Ejemplo intercambio de vecinos:*

https://github.com/user-attachments/assets/1da041c8-944d-415b-b8d1-e21abe163f8b


- Como el nodo 2 ya conoce al nodo 1 gracias al descubrimiento recíproco (siendo el intercambio de vecinos), cuando detecta nuevos nodos o cambios en la topología de la red, puede notificar proactivamente al nodo 1 mediante una comunicación push. Es decir, no espera a que el nodo 1 realice una consulta, sino que le envía la información tan pronto como la tiene disponible, como en este ejemplo, donde comunica la existencia de los nodos 9 y 10.

## Selección de peers

El descubrimiento da al nodo una lista de pares posibles, normalmente mucho mayor de la que puede mantener. La selección de peers decide con cuáles conecta y cuáles conserva, y es una de las principales defensas frente a los ataques [Eclipse y Sybil](02-challenges-and-vulnerabilities.md#ataques-a-la-seguridad): si un atacante consigue que todas las conexiones de un nodo sean suyas, controla lo que ese nodo ve de la red.

### Conexiones salientes y entrantes

- Salientes (outbound): las inicia el propio nodo, eligiendo a quién conecta. Son las más seguras, porque el atacante no decide el destino.
- Entrantes (inbound): las inician otros nodos. Aportan capacidad a la red, pero el nodo no controla quién se conecta, así que un atacante puede ocuparlas en masa.

Por eso los clientes limitan el número total de conexiones y reservan una parte para conexiones salientes. Según la [documentación de Bitcoin Core](https://github.com/bitcoin/bitcoin/blob/master/doc/reduce-traffic.md), en sus versiones recientes un nodo admite por defecto hasta 200 conexiones, de las que 11 son salientes: 8 de retransmisión completa, 2 solo de bloques (block-relay-only) y, ocasionalmente, una conexión breve de sondeo (feeler) para comprobar direcciones. En Besu, el límite total se ajusta con `--max-peers`, cuyo valor por defecto es 25, y `--remote-connections-max-percentage` limita qué parte de esas conexiones pueden iniciar otros nodos: por defecto, el 60 % (valores comprobados en el [código de Besu 26.9](../../besu-eth/besu/app/src/main/java/org/hyperledger/besu/cli/options/P2PDiscoveryOptions.java)).

### Criterios de diversidad

Elegir pares al azar entre todas las direcciones conocidas no basta: un atacante con muchas direcciones en el mismo rango de red tendría muchas posibilidades de salir elegido. Para evitarlo:

- Diversidad de red: Bitcoin Core agrupa las direcciones por rango (por ejemplo, /16 en IPv4) y evita tener varias conexiones salientes en el mismo grupo. Opcionalmente puede agruparlas por sistema autónomo (ASMap), que refleja mejor qué operador controla cada rango.
- Conexiones de anclaje (anchors): al apagarse, Bitcoin Core guarda sus conexiones solo de bloques y vuelve a conectar con ellas al arrancar, para que un atacante no pueda aprovechar el reinicio y rodear al nodo.
- Conexiones solo de bloques: no retransmiten transacciones ni direcciones, lo que hace más difícil que un observador descubra la topología de la red a partir del tráfico.

### Rotación y desalojo

Las conexiones no son permanentes. Los nodos sustituyen pares inactivos o lentos y, cuando se alcanza el límite de conexiones entrantes, desalojan (eviction) a alguno para hacer sitio. El desalojo también es un punto de ataque, así que Bitcoin Core protege de él a los pares más valiosos: los de grupos de red distintos, los de menor latencia, los que le han entregado transacciones o bloques recientes y los que llevan más tiempo conectados.

### Puntuación de pares (peer scoring)

Algunos protocolos asignan una puntuación a cada par según su comportamiento y desconectan a los que bajan de un umbral. La [especificación de Gossipsub v1.1](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/gossipsub-v1.1.md) define una puntuación basada, entre otros factores, en si el par entrega mensajes válidos a tiempo, si envía mensajes inválidos y en cuántos pares comparten la misma IP. La usa, por ejemplo, la capa de consenso de Ethereum.

> En libp2p, el identificador de cada par (peer ID) se deriva de su clave pública, lo que impide que un nodo suplante a otro. No protege frente a Sybil: generar claves nuevas no cuesta nada, así que un atacante puede crear tantas identidades como quiera. La defensa frente a Sybil está en los criterios de diversidad y en la puntuación.
