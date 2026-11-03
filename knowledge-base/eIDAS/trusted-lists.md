# Listas de confianza (TL y LOTL)

Una lista de confianza (Trusted List, TL) es la lista oficial que publica cada Estado miembro con los prestadores cualificados de servicios de confianza (QTSP) de su país y los servicios cualificados que prestan, junto con su estado. La publica el órgano de supervisión competente, conforme al artículo 22 de eIDAS. Técnicamente se especifica como Trust Service Status List (TSL).

Las listas de los Estados miembros se agrupan en la List of Trusted Lists (LOTL), que publica la Comisión Europea y que enlaza a cada lista nacional. EUTL (EU Trusted List) es la denominación habitual para referirse a este conjunto, aunque el término técnico oficial es LOTL.

## Para qué sirven

Responden a una pregunta concreta: si un prestador o un servicio es cualificado. Quien recibe una firma, un sello o una declaración electrónica cualificada de atributos (QEAA) comprueba en la lista de confianza que su emisor es un prestador cualificado y que lo era en el momento de emitirla.

Se basan en certificados X.509: la lista asocia cada servicio cualificado con los certificados con los que firma.

## En la EUDI Wallet

En el ecosistema de la EUDI Wallet, las listas de confianza cumplen el papel de decir al verificador qué emisores son de confianza. eIDAS2 extiende el mecanismo a otros actores del ecosistema, como los proveedores de PID y de wallets.

Es el equivalente en eIDAS al [registro de emisores de confianza (TIR) de EBSI](../identity.md#tir-trusted-issuers-registry), pero con valor legal y basado en certificados X.509 en lugar de DIDs.

Referencias:

- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
