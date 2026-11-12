# ISBE (Infraestructura de Servicios Blockchain de España)

Red blockchain nacional, público-permisionada e interoperable con EBSI. La impulsa la Comunidad de Madrid con fondos del Plan de Recuperación, Transformación y Resiliencia (Next Generation EU), mediante un convenio con la asociación Alastria, que la desarrolla y la opera sobre Hyperledger Besu. ISBE es una red distinta de las de Alastria.

Su finalidad declarada es verificar documentos e identidades con plena validez jurídica sin depender de plataformas privadas de fuera de la UE.

## Marco regulatorio

ISBE se diseña desde el principio para cumplir la regulación y presenta ese cumplimiento como una ventaja competitiva para las empresas que la usan. Les ahorra trabajo para cumplir, pero no las exime de sus obligaciones. Estas son las normas que tiene en cuenta:

- eIDAS2: aspira a ser un [libro mayor electrónico cualificado](electronic-ledger.md) conforme al Reglamento de Ejecución (UE) 2025/2531. A noviembre de 2026 no figura en la lista de confianza, y Alastria reconoce que ISBE no es un QTSP
- [RGPD](https://gdpr-text.com/es/): el cumplimiento se plantea desde el diseño, con piezas técnicas como el Filtering Proxy y con reglas de gobernanza que obligan a minimizar los datos personales on-chain (hash, referencias o pseudonimización)
- [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj?locale=es), sobre la resiliencia operativa digital del sector financiero: si un caso de uso da servicio a entidades financieras, hay que firmar una adenda DORA antes de llevarlo a producción
- [MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj?locale=es), que regula la emisión de criptoactivos y los servicios sobre ellos
- [Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj?locale=es), que regula el acceso a los datos de los productos conectados y fija requisitos para los smart contracts que ejecutan acuerdos de intercambio de datos
- [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=es), que exige medidas de ciberseguridad y notificación de incidentes a las entidades esenciales e importantes
- [ENS (Esquema Nacional de Seguridad)](https://www.boe.es/eli/es/rd/2022/05/03/311/con), que fija la seguridad exigida al sector público español y a sus proveedores tecnológicos
- [LMVSI (Ley de los Mercados de Valores y de los Servicios de Inversión)](https://www.boe.es/eli/es/l/2023/03/17/6/con), que admite representar valores con tecnología de registro distribuido

## Arquitectura

ISBE sigue un modelo de red de redes federada, que combina una capa pública abierta con control permisionado. La red es abierta y colaborativa, pero cada participante solo puede hacer lo que le permite su nivel de participación. Hay una red base y varias redes de casos de uso, que es donde se despliegan los smart contracts de cada solución.

Sus piezas principales son estas:

- Smart Contract Framework, basado en el patrón Diamond (EIP-2535) y con control de acceso por roles (RBAC). Ningún smart contract llega a la red sin pasar un test de conformidad técnica y de ciberseguridad, y siempre se despliega a través de los contratos fábrica autorizados
- Identidad digital soberana con el método `did:isbe`, compatible con EBSI
- Filtering Proxy, la pieza orientada a garantizar el cumplimiento del RGPD
- Token TKN, un utility token denominado en euros y exento de MiCA

> [Capacidades, pilares y versiones del proyecto](#capacidades-pilares-y-versiones).

## Gobernanza y participación

Una entidad gestora administra la red y es la única contraparte de cada participante. Admite y excluye participantes, aprueba las políticas ISBE y define el protocolo de consenso. Las políticas prevalecen sobre el contrato en los aspectos técnicos y operativos, y la entidad gestora puede modificarlas. Si un cambio resulta sustancialmente más gravoso, el participante puede darse de baja sin penalización.

Para participar, una persona jurídica firma el Contrato Marco de Adhesión junto con al menos un anexo de rol y supera una verificación KYB (Know Your Business). Los niveles de participación no tienen jerarquía entre ellos y se pueden acumular, siempre que se respete la separación de funciones:

- Básico: acceso al portal, asistentes no-code supervisados para desplegar smart contracts, servicios de notarización y registro de evidencias, y gas a través de un faucet. No permite operar nodos ni interactuar directamente con la blockchain. El alta es automática
- Observador: acceso de solo lectura con herramientas de monitorización, reservado a supervisores, reguladores y organismos públicos de la UE o el EEE. Por lo general es incompatible con el resto de niveles
- Desarrollador: despliega casos de uso y smart contracts homologados, consume servicios BaaS (Blockchain as a Service) y puede pedir su inclusión en el catálogo de ISBE. Responde del ciclo de vida de sus contratos y de los controles KYC/AML sobre sus usuarios. El alta es automática
- Operador de nodo de ejecución: opera nodos que procesan transacciones, mantienen el estado de la red y exponen endpoints RPC o APIs, también para dar servicio a terceros. No participa en el consenso. Requiere aprobación de la entidad gestora
- Operador de nodo de consenso: propone y valida bloques. Sus nodos deben estar en la UE, el EEE u otro territorio autorizado, en una red cerrada y cumpliendo SLAs, y puede recibir una compensación. Requiere aprobación de la entidad gestora

> [Las políticas ISBE que aplican a cada nivel](#políticas-isbe).

## Modelo económico

ISBE cobra tarifas fijas y no hay gas fees por transacción. El acceso a los niveles Básico, Observador y Desarrollador es gratuito, y lo que se paga son los servicios que se consumen:

- BaaS, para desplegar y mantener contratos en la red Main
- Trust Framework & Registry, para montar un marco de identidad y confianza
- Programa Network Service Provider, para los operadores de nodo, que es el único que cobra un recargo por las transacciones que superan el límite contratado

El servicio de libro mayor electrónico cualificado (QEL) se presta sobre otra red, la red Bare, y tiene su propio instrumento contractual.

> [Tarifas orientativas](#tarifas-orientativas).

## Alastria

Asociación española sin ánimo de lucro, creada en 2017, que reúne empresas, universidades y administraciones en torno a redes blockchain permisionadas. Tiene sus propias redes, independientes de ISBE. Además desarrolla y opera ISBE para la Comunidad de Madrid, y lleva a esa red su enfoque regulatorio, centrado en eIDAS y el RGPD.

## Aclaraciones

### Capacidades, pilares y versiones

ISBE ofrece 9 capacidades básicas (Core Capabilities) sobre las que los proveedores de servicios construyen los suyos sin competir con la infraestructura. Sus pilares estratégicos van desde la certificación de evidencias y la lógica de negocio verificable hasta la identidad descentralizada, el dinero digital y la tokenización de activos reales.

La Release 2026.1 es la entrega formal del proyecto. La 2026.2 actualiza Besu a la versión 26.01 y a Cancún, añade un plugin HSM para Besu y despliega nodos en un proveedor europeo. La 2026.3 está prevista para el segundo semestre de 2026.

### Políticas ISBE

Las políticas se agrupan en cuatro bloques:

- Normativa y gobernanza (NOR1020 a NOR1090): responsabilidad, código ético, conflictos de interés, confidencialidad, protección de datos, propiedad intelectual, competencia y neutralidad, y sostenibilidad medioambiental
- Ecosistema: adhesión y salida (ECO1010), gestión de casos de uso y smart contracts (ECO1020), y pausado o bloqueo de contratos y borrado de datos (ECO1030)
- Infraestructura: gestión de nodos (INF1040) y gestión de identidades, credenciales y accesos (INF1050)
- Administración: tarifas y retribuciones (ADM1010)

Las de normativa, ECO1010, INF1050 y ADM1010 aplican a todos los niveles. ECO1020 y ECO1030 se suman en los niveles que despliegan contratos, e INF1040 en los de operador de nodo.

### Tarifas orientativas

El anexo de contribuciones económicas vigente entre el 1 de julio de 2026 y el 30 de junio de 2027 fija, sin IVA, un alta de entre 1.500 y 15.000 € por contrato en BaaS más una cuota de 75 a 300 € al mes por contrato desplegado. El programa Network Service Provider empieza en 1.500 € al mes. El nivel Enterprise y los marcos de confianza a medida se negocian.

## Referencias

- [Documentación del proyecto ISBE, Release 2026.1](../isbe/start-here/README.md)
- [Contrato Marco de Adhesión a la red ISBE](<../isbe/legal/ISBE CMA(ES).md>)
- [Anexo de contribuciones económicas generales](<../isbe/legal/ANEXO CEG (ES).md>)
- [Políticas ISBE](../isbe/legal/políticas/)
- [Documentación técnica de ISBE](https://docs.redisbe.com/documentation/)
- [Proyecto ISBE (Alastria)](https://alastria.io/en/proyectos/isbe-blockchain-services-infrastructure-of-spain/)
- [Webinar sobre ISBE como infraestructura conforme a la regulación (LF Decentralized Trust)](https://www.lfdecentralizedtrust.org/learn/webinars/webinar-with-alastria-building-isbe-europes-regulation-compliant-blockchain-infrastructure-on-besu)
