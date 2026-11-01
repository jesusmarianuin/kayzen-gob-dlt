# Blockchain Operational Resilience and Governance (resiliencia operativa y gobernanza de redes blockchain)

Objetivo: Identificar los factores de ingeniería necesarios para que los sistemas complejos —en particular, las redes DLT permisionadas— sean automatizados y redundantes, garantizando su continuidad operativa, resiliencia y capacidad de evolución. Esta es la razón de ser del análisis: reducir la dependencia de intervenciones manuales y evitar puntos únicos de fallo.

## Alcance y principios del análisis

### Scope

- Redes DLT permissioned.
- Operación de nodos y participantes.
- Infraestructura física, virtualizada y contenerizada.
- Sistemas operativos, almacenamiento y comunicaciones.
- Identidad criptográfica, PKI y gestión de claves.
- Ciclo de vida del software y del protocolo.
- Gobernanza técnica y operativa.
- Smart contracts y su ciclo de vida.
- Continuidad del servicio y recuperación ante fallos.
- Automatización y supervisión humana.

### Exclusions

- Mecánica interna del registro distribuido: el análisis no pretende estudiar cómo funciona internamente la tecnología DLT, sino cómo automatizar y dotar de redundancia a los sistemas complejos construidos sobre ella.
- Algoritmos de consenso y replicación: se consideran mecanismos propios del protocolo. El interés está en la ingeniería operativa que permite mantener el sistema disponible y resiliente, independientemente de esos mecanismos.
- Redes permissionless: el ámbito de estudio son las redes permisionadas, donde la participación, la identidad de los nodos y las responsabilidades operativas están sujetas a un modelo de autorización y gobernanza.
- Dependencias operativas de terceros (oráculos, proveedores RPC externos, proveedores externos de identidad y servicios de custodia): quedan fuera porque son una mala decisión de diseño: por seguridad, todo debe vivir en la cadena y de forma determinista, para que la red de nodos pueda validarlo.
- Autoridad operativa delegada en terceros: se excluyen los modelos en los que servicios externos tienen capacidad de decisión o control sobre la operación de la red. La gestión y las decisiones operativas deben permanecer bajo el control de la propia organización o de los mecanismos de gobernanza de la red. Por ejemplo, un servicio externo capaz de autorizar la incorporación de nodos, modificar permisos, aprobar cambios de configuración o decidir quién participa en la red. Al igual que las dependencias anteriores, es una mala decisión de diseño para un registro DLT: ata la red a decisiones centralizadas y crea un punto único de fallo. Una red permisionada asume cierto grado de centralización, pero estos atajos, como los puentes en Web3, conocidos por su inseguridad, deben excluirse desde el diseño inicial.

### Restricciones de arquitectura de la red

- No introducir dependencias externas de confianza como condición para el funcionamiento de la red.
- Considerar las atestaciones como mecanismo de incorporación de evidencias externas.
- Distinguir entre automatización, autonomía operativa y gobernanza.
- Distinguir entre disponibilidad de la red y disponibilidad de los servicios que la consumen.
  - Disponibilidad de la red: los nodos siguen funcionando, comunicándose y procesando transacciones.
  - Disponibilidad de los servicios consumidores: las aplicaciones, API, clientes RPC o servicios que consultan la blockchain y envían transacciones siguen pudiendo acceder a ella.

---

## Factores de estudio

Un factor es un aspecto de la operación de la red que se estudia para decidir si conviene automatizarlo, dotarlo de redundancia o ambas cosas. Los factores se agrupan por área y cada uno se describe en una línea.

### Pertenencia y participación de los nodos

Quién forma parte de la red, con qué rol y bajo qué condiciones.

- Pertenencia a la red: alta, suspensión, expulsión y reincorporación de organizaciones y nodos.
- Condiciones de participación: requisitos que un nodo debe cumplir para participar, como versión, sincronización o disponibilidad.
- Quórum de validadores: número y reparto de validadores que la red necesita para seguir produciendo bloques.

Referencias:

- [Hyperledger Besu — Permissioning](https://besu.hyperledger.org/private-networks/concepts/permissioning)
- [Hyperledger Besu — QBFT](https://besu.hyperledger.org/private-networks/how-to/configure/consensus/qbft)

**Concepto de solución**:

- etc

### Identidad criptográfica: PKI, certificados y claves

Certificados, claves y secretos con los que se identifican y comunican los nodos y participantes.

- Arquitectura de la PKI: jerarquía de autoridades de certificación y relaciones de confianza entre organizaciones.
- Ciclo de vida de los certificados: emisión, renovación, expiración y revocación de los certificados de nodos y participantes.
- Custodia de las claves: quién guarda cada clave, dónde, y cómo se rota o se recupera.
- Módulos criptográficos (HSM): dispositivos donde se guardan las claves y dependencia de ellos.
- Gestión de secretos: contraseñas, tokens y credenciales que no son claves criptográficas.

Referencias:

- [RFC 5280 — Internet X.509 PKI](https://www.rfc-editor.org/rfc/rfc5280)
- [RFC 8555 — ACME](https://www.rfc-editor.org/rfc/rfc8555)
- [NIST SP 800-57 Part 1 Rev. 5 — Key Management](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)

### Ciclo de vida y salud de los nodos

Vida de cada nodo, desde que se aprovisiona hasta que se retira.

- Alta y baja de nodos: aprovisionamiento, sincronización inicial, mantenimiento y retirada.
- Salud del nodo: diferencia entre un proceso que responde y un nodo sincronizado que participa.
- Recuperación del nodo: vuelta a la operación tras una caída, una desincronización o una pérdida de datos.

Referencias:

- [Kubernetes — Probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- [Kubernetes — StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

### Infraestructura y topología

Cómputo, comunicaciones, almacenamiento y reloj sobre los que se ejecutan los nodos.

- Topología de la red: reparto de los nodos entre organizaciones, centros de datos y zonas, y dependencias compartidas.
- Cómputo: servidores, máquinas virtuales y contenedores donde se ejecutan los nodos.
- Comunicaciones: conectividad entre nodos y entre organizaciones.
- Almacenamiento: disco persistente donde cada nodo guarda el registro.
- Sincronización horaria: coincidencia de los relojes entre nodos, de la que dependen certificados y comunicaciones.
- Infraestructura como código: declaración de la infraestructura y la configuración de los nodos en ficheros versionados.

Referencias:

- [Kubernetes — Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
- [OpenGitOps — Principios](https://opengitops.dev/)

### Software y protocolo

Cambios en el software de los nodos y en las reglas del protocolo a lo largo del tiempo.

- Actualización del software: versiones del cliente y del sistema, y cómo se despliegan.
- Cadena de suministro del software: origen e integridad del software desde que se construye hasta que llega al nodo.
- Compatibilidad entre versiones: convivencia de nodos con versiones o clientes distintos.
- Evolución del protocolo: cambios en las reglas de la red, incluidos los hard forks.

Referencias:

- [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/)
- [Ethereum — Actualizaciones de la red](https://ethereum.org/ethereum-forks/)

### Gobernanza y límites de la automatización

Quién decide los cambios en la red y qué papel tienen las personas frente a la automatización.

- Gobernanza de la red: cómo se proponen y aprueban los cambios entre organizaciones.
- Gobernanza de la configuración: quién puede cambiar los parámetros compartidos y los de cada nodo.
- Frontera entre automatización y decisión humana: qué decisiones pueden tomarse sin una persona y cuáles no.
- Operaciones automatizadas: tareas que ya se ejecutan solas y cómo interactúan entre sí.

Referencias:

- [Hyperledger Fabric — Policies](https://hyperledger-fabric.readthedocs.io/en/latest/policies/policies.html)
- [Google SRE — Eliminar el trabajo repetitivo](https://sre.google/sre-book/eliminating-toil/)

### Smart contracts

Lógica compartida desplegada en la red, que no se para ni se corrige como un servicio convencional.

- Ciclo de vida de los contratos: despliegue, versionado, actualización y retirada.
- Gobernanza de los contratos: quién puede cambiar la lógica, los parámetros o los permisos de un contrato.
- Fallos en los contratos: errores de lógica, vulnerabilidades y pérdida del control administrativo.

Referencias:

- [Ethereum — Actualizar smart contracts](https://ethereum.org/developers/docs/smart-contracts/upgrading/)
- [Ethereum — Seguridad de smart contracts](https://ethereum.org/developers/docs/smart-contracts/security/)

### Datos: retención, copias y recuperación

Datos que guarda la red y los nodos, y cómo se conservan.

- Dominios de datos: tipos de datos que maneja la red, compartidos o privados, reconstruibles o no.
- Retención de datos: cuánto histórico y estado se conserva, se poda o se archiva.
- Copias y recuperación: copias de seguridad y restauración de los datos de los nodos.

Referencias:

- [Hyperledger Fabric — Ledger](https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html)
- [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)

### Redundancia y continuidad del servicio

Capacidad de la red y de los servicios que la consumen para seguir funcionando ante fallos.

- Redundancia de nodos: réplicas de validadores y de nodos de acceso.
- Continuidad para las aplicaciones cliente: acceso de las aplicaciones a la red cuando cae el nodo al que se conectan.
- Recuperación ante desastres: vuelta a la operación tras la caída de un centro de datos o una interrupción generalizada.
- Capacidad y rendimiento: recursos, latencia y throughput de la red y de los nodos.

Referencias:

- [Ethereum — Ejecutar un nodo](https://ethereum.org/developers/docs/nodes-and-clients/run-a-node/)
- [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)

### Observabilidad, seguridad e incidentes

Cómo se conoce el estado de la red y cómo se responde a los problemas.

- Observabilidad: métricas, logs y alertas de la red y de los nodos.
- Operaciones de seguridad: privilegios, accesos administrativos y cambios no autorizados.
- Gestión de incidentes: detección, respuesta y análisis de incidentes entre organizaciones.

Referencias:

- [Prometheus — Overview](https://prometheus.io/docs/introduction/overview/)
- [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

### Verificación: pruebas, auditoría y atestaciones

Comprobación de que la red se comporta como se espera, dentro y fuera de ella.

- Pruebas de resiliencia: comportamiento de la red ante fallos provocados.
- Aseguramiento operativo: verificación de que la configuración, las versiones y los permisos son los esperados.
- Atestaciones externas: evidencias firmadas por terceros que se incorporan a la red sin darles autoridad sobre ella.

Referencias:

- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [W3C — Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)

---

## Soluciones

Una solución es un concepto de ingeniería que ya existe en el sector y que contribuye a automatizar un factor o a dotarlo de redundancia. Ninguna está pensada para una red DLT permisionada en concreto: una solución puede tocar varios factores, a veces de pasada, y un factor puede necesitar varias soluciones.

- [Despliegue declarativo con reconciliación](solutions/declarative-deployment.md)
- [Redundancia en dominios de fallo independientes](solutions/failure-domain-redundancy.md)
- [Autorreparación basada en comprobaciones de salud](solutions/health-based-self-healing.md)
- [Acceso de las aplicaciones a través de varios nodos](solutions/multi-node-client-access.md)
- [Gestión automatizada de certificados](solutions/automated-certificate-management.md)
- [Custodia de claves y secretos fuera del nodo](solutions/external-key-custody.md)
- [Gobernanza en cadena](solutions/on-chain-governance.md)
- [Entrega de software verificable](solutions/verifiable-software-delivery.md)
- [Copias y reconstrucción del estado](solutions/state-backup-and-rebuild.md)
- [Observabilidad con alertas accionables](solutions/actionable-observability.md)
- [Políticas verificadas de forma continua](solutions/continuous-policy-enforcement.md)
- [Inyección controlada de fallos](solutions/fault-injection-testing.md)
- [Atestaciones verificables en cadena](solutions/on-chain-attestations.md)
