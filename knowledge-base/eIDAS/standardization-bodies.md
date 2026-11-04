# Organismos de normalización

Organismos europeos e internacionales que elaboran las normas técnicas que citan eIDAS y sus [actos de ejecución](implementing-acts.md).

Ninguno de estos organismos es un departamento de la UE ni de la Comisión: son asociaciones independientes sin ánimo de lucro. En ETSI participan directamente empresas, administraciones, universidades y centros de investigación. En CEN, CENELEC e ISO los miembros son los organismos nacionales, como UNE en España, y a través de ellos participan la industria y los expertos.

La Comisión no les da órdenes, pero puede encargar normas a ETSI, CEN y CENELEC, que deciden si aceptan el encargo. Sus normas no obligan por sí solas: adquieren valor normativo cuando un acto de ejecución las cita como referencia.

## ETSI (European Telecommunications Standards Institute)

Instituto Europeo de Normas de Telecomunicaciones, con sede en Sophia Antipolis (Francia). Es uno de los tres organismos europeos de normalización reconocidos por el Reglamento (UE) 1025/2012, junto con CEN y CENELEC. Su comité ESI (Electronic Signatures and Infrastructures) elabora las normas técnicas que desarrollan eIDAS (firmas, certificados, prestadores de servicios de confianza, listas de confianza).

Referencias:

- [Web de ETSI](https://www.etsi.org/)
- [Comité ESI de ETSI](https://www.etsi.org/committee/esi)

## CEN y CENELEC

El Comité Europeo de Normalización (CEN) y el Comité Europeo de Normalización Electrotécnica (CENELEC) son, junto con ETSI, los organismos europeos de normalización reconocidos oficialmente por la UE (Reglamento (UE) 1025/2012). Tienen su sede en Bruselas y se encargan de elaborar las normas europeas formales (EN), que posteriormente los organismos nacionales (como [UNE](https://www.une.org/) en España) adoptan como propias.

Su función principal es traducir los requisitos legales generales de la Unión Europea en especificaciones técnicas concretas. Cuando la Comisión Europea aprueba una ley, encarga a estos organismos la creación de la norma técnica correspondiente; cumplir esa norma puede dar a un sistema o servicio una presunción de conformidad respecto a los requisitos que cubre, cuando así lo establece el marco normativo.

Esta labor estandarizadora es clave para la infraestructura digital europea, operando a través de comités técnicos especializados en cada ámbito:

- eIDAS y EUDI Wallet: el comité CEN/TC 224 elabora normas como la serie EN 419, que define los requisitos de seguridad de los dispositivos de creación de firma y sello electrónico (tarjetas inteligentes, módulos criptográficos HSM y firmas en servidor). Estas especificaciones son la base técnica ineludible para certificar los esquemas de seguridad de nivel "alto" que exige la arquitectura de la EUDI Wallet y los prestadores de servicios de confianza cualificados.
- Blockchain, EBSI e ISBE: el comité conjunto CEN/CENELEC JTC 19 (Blockchain and Distributed Ledger Technologies) adapta los estándares internacionales de ISO al marco europeo y desarrolla normativas propias, especialmente sobre privacidad y protección de datos en redes DLT. Estos estándares son la referencia para las redes públicas permisionadas que buscan validez legal en la UE: [EBSI](ebsi.md), la infraestructura de la Comisión y los Estados miembros para verificar credenciales de forma transfronteriza, e ISBE (Infraestructura de Servicios Blockchain de España), la red nacional alineada con EBSI. En ambos casos, cumplirlos es lo que permite garantizar la interoperabilidad, cumplir con el RGPD y articular la integración legal con los servicios eIDAS.
- Espacios de datos: el comité conjunto CEN/CENELEC JTC 25 (Data management, Dataspaces, Cloud and Edge), creado en septiembre de 2024, elabora las normas que concretan los requisitos de interoperabilidad del artículo 33 del Data Act por mandato de la Comisión.

Referencias:

- [Web de CEN y CENELEC](https://www.cencenelec.eu/)
- [Creación del comité JTC 25 (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2024/brief-news/2024-09-25-jtc-25/)
- [Aceptación del mandato del Data Act (CEN y CENELEC)](https://www.cencenelec.eu/news-events/news/2025/brief-news/2025-07-11-data-act-standardization-request/)

## ISO (International Organization for Standardization)

Organización Internacional de Normalización, con sede en Ginebra (Suiza). No es un organismo de la UE ni figura entre los reconocidos por el Reglamento (UE) 1025/2012: es una organización internacional independiente cuyos miembros son los organismos nacionales de normalización, como UNE en España.

Sus normas no obligan por sí mismas en la UE. Entran en el marco de eIDAS por dos vías:

- Cita directa en un acto de ejecución: el [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj) fija como referencia para los libros mayores electrónicos cualificados de variante distribuida las normas ISO 23257:2022 (arquitectura de referencia) e ISO/TS 23635:2022 (gobernanza), ambas del comité ISO/TC 307 (Blockchain and Distributed Ledger Technologies).
- Adaptación por los organismos europeos: el comité conjunto CEN/CENELEC JTC 19 adapta los estándares de ISO sobre blockchain y DLT al marco europeo.

Referencias:

- [Web de ISO](https://www.iso.org/)
- [ISO 23257:2022](https://www.iso.org/standard/75093.html)
- [ISO/TS 23635:2022](https://www.iso.org/standard/76480.html)
