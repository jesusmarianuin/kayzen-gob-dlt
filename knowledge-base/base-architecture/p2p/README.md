# Introducción a redes peer to peer (p2p)

## TL;DR

Las redes peer-to-peer (P2P) permiten que los nodos se comuniquen y colaboren directamente, sin depender de servidores centrales, lo que mejora la resiliencia y la resistencia a la censura. Existen diferentes modelos de gobernanza, descentralización, confianza y autorización, que determinan cómo se organizan y operan estas redes. Las P2P pueden ser estructuradas (con topologías e índices definidos, como DHT/Kademlia) o no estructuradas (con conexiones aleatorias y propagación de consultas, como Gossip).

Los nodos pueden asumir distintos roles (semilla, completo, ligero, coordinador, relay, etc.) y especializarse en funciones como almacenamiento, validación o auditoría. Para escalar, se usan técnicas como sharding (fragmentación en subredes coordinadas). Los principales retos de las redes P2P son la seguridad, la disponibilidad (churn), el rendimiento y la consistencia de los datos. Ejemplos conocidos incluyen BitTorrent, Bitcoin, Ethereum, IPFS y Filecoin.

## Fundamentos de redes de computadoras

> Puedes ir a revisar para tener algo de contexto los [fundamentos de redes de computadoras y comunicación entre nodos](../computer-networks-and-node-communication.md)

## Redes entre pares - peer-to-peer o p2p

En las redes entre pares, [peer-to-peer o p2p](https://academy.bit2me.com/que-es-una-red-p2p/), todos los nodos funcionan como iguales para el mismo propósito de la red.

> 💡 No debe confundirse una red P2P con una red distribuida. Como su nombre indica, una red P2P implica comunicación entre pares: si un nodo no puede conectarse en igualdad de condiciones con otro, no es una red P2P. Tampoco debe confundirse que una red P2P sea inherentemente descentralizada; una red entre pares puede tener un nodo coordinador central, y en ese caso no lo sería del todo.

Una red P2P elimina el punto único de fallo (SPOF), aumentando la resiliencia y dificultando la censura, ya que no depende de un único nodo o servidor central para funcionar.

Suelen funcionar mediante un protocolo o varios subprotocolos, implementado en un programa que se ejecuta como servicio en cada nodo, permitiendo la interacción entre nodos según las reglas definidas.

No tenemos que confundir redes p2p con blockchain, ya que no es lo mismo y spoiler, blockchain es una estructura de datos diseñada para operar como libro contable distribuido (ledger) en redes P2P, donde existe un consenso, es decir, que opere en una red p2p, no implica que sean lo mismo, simplemente blockchain opera sobre una red p2p y suele confundirse.

Si lo vemos de forma menos abstracta, podemos ver el ejemplo de [BitTorrent](https://es.wikipedia.org/wiki/BitTorrent), donde cada persona instala un programa en su PC, que sería un nodo. Cuando quieres un archivo, tu programa busca otros usuarios (otros nodos) que ya tienen partes de ese archivo para descargar varias partes a la vez, que ese sería el propósito de la red.
Al mismo tiempo, tú también compartes las partes que ya tienes con otros, sin depender de un servidor central.

## Índice

El contenido se reparte en estos documentos, pensados para leerse en orden:

- [Características de una red p2p](01-characteristics.md)
- [Desafíos y Vulnerabilidades en Redes P2P](02-challenges-and-vulnerabilities.md)
- [Clasificación principal de redes p2p](03-topologies.md)
- [Mecanismos de las redes p2p: conexión inicial, descubrimiento y selección de peers](04-bootstrap-and-node-discovery.md)
- [Mecanismos de las redes p2p: enrutamiento, difusión y propagación](05-routing-and-diffusion.md)
- [Mecanismos de las redes p2p: conectividad y transferencia de datos](06-connection-and-data-transfer.md)
- [Mecanismos de las redes p2p: replicación y consistencia](07-replication-and-consistency.md)
- [Clasificación y roles de los nodos](08-node-roles.md)
- [Dominios funcionales y subredes lógicas](09-functional-domains-and-subnets.md)
- [Algunos ejemplos de redes p2p](10-network-examples.md)
- [Libp2p: Framework modular para redes P2P](11-libp2p.md)
- [Sincronización de nodos](12-node-synchronization.md)

## Referencias

- Las referencias sobre todo son semanas de consultas a chatgpt y deepseek.
- [geeksforgeeks.com](https://www.geeksforgeeks.org/structured-and-unstructured-peer-to-peer-systems/)
- Varios autores de Wikipedia...
- [bit2me academy](https://academy.bit2me.com/).

## Aclaración y agradecimiento

La tecnología de las redes P2P realmente es muy compleja, y complicado de digerir, pero es la base de la descentralización, por lo tanto, aunque no seamos expertos, considero importare esta introducción técnica para tener una base, que puede ayudar cuando tengas que abordar un documento técnico complicado de una red P2P.

Agradecimiento a quien encuentre fallos y proponga mejoras.

Este documento tiene cierto enfoque heurístico, ha sido complicado encontrar y digerir la información, por lo tanto, disculpas por adelantado si encuentras un error, e igualmente gracias por adelantado si luego propones mejoras.

Hay partes que quizás le falta alguna explicación, pero es porque es un resumen introductorio y en algún momento tengo que parar.

Gracias ;).
