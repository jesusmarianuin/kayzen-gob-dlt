# ZK en EBSI e ISBE: soluciones y límites para un nodo o servicio nacional

**Borrador técnico — 12/11/2026.** Síntesis completa de los puntos tratados. **Foco institucional**, no identidad del ciudadano. Se diferencian hechos publicados, propuestas técnicas y cuestiones sin respuesta oficial.

## 1. Problema y objetivo

- **Pregunta:** ¿por qué EBSI e ISBE (infraestructuras basadas en Hyperledger Besu) no ofrecen de forma general una capacidad ZK, qué se lo impide y qué han declarado al respecto?
- **Escenario:** una administración o **servicio conectado a un nodo nacional** prueba condiciones sobre expedientes, registros, firmas, autorizaciones o cálculos **sin distribuir los datos de origen por toda la red**.
- **No confundir**: (a) probar una afirmación sobre datos privados, (b) ocultar el contenido de transacciones, (c) ocultar metadatos/relaciones, (d) anonimizar un tratamiento a efectos del RGPD. Son metas distintas.
- **Distinción de roles:** un nodo Besu replica y valida bloques; el **probador ZK** normalmente es un componente aplicativo del operador nacional, no una extensión de QBFT.

## 2. Soluciones viables y sus límites (lo principal)

| Solución | Qué aporta y cómo se integra | Limitación crítica | Encaje propuesto |
|---|---|---|---|
| **A. Longfellow-ZK / Frigo–Shelat sobre ECDSA P-256** | El servicio nacional prueba atributos sobre un documento/credencial **ya firmado**; el emisor puede conservar ECDSA P-256. Verificación preferentemente **fuera de cadena**; Besu ofrece registro de confianza y anclajes mínimos. | No sirve automáticamente para cualquier documento ECDSA: hacen falta **formato de datos y circuitos compatibles**, validación de cadena de confianza y estado/revocación. No convierte la red en privada; verificación directa en EVM no está acreditada aquí como eficiente. | **Piloto prioritario si existen datos institucionales ya firmados de forma compatible.** |
| **B. SNARK específico (Groth16 / PLONK u otro) + verificador Solidity** | El servicio nacional computa una prueba sobre una relación acordada; el contrato EVM la verifica y **todos los nodos validan el mismo resultado**, sin ver los datos testigo. | Circuito y entradas públicas deben modelarse cuidadosamente. Coste de desarrollo/auditoría; primitivas EVM, gas, tamaños; *trusted setup* según esquema. No certifica la veracidad de la fuente de datos. | Cuando la **verificación descentralizada on-chain sea requisito explícito**. |
| **C. Verificación ZK off-chain + compromiso/resultado mínimo on-chain** | Un verificador institucional o conjunto de verificadores comprueba la prueba y registra compromiso, estado o atestación mínima. Reduce carga EVM y replicación. | El resto de la red no valida por sí mismo la prueba si recibe solo el «OK»; debe confiar en el verificador, poder auditar la prueba conservada o exigir firmas/quórum verificables. Riesgos de correlación en anclajes. | **Despliegue inicial más sencillo**, si se acepta su modelo de confianza. |
| **D. Datos off-chain + compromisos con ocultación + ZK de pertenencia/estado** | Permite demostrar pertenencia a un registro, estado válido, elegibilidad o cumplimiento sin publicar expedientes. Puede usar árboles de Merkle, compromisos ocultantes y acumuladores. | Un **hash ordinario** de datos predecibles puede permitir ataques de diccionario; incluso un compromiso puede ser correlacionable. Requiere sal/aleatoriedad, gestión de testigos, actualización, revocación y diseño de revelación mínima. | Registros y estados administrados por autoridades nacionales. |
| **E. Privacidad transaccional completa** | Circuitos, compromisos/nullifiers, ocultación de importes/destinatarios y posible capa/rollup o sistema privado específico. | **Longfellow por sí solo no la proporciona**. Cambia arquitectura, modelo de estado, monitorización, gobernanza, operación y posiblemente compatibilidad con aplicaciones existentes. | Solo si hay un requisito de **confidencialidad de transacciones**, no meramente de credenciales. |
| **F. Mantener solo datos fuera de cadena, sin ZK** | Evita replicar datos personales; contratos registran únicamente eventos o estados no sensibles. | Si los otros participantes deben **comprobar por sí mismos** una condición sin ver las evidencias, una simple afirmación firmada requiere confiar en el emisor. ZK añade verificabilidad de la relación computada. | Línea base con la que comparar el valor adicional de ZK. |

### Arquitectura institucional de referencia

```text
Sistemas administrativos nacionales (datos y expedientes privados)
       │ datos + autenticidad de origen + vigencia
       ▼
Servicio probador nacional (circuito, testigo, claves, prueba ZK)
       │ prueba + entradas públicas mínimas + versión del circuito
       ├── A: servicio verificador off-chain / quórum ──► anclaje mínimo
       └── B: contrato verificador en Besu ────────────► estado mínimo
                                                       │
                                              EBSI / ISBE (QBFT)
                                         demás nodos no ven expediente
```

**Regla fundamental:** ZK demuestra únicamente que **existe un testigo que satisface la relación programada**, no que un expediente administrativo sea auténtico, actualizado, legal o correcto. Estas propiedades requieren firmas verificadas dentro del circuito o fuera con un modelo de confianza explícito, fuentes autorizadas, marcas de vigencia y procedimientos de control.

### Ejemplos concretos

1. **Empresa habilitada:** probar registro válido + condición de solvencia sin exponer balances ni número de expediente. **Límites:** confianza en emisor del registro, actualización, revocación, identificación de la empresa si la operación exige identificarla.
2. **Comprobación reglamentaria:** demostrar que un conjunto de reglas aprobadas se evaluó sobre datos comprometidos. **Límites:** integridad de esos datos, definición jurídica de las reglas y cambios normativos.
3. **Cálculo interadministrativo:** demostrar un cálculo correcto sobre cifras confidenciales. **Límites:** circuitos complejos, aritmética, origen de datos, redondeos y costes de generación.
4. **Registro compartido de autorizaciones:** prueba de pertenencia/no revocación. **Límites:** actualizaciones de árbol/acumulador, correlabilidad del identificador y pruebas obsoletas.

## 3. Frigo–Shelat, Longfellow y Google: qué obstáculos eliminan

- **Frigo–Shelat, _Anonymous Credentials from ECDSA_**, referencia **[Fri2024]**, citada en el **Topic G del EUDI Wallet ARF** (la localización exacta depende de la versión). Permite construir pruebas privadas sobre firmas **ECDSA P-256 existentes**. **No exige por ese motivo migrar a BBS+ ni sustituir los chips seguros de los teléfonos.**
- **Longfellow-ZK** implementa la familia de protocolos y existe una especificación IRTF/CFRG: borrador de **19/10/2026**, *draft-irtf-cfrg-longfellow-00* ([enlace](https://www.ietf.org/ietf-ftp/internet-drafts/draft-irtf-cfrg-longfellow-00.html)). Su especificación y circuito siguen sujetos a evolución; un borrador IETF/IRTF **no es estándar final**.
- **Google Wallet** soporta presentación ZK en formato **`mso_mdoc_zk`**, con sistema **`longfellow-libzk-v1`** y validación mediante su biblioteca/servicio de verificación, según [documentación oficial](https://developers.google.com/wallet/identity/verify/accepting-ids-from-wallet-online). Google anunció aplicación de ZK a edad con **Bumble** en 2025 ([anuncio](https://blog.google/products-and-platforms/platforms/google-pay/google-wallet-age-identity-verifications/)). La especificación europea de verificación de edad de julio de 2026 incluye datos sobre uso, revisiones externas e implementación compatible en Rust ([anexo B](https://docs.ageverification.dev/av-doc-technical-specification/docs/annexes/annex-B/annex-B-zkp/)).
- El **02/09/2026**, Google anunció la transferencia de la biblioteca Longfellow a un proyecto bajo Linux Foundation Europe, un avance de gobernanza abierta, **no prueba de estandarización final** ([fuente](https://blog.google/products-and-platforms/platforms/google-pay/zero-knowledge-proof-library-linux-foundation/)).
- Consecuencia: ya **no bastan** como rechazo genérico ni «ZK necesita sustituir hardware de los emisores/teléfonos» ni «solo existe sobre el papel». **Pero Google valida un caso de presentación de credenciales fuera de blockchain**: no certifica coste de verificación Longfellow en EVM/Besu ni la aplicabilidad directa a todo registro administrativo.
- Para **un nodo nacional**, limitaciones de batería, chip o UX móvil son marginales. Importan más interoperabilidad, verificación distribuida, coste, semántica, fuentes y gobernanza.

## 4. EBSI e ISBE: estado y decisiones observables

| Aspecto | EBSI | ISBE |
|---|---|---|
| Arquitectura descrita | Ledger para **registros de confianza** y elementos verificables; credenciales y datos de usuario en general **fuera de cadena** | Red institucional Besu/QBFT con **Cliente ISBE / Filtering Proxy** y restricciones de operaciones y acceso |
| Estrategia de privacidad tratada | Minimización de datos registrados; divulgación selectiva en ecosistema de credenciales (p. ej. SD-JWT, que **no garantiza unlinkability** por sí mismo) | **Filtrado** y llamado **borrado lógico** de acceso; ciertas funciones de divulgación selectiva de wallet constaban pendientes en documentación consultada (verificar versión actual) |
| Riesgo residual | Metadatos on-chain, correlaciones, y que una afirmación de entidad pueda requerir confianza si no se verifica criptográficamente | Los datos pueden **seguir replicados físicamente** aunque una interfaz impida consultarlos; comprobar acceso directo, respaldos, históricos y operadores |
| Qué falta esclarecer | Motivo oficial para no ofrecer un **servicio ZK institucional común**, si se estudió y qué normas se exigen | Motivo oficial para preferir filtrado frente a prevención de publicación, y evaluación comparativa de ZK |

**No se ha identificado una declaración oficial específica** en la documentación examinada que afirme: «EBSI/ISBE evaluó Longfellow y lo descartó por X». **No atribuirles** las razones de la Comisión/ARF/EUDI Wallet: éstas se refieren al ecosistema de credenciales y no son decisión específica de arquitectura de Besu.

## 5. Frenos reales: obstáculos y respuesta técnica posible

| Barrera | ¿ZK/Longfellow la elimina? | Mitigación o trabajo requerido |
|---|---|---|
| Cambio del esquema de firma del emisor | **A menudo sí**, para documentos compatibles con ECDSA P-256 | Inventariar firmas, formatos y circuitos; validar cadena y formato del documento |
| Hardware móvil especial | **No hace falta** para un servicio nacional; Longfellow tampoco lo exige necesariamente para su caso móvil | Generador en infraestructura controlada, HSM para claves cuando proceda |
| Prueba de **veracidad de los datos de entrada** | **No** | Firma de fuente, integridad, certificación, fecha, responsabilidad y pruebas de autenticidad |
| Verificación eficiente en EVM | **No está garantizada** con Longfellow | Benchmark real; alternativa de SNARK EVM-friendly, verificación fuera de cadena, agregación o comprobación por quórum |
| Tamaño de pruebas, generación y latencia | **No**; dependen de circuitos y protocolo | Medir en servidor, pruebas de concurrencia, coste total de operación; no extrapolar cifras de móvil |
| Normalización e interoperabilidad | **No del todo** | Perfil común de afirmaciones, formatos, circuitos, versiones, parámetros, verificadores, canales de actualización |
| Revocación y vigencia | **No** | Estado firmado/comprometido, acumuladores o árboles, timestamp, ventanas de validez y actualización de testigos |
| Unlinkability y metadatos | **No automáticamente** | Evitar identificadores estables, usar aleatoriedad/nullifiers bien diseñados, minimizar logs y eventos |
| Auditoría, evidencia y recurso administrativo | **Parcialmente** | Custodia de expediente original fuera de cadena, trazabilidad legal, reconstrucción de versiones y revisión humana |
| Gobernanza de una red permisionada | **No** | Acordar aprobadores de circuitos, identidades de operadores, permisos, verificadores, actualizaciones y respuesta a incidentes |
| Privacidad de **todas** las transacciones | **No** | Requiere capa de transacciones privadas o protocolo específico, no únicamente ZK sobre firmas |
| Derecho de supresión RGPD | **No automáticamente** | Minimización, política de metadatos y compromisos, borrado off-chain, roles y evaluación de impacto |

## 6. Límites jurídicos: RGPD y borrado lógico

- **Ventaja principal:** datos originales no replicados on-chain; ZK permite verificar ciertos hechos **sin exponer el expediente**.
- **No equivale a «saltarse todo el RGPD»**: identificadores, hashes, compromisos, direcciones, enlaces entre operaciones, marcas temporales y registros auxiliares pueden seguir siendo datos personales.
- **Un hash sin secreto** de datos previsibles puede ser reversible por diccionario; usar sal/clave o **compromisos ocultantes** adecuados según el modelo de amenazas. La prueba ZK no anonimiza por sí sola todo el entorno.
- **Borrado lógico de ISBE:** filtrar JSON-RPC/contratos o denegar lecturas no prueba supresión de la copia de ledger de todos los nodos, snapshots, backups, logs o accesos alternativos. Puede ser una defensa útil, pero no reemplaza el análisis de derechos.
- **EDPB Guidelines 02/2025**, versión revisada: recomiendan valorar explícitamente una **arquitectura zero-knowledge**, justificar las alternativas, minimizar datos on-chain, usar compromisos adecuados, evaluar metadatos y acompañar ZK de otras medidas ([documento](https://www.edpb.europa.eu/documents/guideline/guidelines-022025-on-processing-of-personal-data-through-blockchain_en)). La conformidad exige análisis **por tratamiento y actor**, no solo elegir una primitiva.
- Persisten las exigencias de necesidad/proporcionalidad, base jurídica, responsables, plazos, supresión y eventualmente EIPD/DPIA. Al emitir decisiones administrativas automatizadas, deben atenderse además garantías y posibilidad de impugnación donde corresponda.

## 7. Propuesta realizable para EBSI/ISBE

**Fase 0 — Inventario y decisión de arquitectura**
- Definir una afirmación concreta y sus fuentes; comprobar si ya está firmada con ECDSA P-256 en un formato admitido, y si necesita prueba verificable **por todos los nodos** o basta con un conjunto de verificadores institucionales.
- Fijar qué NO puede aparecer en ledger, RPC, mempool, logs, eventos, backups y telemetría.

**Fase 1 — Piloto mínimo (preferible: off-chain)**
- Servicio probador nacional + verificador independiente, reutilizando **Longfellow** si los documentos firmados son compatibles; de lo contrario construir circuito ad hoc.
- Mantener el dato y la prueba completa fuera de cadena; anclar como máximo un resultado/compromiso **no correlacionable** junto a referencias de política/circuito cuando sea indispensable.
- Verificar también quién firmó los datos, **estado de revocación**, versión de reglas y frescura; incluir desafío anti-replay.

**Fase 2 — Comparativa on-chain**
- Misma regla implementada como verificador EVM para un esquema eficiente en contratos; medir gas, tiempo de verificación, tamaño, coste de nodos, actualización de circuitos y riesgos de claves.
- Si la verificación en Besu cuesta demasiado, mantenerla off-chain con mecanismos explícitos de verificabilidad/auditoría; **no presentar una mera firma de «OK» como prueba ZK verificada por la red**.

**Fase 3 — Gobernanza e interoperabilidad**
- Catálogo de afirmaciones y circuitos aprobados, registro de versiones y claves de verificación, política de cambios, recuperación ante fallos, auditorías, responsables, revocación y formatos interoperables.
- Evaluar el esquema frente al **filtrado/borrado lógico** actual y frente a una solución **simplemente off-chain sin ZK**, para justificar el coste añadido.

**Criterios de aceptación del piloto**: (i) expediente no accesible desde nodos no autorizados ni sus copias; (ii) verificabilidad reproducible; (iii) fuente y vigencia demostradas; (iv) no correlación injustificada; (v) reversión/actualización del circuito y plan de incidentes; (vi) costes medidos; (vii) evaluación RGPD documentada.

## 8. Balance: qué sabemos y qué falta

**Fundamentado:** Besu puede ejecutar verificadores EVM compatibles; el consenso QBFT no necesita ser ZK; Frigo–Shelat/Longfellow reutiliza ECDSA P-256 para casos compatibles; Google documenta su despliegue como verificación de atributos; el EDPB pide evaluar arquitecturas ZK; controlar la lectura no equivale automáticamente a eliminar datos replicados.

**Hipótesis (no explicación oficial):** en el caso de un nodo/servicio nacional, los frenos predominantes son **gobernanza, interoperabilidad, integración y modelo de confianza**, no hardware móvil ni obligación general de cambiar firmas.

**Preguntas documentales pendientes:** (1) decisiones expresas de EBSI/ISBE sobre ZK institucional; (2) versión efectiva de Besu/precompilados y gas de cada red; (3) formatos firmados disponibles en administraciones; (4) alcance real del Filtering Proxy para operadores y backups; (5) estado actual de wallet ISBE y de los perfiles EBSI; (6) benchmarks reales Longfellow vs SNARK on-chain para el circuito elegido; (7) normativa y perfiles ETSI/ARF finales aplicables.

## 9. Referencias principales

- Frigo y Shelat, *Anonymous Credentials from ECDSA*; referencia [Fri2024] del EUDI Wallet ARF, Topic G.
- Longfellow-ZK, especificación CFRG/IRTF, 19/10/2026: https://www.ietf.org/ietf-ftp/internet-drafts/draft-irtf-cfrg-longfellow-00.html
- Google Wallet, integración técnica Longfellow: https://developers.google.com/wallet/identity/verify/accepting-ids-from-wallet-online
- Google, integración con Bumble: https://blog.google/products-and-platforms/platforms/google-pay/google-wallet-age-identity-verifications/
- Google, donación Longfellow a Linux Foundation Europe, septiembre de 2026: https://blog.google/products-and-platforms/platforms/google-pay/zero-knowledge-proof-library-linux-foundation/
- Especificación europea de verificación de edad, anexo ZK: https://docs.ageverification.dev/av-doc-technical-specification/docs/annexes/annex-B/annex-B-zkp/
- EDPB, Guidelines 02/2025: https://www.edpb.europa.eu/documents/guideline/guidelines-022025-on-processing-of-personal-data-through-blockchain_en
- Documentación oficial de arquitectura, nodos y registros EBSI; documentación técnica del Cliente ISBE y Filtering Proxy: **verificar la URL y la versión concreta antes de convertir una descripción provisional en una afirmación normativa**.

> **Alcance:** propuesta técnica y análisis de riesgos, no dictamen jurídico ni postura oficial de EBSI, ISBE o la Comisión Europea.
