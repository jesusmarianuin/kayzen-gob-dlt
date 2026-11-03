# eIDAS

## eIDAS (electronic IDentification, Authentication and trust Services)

Reglamento (UE) relativo a la identificación electrónica, autenticación y los servicios de confianza para las transacciones electrónicas en el mercado interior (de los estados miembro como personas, bienes, servicios o capitales). Se aplica en toda la UE desde el 1 de julio de 2016.

Por una parte, permite el reconocimiento de sistemas nacionales de identificación electrónica (eID), incluyendo los procesos de autenticación asociados, notificados por los Estados miembros. Por ejemplo, DNI electrónico es reconocido como sistema de identificación electrónica.

Define que por estado miembro existen los **servicios de confianza**, que es un servicio electrónico que permite realizar determinadas operaciones relacionadas con la confianza en transacciones electrónicas y que está regulado, como puede ser la firma, sello de tiempo electrónicos (TSA), entrega electrónica certificada (ERDS o Qualified Electronic Registered Delivery Service) y certificados de autenticación de sitios web.

Un servicio de confianza, tiene un **Prestador de Servicios de Confianza** (TSP Trust Service Provider) que es la entidad que presta dichos servicios.

Los prestadores de servicios de confianza pueden obtener la categoría de **Prestadores Cualificados de Servicios de Confianza** (*Qualified Trust Service Provider*, QTSP). Para ello, deben cumplir los requisitos previstos en el Reglamento eIDAS y contar con el reconocimiento formal del órgano de supervisión competente de su país, el cual los incluye en la [**lista de confianza**](trusted-lists.md) del Estado miembro correspondiente (*Trusted List*, TL, especificada técnicamente como *Trust Service Status List*, TSL).

A su vez, las listas de cada Estado miembro (TL/TSL) se engloban centralmente en la *List of Trusted Lists* (LOTL). Al respecto, *EUTL (EU Trusted List)* es la denominación funcional y divulgativa habitual para referirse a esta infraestructura europea, mientras que la terminología técnica oficial bajo eIDAS y los estándares ETSI utiliza la sigla **LOTL**.

Estos servicios pueden ser **servicios cualificados**, es decir, servicios que cumplen los requisitos establecidos por eIDAS para una determinada categoría y que son prestados por un prestador cualificado (QTSP).

**Aclaraciones**:

Un TSP puede prestar servicios a ciudadanos, empresas, organizaciones o administraciones públicas.

Una **firma electrónica cualificada** tiene, conforme al artículo 25 de eIDAS, un efecto jurídico equivalente al de una firma manuscrita.

"Cualificado" es un atributo que se aplica a diferentes elementos en distintos contextos. Por ejemplo, pueden ser cualificados un prestador o un servicio de confianza, un certificado electrónico o un dispositivo de creación de firma. En el caso de una firma electrónica, existen distintos niveles (simple, avanzada y cualificada), siendo la firma cualificada aquella que cumple los requisitos adicionales de eIDAS, incluyendo el uso de un certificado cualificado y un dispositivo cualificado de creación de firma.

### Referencias de eIDAS

- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)

## eIDAS2

eIDAS2 establece un nuevo marco europeo de identidad digital.

> Se puede valorar que existe un [cambio de paradigma](../idea-sandbox/decentralization-paradox-idea.md).

Su objetivo principal es evolucionar desde un sistema centrado en el reconocimiento mutuo de sistemas nacionales de identificación electrónica hacia un ecosistema europeo de identidad digital interoperable, donde los ciudadanos y organizaciones puedan utilizar una identidad digital reconocida en toda la Unión Europea.

La principal novedad es la creación de la Cartera Europea de Identidad Digital (European Digital Identity Wallet, EUDI Wallet).

### Nuevos servicios de confianza

eIDAS2 amplía la lista de servicios de confianza regulados, incorporando:

[**Declaración electrónica de atributos (*Electronic Attestation of Attributes, EAA*)**](electronic-attestation-of-attributes.md):

Permite emitir y verificar atributos electrónicos sobre una persona o entidad. Un atributo es una información asociada a una identidad como edad, titulación académica, permiso profesional, condición de estudiante, etc.

Permite que estos datos puedan ser utilizados de forma confiable en transacciones electrónicas.

[**Archivo electrónico (*Electronic Archiving*)**](electronic-archiving.md):

Introduce el servicio de archivo electrónico. Su finalidad es garantizar la conservación de documentos electrónicos durante largos periodos asegurando: integridad, autenticidad, origen, disponibilidad.

Está orientado a conservar evidencias digitales con valor jurídico.

[**Libros mayores electrónicos (*Electronic Ledger*)**](electronic-ledger.md):

Introduce los libros mayores electrónicos como servicio de confianza.

Un libro mayor electrónico es una secuencia de registros de datos que garantiza su integridad y la exactitud de su orden cronológico. El reglamento no exige una tecnología concreta: puede implementarse con o sin blockchain.

### Plazos de aplicación de la cartera europea

- 24 de diciembre de 2026: cada Estado miembro debe poner a disposición al menos una cartera europea, y las administraciones públicas deben aceptarla como medio de identificación. Es el plazo de emisión y aceptación por el sector público, no de adopción generalizada
- 24 de diciembre de 2027: el sector privado regulado (banca, telecomunicaciones, energía, transporte, sanidad, seguros, educación e infraestructura digital) debe aceptarla cuando la normativa le exija autenticación reforzada

### Referencias de eIDAS2

- [Reglamento (UE) 910/2014 (eIDAS) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [Reglamento eIDAS (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eidas-regulation)
- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)

## Cartera Europea de Identidad Digital (EUDI Wallet)

La IDUE (Identidad Digital de la Unión Europea) conocida como [la Cartera Europea de Identidad Digital (EUDI Wallet)](eudi-wallet.md) es una aplicación digital segura y controlada por el usuario que permite gestionar, almacenar y utilizar su identidad digital y otras credenciales electrónicas verificables en sus interacciones con servicios públicos y privados, tanto a nivel nacional como transfronterizo dentro de la Unión Europea.

La cartera forma parte de un ecosistema europeo de identidad digital en el que intervienen diferentes actores, entre ellos los usuarios, los proveedores que emiten datos de identidad y credenciales electrónicas, los proveedores de la cartera y las entidades que solicitan y verifican dichas credenciales. Este ecosistema se basa en mecanismos comunes de interoperabilidad, seguridad y confianza.

Entre sus principales capacidades se encuentran:

- Identificación y autenticación electrónica frente a servicios públicos y privados.
- Almacenamiento y gestión de datos de identidad y credenciales digitales verificables.
- Presentación de credenciales para demostrar determinados atributos ante terceros.
- Interoperabilidad transfronteriza, permitiendo utilizar la identidad y las credenciales en diferentes Estados miembros.
- Firma electrónica, como [firma cualificada (QES)](https://www.e-signature.eu/en/eidas-2-electronic-signature/#:~:text=*%20QES%20via%20smartphone%20(software%20QSCD)%20becomes,and%20compliant%20during%20and%20after%20the%20transition.), en los casos y condiciones previstos por el marco europeo.
- Control por parte del usuario sobre la información que comparte, permitiendo proporcionar únicamente los datos necesarios para una determinada operación.

Las credenciales digitales pueden ser emitidas por autoridades públicas y entidades privadas para acreditar atributos de personas físicas o jurídicas, como datos de identidad, permisos de conducción, titulaciones académicas o cualificaciones profesionales. En el marco europeo de identidad digital, pueden adoptar la forma de [declaraciones electrónicas de atributos](electronic-attestation-of-attributes.md) cualificadas o no cualificadas, sujetas a distintos requisitos y efectos jurídicos conforme al Reglamento eIDAS. Los casos de uso incluyen el acceso a servicios públicos y privados, la apertura de cuentas bancarias, los pagos, la firma de contratos, los viajes, la educación y la seguridad social, de acuerdo con la normativa aplicable.

Un principio especialmente relevante de la EUDI Wallet es la **minimización de datos**. Por ejemplo, para demostrar que una persona cumple un requisito de edad, no necesariamente tendría que revelar su fecha de nacimiento completa: podría presentar una prueba verificable de que **es mayor de 18 años**, evitando revelar información adicional que no sea necesaria para la operación.

Por tanto, la EUDI Wallet no debe entenderse simplemente como una versión digital de un documento de identidad, sino como una **infraestructura de identidad y credenciales digitales controlada por el usuario**, diseñada para permitir que diferentes entidades puedan emitir, solicitar y verificar información digital de forma segura e interoperable en toda la Unión Europea.

Su arquitectura y requisitos técnicos se definen en el **European Digital Identity Wallet Architecture and Reference Framework (ARF)**, desarrollado en el marco del Reglamento Europeo de Identidad Digital. El ARF establece la arquitectura, los componentes, las interacciones y los mecanismos de confianza necesarios para que las diferentes implementaciones nacionales sean interoperables.

### Referencias

- [European Digital Identity Wallet — Architecture and Reference Framework](https://eudi.dev/latest/main/01-introduction/?utm_source=chatgpt.com#11-eudi-wallet-ecosystem)
- [Comisión Europea — Aplicación de la cartera de identidad digital de la UE](https://digital-strategy.ec.europa.eu/es/policies/eudi-wallet-implementation)
