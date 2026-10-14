# Libp2p: Framework modular para redes P2P

[Libp2p](https://libp2p.io/) es un framework de red modular que proporciona los componentes fundamentales para construir aplicaciones P2P. Desarrollado originalmente para IPFS, se ha convertido en el estándar de facto para implementar redes P2P en Web3.

**Arquitectura modular de libp2p:**

- Transport: Abstracción sobre protocolos de transporte (TCP, UDP, WebSockets, QUIC). Permite que una aplicación funcione sobre múltiples transportes simultáneamente.
- Security: Capa de cifrado y autenticación (TLS, Noise Protocol). Garantiza comunicación segura entre peers.
- Stream Multiplexing: Permite múltiples streams lógicos sobre una única conexión física (yamux, mplex).
- Peer Discovery: Mecanismos para encontrar otros nodos (mDNS, DHT, Rendezvous).
- Peer Routing: DHT (Kademlia) para localizar peers y contenido distribuido.
- NAT Traversal: Circuit Relay y hole punching para conectividad detrás de NAT.
- Pub/Sub: Protocolo Gossipsub para mensajería distribuida.
- Content Routing: Localización de contenido usando DHT o delegates.

**Ventajas de libp2p:**

- Portabilidad: Funciona en navegadores, servidores, móviles y dispositivos IoT.
- Interoperabilidad: Implementaciones en múltiples lenguajes (Go, Rust, JavaScript, etc.).
- Flexibilidad: Componentes intercambiables según necesidades.
- Usado por: IPFS, Filecoin, Ethereum 2.0, Polkadot, Substrate.

Libp2p abstrae la complejidad de la red P2P, permitiendo a los desarrolladores enfocarse en la lógica de aplicación en lugar de problemas de conectividad y descubrimiento.

Que una red P2P sea entre iguales facilita un diseño descentralizado, lo que la hace muy relevante en la Web3. Sin embargo, en la práctica, Web3 adopta lo que sea necesario para ofrecer la funcionalidad requerida, incluso soluciones centralizadas, ya que debe mantenerse un equilibrio entre descentralización, seguridad y escalabilidad.
