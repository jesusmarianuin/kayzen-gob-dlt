# Declaración electrónica de atributos (EAA)

Una declaración electrónica de atributos es una manifestación electrónica firmada que acredita que un atributo de una persona física o jurídica es cierto (edad, titulación, permiso, cargo en una sociedad) sin tener que identificarla por completo. El término oficial en español es "declaración", no "atestación".

Complementa a los datos de identificación personal (PID) de la cartera EUDI. El PID responde a "¿quién eres?" y la declaración a "¿es cierto este dato sobre ti?". Así se puede demostrar que alguien es mayor de edad sin revelar su fecha de nacimiento, lo que se conoce como divulgación selectiva.

Emitirlas es uno de los servicios de confianza que define eIDAS2, como la firma, el sello o el [libro mayor electrónico](electronic-ledger.md). Por eso sigue el mismo esquema: puede prestarlo cualquier prestador de servicios de confianza, pero la ley solo le reconoce efectos reforzados cuando lo presta un prestador cualificado (QTSP).

## Quién la emite y qué valor tiene

Hay tres tipos, y lo que los distingue es quién la emite:

- EAA: cualquier prestador de servicios de confianza. No se le puede negar valor como prueba solo por ser electrónica.
- QEAA (cualificada): un QTSP, es decir, un prestador supervisado por el organismo nacional de supervisión, auditado por un organismo de evaluación de la conformidad y que figura en las [listas de confianza](trusted-lists.md). Equivale a una declaración en papel y se reconoce en toda la UE.
- PuB-EAA: un organismo público responsable de una fuente auténtica, o alguien en su nombre. No es un QTSP, pero el reglamento le exige garantías equivalentes. Equivale también a la declaración en papel.

La fuente auténtica es el registro oficial que custodia el dato, como el registro civil, el registro mercantil o el de la DGT. Si el atributo está en el anexo VI (dirección, edad, estado civil, nacionalidad, titulaciones, permisos, datos registrales...), el QTSP que emite una QEAA debe poder comprobarlo en esa fuente. La PuB-EAA no necesita esa comprobación porque la emite la propia fuente.

Para quien recibe una QEAA, esto se traduce en dos comprobaciones: la firma o el sello cualificado del QTSP que la emite, y que ese prestador figure en la lista de confianza con el servicio de declaraciones cualificadas.

## Formatos en la cartera EUDI

Para que la cartera pueda guardar y presentar una declaración, esta tiene que estar en un formato técnico concreto. El [ARF](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/main/05-data-model-and-data-exchange-protocols.md#54-technical-attestation-formats-and-proof-mechanisms) enumera tres:

- ISO/IEC 18013-5 (mdoc): el formato del carné de conducir móvil. La cartera debe admitirlo.
- SD-JWT VC: credencial en JSON con divulgación selectiva, definida en el IETF. La cartera también debe admitirlo.
- W3C VCDM 2.0: opcional y solo para EAA no cualificadas.

Por tanto, una QEAA o una PuB-EAA se emite en mdoc o en SD-JWT VC. El formato también condiciona el uso, porque en una presentación presencial (proximidad), por ejemplo enseñando el móvil en un mostrador, solo sirve mdoc.

> El ARF es una guía, no una norma, y prevé que W3C VCDM pueda pasar a ser obligatorio cuando ETSI publique perfiles para ese formato. Su relación con los actos de ejecución se explica en [actos de ejecución de eIDAS2](implementing-acts.md).

## Normativa que la regula

Su régimen está en los [artículos 45 ter a 45 nonies del Reglamento eIDAS modificado (45b a 45h en inglés) y en los anexos V a VII](https://inza.blog/category/declaraciones-electronicas-de-atributos/).

Lo desarrollan los [actos de ejecución de la cartera](implementing-acts.md#cartera-eudi), sobre todo el [Reglamento de Ejecución (UE) 2024/2977](https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX:32024R2977), sobre PID y declaraciones expedidas a la cartera, y el [2026/1735](https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX:32026R1735), sobre declaraciones cualificadas. Como el emisor de una QEAA es un QTSP, también le aplican los actos de ejecución comunes a todos los prestadores cualificados. Los requisitos técnicos se completan con normas de [ETSI](standardization-bodies.md#etsi-european-telecommunications-standards-institute) y [CEN](standardization-bodies.md#cen-y-cenelec).

En septiembre de 2026 había todavía pocos prestadores de QEAA en las [listas de confianza](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls).

## Referencias

- [Reglamento (UE) 2024/1183 (eIDAS2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento (UE) 910/2014, versión consolidada tras eIDAS2, en EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018)
- [Architecture and Reference Framework (ARF) de la cartera EUDI](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework)
- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [Qué son las declaraciones electrónicas de atributos EAA, QEAA y PuB-EAA en eIDAS2 (inza.blog)](https://inza.blog/2026/09/20/que-son-las-declaraciones-electronicas-de-atributos-eaa-qeaa-y-las-del-sector-publico-pub-eaa-en-eidas2/)
