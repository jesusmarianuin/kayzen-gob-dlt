# Listas de confianza (TL y LOTL)

Una lista de confianza (Trusted List, TL) es la lista oficial que publica cada Estado miembro con los prestadores cualificados de servicios de confianza (QTSP) de su país y los servicios cualificados que prestan, junto con su estado. Pueden incluir también, de forma voluntaria, prestadores y servicios no cualificados. La publica el organismo que designa cada Estado, conforme al artículo 22 de eIDAS. Técnicamente se especifica como Trust Service Status List (TSL).

Las listas de los Estados miembros se agrupan en la List of Trusted Lists (LOTL), que publica la Comisión Europea y que enlaza a cada lista nacional. EUTL (EU Trusted List) es la denominación habitual para referirse a este conjunto, aunque el término técnico oficial es LOTL.

## Para qué sirven

Responden a una pregunta concreta: si un prestador o un servicio es cualificado. Quien recibe una firma, un sello o una declaración electrónica cualificada de atributos (QEAA) comprueba en la lista de confianza que su emisor es un prestador cualificado y que lo era en el momento de emitirla.

Se basan en certificados X.509. La lista asocia cada servicio cualificado con los certificados con los que firma.

## En la EUDI Wallet

En el ecosistema de la EUDI Wallet, el verificador necesita saber qué emisores son de confianza. Las TL solo cubren a quienes prestan un servicio de confianza cualificado, y en este ecosistema hay actores que no lo son, como los proveedores de PID o de wallets (la provisión de wallets tiene su propio régimen de certificación y supervisión). Para ellos, eIDAS2 añade las listas de entidades de confianza (List of Trusted Entities, LoTE), que publica la Comisión a partir de lo que le notifican los Estados miembros.

Según el ARF 2.8, cada tipo de emisor publica su confianza así:

- Proveedores de PID: el Estado miembro los registra y los notifica a la Comisión, que publica sus anclas de confianza en una LoTE.
- Proveedores de QEAA: sus anclas entran en la TL de su país cuando obtienen el estatus cualificado, porque emitir QEAA sí es un servicio de confianza cualificado.
- Proveedores de PuB-EAA: se registran y notifican igual que los de PID, y sus anclas se publican en una LoTE.
- Proveedores de EAA no cualificadas: no hay una lista común, su confianza depende de mecanismos nacionales o sectoriales.

Registrar una entidad no basta para que un verificador confíe en ella. El registro es el trámite administrativo ante el Estado miembro; lo que el verificador consulta es la lista publicada, TL o LoTE, con los certificados de cada emisor. Los proveedores de wallets también tienen su LoTE, que el proveedor de PID consulta para comprobar que la wallet es auténtica antes de emitir.

Es el equivalente en eIDAS al [registro de emisores de confianza (TIR) de EBSI](../identity.md#tir-trusted-issuers-registry), pero con valor legal y basado en certificados X.509 en lugar de DIDs.

## Ejemplo práctico

Una ciudadana española abre una cuenta en un banco alemán desde su EUDI Wallet.

1. El banco le pide su identidad y la wallet presenta el PID, firmado por el proveedor de PID español. El banco busca ese proveedor en la LoTE de proveedores de PID, encuentra su certificado y comprueba la firma.
2. El banco le pide también su título universitario, emitido como QEAA por un prestador cualificado español. Esta vez el banco va a la LOTL, de ahí salta a la TL española y comprueba que el prestador era cualificado cuando emitió la declaración.
3. Si el título fuera una EAA no cualificada, el banco no tendría una lista común donde mirar y dependería de los acuerdos del sector educativo.

En ningún paso el banco necesita conocer de antemano al emisor. Le basta con fiarse de las listas.

## Cómo se valida técnicamente

Las listas son ficheros que cualquier programa puede descargar y leer. Las TL y la LOTL son ficheros XML con un formato común definido por el estándar ETSI TS 119 612. Gracias a ese formato común, un verificador interpreta igual la lista de cualquier Estado miembro. Las LoTE usan otro formato, ETSI TS 119 602, y hay una lista por cada tipo de entidad, por ejemplo una para proveedores de PID y otra para proveedores de wallets.

Todas las listas van firmadas. Así, quien las consulta puede comprobar que nadie las ha alterado y que las publicó quien dice publicarlas.

Quien recibe algo firmado por un prestador cualificado, como un documento con firma cualificada o una QEAA que le presenta una wallet, actúa como verificador y comprueba al emisor siguiendo estos pasos:

- Descarga la LOTL. Su dirección oficial la publica la Comisión en el Diario Oficial de la UE, así que el verificador sabe que está descargando la buena.
- Comprueba la firma de la LOTL antes de fiarse de su contenido.
- En la LOTL busca el enlace a la TL del país del emisor, la descarga y comprueba también su firma.
- En esa TL busca el certificado con el que se hizo la firma. Si aparece, sabe qué prestador y qué servicio lo emitieron.
- Revisa el historial de ese servicio. Las listas guardan cuándo un servicio obtuvo o perdió el estatus de cualificado, y lo que importa es que lo fuera en la fecha de la firma, no hoy.

Con las LoTE el recorrido es más corto. No hay una lista de listas por medio, así que el verificador va directamente a la lista del tipo de entidad que le interesa.

## Referencias

- [Buscador de prestadores y servicios de confianza de la UE (EU Trust Services Dashboard)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [Reglamento (UE) 2024/1183 (eIDAS 2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento de Ejecución (UE) 2024/2980 sobre las notificaciones del ecosistema de la cartera](https://eur-lex.europa.eu/eli/reg_impl/2024/2980/oj)
