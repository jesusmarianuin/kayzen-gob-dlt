cosas por saber


- vocabulario eIDAS eIDAS, electronic IDentification, Authentication and trust Services
    https://es.wikipedia.org/wiki/EIDAS
    - EUTL (European Union Trusted Lists) 
- ETSI https://es.wikipedia.org/wiki/Instituto_Europeo_de_Normas_de_Telecomunicaciones
- CEN/CENELEC → estándares europeos formales.

- que es GAID
- que es https://dssc.eu/
    su trabajo es ser una especie de secretaría técnica/normativa para los "espacios de datos europeos" — que son los sistemas mediante los cuales sectores enteros (salud, agricultura, movilidad, Green Deal...) se supone que van a compartir datos entre empresas y administraciones de forma "soberana, interoperable y de confianza", en vez de que cada sector monte su propio Frankenstein incompatible.
    En la práctica, lo que producen es:

    El DSSC Blueprint: una guía/estándar de cómo debería construirse un "data space" (piezas legales, técnicas, de gobernanza...).
    El DSSC Toolbox: catálogo de componentes software que implementan esas piezas.
    El Glosario: para que todo el mundo llame igual a las mismas cosas.
    La Data Spaces Radar / Observatory: mapa de qué iniciativas de espacios de datos existen por Europa.
    Reciente hito: su investigación sobre madurez de espacios de datos comunes europeos se ha convertido en un estándar europeo formal. 

    El Blueprint de DSSC menciona explícitamente blockchain/ledgers como uno de los "building blocks" posibles para la capa de confianza de un espacio de datos — literalmente lo llama "Electronic Ledgers": servicios que permiten almacenar datos de forma inmutable, incluyendo tecnologías como distributed ledgers y blockchain. EBSI es el candidato obvio de la UE para cubrir ese building block cuando un espacio de datos necesita verificar credenciales o identidad entre participantes de distintos países. 

    en arquitecturas de identidad soberana (SSI) para espacios de datos, el patrón típico es: el "credential trust triangle" se apoya en un Verifiable Data Registry implementado a través de la blockchain de EBSI. O sea, si un espacio de datos quiere emitir/verificar credenciales de forma descentralizada, EBSI hace de registro de confianza subyacente.
    https://www.sciencedirect.com/science/article/pii/S2352340926002210
    https://www.sciencedirect.com/science/article/pii/S2352340926002210

    A nivel de ecosistema, ambos aparecen listados como iniciativas hermanas del mismo universo: Gaia-X, IDSA, FIWARE, BDVA, DSSC, SIMPL, EBSI, entre otras, avanzan en paralelo, a veces solapándose en alcance y resultados

IDSA
    IDSA = el estándar técnico de facto (protocolo DSP, modelo de referencia, certificación de conectores) — viene desde 2016, independiente de la financiación europea puntual.
    DSSC = el proyecto financiado por la Comisión (2022-2029) que coge ese trabajo técnico de IDSA (y de Gaia-X, FIWARE...) y lo convierte en un Blueprint/glosario/toolbox oficial "paraguas", coordinando que todos los espacios de datos sectoriales (salud, agricultura, movilidad...) usen las mismas piezas en vez de reinventar la rueda cada uno.
    Muestra de ese matrimonio: el Blueprint del DSSC recomienda usar el Dataspace Protocol de IDSA (con ODRL como lenguaje de políticas) para el intercambio real de datos entre participantes, y IDSA aloja/mantiene herramientas como el Data Spaces Radar con contribuciones de la comunidad del DSSC.

volver a recupear
    redes p2p revisado, pero con efoque en modelo gobernanza y hablamos bien que es eso de federado