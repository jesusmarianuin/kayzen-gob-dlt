# Comunidad

Aquí encontrarás una selección de sitios web y autores que considero valiosos para adquirir conocimientos y desarrollar proyectos relacionados con la descentralización.

> **Nadie patrocina esta repositorio**, por lo tanto, los enlaces propuestas son realmente los sitios que considero válidos, independientemente de que en algunos, existan empresas detrás con intereses económicos, sean de pago o simplemente sean incorrectos y fue un error elegirlos.

Están organizados por **para lo que sirve**: así puedes ir directo a lo que necesitas aunque eso signifique que una misma organización aparezca en más de un sitio con un enlace distinto según el caso. Como el enfoque de este repositorio es DLT aplicada a la Administración Pública española y europea (ver [README](README.md) y [MANIFESTO](MANIFESTO.md)), los primeros bloques son los directamente relevantes para eso; el resto es formación general de Web3 que sigue siendo útil como base técnica, pero ya no es el centro.

## Identidad digital y confianza (Europa)

- [eIDAS2 y la Cartera Europea de Identidad Digital (EUDI Wallet)](https://digital-strategy.ec.europa.eu/es/policies/eudi-regulation) - Página oficial de la Comisión Europea sobre el Reglamento eIDAS2 y la futura cartera de identidad digital europea, la pieza normativa central para identidad descentralizada y credenciales verificables en la UE.
- [W3C - Decentralized Identifiers (DID) Core](https://www.w3.org/TR/did-core/) - Especificación técnica del W3C sobre identificadores descentralizados (DID), la base sobre la que se apoyan la EUDI Wallet y EBSI para representar identidad sin autoridad central.
- [W3C - Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model-2.0/) - Especificación técnica del W3C sobre credenciales verificables (VC), el estándar de facto para representar títulos, certificados y atributos firmados criptográficamente.

## Interoperabilidad y espacios de datos (Europa)

- [Gaia-X](https://gaia-x.eu/) - Iniciativa europea para una infraestructura de datos federada y soberana; marco de referencia detrás de los espacios de datos sectoriales que impulsa la Comisión Europea.
- [Data Spaces Support Centre (DSSC)](https://dssc.eu/) - Centro de apoyo de la Comisión Europea para la creación de espacios de datos interoperables entre sectores y países, con guías técnicas y el Data Spaces Blueprint.
- [International Data Spaces Association (IDSA)](https://internationaldataspaces.org/) - Asociación que define la arquitectura de referencia para espacios de datos soberanos, ampliamente usada como base técnica de Gaia-X y de los espacios de datos europeos.

## Administración electrónica y seguridad (España)

- [Portal de Administración Electrónica (PAe)](https://administracionelectronica.gob.es/) - Portal oficial de la Administración española sobre administración electrónica: normativa, interoperabilidad, esquemas y actualidad del sector; la fuente primaria que sigue este repositorio.
- [Esquema Nacional de Seguridad (ENS)](https://administracionelectronica.gob.es/pae_Home/pae_Estrategias/pae_Seguridad_Inicio/pae_Esquema_Nacional_de_Seguridad.html) - Página oficial del ENS, la normativa que regula la seguridad de los sistemas de información en la Administración española; ver también la carpeta [ENS](ENS/) de este repositorio.
- [CCN-CERT](https://www.ccn-cert.cni.es/) - CERT gubernamental español (Centro Criptológico Nacional), referencia en ciberseguridad, guías CCN-STIC y cumplimiento del ENS.
- [Red.es](https://red.es/) - Entidad pública empresarial adscrita al Ministerio, responsable de impulsar la digitalización y proyectos de innovación —incluidos pilotos blockchain— en España.

## Administración pública y blockchain institucional (Europa)

- [EBSI (European Blockchain Services Infrastructure)](https://hub.ebsi.eu/) - Infraestructura blockchain paneuropea impulsada por la Comisión Europea y los Estados miembro para casos de uso institucionales (diplomas verificables, credenciales, trazabilidad); la referencia más directa de "DLT + administración" a nivel de la UE.
- [European Blockchain Partnership (EBP)](https://digital-strategy.ec.europa.eu/en/policies/blockchain-partnership) - Iniciativa de la Comisión Europea y los Estados miembro, incluida España, para coordinar el despliegue de infraestructura blockchain pública; el marco político detrás de EBSI.
- [Alastria](https://alastria.io/) - Principal consorcio blockchain de España, con participación de administraciones y grandes empresas; referencia práctica de red permissionada institucional en español.
- [ISBE (Infraestructura de Servicios Blockchain de España)](https://redisbe.com/) - Red blockchain operativa (desde diciembre de 2025) impulsada por la Comunidad de Madrid junto con Alastria, pensada para administraciones, empresas y ciudadanos, con cumplimiento de ENS, MiCA, DORA, Data Act, LSMV y NIS2 integrado desde el diseño; probablemente el ejemplo más concreto hoy de "DLT + administración española" en producción.

## Clientes DLT permissionados (consorcios)

- [Hyperledger Besu](https://docs.besu-eth.org/) - Cliente Ethereum de nivel empresarial (Java, Apache 2.0), compatible con EVM y usable tanto en redes públicas como permissionadas. Es el cliente que realmente eligió [EBSI](https://hub.ebsi.eu/) y buena parte de las redes institucionales europeas, precisamente por esa compatibilidad con el ecosistema Ethereum/EVM en vez de un stack propietario. [Repositorio en GitHub](https://github.com/besu-eth/besu).
- [Hyperledger Fabric](https://hyperledger-fabric.readthedocs.io/es/latest/whatis.html) - Framework DLT permissionado orientado a redes con participantes conocidos (consorcios, empresas, administraciones). Técnicamente encaja con el contexto de una Administración Pública, pero en la práctica europea es Besu, no Fabric, la elección más habitual; se deja aquí solo como referencia informativa.
- [LF Decentralized Trust](https://www.lfdecentralizedtrust.org/) - Fundación de la Linux Foundation que desde 2025 alberga Hyperledger Besu, Hyperledger Fabric y el resto de proyectos DLT que antes vivían bajo el nombre "Hyperledger Foundation".

## Infraestructura Web3 de referencia

- [IOTA](https://www.iota.org/) - Protocolo DLT orientado a IoT y cadena de suministro. Fundación alemana y miembro fundador de [INATBA](https://inatba.org/) (la asociación que sirve de puente entre proyectos DLT y reguladores/administraciones), con años de trabajo real detrás, caídas incluidas, de los que se puede aprender.
- [Ethereum](https://ethereum.org/) - Red pública de contratos inteligentes de referencia en el espacio Web3; su máquina virtual (EVM) se ha convertido en el estándar de facto que otras muchas redes, incluidas algunas permissionadas, terminan replicando.
- [IPFS (InterPlanetary File System)](https://ipfs.tech/) - Protocolo de Protocol Labs para almacenamiento y direccionamiento de contenido distribuido, sin depender de un servidor único; el mismo problema que resuelve mal cualquier "repositorio único" de expediente electrónico.

## Estándares Web3

Ofrecen una base sólida técnica de otros caminos ya recorridos que pueden servir de referencia.

- [Ethereum para Desarrolladores](https://ethereum.org/es/developers/) - Portal oficial para desarrolladores con guías, documentación y herramientas para construir en Ethereum.
- [Ethereum Docs](https://ethereum.org/es/developers/docs/) - Documentación oficial para desarrolladores sobre Ethereum, contratos inteligentes y herramientas del ecosistema.
- [Ethereum Standards Documentation](https://ethereum.org/en/developers/docs/standards/) - Documentación sobre los principales estándares de Ethereum, como ERC-20, ERC-721 y otros, fundamentales para el desarrollo de contratos inteligentes y aplicaciones descentralizadas.
- [Ethereum Improvement Proposals (EIP)](https://eips.ethereum.org/) - Proceso de estándares de Ethereum, citado en el [MANIFESTO](MANIFESTO.md) de este repositorio como ejemplo de gobernanza de estándares abierta de la que la administración podría aprender.
- [Solidity Docs](https://docs.soliditylang.org/) - Documentación oficial del lenguaje Solidity para escribir contratos inteligentes en Ethereum y otras blockchains compatibles.
- [OpenZeppelin Learn](https://docs.openzeppelin.com/learn/) - Plataforma interactiva para aprender sobre seguridad y desarrollo de contratos inteligentes con OpenZeppelin.
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/4.x/) - Implementaciones seguras y auditadas de los principales estándares de contratos inteligentes.
- [Chainlink Tutorials](https://docs.chain.link/) - Tutoriales y documentación oficial para aprender a integrar oráculos Chainlink en proyectos Web3.
- [Chainlink Education](https://chain.link/education) - Recursos educativos y cursos para aprender sobre oráculos, contratos inteligentes y el ecosistema Chainlink.

## Formación developer (general)

- [RareSkills](https://rareskills.io/web3-blockchain-bootcamps) - Bootcamps avanzados de Solidity y ZK muy centrados en seguridad y profundidad técnica, orientados a desarrolladores con base previa.
- [freeCodeCamp](https://www.freecodecamp.org/) - Plataforma gratuita con miles de horas de contenido interactivo para aprender desarrollo web y programación.
- [O'Reilly](https://www.oreilly.com/) - Plataforma líder en aprendizaje técnico con libros, cursos, videos y recursos sobre programación, arquitectura de software, IA, cloud computing, blockchain y tecnologías emergentes.
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Plataforma educativa con tutoriales, artículos y ejercicios sobre programación, algoritmos, estructuras de datos, desarrollo web y ciencias de la computación.
- [midudev](https://midu.dev/) - Sitio y canal de YouTube de @midudev, con tutoriales, cursos y recursos en español sobre desarrollo web, JavaScript y tecnologías modernas.
- [EDTeam](https://ed.team/) - Plataforma educativa en español con cursos sobre desarrollo web, programación, blockchain y tecnologías emergentes.

## Sitios de interés referentes en su área

No encajan en un caso de uso concreto del repositorio, pero son referentes en su ámbito y hablan de tecnología, descentralización e innovación de una forma que me parece valiosa.

- [metlabs](https://metlabs.io/blog/) - Empresa especializada en blockchain y tokenización de activos.
- [Opt Out Podcast](https://optoutpod.com/) - Podcast sobre privacidad, seguridad digital, Bitcoin y soberanía de datos, con entrevistas a expertos en herramientas y técnicas de privacidad.
  - Puedes seguirlos en [YouTube](https://www.youtube.com/c/OptOutPodcast), [Spotify](https://open.spotify.com/show/59fX0wRUKhWGK9IAKt7bQM) o [RSS](https://feeds.buzzsprout.com/1790481.rss).
- [Obscuro Labs](https://medium.com/obscuro-labs) - Blog en Medium sobre privacidad, confidencialidad y soluciones de encriptación en blockchain.
- [Dexa](https://dexa.ai/) - Plataforma que permite realizar preguntas y obtener respuestas directamente de expertos a través de sus contenidos en podcasts. Incluye expertos en crypto y Web3 como Bankless y Rehash, entre otros temas de tecnología, salud y negocios.
- [IBM Think Topics](https://www.ibm.com/es-es/think/topics) - Plataforma de conocimiento de IBM con artículos, guías y recursos sobre tecnología, IA, blockchain, cloud computing e innovación empresarial.

---

Si tienes alguna sugerencia de otros sitios interesantes, ¡no dudes en compartirla!

---
