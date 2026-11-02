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
- Dependencias operativas de terceros (oráculos, proveedores RPC externos, proveedores externos de identidad y servicios de custodia): quedan fuera porque lo que la red valida debe residir en la cadena y evaluarse de forma determinista, de modo que todos los nodos lleguen al mismo resultado.
- Autoridad operativa delegada en terceros: se excluyen los modelos en los que servicios externos tienen capacidad de decisión o control sobre la operación de la red. La gestión y las decisiones operativas deben permanecer bajo el control de la propia organización o de los mecanismos de gobernanza de la red. Por ejemplo, un servicio externo capaz de autorizar la incorporación de nodos, modificar permisos, aprobar cambios de configuración o decidir quién participa en la red. Al igual que las dependencias anteriores, ata la red a decisiones centralizadas y crea un punto único de fallo. Una red permisionada asume cierto grado de centralización, pero estos atajos, como los puentes en Web3, conocidos por su inseguridad, deben excluirse desde el diseño inicial.

### Restricciones de arquitectura de la red

- No introducir dependencias externas de confianza como condición para el funcionamiento de la red.
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

- [Hyperledger Besu — Permissioning](https://docs.besu-eth.org/private-networks/concepts/permissioning)
- [Hyperledger Besu — QBFT](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft)
- [Hyperledger Besu — Node synchronization](https://docs.besu-eth.org/private-networks/concepts/node-sync-private)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Smart contract de selección de validadores, encaje total para automatizar la pertenencia: el contrato fija el conjunto de validadores; alta, baja y reincorporación se ejecutan en cadena, sin configurar nodos. Referencia: [ConsenSys — contratos de validadores](https://github.com/ConsenSys/validator-smart-contracts), implementado como contract validator selection en [Besu — QBFT](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft).
- Votación de validadores por API JSON-RPC, encaje parcial para automatización: QBFT expone métodos para votos de alta y baja, automatizables en su ejecución; la decisión sigue siendo humana. Referencia: [Hyperledger Besu — QBFT](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft).
- Local permissioning, encaje parcial: restringe en cada nodo, desde su fichero de configuración, con qué nodos y cuentas interactúa; no automatiza el ciclo de vida de la pertenencia. Referencia: [Hyperledger Besu — Permissioning](https://docs.besu-eth.org/private-networks/concepts/permissioning).
- Modos de sincronización, encaje parcial: un nodo nuevo se sincroniza solo (full o snap) y cumple la condición de estar sincronizado; no define las condiciones de entrada. Referencia: [Hyperledger Besu — Node synchronization](https://docs.besu-eth.org/private-networks/concepts/node-sync-private).
- Reparto de validadores en dominios de fallo independientes, encaje total para redundancia: si más de un tercio de validadores deja de participar la red se para, así que un mismo fallo no debe tumbar a más de un tercio. Referencia: [Kubernetes — Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/).
- Health probes, encaje parcial: detectan la indisponibilidad y aíslan el nodo de los servicios, no pueden impedir ni forzar su participación en el consenso. Referencia: [Kubernetes — Probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/).
- Cambiar el quórum, no existe solución: el quórum de QBFT (supermayoría de 2/3) es regla del protocolo; la ingeniería no lo modifica, solo puede aportar reparto de validadores y monitorización de su participación. Referencia: [Hyperledger Besu — QBFT](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft).

### Identidad criptográfica: PKI, certificados y claves

Certificados, claves y secretos con los que se identifican y comunican los nodos y participantes.

- Arquitectura de la PKI: jerarquía de autoridades de certificación y relaciones de confianza entre organizaciones.
- Ciclo de vida de los certificados: emisión, renovación, expiración y revocación de los certificados de nodos y participantes.
- Custodia de las claves: quién guarda cada clave, dónde, y cómo se rota o se recupera.
- Módulos criptográficos (HSM): dispositivos donde se guardan las claves y dependencia de ellos.
- Gestión de secretos: contraseñas, tokens y credenciales que no son claves criptográficas.

Referencias:

- [RFC 5280 — PKI de certificados X.509 y CRL](https://www.rfc-editor.org/rfc/rfc5280)
- [RFC 8555 — ACME](https://www.rfc-editor.org/rfc/rfc8555)
- [NIST SP 800-57 Part 1 Rev. 5 — gestión de claves](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [Hyperledger Besu — TLS](https://docs.besu-eth.org/private-networks/how-to/configure/tls)
- [OpenBao — Documentación](https://openbao.org/docs/)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- ACME, encaje total para automatizar el ciclo de vida de certificados: RFC 8555 define la emisión, la renovación y la revocación automatizadas sin intervención humana; no toca la arquitectura de la PKI. Referencia: [RFC 8555 — ACME](https://www.rfc-editor.org/rfc/rfc8555).
- CA automatizada, encaje total para automatización, parcial para redundancia: step-ca implementa ACME con emisión, renovación y revocación pasiva, e integra HSM PKCS#11; admite varias instancias, que dependen de una base de datos y una configuración compartidas. Referencias: [Smallstep — step-ca](https://smallstep.com/docs/step-ca/), [Smallstep — step-ca en producción](https://smallstep.com/docs/step-ca/certificate-authority-server-production/).
- Custodia en HSM, encaje total en custodia, no es automatización: NIST SP 800-57 prescribe el almacenamiento y la protección de claves; el plugin HSM de Besu guarda en el HSM la clave de nodo, la que firma el consenso QBFT y el handshake P2P; Web3Signer saca del nodo la firma de transacciones, que usa claves de cuenta y no la clave de nodo; un HSM único es un punto único de fallo y su alta disponibilidad no está estandarizada. Referencias: [NIST SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), [Besu HSM plugin](https://github.com/besu-eth/besu-hsm-plugin), [Web3Signer](https://docs.web3signer.consensys.net/).
- Gestor de secretos, encaje parcial: OpenBao cubre los secretos que no son claves con leases, credenciales dinámicas, rotación y modo de alta disponibilidad; también gestiona claves con su motor transit y emite certificados con su motor PKI, pero Besu no lo admite como custodio de la clave de nodo. Referencia: [OpenBao — Documentación](https://openbao.org/docs/).
- Arquitectura de PKI entre organizaciones, no existe solución de ingeniería: la jerarquía de confianza y las relaciones entre organizaciones son decisión de gobernanza; la ingeniería aporta mecanismos de representación y federación, no la decisión. Referencia: [RFC 5280 — PKI de certificados X.509 y CRL](https://www.rfc-editor.org/rfc/rfc5280).

### Ciclo de vida y salud de los nodos

Vida de cada nodo, desde que se aprovisiona hasta que se retira.

- Alta y baja de nodos: aprovisionamiento, sincronización inicial, mantenimiento y retirada.
- Salud del nodo: diferencia entre un proceso que responde y un nodo sincronizado que participa.
- Recuperación del nodo: vuelta a la operación tras una caída, una desincronización o una pérdida de datos.

Referencias:

- [Kubernetes — Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/)
- [Kubernetes — StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup)
- [Hyperledger Besu — Upgrade](https://docs.besu-eth.org/private-networks/how-to/upgrade)
- [Hyperledger Besu — Validators](https://docs.besu-eth.org/private-networks/how-to/configure/validators)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- StatefulSet, encaje total para automatizar el ciclo de vida: despliegue declarativo y versionado de los nodos, con almacenamiento e identidad propios de cada réplica; el reinicio y el reemplazo del nodo caído se ejecutan solos. Referencia: [Kubernetes — StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).
- Health probes, encaje parcial: la probe de vida reinicia el proceso que no responde y la de preparación aísla el nodo de los servicios; ninguna detecta la pérdida de datos, la profundidad de sincronización ni la pérdida de participación en el consenso. Referencia: [Kubernetes — Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/).
- Sincronización automática al arrancar, encaje total para recuperar la desincronización, parcial para la pérdida de datos: Besu sincroniza el nodo solo, en modo full o snap, desde el arranque; una pérdida total de datos exige restaurar desde copia, que es procedimiento manual. Referencias: [Hyperledger Besu — Node synchronization](https://docs.besu-eth.org/private-networks/concepts/node-sync-private), [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup).
- Actualización de versión, encaje parcial: Besu documenta el procedimiento de upgrade y advierte de que la red se bifurca si no todos los nodos se actualizan antes del bloque de la milestone; el despliegue es automatizable por declaración, la coordinación entre participantes no. Referencia: [Hyperledger Besu — Upgrade](https://docs.besu-eth.org/private-networks/how-to/upgrade).
- Retirada de un nodo, encaje total para automatización: la votación de alta y baja del pool de validadores se ejecuta en cadena, sin tocar la configuración de los nodos. Referencia: [Hyperledger Besu — Validators](https://docs.besu-eth.org/private-networks/how-to/configure/validators).

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
- [chrony — Daemon NTP](https://chrony-project.org/)
- [Hyperledger Besu — Bootnodes](https://docs.besu-eth.org/private-networks/how-to/configure/bootnodes)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Topology Spread Constraints, encaje total para redundancia y para automatizar el reparto: la declaración de topología reparte los nodos entre zonas y máquinas de un clúster, y el planificador lo aplica y lo mantiene sin intervención; no reparte entre organizaciones, que operan infraestructuras separadas. Referencia: [Kubernetes — Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/).
- Múltiples bootnodes y static nodes, encaje total para redundancia de comunicaciones: Besu recomienda dos o más bootnodes en producción y conecta a los static nodes de forma periódica si se pierde la conexión, así la red no depende de un único nodo de descubrimiento. Referencia: [Hyperledger Besu — Bootnodes](https://docs.besu-eth.org/private-networks/how-to/configure/bootnodes).
- chrony, encaje total para automatizar la sincronización horaria: daemon NTP permanente, con varios servidores como fuentes y una precisión típica de pocos milisegundos por Internet y de decenas de microsegundos en red local, suficiente para certificados y comunicaciones. Referencia: [chrony — Daemon NTP](https://chrony-project.org/).
- Infraestructura como código con GitOps, encaje total para automatizar la declaración: infraestructura y configuración declaradas en ficheros versionados, desplegadas automáticamente y verificadas contra el repositorio, según los principios de OpenGitOps. Referencia: [OpenGitOps — Principios](https://opengitops.dev/).
- Almacenamiento persistente del nodo, encaje parcial: el disco local guarda el registro de un nodo; su redundancia no la da el disco, la da la replicación entre nodos de la red, y las copias se tratan en la sección de datos. Referencia: [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup).

### Software y protocolo

Cambios en el software de los nodos y en las reglas del protocolo a lo largo del tiempo.

- Actualización del software: versiones del cliente y del sistema, y cómo se despliegan.
- Cadena de suministro del software: origen e integridad del software desde que se construye hasta que llega al nodo.
- Compatibilidad entre versiones: convivencia de nodos con versiones o clientes distintos.
- Evolución del protocolo: cambios en las reglas de la red, incluidos los hard forks.

Referencias:

- [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/)
- [Ethereum — Actualizaciones de la red](https://ethereum.org/ethereum-forks/)
- [Hyperledger Besu — Upgrade](https://docs.besu-eth.org/private-networks/how-to/upgrade)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- SLSA, encaje total para trazabilidad e integridad, parcial para automatización: la cadena de suministro se controla con provenancias de build firmadas que se verifican de forma automática antes de desplegar; no cubre la evolución del protocolo. Referencia: [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Despliegue continuo de versiones, encaje total para automatizar la actualización: las versiones se declaran en ficheros y se despliegan de forma controlada, con reinicio coordinado; Besu documenta los pasos —actualizar el cliente o el genesis y reiniciar cada nodo— y la declaración en ficheros los automatiza. Referencia: [Hyperledger Besu — Upgrade](https://docs.besu-eth.org/private-networks/how-to/upgrade).
- Control de compatibilidad entre versiones, encaje parcial: Besu no controla la convivencia de versiones entre nodos; si no todos se actualizan antes de la milestone acordada, la red se bifurca, y el despliegue escalonado sigue siendo decisión. Referencia: [Hyperledger Besu — Upgrade](https://docs.besu-eth.org/private-networks/how-to/upgrade).
- Evolución del protocolo, encaje parcial: un hard fork requiere el acuerdo de los participantes de la red, que es una decisión de gobernanza; la implantación —milestone en el genesis y despliegue antes del bloque de la milestone— es automatizable. Referencias: [Ethereum — Actualizaciones de la red](https://ethereum.org/ethereum-forks/), [Hyperledger Besu — Upgrade](https://docs.besu-eth.org/private-networks/how-to/upgrade).

### Gobernanza y límites de la automatización

Quién decide los cambios en la red y qué papel tienen las personas frente a la automatización.

- Gobernanza de la red: cómo se proponen y aprueban los cambios entre organizaciones.
- Gobernanza de la configuración: quién puede cambiar los parámetros compartidos y los de cada nodo.
- Frontera entre automatización y decisión humana: qué decisiones pueden tomarse sin una persona y cuáles no.
- Operaciones automatizadas: tareas que ya se ejecutan solas y cómo interactúan entre sí.

Referencias:

- [Hyperledger Fabric — Policies](https://hyperledger-fabric.readthedocs.io/en/latest/policies/policies.html)
- [Google SRE — Eliminar el trabajo repetitivo](https://sre.google/sre-book/eliminating-toil/)
- [OpenZeppelin — Upgrades](https://docs.openzeppelin.com/upgrades)
- [Open Policy Agent — Documentación](https://www.openpolicyagent.org/docs)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Gobernanza en cadena, encaje total para automatizar la ejecución de la aprobación: el smart contract de validadores convierte el acuerdo en estado de la cadena y lo ejecuta sin intervención; la propuesta y el voto humanos permanecen. Referencia: [ConsenSys — contratos de validadores](https://github.com/ConsenSys/validator-smart-contracts).
- Timelocks, multisig y DAO como control de cambios de contratos, encaje parcial: OpenZeppelin documenta la práctica de gobernanza de upgrades —retraso obligatorio, varias firmas, voto—; automatiza la ejecución, no la aprobación. Referencia: [OpenZeppelin — Upgrades](https://docs.openzeppelin.com/upgrades).
- Política como código, encaje total para automatizar la verificación, parcial para la aprobación: OPA, proyecto graduado de CNCF, declara políticas en Rego y las hace cumplir de forma automática en Kubernetes, CI/CD y APIs; la política la escriben y la aprueban personas. Referencia: [Open Policy Agent — Documentación](https://www.openpolicyagent.org/docs).
- Políticas de la red (Fabric), encaje parcial: las policies de firma, ACL y endorsement se aplican mecánicamente por el software; quién las define y qué se aprueba es acuerdo entre organizaciones. Referencia: [Hyperledger Fabric — Policies](https://hyperledger-fabric.readthedocs.io/en/latest/policies/policies.html).
- Frontera entre automatización y decisión humana, encaje total como criterio: la definición de toil de Google SRE marca la línea —si un operador humano debe intervenir en la operación normal, es toil—; el criterio es metodológico, no un mecanismo. Referencia: [Google SRE — Eliminar el trabajo repetitivo](https://sre.google/sre-book/eliminating-toil/).

### Smart contracts

Lógica compartida desplegada en la red, que no se para ni se corrige como un servicio convencional.

- Ciclo de vida de los contratos: despliegue, versionado, actualización y retirada.
- Gobernanza de los contratos: quién puede cambiar la lógica, los parámetros o los permisos de un contrato.
- Fallos en los contratos: errores de lógica, vulnerabilidades y pérdida del control administrativo.

Referencias:

- [Ethereum — Actualizar smart contracts](https://ethereum.org/developers/docs/smart-contracts/upgrading/)
- [Ethereum — Seguridad de smart contracts](https://ethereum.org/developers/docs/smart-contracts/security/)
- [ERC-1967 — Proxy Storage Slots](https://eips.ethereum.org/EIPS/eip-1967)
- [OpenZeppelin — Upgrades](https://docs.openzeppelin.com/upgrades)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Proxy con slots de almacenamiento estándar, encaje total para automatizar el ciclo de vida con verificación: ERC-1967 define dónde vive la dirección de la lógica y qué eventos emitir al cambiarla, así el upgrade es ejecutable y verificable por herramientas; el patrón y los plugins de OpenZeppelin aportan la implementación con comprobaciones automáticas. Referencias: [ERC-1967 — Proxy Storage Slots](https://eips.ethereum.org/EIPS/eip-1967), [OpenZeppelin — Upgrades](https://docs.openzeppelin.com/upgrades).
- Control administrativo de timelock, multisig y roles, encaje total como control, parcial para automatización: el retraso obligatorio y la firma múltiple ejecutan la aprobación registrada, no la sustituyen. Referencia: [Ethereum — Actualizar smart contracts](https://ethereum.org/developers/docs/smart-contracts/upgrading/).
- Verificación de contratos, encaje total para automatizar la verificación: revisión de código con revisor independiente, herramientas de análisis, compilación sin warnings y documentación NatSpec son práctica documentada, integrable en CI. Referencia: [Ethereum — Seguridad de smart contracts](https://ethereum.org/developers/docs/smart-contracts/security/).
- Recuperación de la pérdida de control administrativo, no existe solución: las mitigaciones conocidas son preventivas —timelock, multisig, roles—; no hay mecanismo estándar para recuperar el control una vez perdido. Referencia: [Ethereum — Actualizar smart contracts](https://ethereum.org/developers/docs/smart-contracts/upgrading/).

### Datos: retención, copias y recuperación

Datos que guarda la red y los nodos, y cómo se conservan.

- Dominios de datos: tipos de datos que maneja la red, compartidos o privados, reconstruibles o no.
- Retención de datos: cuánto histórico y estado se conserva, se poda o se archiva.
- Copias y recuperación: copias de seguridad y restauración de los datos de los nodos.

Referencias:

- [Hyperledger Fabric — Ledger](https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html)
- [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
- [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup)
- [Hyperledger Besu — Reduce storage for Bonsai Tries](https://docs.besu-eth.org/public-networks/how-to/bonsai-limit-trie-logs)
- [Kubernetes — Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
- [Hyperledger Fabric — Private data](https://hyperledger-fabric.readthedocs.io/en/latest/private-data/private-data.html)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Replicación del registro entre nodos, encaje total para redundancia: el ledger vive replicado en los nodos de la red; la caída de un nodo no destruye el dato, y la pérdida simultánea de réplicas se cubre con el reparto de nodos. Referencias: [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup), [Hyperledger Fabric — Ledger](https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html).
- Copia de seguridad del data directory, encaje parcial: Besu documenta la copia del directorio de datos; automatizable como tarea periódica, la restauración es procedimiento manual. Referencia: [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup).
- VolumeSnapshot, encaje total para automatizar la captura, parcial para la restauración: la captura se declara como objeto de Kubernetes y se ejecuta sola; restaurar crea un volumen desde la snapshot y exige reinstalar el nodo. Referencia: [Kubernetes — Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/).
- Retención y podado automáticos, encaje total para automatizar el almacenamiento: el formato Bonsai limita y poda los trie logs de forma continua, activado por defecto; el histórico del registro no se poda, es una regla del protocolo. Referencias: [Hyperledger Besu — Reduce storage for Bonsai Tries](https://docs.besu-eth.org/public-networks/how-to/bonsai-limit-trie-logs), [Hyperledger Fabric — Ledger](https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html).
- Colecciones de datos privados, encaje total para definir el dominio, parcial para retención: las collections de Fabric definen quién ve el dato, dejan evidencia en la cadena y purgan el dato privado de forma automática y configurable; la retención solo cubre el dato privado, no el histórico del registro. Referencia: [Hyperledger Fabric — Private data](https://hyperledger-fabric.readthedocs.io/en/latest/private-data/private-data.html).
- Restauración completa, encaje parcial: la planificación de contingencia define el procedimiento y su prueba, no existe un mecanismo que restaure la red de forma autónoma. Referencia: [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).

### Redundancia y continuidad del servicio

Capacidad de la red y de los servicios que la consumen para seguir funcionando ante fallos.

- Redundancia de nodos: réplicas de validadores y de nodos de acceso.
- Continuidad para las aplicaciones cliente: acceso de las aplicaciones a la red cuando cae el nodo al que se conectan.
- Recuperación ante desastres: vuelta a la operación tras la caída de un centro de datos o una interrupción generalizada.
- Capacidad y rendimiento: recursos, latencia y throughput de la red y de los nodos.

Referencias:

- [Ethereum — Ejecutar un nodo](https://ethereum.org/developers/docs/nodes-and-clients/run-a-node/)
- [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
- [Hyperledger Besu — High availability](https://docs.besu-eth.org/public-networks/how-to/configure-ha)
- [Hyperledger Besu — Validators](https://docs.besu-eth.org/private-networks/how-to/configure/validators)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Validadores en dominios de fallo independientes, encaje total para redundancia: cada bloque necesita la firma de al menos 2/3 de los validadores, así que si más de un tercio deja de participar la red se para, y el reparto debe garantizar que un mismo fallo no tumbe a más de un tercio; frente a fallos bizantinos, en los que un validador se comporta de forma incorrecta en lugar de caer, la red tolera f = ⌊(n-1)/3⌋ validadores, por lo que el número de validadores se dimensiona con n ≥ 3f+1, con un mínimo de cuatro. Referencias: [Hyperledger Besu — Validators](https://docs.besu-eth.org/private-networks/how-to/configure/validators), [Kubernetes — Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/).
- Acceso redundante con balanceador, encaje total para redundancia de acceso: varios nodos sincronizados detrás de un balanceador que enruta a los nodos en estado de preparación; las aplicaciones siguen sirviéndose de la red cuando un nodo de acceso cae. Referencia: [Hyperledger Besu — High availability](https://docs.besu-eth.org/public-networks/how-to/configure-ha).
- Recuperación del nodo perdido, encaje total para la caída del nodo, parcial para la pérdida de datos: StatefulSet reinicia el nodo y Besu lo sincroniza solo; la restauración desde copia es procedimiento manual. Referencia: [Hyperledger Besu — Backup and restore](https://docs.besu-eth.org/private-networks/how-to/backup).
- Plan de contingencia, encaje total como método, parcial para automatización: NIST SP 800-34 define análisis de impacto, objetivos de recuperación y pruebas; es proceso, no mecanismo autónomo. Referencia: [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- Capacidad y rendimiento, no existe solución formal: la planificación de capacidad es parte de la planificación de contingencia; no hay estándar de ingeniería que garantice latencia y throughput de una red DLT. Referencia: [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).

### Observabilidad, seguridad e incidentes

Cómo se conoce el estado de la red y cómo se responde a los problemas.

- Observabilidad: métricas, logs y alertas de la red y de los nodos.
- Operaciones de seguridad: privilegios, accesos administrativos y cambios no autorizados.
- Gestión de incidentes: detección, respuesta y análisis de incidentes entre organizaciones.

Referencias:

- [Prometheus — Overview](https://prometheus.io/docs/introduction/overview/)
- [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [Hyperledger Besu — Monitoring](https://docs.besu-eth.org/private-networks/how-to/monitor)
- [Hyperledger Besu — Use metrics](https://docs.besu-eth.org/public-networks/how-to/monitor/metrics)
- [Google SRE — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Métricas con Prometheus y Grafana, encaje total para automatizar la detección: Besu expone métricas con la opción metrics-enabled, con dashboard de muestra y alertas de nodos que no alcanzan la cabeza de la cadena. Referencias: [Hyperledger Besu — Use metrics](https://docs.besu-eth.org/public-networks/how-to/monitor/metrics), [Prometheus — Overview](https://prometheus.io/docs/introduction/overview/).
- Logs, eventos y trazas, encaje total para la visibilidad: Besu se integra con Loki, Elastic Stack, Splunk y OpenTelemetry para centralizar logs y trazas de todos los nodos. Referencia: [Hyperledger Besu — Monitoring](https://docs.besu-eth.org/private-networks/how-to/monitor).
- SLO, encaje total como método, parcial para automatización: SLI, SLO y presupuesto de error forman un bucle de control; los umbrales y las alertas se ejecutan solos, la decisión de aceptar el riesgo es humana. Referencia: [Google SRE — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/).
- Respuesta a incidentes, encaje parcial: NIST SP 800-61 Rev. 3 integra la respuesta a incidentes en las funciones del CSF 2.0 (gobernar, identificar, proteger, detectar, responder y recuperar); la detección es automatizable, la respuesta y la coordinación entre organizaciones son humanas. Referencia: [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- Operaciones de seguridad entre organizaciones, no existe solución de ingeniería: compartir evidencia y coordinar la respuesta es acuerdo de gobernanza; la norma aporta el proceso, no un mecanismo técnico entre organizaciones. Referencia: [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

### Verificación: pruebas, auditoría y atestaciones

Comprobación de que la red se comporta como se espera, dentro y fuera de ella.

- Pruebas de resiliencia: comportamiento de la red ante fallos provocados.
- Aseguramiento operativo: verificación de que la configuración, las versiones y los permisos son los esperados.
- Atestaciones externas: evidencias firmadas por terceros que se incorporan a la red sin darles autoridad sobre ella.

Referencias:

- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [W3C — Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [Chaos Mesh — Chaos Engineering para Kubernetes](https://chaos-mesh.org/)
- [Open Policy Agent — Documentación](https://www.openpolicyagent.org/docs)

#### Concepto de solución

Soluciones conocidas del sector, con su grado de encaje en los factores y su objetivo: automatización o redundancia. Se marca encaje total, encaje parcial o inexistencia.

- Chaos engineering, encaje total para automatizar las pruebas de resiliencia: Chaos Mesh, proyecto de CNCF, declara inyecciones de fallo como objetos de Kubernetes y orquesta escenarios completos, ejecutables en producción sin cambiar el despliegue. Referencia: [Chaos Mesh — Chaos Engineering para Kubernetes](https://chaos-mesh.org/).
- Aseguramiento operativo continuo, encaje total como método, parcial para automatización: NIST SP 800-53 define controles con evaluación continua; la política como código, con OPA, convierte ese aseguramiento en comprobaciones automáticas en Kubernetes y CI. Referencias: [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [Open Policy Agent — Documentación](https://www.openpolicyagent.org/docs).
- Atestaciones externas, encaje parcial: el modelo W3C VC 2.0 define credenciales verificables firmadas por emisores, el patrón conocido para incorporar evidencias de terceros sin darles autoridad sobre la red; no existe un sistema estándar de atestación de la operación de nodos. Referencia: [W3C — Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/).
- Verificación integral de la red, no existe solución única: no hay un sistema que verifique la red entera; se compone de chaos engineering, política como código, controles continuos y atestaciones. Referencia: [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).

---

