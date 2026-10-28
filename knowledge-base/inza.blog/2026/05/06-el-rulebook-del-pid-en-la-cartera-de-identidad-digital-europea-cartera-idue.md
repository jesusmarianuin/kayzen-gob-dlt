# El "rulebook" del PID en la Cartera de Identidad Digital Europea (Cartera IDUE)

Post: <https://inza.blog/2026/05/06/el-rulebook-del-pid-en-la-cartera-de-identidad-digital-europea-cartera-idue/>

Fecha: 2026-05-06

Un rulebook es un documento técnico del [ARF](https://inza.blog/2025/11/15/arf-2-7-2-arquitectura-y-marco-de-referencia-de-la-cartera-idue/) que fija los requisitos de un tipo de declaración de atributos. No es vinculante, pero es necesario para la interoperabilidad y la certificación. El PID Rulebook (anexo 3.01) define cómo se estructura, codifica, emite y valida el PID, a partir del [CIR 2024/2977](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-81789):

- Espacio de nombres europeo `eu.europa.ec.eudi.pid.1` y espacios nacionales, como `eu.europa.ec.eudi.pid.es.1`
- Atributos obligatorios (apellidos, nombre, fecha de nacimiento y metadatos de emisión) y opcionales (edad, domicilio, nacionalidad...), descritos en [CDDL](https://www.rfc-editor.org/rfc/rfc8610)
- Doble formato: mdoc ISO/IEC 18013-5 sobre [CBOR](https://www.rfc-editor.org/rfc/rfc8949) para uso presencial y [SD-JWT VC](https://www.rfc-editor.org/rfc/rfc9901) para uso en línea
- Emisión por OpenID4VCI, emisores en listas de confianza según [ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) y activación a nivel alto

El reto principal es la carga inicial del PID con nivel alto de seguridad. En España se espera que la FNMT sea el proveedor del PID, y la vía más directa sería leer el DNIe por NFC con verificación facial según [ETSI TS 119 461](https://www.etsi.org/deliver/etsi_ts/119400_119499/119461/02.01.01_60/ts_119461v020101p.pdf). El número de DNI iría en un atributo opcional. La app tendría que superar la [certificación de ENISA](../04/04-enisa-anticipa-el-borrador-de-la-norma-de-evaluacion-de-las-carteras-de-identidad-digital-de-la-ue.md), posiblemente a través de Lince.

En una frase: el PID Rulebook fija atributos, formatos y emisión del PID, y en España su carga inicial pasaría por leer el DNIe con el móvil.

---
