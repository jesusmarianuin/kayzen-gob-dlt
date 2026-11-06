# Listas de confianza (TL y LOTL)

//TOOD: la provisión de EUDI Wallet no es un servicio de confianza según eIDAS2. Es una actividad regulada con régimen propio de supervisión y certificación.



Una lista de confianza (Trusted List, TL) es la lista oficial que publica cada Estado miembro con los prestadores cualificados de servicios de confianza (QTSP) de su país y los servicios cualificados que prestan, junto con su estado. La publica el órgano de supervisión competente, conforme al artículo 22 de eIDAS. Técnicamente se especifica como Trust Service Status List (TSL).

Las listas de los Estados miembros se agrupan en la List of Trusted Lists (LOTL), que publica la Comisión Europea y que enlaza a cada lista nacional. EUTL (EU Trusted List) es la denominación habitual para referirse a este conjunto, aunque el término técnico oficial es LOTL.

## Para qué sirven

Responden a una pregunta concreta: si un prestador o un servicio es cualificado. Quien recibe una firma, un sello o una declaración electrónica cualificada de atributos (QEAA) comprueba en la lista de confianza que su emisor es un prestador cualificado y que lo era en el momento de emitirla.

Se basan en certificados X.509: la lista asocia cada servicio cualificado con los certificados con los que firma.

## En la EUDI Wallet

//TODO LoTE (List of Trusted Entities): lista de entidades de confianza del ecosistema EUDI.

En el ecosistema de la EUDI Wallet, las listas de confianza cumplen el papel de decir al verificador qué emisores son de confianza. eIDAS2 extiende el mecanismo a otros actores del ecosistema, como los proveedores de PID y de wallets.

//¿Qué entidades están autorizadas o reconocidas como emisoras de PID y de atestaciones electrónicas (EAA, QEAA y PuB-EAA), y cómo se publica y verifica esa confianza?
el TIR es el registro gestionado por el Registrar nacional, pero no es el mecanismo completo de publicación de confianza.
//Definido por el ARF 2.8

Según el ARF 2.8:
- PID Providers: se registran y notifican a la Comisión; sus anclas de confianza se publican en la LoTE.
- QEAA Providers: sus anclas se incorporan a la Trusted List cuando obtienen el estatus cualificado. Asi es, una QEAA es un servicio de confianza, aunque no lo es la EUDI
- PuB-EAA Providers: se registran y notifican; sus anclas se publican en la LoTE.
- EAA no cualificadas: su registro depende de los mecanismos nacionales o sectoriales.

Es el equivalente en eIDAS al [registro de emisores de confianza (TIR) de EBSI](../identity.md#tir-trusted-issuers-registry), pero con valor legal y basado en certificados X.509 en lugar de DIDs.

Referencias:

- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)

## llevar esto a la tierra

//ll