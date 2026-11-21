# Encoding european citizens’ identity numbers: from qualified certificates to the EUDI Wallet PID

Post: <https://inza.blog/2026/10/24/encoding-citizens-identity-numbers-from-qualified-certificates-to-the-eudi-wallet-pid/>

Fecha: 2026-10-24

El post, en inglés, actualiza un artículo de 2022 sobre la [codificación de los números de identidad de los ciudadanos de la UE en los certificados](https://inza.blog/2022/12/11/codificacion-de-los-numeros-de-identidad-de-los-ciudadanos-de-la-union-europea-en-los-certificados/). Su tesis es que, mientras el atributo personal_administrative_number siga siendo opcional en el PID de la cartera europea, el cotejo transfronterizo de identidades y la emisión de certificados cualificados serán menos fiables para los ciudadanos de Alemania, Francia, Austria y otros Estados.

El contenido del PID lo fija el [Reglamento de Ejecución (UE) 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj), cuyo anexo sustituyó el [Reglamento de Ejecución (UE) 2026/1731](https://eur-lex.europa.eu/eli/reg_impl/2026/1731/oj). Son obligatorios el nombre, los apellidos, la fecha y el lugar de nacimiento, la nacionalidad y la fotografía, salvo que el usuario no la incluya. El número administrativo personal es opcional y debe ser único entre los que emite el mismo proveedor de PID. El document_number identifica el PID como documento, no a la persona.

En los certificados cualificados, el [Reglamento de Ejecución (UE) 2025/1943](https://eur-lex.europa.eu/eli/reg_impl/2025/1943/oj) toma como referencia la norma [ETSI EN 319 412-1 V1.6.1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf). El identificador de la persona física va en el atributo serialNumber con un prefijo de tipo, el código de país y el número: PAS para pasaporte, IDC para documento de identidad, PNO para número personal nacional, TIN para identificador fiscal y EID, nuevo en esta versión, para identificadores del esquema de identificación electrónica. En las personas jurídicas, NTR puede llevar ya el EUID de los registros mercantiles europeos, por ejemplo NTRES-ES28065.080862918.

Cuando un prestador emite un certificado a partir del PID, el prefijo depende de lo que traiga el PID. Si no trae número personal, solo queda el del documento, que cambia con cada renovación.

Según los modelos del registro [PRADO](https://www.consilium.europa.eu/prado/en/prado-start-page.html), Alemania, Austria y Francia solo imprimen un número de documento que cambia al renovarlo. Luxemburgo tiene un número nacional que no aparece en la tarjeta, e Irlanda y Dinamarca no tienen tarjeta de identidad. El [Reglamento (UE) 2025/1208](https://eur-lex.europa.eu/eli/reg/2025/1208/oj) armoniza las tarjetas, pero solo el número de documento de la zona de lectura mecánica. Incluso en el DNI español esa zona lleva el número de soporte, y el número permanente va en el campo de datos opcionales.

El [Reglamento de Ejecución (UE) 2025/846](https://eur-lex.europa.eu/eli/reg_impl/2025/846/oj) sobre cotejo de identidades funciona bien con un número estable. Sin él, hay que recurrir al nombre, la fecha y el lugar de nacimiento y la nacionalidad, que no son únicos.

El autor recomienda:

- A los Estados y proveedores de PID: incluir el número permanente aunque no figure en la tarjeta, asignar uno estable cuando no exista y no usar nunca el número del documento
- A los prestadores de servicios de confianza: usar EID cuando el número venga del esquema y documentar su origen en la política de certificación
- A las partes usuarias: prever un cotejo menos fiable

Propone también reforzar el rulebook del PID para que el número estable sea obligatorio cuando exista. Para personas jurídicas remite a [el EUID necesario para los certificados QSEAL de EPREL](https://inza.blog/2025/02/02/el-euid-de-empresa-es-necesario-para-solicitar-certificados-qseal-para-eprel/) y a [los actos de ejecución de eIDAS2 al día](https://inza.blog/2026/08/30/los-actos-de-ejecucion-de-eidas2-al-dia-y-las-normas-etsi-y-cen-que-citan-the-eidas2-implementing-acts-up-to-date-and-the-etsi-and-cen-standards-they-cite/).

En una frase: sin un número personal estable obligatorio en el PID, el cotejo transfronterizo y la emisión de certificados cualificados quedan en desventaja para los ciudadanos de los países que no lo tienen.

---
