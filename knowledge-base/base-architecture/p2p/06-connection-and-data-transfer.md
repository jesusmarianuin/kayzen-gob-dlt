# Mecanismos de las redes p2p: conectividad y transferencia de datos

## Comprobación de conectividad

La comprobación de conectividad en redes P2P es fundamental no solo para asegurar que los nodos están activos y disponibles, sino también por motivos de seguridad y resiliencia: evita ataques de enrutamiento, reduce la propagación hacia nodos muertos y permite una respuesta efectiva ante cambios dinámicos en la red (churn).

Este proceso varía según el tipo de red:

- En redes estructuradas (como DHTs), los nodos realizan comprobaciones periódicas (PING/PONG o heartbeats) a los pares en sus tablas de enrutamiento para detectar inactividad y mantener la tabla actualizada. Además, los datos almacenados en la DHT suelen tener un tiempo de vida limitado (TTL); si el nodo propietario del dato —es decir, el que lo publicó inicialmente— no lo vuelve a anunciar (por ejemplo, mediante operaciones STORE), el dato puede desaparecer. Por ello, es común que este nodo lo anuncie periódicamente.
- En redes no estructuradas, la comprobación de conectividad suele integrarse en los propios mecanismos de propagación, es decir, cuando una operación es solicitada, ya que como vimos, realizar una consulta también supone obtener información de nodos, aunque también hay comprobaciones periódicos que ayudan (por ejemplo, mediante mensajes PING/PONG o heartbeats) a identificar nodos activos y a eliminar de la lista de vecinos aquellos que no responden.

En ambos modelos, la comprobación de conectividad es clave para preservar la salud de la red, gestionar la rotación constante de nodos inactivos (churn) y garantizar la resiliencia y disponibilidad de la red.

## Establecimiento de la conexión

Es el proceso mediante el cual un nodo inicia comunicación y abre un canal de comunicación (por ejemplo, vía TCP o UDP o QUIC) con otro nodo previamente descubierto o conocido para cualquiera de las operaciones necesarias posteriores, como realizar una consulta o propagar información.

Es importante distinguir entre el establecimiento de la comunicación y la transferencia de información: establecer comunicación entre nodos de red significa que ambos pueden reconocerse y abrir un canal de conexión, pero esto no implica que se estén transmitiendo datos útiles (payload). La transferencia de información ocurre después, cuando los nodos ya conectados intercambian mensajes o datos concretos a través del canal previamente establecido. Así, el establecimiento de la conexión es el paso previo y necesario para que la transferencia de información pueda producirse, pero ambos procesos son independientes y pueden ocurrir en momentos distintos.

La comunicación entre dos nodos puede ser activa, o mantenerse con una actividad mínima mediante mecanismos como [keep-alive](https://en.wikipedia.org/wiki/Keepalive), que permiten conservar la conexión abierta enviando mensajes periódicos para evitar su cierre por inactividad.

Este proceso puede incluir el uso de comunicación cifrada ([TLS](https://es.wikipedia.org/wiki/Seguridad_de_la_capa_de_transporte), [Noise](https://en.wikipedia.org/wiki/Noise_Protocol_Framework), etc.).

Igualmente, cuando la comunicación directa entre nodos no es posible debido a que alguno de ellos está detrás de un NAT o firewall, se emplean técnicas de [NAT traversal](https://es.wikipedia.org/wiki/NAT_traversal), como el [UDP hole punching](https://en.wikipedia.org/wiki/UDP_hole_punching). Estas técnicas permiten que los nodos establezcan conexiones entrantes a pesar de las restricciones impuestas por el NAT, facilitando la entrada y participación en la red incluso cuando otros nodos no pueden acceder directamente a ellos. Si estas técnicas no resultan efectivas, se recurre al uso de nodos relay como intermediarios para asegurar la conectividad.

### NAT Traversal y el problema de CGNAT

El **NAT (Network Address Translation)** es una técnica que permite a múltiples dispositivos en una red privada compartir una única dirección IP pública. Esto crea un problema para las redes P2P: los nodos detrás de NAT no son directamente accesibles desde Internet.

**CGNAT (Carrier-Grade NAT)** agrava este problema:

- **Definición**: Es un NAT implementado a nivel de proveedor de internet (ISP), donde múltiples usuarios (incluso hogares enteros) comparten la misma IP pública.
- **Problema para P2P**: 
  - Los nodos detrás de CGNAT no tienen control sobre el NAT (a diferencia del NAT doméstico donde puedes abrir puertos).
  - Dificulta extremadamente las conexiones entrantes directas.
  - Dos nodos ambos detrás de CGNAT no pueden conectarse directamente entre sí sin ayuda externa.

**Técnicas de NAT Traversal:**

- **STUN (Session Traversal Utilities for NAT)**: Servidor que ayuda a un nodo a descubrir su IP pública y el tipo de NAT que tiene.
- **TURN (Traversal Using Relays around NAT)**: Servidor relay que retransmite tráfico cuando la conexión directa es imposible.
- **UDP Hole Punching**: Técnica donde ambos nodos intentan conectarse simultáneamente, "abriendo agujeros" en sus respectivos NATs:
  1. Nodo A y B contactan a un servidor de rendez-vous (coordinador).
  2. El servidor les informa de la IP:puerto público del otro.
  3. Ambos envían paquetes UDP simultáneamente al otro.
  4. Si el timing es correcto, los NATs permiten el paso al creer que la conexión fue iniciada desde dentro.

**Soluciones en redes P2P modernas:**

- **Libp2p Circuit Relay**: Protocolo donde un nodo accesible actúa de intermediario.
- **AutoNAT**: Detección automática de accesibilidad del nodo.
- **Hole Punching directo**: Implementado en libp2p, BitTorrent, etc.
- **Servidores bootstrap con IPs públicas**: Actúan como puntos de encuentro iniciales.

**Impacto en descentralización:**

CGNAT fuerza a muchos nodos a depender de relays o nodos con IPs públicas, introduciendo cierto grado de centralización parcial. Por ello, mantener nodos con IPs públicas (servidores, VPS) es crucial para la salud de redes P2P descentralizadas.

Un [Relay](https://en.wikipedia.org/wiki/Traversal_Using_Relays_around_NAT) se utiliza cuando las técnicas como hole punching no son efectivas.

https://github.com/user-attachments/assets/1e094644-53d9-45d8-b557-54ef89da4327

- Cuando otros nodos no pueden acceder al nodo 1 porque está detrás de NATs o firewalls.

https://github.com/user-attachments/assets/3fc2eeb1-e80f-4f76-87cd-ff0d0bc65344

- El nodo que no puede atender peticiones, sí puede conectarse a otro nodo relay.

  > En telecomunicaciones, cuando un nodo establece una conexión de salida hacia otro, ambos pueden enviar y recibir información, logrando comunicación duplex (half o full-duplex). Esto es posible porque la conexión abre canales bidireccionales (como sockets TCP), permitiendo el intercambio continuo de datos en ambos sentidos.

  > El uso de nodos relay puede impactar el rendimiento debido a la latencia adicional en la comunicación y plantea consideraciones de seguridad, como la confianza en el nodo relay para manejar los datos de forma adecuada.

- El nodo 1 cuando anuncie su dirección, usará la del nodo relay, de esta forma, el resto de nodos cuando quieran hacer una comunicación al nodo 1, en realidad se conectaran al nodo relay.
- El nodo relay solo actúa de intermediario de comunicaciones, cualquier otra actividad de la red se la pasará al nodo 1.

## Transferencia de datos (Data Transfer)

La transferencia de datos en redes P2P consiste en el intercambio directo de información entre nodos que ya se han descubierto, conocen sus direcciones y han establecido una conexión.
Una vez establecida la conexión, existen principalmente dos enfoques de transmisión:

- Pull: un nodo solicita activamente la información a otro.
- Push: un nodo envía activamente información a otro sin que este la haya solicitado.

Estos enfoques suelen asociarse a:

- Redes estructuradas, donde predomina el modelo pull mediante mecanismos de enrutamiento.
- Redes no estructuradas, donde es común el modelo push mediante difusión o propagación.

La información se transfiere generalmente en fragmentos, utilizando mecanismos como hashes o checksums para garantizar la integridad de los datos.

Este proceso es independiente del establecimiento de la conexión y se enfoca exclusivamente en la transmisión de la carga útil entre los pares.
