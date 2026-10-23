# Glosario generales de términos

## ETSI (European Telecommunications Standards Institute)

Instituto Europeo de Normas de Telecomunicaciones, con sede en Sophia Antipolis (Francia). Es uno de los tres organismos europeos de normalización reconocidos por el Reglamento (UE) 1025/2012, junto con CEN y CENELEC. Su comité ESI (Electronic Signatures and Infrastructures) elabora las normas técnicas que desarrollan eIDAS (firmas, certificados, prestadores de servicios de confianza, listas de confianza).

Referencias:

- [web de ETSI](https://www.etsi.org/)
- [comité ESI de ETSI](https://www.etsi.org/committee/esi)

## CEN y CENELEC

Comité Europeo de Normalización (CEN) y Comité Europeo de Normalización Electrotécnica (CENELEC), con sede en Bruselas. Junto con ETSI son los tres organismos europeos de normalización reconocidos oficialmente por la UE (Reglamento (UE) 1025/2012). Elaboran las normas europeas formales (EN), que los organismos nacionales (UNE en España) adoptan como propias.

Su papel en la regulación europea es este: una ley de la UE fija requisitos generales, la Comisión encarga a estos organismos las normas técnicas que los concretan, y quien cumple esas normas se presume que cumple la ley. Por eso aparecen en los tres ámbitos de este glosario, cada uno a través de un comité técnico distinto:

- eIDAS: el comité CEN/TC 224 elabora la serie de normas EN 419, que fija los requisitos de seguridad de los dispositivos de firma y sello (tarjetas, módulos criptográficos de los prestadores, firma en servidor). La mayoría de las normas de los servicios de confianza las elabora ETSI, no CEN
- Blockchain: el comité conjunto CEN/CENELEC JTC 19 (Blockchain and Distributed Ledger Technologies) adapta al ámbito europeo las normas internacionales de ISO/TC 307 y trabaja en normas propias, como la protección de datos personales en DLT
- Espacios de datos: el comité conjunto CEN/CENELEC JTC 25 (Data management, Dataspaces, Cloud and Edge), creado en septiembre de 2024, elabora las normas que concretan los requisitos de interoperabilidad del artículo 33 del Data Act, por encargo de la Comisión (mandato M/614, aceptado en julio de 2025). Lo preside un representante de IDSA

Referencias:

- [web de CEN y CENELEC](https://www.cencenelec.eu/)
- [creación del comité JTC 25 (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2024/brief-news/2024-09-25-jtc-25/)
- [aceptación del mandato del Data Act (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2025/brief-news/2025-07-11-data-act-standardization-request/)

## OSCAL (Open Security Controls Assessment Language)

Lenguaje estándar desarrollado por el NIST (National Institute of Standards and Technology) para representar de forma estructurada (JSON, XML o YAML) controles de seguridad, catálogos de cumplimiento, planes de seguridad (SSP) y evaluaciones de riesgo. Su objetivo es que la información de cumplimiento normativo se pueda leer, validar y transformar de forma automatizada, en lugar de mantenerla en documentos manuales (PDF o Word).

Herramientas que lo soportan:

- NIST OSCAL CLI: herramienta oficial que convierte entre JSON, XML y YAML y valida documentos contra el esquema oficial
- Trestle (compliance-trestle): la herramienta más usada para trabajar con catálogos OSCAL en Python y generar SSP (System Security Plan), profiles, etc.
- OpenControl y GovReady-Q: también consumen documentos OSCAL
- Cualquier parser genérico (Python, `jq`, JavaScript...), al ser JSON, XML o YAML estándar, si solo se quieren extraer datos

Referencia: [documentación de OSCAL (NIST)](https://pages.nist.gov/OSCAL/)

## FIWARE

Fundación que mantiene un conjunto de componentes open source para gestionar datos de contexto (por ejemplo, el Orion Context Broker), basados en la especificación NGSI-LD de ETSI. Es muy usado en ciudades inteligentes y aporta conectores e implementaciones de referencia a los espacios de datos.

Referencia: [web de FIWARE](https://www.fiware.org/)

---
