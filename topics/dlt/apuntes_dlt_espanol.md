# Apuntes: DLT Español

*Apunte maestro — actualizado continuamente. Última actualización: 18-oct-2026 (secciones 1-12).*

---

## 1. Tecnología base

**Referencia: familia Hyperledger.** Ojo, no es una sola tecnología:

- **Hyperledger Fabric**: permisionado clásico. NO es EVM-compatible nativo. Smart contracts ("chaincode") en Go, Java o Node.js.
- **Hyperledger Besu**: cliente Ethereum completo → **EVM-compatible al 100%** (Solidity estándar).

**Verificado (sesión 1):**
- **EBSI** usa arquitectura de protocolos "enchufables", pero su protocolo principal es **Hyperledger Besu con consenso IBFT 2.0**. (En origen contemplaba también Fabric; Besu se consolidó.)
- **Alastria** (España): su **Red B** corre sobre Besu desde 2020. También mantiene Red T sobre Quorum (igualmente EVM).
- **LACChain** (Latinoamérica) también usa Besu → todo el ecosistema hispano/europeo converge en Besu.
- Modelo de permisos de EBSI a imitar: **lectura pública, escritura limitada a entidades de confianza**.

**Conclusión**: para un DLT español alineado con Europa, **Besu + IBFT 2.0 es el estándar de facto**. La duda Fabric vs Besu queda prácticamente resuelta a favor de Besu.

## 2. Smart contracts

- La creación del smart contract es una parte **no trivial** pero es la parte "que mola" / visible del proyecto.
- Al ser inmutables, necesitan **patrones de upgradeabilidad** (proxies, versionado) → conecta directamente con gobernanza (§3.3).

## 3. Lo que "no mola" (pero es el 80% del trabajo real)

### 3.1 Indexación
- El ledger no es consultable eficientemente por sí solo; hace falta capa de indexación (tipo The Graph, o indexador propio) para búsquedas y APIs.

### 3.2 Almacenamiento histórico
- Crecimiento del ledger con el tiempo: nodos de archivo vs. nodos ligeros.
- Cruce con **plazos legales de conservación documental** de la administración.

### 3.3 Gobernanza
- ¿Qué proceso hace que se apruebe un cambio (de contrato, de protocolo, de miembros)?
- ¿Cómo se coordinan los participantes? (votaciones, comités técnicos, mayorías necesarias)
- Incluye la gobernanza de los upgrades de smart contracts.
- **Desdoblada en dos planos** → ver §5.2.

## 4. Factores adicionales en una administración pública

- **Identidad y firma**: integración con eIDAS, Cl@ve, certificados FNMT. Quién firma transacciones y validez legal de esa firma.
- **RGPD vs inmutabilidad**: derecho al olvido incompatible con ledger inmutable → patrón datos off-chain + hash on-chain, diseñado desde el inicio.
- **ENS (Esquema Nacional de Seguridad)**: cumplimiento obligatorio para sistemas de la administración.
- **Operación de nodos**: quién opera cada nodo, SLAs, resiliencia si un participante desaparece o apaga el suyo.
- **Custodia de claves**: gestión de claves privadas por organismos/funcionarios; recuperación ante pérdida. Problema silencioso pero crítico.
- **Interoperabilidad**: con EBSI, con sistemas legacy de la administración, entre AGE / CCAA / EELL.
- **Contratación pública**: cómo se licita y adjudica el desarrollo y la operación.
- **Auditoría y monitorización**: auditorías de seguridad de contratos, observabilidad de la red.
- **Coste y talento**: presupuesto de operación continua y perfiles técnicos escasos en la administración.

---

## 5. Caso de uso: credenciales de formación

*"Ese curso de formación realizado en el centro X"* — certificados verificables de cursos, títulos, formación continua. Incluye entidades fuera del ámbito estrictamente gubernamental.

- Es el **caso de uso estrella de EBSI** ("diploma use case") → hay estándares maduros: **Verifiable Credentials (W3C)**, modelo de datos educativo europeo (ELM).
- Ejemplo de participante: **Universidad de Valencia** con nodo propio vía consorcio.

### 5.1 Consecuencia: el consorcio se abre
Ya no hablamos solo de nodos operados por AGE/CCAA/EELL. Modelo de consorcio (tipo Alastria): universidades, centros de formación, colegios profesionales, potencialmente empresas.

### 5.2 Las DOS gobernanzas (separarlas simplifica todo)

**A) Gobernanza de RED — ¿quién opera nodos?**
- Requisitos de entrada al consorcio.
- ¿Todos los nodos son validadores (consenso IBFT) o algunos solo lectores/réplica?
- Salida, incumplimiento o abandono de un miembro.
- Coordinación de upgrades de protocolo.

**B) Gobernanza de CONFIANZA — ¿quién emite credenciales?**
- **Emitir NO requiere operar nodo** → un centro pequeño puede emitir sin infraestructura.
- Modelo EBSI: **registros de confianza jerárquicos** on-chain — organismos acreditadores (consejería de educación, ANECA, SEPE...) que acreditan a emisores (el centro X).
- Árbol de confianza: acreditador → emisor → credencial.

**Nota**: una misma entidad puede estar en ambos planos (la Univ. de Valencia = operadora de nodo + emisora acreditada) y otra en solo uno (centro X = solo emisor).

---

## 6. EUDI Wallet, VC cualificados (QEAA) y encaje con EBSI

*(verificado sesión 1, panorama 2024-2026)*

### 6.1 Relación EBSI ↔ EUDI Wallet
- **Complementarios, no lo mismo**: el EUDI Wallet es la capa del ciudadano (custodia y presentación); EBSI es infraestructura de confianza subyacente.
- EBSI ahora gobernada por **EUROPEUM EDIC** (European Digital Infrastructure Consortium). Entre sus funciones: soporte al EUDI Wallet en casos transfronterizos.
- Roles de EBSI en eIDAS: **Trusted Issuer Registry**, infraestructura para servicios de confianza cualificados (emisión QEAA como diplomas, sellos de tiempo, validación, preservación, archivo).

### 6.2 QEAA — matices legales clave
- Un **QEAA solo puede emitirlo un QTSP** (Qualified Trust Service Provider). → Si un centro de formación quiere emitir credenciales *cualificadas*, necesita apoyarse en un QTSP.
- El **ledger no es obligatorio ni está prohibido** como infraestructura del QTSP: un QEAA emitido con DLT como PKI descentralizada debe ser aceptado por todos los EEMM igual que uno con PKI clásica.
- **Sección 11 de eIDAS 2**: define el "ledger electrónico" como servicio de confianza cualificado en sí mismo → el propio DLT español podría certificarse como servicio de confianza. Estándares en CEN JTC 19.
- Jerarquía de credenciales eIDAS 2: **PID** (identidad, emisión estatal) / **PuB-EAA** (organismos públicos, mismo valor que el papel) / **QEAA** (vía QTSP) / **EAA** (no cualificadas).

### 6.3 Tensión de formatos (¡diseñar con esto en mente!)
- Actos de implementación EUDI (enmienda jul-2026, Reg. 2026/1731): formatos reconocidos = **IETF SD-JWT VC** e **ISO mdoc**.
- **W3C VC** (el formato de EBSI) fuera del texto operativo, pero en hoja de ruta — y es el formato de referencia **en educación**.
- Conclusión práctica: para credenciales de formación, W3C VC sigue vivo, pero el sistema debe poder convivir/traducir a SD-JWT VC y mdoc de cara al wallet.

### 6.4 🎯 El embrión real ya existe: ISBE + DC4EU
- **ISBE** = Infraestructura de Servicios Blockchain de España. Base tecnológica nacional que **se integra con EBSI** para el sistema de confianza transfronterizo. → *El "DLT español" ya tiene nombre; estudiar ISBE a fondo.*
- **DC4EU**: piloto europeo a gran escala **liderado por España** (80+ organizaciones, 22 EEMM), pilar educativo — usa EBSI en contexto EUDI Wallet. → Nuestro caso de uso (§5) es exactamente el que España lidera.
- Calendario: cada EEMM debe ofrecer EUDI Wallet a **finales de 2026**; desde 2027, sectores regulados (incl. educación) deberán aceptarlo.

---

## 7. La capa convenial: marcos y convenios legales

*El ingrediente que "repite y es consistente" — posiblemente el mayor dolor de cabeza. No hablamos de leyes (que fijan requisitos, impulsados por Europa) sino de la **capa de acuerdos** entre entidades.*

### 7.1 El mapa convenial español
- **Régimen foral**: Navarra (Convenio Económico), País Vasco (Concierto) → federalismo asimétrico; su encaje nunca es "uno más".
- **Convenios AGE ↔ CCAA**: regulados por Ley 40/2015 (arts. 47-53): contenido obligatorio, duración máxima, registro estatal de instrumentos de cooperación.
- **Convenios con EELL**, consorcios, encomiendas de gestión.
- **Acuerdos con terceros privados** e intereses organizados (lobbies).
- Propiedad clave: cada entidad nueva que entra arrastra su propio marco convenial.

### 7.2 Cómo se "capea": adhesión, no bilateralidad
- El anti-patrón: convenios bilaterales par a par → N² acuerdos → muerte del proyecto.
- El patrón que funciona: **marco único de adhesión** — firmas una vez las reglas comunes y entras.
  - EBSI → adhesión vía European Blockchain Partnership.
  - Alastria → estatutos de asociación.
  - **ISBE** → "convenio → código": gobernanza descentralizada con las reglas (quién participa, cómo se aprueban cambios, transparencia) **integradas en el diseño técnico de la red**.
- Segundo mecanismo de ISBE: **modularidad por perfil de cumplimiento** — no es una única red sino varias redes/servicios adaptados a los requerimientos normativos de cada caso de uso. La heterogeneidad legal se absorbe segmentando, no se "resuelve".

### 7.3 Dato político relevante
- ISBE está impulsada por la **Comunidad de Madrid** + Alastria (fondos Next Generation / PRTR). Una infraestructura "nacional interterritorial" liderada por una CCAA → previsible fricción convenial con forales (Navarra, Euskadi) y otras CCAA. *Observar cómo evoluciona su modelo de adhesión territorial.*

### 7.4 ⚖️ Distinción estructural: ¿DLT de la administración o ancla de VC?
*El matiz determina cuánto derecho arrastra el sistema:*

| | **Ancla de VC** (modelo EBSI) | **DLT de la administración** |
|---|---|---|
| Qué vive on-chain | Registros de confianza, DIDs de entidades, esquemas, revocación | Actuaciones administrativas (expedientes, subvenciones, trazabilidad) |
| Datos personales on-chain | Ninguno | Riesgo constante |
| Naturaleza jurídica de una escritura | Apunte técnico | Potencial **acto administrativo** |
| Derecho aplicable | Ligero: acuerdos de operación de nodos + gobernanza de registros | Ley 39/2015, Ley 40/2015, ENI/ENS, reparto competencial completo |
| Peso convenial | Bajo | El mapa completo de §7.1, por cada caso de uso |

→ **Para credenciales de formación (§5), el modelo natural es "ancla de VC"**: el ligero. Mantener esta disciplina de diseño (nada administrativo on-chain) es la mejor vacuna contra el dolor de cabeza convenial.

---

## 8. Dos problemas "no divertidos" pero recurrentes

### 8.1 Calendario de gobernanza de actualizaciones de red (modelo épocas, ref. IOTA)
- **IOTA como referencia**: opera en **épocas de duración fija (~24h)**. Durante la época, el comité de validadores está congelado. En el límite de época puede haber reconfiguración (entran/salen validadores) y las **actualizaciones de protocolo requieren mayoría cualificada (2f+1)** justo en ese punto de corte — nunca "en caliente" a discreción de un admin.
- **Por qué importa aquí**: en una red permisionada tipo **Besu/IBFT no hay épocas nativas** — no viene de fábrica. Es un mecanismo que **hay que diseñar** para el consorcio (conecta directo con §3.3 y §5.2A, gobernanza de red).
- Preguntas de diseño pendientes de resolver:
  - ¿Cada cuánto hay "ventana de actualización" (época administrativa, no técnica)?
  - ¿Qué mayoría (de nodos validadores, y de entidades del consorcio — no es lo mismo) aprueba un cambio de protocolo / smart contract / alta-baja de miembro?
  - ¿Existe periodo de aviso previo obligatorio, tipo "anuncio de época", antes de que un cambio entre en vigor?
- **Sin esto**: cada actualización es negociación ad-hoc → lento y frágil con administración + universidades + terceros en la mesa.

### 8.2 El infierno de las claves: certificados caducos vs. inmutabilidad perpetua
- **La contradicción de fondo**: certificados X.509 (PKI, eIDAS, FNMT) caducan por diseño (1-5 años). Un ledger "inmutable perpetuo" promete que lo firmado hoy siga siendo verificable dentro de 30 años. Cuando el certificado caduca, la CA cierra, o el algoritmo se debilita (ej. SHA-1), la firma "muere" salvo mantenimiento activo.
- **La estrategia correcta = familia LTV (Long-Term Validation)**, ya estandarizada en eIDAS vía PAdES/CAdES:
  1. **Sellado de tiempo cualificado** en el momento de firmar → prueba que la firma existía y era válida *antes* de la caducidad del certificado.
  2. **Embeber cadena de certificación completa + datos de revocación (CRL/OCSP)** dentro del objeto firmado → no depender de servidores externos vivos dentro de 20-30 años.
  3. **Re-sellado periódico (archive timestamping)**: cuando el algoritmo se debilita, se aplica un nuevo timestamp sobre la firma anterior, en cadena. **Es mantenimiento activo, no "fire and forget".**
- **Aplicación a nodos/validadores del DLT** (no solo a documentos firmados): rotación de claves de nodo sin romper la confianza histórica → usar **DIDs con historial de claves versionado** (modelo que ya usa EBSI para sus Trusted Issuers) en vez de un certificado estático. La clave "de hoy" caduca; el DID y su historial de claves no.
- **Conecta con**: §4 (custodia de claves, ya apuntado como "problema silencioso") — este es el mecanismo concreto que lo resuelve.

---

## 9. Modelo de verdad: log inmutable vs. estado mutable (event sourcing)

*Origen: la "paranoia sobre inmutabilidad no entendida" — el miedo a que un error quede grabado en piedra para siempre.*

### 9.1 La intuición (correcta) de partida
- Web3/Ethereum usa **modelo de cuentas** (balance como dato directo) en vez de UTXO (Bitcoin) → razón principal citada: **composabilidad** — un smart contract necesita leer `balanceOf()` en O(1) para poder componerse con otros contratos (ej. DeFi).
- Propuesta para la administración: el ledger de verdad **no es** "Jesús tiene 5" (estado fijo), sino un **log de transacciones autenticado**: "Pepe envía 5 a Jesús". Si hay error, el admin no lo borra, **emite una nueva transacción** ("Jesús envía 5 a Pepe") que corrige el efecto. El **log es inmutable**; el **registro/estado derivado es corregible** (hacia delante, nunca hacia atrás).

### 9.2 Matiz/corrección: no es alternativa a Web3, es CÓMO YA FUNCIONA Web3
- Ethereum no sustituye el log por el balance: tiene **ambos**. La cadena de bloques (secuencia de transacciones) = log inmutable. El balance que se consulta (`state trie`) = **estado derivado**, una vista materializada calculada aplicando el log en orden. Rápido de leer, pero no es la fuente de verdad — el log lo es.
- Conclusión: el modelo propuesto para la administración **no es una alternativa al modelo Web3, es su misma arquitectura de fondo**, aplicada explícitamente.

### 9.3 Fundamentos formales (dos mundos que confluyen)
- **Event Sourcing** (patrón de arquitectura software, Fowler/CQRS): estado nunca se muta directo; se deriva reproduciendo un log inmutable de eventos. Correcciones = eventos compensatorios nuevos, nunca ediciones del pasado.
- **Contabilidad de partida doble** (ya obligatoria en la administración pública, Plan General de Contabilidad Pública): un asiento erróneo no se borra, se corrige con **asiento de rectificación/abono**. No es una novedad blockchain — es disciplina contable centenaria, ahora con autenticación criptográfica encima.

### 9.4 Resuelve la "paranoia" de inmutabilidad
- El malentendido típico: confundir **inmutabilidad del histórico** (nadie puede borrar/ocultar que hubo un evento X, ni que se corrigió después) con **inmutabilidad de la verdad vigente** (el estado actual SÍ evoluciona, libremente, hacia delante, vía nuevos eventos autenticados).
- Lo inmutable es la trazabilidad del error y su corrección — **no** la imposibilidad de corregir.

### 9.5 Conexión con §7.4 (ancla VC vs. DLT administrativo)
- Este modelo **suaviza** la tabla de §7.4: si lo que sube a la cadena es "declaración de evento firmado" (una transacción) y no "estado de verdad final" (un balance/hecho fijo), el peso jurídico de tratar cada escritura como acto administrativo pétreo se reduce.
- Analogía: se parece más a un **folio de expediente con diligencias de corrección** que a una sentencia grabada en mármol.

### 9.6 ⚠️ Corrección (tras discusión): la pregunta real no es la mecánica, es DÓNDE VIVE LA FINALIDAD
*El §9.2 se quedó corto: dijo que el modelo propuesto "es la misma arquitectura que Ethereum" y eso es cierto solo en la mecánica (log + estado derivado). Pero hay un eje que no es igual: la FINALIDAD/AUTORIDAD sobre la verdad.*

- **En Ethereum/DeFi**: el estado derivado (balance) **ES la verdad final y no apelable**. Nadie —ni juez ni gobierno— puede revertirlo (salvo hard fork extremo, evento social excepcional, no mecanismo del sistema). La finalidad la da el protocolo. Esto es una *feature* buscada.
- **Para una administración, esto NO puede replicarse tal cual**: la Ley 39/2015 obliga a que todo acto administrativo sea recurrible (alzada, reposición, revisión de oficio) y el art. 24 CE garantiza tutela judicial efectiva. **Un Estado no puede ceder la finalidad legal a un consenso de validadores determinista** — sería incompatible con el derecho a recurrir.
- **Por tanto, dos ejes de descentralización distintos** (antes tratados como uno solo):

| Eje | Qué decide | Dónde debería estar, para una administración |
|---|---|---|
| **1. Infraestructura** | Quién opera nodos, cómo se gobiernan actualizaciones (§3.3/§5.2A/§8.1) | Puede estar bastante descentralizado (consorcio multi-nodo) |
| **2. Finalidad** | ¿El estado derivado on-chain tiene la última palabra legal, o es evidencia que alimenta una decisión cuya autoridad final sigue siendo administrativa/judicial? | **Debe quedarse centralizado** — el chain valida y da prueba (integridad, no repudio, timestamp), pero no adjudica; la última palabra la retiene la administración/tribunal |

- El mecanismo de §9.1 (corrección = nueva transacción, nunca edición del pasado) **sigue siendo correcto** — lo que cambia es **quién tiene legitimidad para emitir esa transacción de corrección**: no es "cualquiera con las claves privadas", es quien tiene **competencia administrativa/legal** para hacerlo. La descentralización técnica no debe traducirse en descentralización de la autoridad legal.
- **Resuelve la pregunta pendiente** que quedó abierta: *"¿quién puede emitir la transacción compensatoria — solo el admin, o también el ciudadano?"* → Ninguno de los dos por sí solo con validez plena: la emite el órgano administrativo con competencia, dentro de un procedimiento (posiblemente iniciado a instancia del ciudadano vía recurso), nunca por la sola posesión de una clave.

---

## 10. Rotación de claves: eIDAS, EBSI y DID — lo documentado, no lo imaginado

*(verificado, documentación oficial EC/EBSI — ARF y hub.ebsi.eu, estado 2026)*

### 10.1 EBSI tiene DOS métodos DID con filosofías de rotación opuestas

**`did:key` (personas físicas, wallet de autocustodia)**
- El DID se **deriva matemáticamente de la clave pública** — el identificador ES la clave. No requiere registro ni resolución on-chain.
- **Consecuencia estructural**: la rotación de clave es **imposible por diseño**. Rotar la clave implica alterar el DID — no es "la misma identidad con clave nueva", es un DID distinto.
- **Confirma la intuición del autor**: "mi clave es mía hasta que cambie de wallet" es literalmente así — cambiar de clave equivale a cambiar de identidad a efectos del DID.
- **Matización clave (afinada por el autor)**: el verdadero ancla de persistencia **no es el DID, es el chip (WSCD)**. La clave privada se genera y opera dentro del WSCD, nunca sale en bruto; "tu clave" es en realidad una operación que solo invocas a través del chip, con autenticación de usuario exigida en cada uso. El DID es solo la *codificación* de una clave concreta generada por ese chip — no la raíz de identidad.
  - **Clave de instancia de wallet**: se rota al reinstalar la app o ante eventos de seguridad → es el ancla real de "hasta que cambie de wallet", no el DID.
  - **Claves por atestación — precisado (VC emisión vs. VP presentación, son mecanismos distintos)**:
    - **En la EMISIÓN (batch issuance)**: el wallet atesta varias claves en una Key Attestation y envía una prueba de posesión; el emisor responde emitiendo **una copia de la credencial por cada clave vinculada** (tamaño de lote = min(N claves atestadas, `batch_size` del emisor)). Aquí es donde de verdad se generan claves nuevas — un lote completo, de una vez, en el momento de obtener la credencial.
    - **En la PRESENTACIÓN (VP)**: mecanismo separado. El wallet **reutiliza una copia ya emitida** del lote y genera una **firma fresca** (prueba de posesión/key-binding con nonce anti-repetición) — firma nueva, NO clave nueva. La no-correlación se logra consumiendo copias distintas del lote en presentaciones distintas, no fabricando clave en cada VP.
    - **Conclusión afinada**: la granularidad de "clave distinta" es **por copia del lote**, no por VP individual. [Fuente: igrant.io, docs sobre Wallet Unit Attestation]
  - → En la práctica no hay "una" clave para siempre; hay muchas, generadas frescas por el chip **en el momento de la emisión**, consumidas una a una en presentaciones sucesivas.
  - **Conclusión**: sí hay rotación funcional — pero no ocurre actualizando un DID persistente en un registro (como en `did:ebsi`), sino **regenerando material nuevo dentro del hardware** cada vez. Rotación por fabricación continua, no por edición de documento.
- **Motivo: RGPD, no limitación técnica.** Los reguladores europeos calificaron los DID como información personal → EBSI DID v2 sacó a las personas físicas del ledger por completo para evitar el choque inmutabilidad/dato personal (conecta con §4, tensión RGPD ya apuntada).
- **No es terreno pacífico**: existe debate activo — crítica de que eliminar la rotación para personas físicas es una regresión de seguridad/usabilidad, no mejora sin matices.

**`did:ebsi` (entidades legales / emisores — aquí entra la administración)**
- Sí registrado on-chain, **diseñado explícitamente para rotación frecuente** (ejemplo oficial de la Comisión: cada dos meses).
- El **DID (identificador) permanece estable**; las claves dentro del documento rotan ("key rolling"), se añaden y desactivan, con **historial de claves revocadas conservado on-chain**.
- Los verificadores siempre resuelven el documento DID vigente — nunca fijan una clave antigua → rotación transparente para ellos.

### 10.2 Respuesta directa: ¿rotarán clave las administraciones?
**Sí, por diseño documentado.** Como emisor legal (Issuer), la administración usaría `did:ebsi` con rotación nativa soportada y recomendada por el propio framework técnico de EBSI. No es ambiguo ni especulativo.

### 10.3 ¿Se eliminó la complejidad de "años de caducidad"? — Depende de la capa

| Capa | ¿Caducidad calendárica clásica? | Mecanismo real |
|---|---|---|
| **Wallet/credencial** (ARF, WSCD) | **No** — cambio de paradigma | Clave nueva **por credencial**, generada bajo demanda dentro del WSCD. Rotación sin re-emisión. Revocación consultada en cada verificación (vía Wallet Unit Attestation), no fecha fija. |
| **QTSP / certificado cualificado raíz** (eIDAS Trust Services) | **Sí, sigue viva** | PKI tradicional, validez temporal clásica. Esta capa de confianza raíz no cambió de filosofía con eIDAS 2.0 → por esto sigue siendo necesaria la estrategia **LTV de §8.2** (sellado de tiempo + re-sellado periódico). |

### 10.4 Conclusión formal
No hay una respuesta única "rota" o "no rota" — es arquitectura de capas con filosofía distinta en cada una:
1. **Ciudadano** (`did:key`): sin rotación posible — nueva clave = nuevo DID. Decisión deliberada por RGPD.
2. **Administración/entidad legal** (`did:ebsi`): rotación nativa, frecuente, histórico on-chain, DID estable.
3. **QTSP/raíz de confianza** (certificado cualificado): caducidad clásica + LTV para sobrevivirla.

### 10.5 🎯 Hallazgo de perímetro: el DLT NO cubre la identificación ciudadana, por diseño

*Pregunta que originó esto: "¿me estoy saliendo del DLT?" → No — esto DEFINE el límite real del DLT en la arquitectura europea.*

- **Dos rutas separadas, confirmado**: identificación de personas físicas (`did:key`) vs. identidad de entidades legales (`did:ebsi`). No convergen.
- **Personas físicas**: resuelta de forma puramente criptográfica, **sin tocar ningún ledger** — ni registro, ni consulta on-chain. Decisión deliberada (RGPD, §10.1).
- **Ni siquiera la verificación de confianza (¿está este emisor acreditado?) depende de DLT por defecto**: el mecanismo base de eIDAS 2.0 es la **Trusted List clásica** (art. 22 eIDAS / ETSI TS 119 612, formato XML) — infraestructura PKI **anterior** a cualquier DLT.
- **El reglamento es tecnológicamente neutro**: usar EBSI es **opcional** para los Estados miembro, no obligatorio. EBSI aportaría mejoras posibles (escalabilidad frente al XML actual, revocación en tiempo real) — pero no es requisito.
- **Conclusión de perímetro**: el DLT en esta arquitectura queda confinado a un papel mucho más estrecho de lo esperable al empezar el marco:
  - Identidad de **entidades legales** (emisores, administraciones) → `did:ebsi`, si se elige esa ruta
  - **Registro de confianza** (quién está acreditado) → *puede* usar DLT, pero el baseline real es XML/PKI clásico
  - **La identificación del ciudadano — el 90% del volumen de interacciones — nunca toca el DLT**
- **Implicación de diseño para el DLT español**: no tiene que dimensionarse para soportar el volumen/lógica de "todos los ciudadanos de España" — solo el de entidades acreditadas y, opcionalmente, el registro de confianza. Esto reduce drásticamente la escala real del sistema a construir.
- [Fuente: eIDAS art. 22, ETSI TS 119 612; análisis "Role of EBSI in eIDAS 2.0"]

---

## 11. MiFID II y el marco financiero UE: ¿cuándo aplica a este DLT?

*(sesión 14-oct-2026; verificado contra el texto del Reglamento (UE) 2022/858 en EUR-Lex)*

### 11.1 Respuesta corta
- **Para el caso de uso actual (credenciales de formación, ancla de VC, §5 y §7.4): MiFID II NO aplica.** No hay instrumentos financieros en la cadena.
- **Se vuelve crítico en cuanto el DLT registre, transfiera o liquide instrumentos financieros** (valores tokenizados, deuda pública, participaciones de fondos…). Ahí cambia el tipo de sistema: deja de ser "ancla de confianza" y pasa a ser infraestructura de mercado.

### 11.2 Cómo encajan las piezas (cuando sí aplica)
- **MiFID II / MiFIR**: regula centros de negociación (MTF), intermediación, instrumentos financieros. La definición de instrumento financiero se enmendó para incluir los emitidos mediante DLT (Reglamento 2022/858, considerando 59).
- **Régimen Piloto DLT (Reglamento (UE) 2022/858)**: puente entre DLT y la regulación de mercados. Crea tres figuras: **DLT MTF** (negociación), **DLT SS** (liquidación) y **DLT TSS** (ambas en el mismo ledger). Un DLT MTF está sujeto a los requisitos de un MTF salvo exenciones concedidas caso a caso (art. 4, considerando 13). Solo admite instrumentos financieros tokenizados, con límites de tamaño por tipo de activo.
- **MiCA**: cubre los criptoactivos que *no* son instrumentos financieros (stablecoins, utility tokens…). Frontera MiFID/MiCA = ¿es o no instrumento financiero?
- Estado del régimen piloto (periodo inicial 2023-2026, prórroga hasta 2029 y revisión ESMA): **fuente secundaria, sin contrastar en fuente primaria** → verificar antes de apoyarse en ello.

### 11.3 Por qué importa para el diseño aunque hoy no aplique
- Es el ejemplo de manual de **"DLT de la administración/mercado" (columna derecha de §7.4)**: cada escritura es un acto con consecuencias jurídicas, y la regulación exige permisos, exenciones y supervisión (CNMV/BdE en España; ESMA a nivel UE).
- Si algún día se quiere ampliar el DLT a deuda pública u otros activos financieros, **no se hereda: hay que tratarlo como línea de negocio regulada aparte** (modularidad por perfil de cumplimiento, §7.2).

### 11.4 🧩 Subproducto: definiciones jurídicas de "ledger" en el Derecho UE
*(responde en parte a la pregunta del 4-oct sobre la definición amplia de "ledger")*

| Norma | Término | Definición | Alcance |
|---|---|---|---|
| **Reg. 2022/858, art. 2** (verbatim) | *Distributed ledger* | "an information repository that keeps records of transactions and that is shared across, and synchronised between, a set of DLT network nodes using a consensus mechanism" | **Estrecha**: exige distribución + sincronización + consenso |
| **Reg. 2022/858, art. 2** | *DLT* | "a technology that enables the operation and use of distributed ledgers" | Deriva de la anterior |
| **eIDAS 2 (Reg. 2024/1183), cons. 68** | *Electronic ledger* | "a sequence of electronic data records" que debe garantizar integridad y orden cronológico exacto (el texto del art. 3 no pudo contrastarse literalmente) | **Amplia**: no exige distribución ni consenso → encaja con ledger centralizado, DLT o blockchain |

- **Lectura clave**: el Derecho UE tiene **dos nociones de ledger**. La financiera (2022/858) es la estrecha: solo DLT con consenso. La de eIDAS es la amplia: cualquier registro secuencial, íntegro y ordenado en el tiempo. Un servicio de confianza de "ledger electrónico" **no tiene por qué ser una blockchain** (refuerza §6.2).
- **Pendiente**: la definición *conceptual* más amplia de "ledger" (contable/ISO 22739) no se obtuvo; la norma ISO no es de acceso libre.

---

## 12. Alastria: qué es jurídicamente, el convenio de ISBE y su postura ante MiFID

*(sesión 14-oct-2026; fuentes primarias: BOCM 7-mar-2025 y respuesta de Alastria a consulta CNMV)*

### 12.1 Naturaleza
- **Asociación** (Asociación Consorcio Red ALASTRIA), no un organismo público ni una empresa. Sus redes (Red B sobre Besu, Red T sobre Quorum; §1) son redes de consorcio de sus socios.

### 12.2 🎯 El instrumento jurídico de ISBE (resuelve en parte el pendiente de §7)
- Es un **convenio de colaboración al amparo de la Ley 40/2015** entre la **Consejería de Digitalización de la Comunidad de Madrid** y **Alastria** (BOCM 7-mar-2025). No es subvención nominativa ni encomienda.
- **Objeto**: tres paquetes de trabajo: (1) cliente de la red ISBE, (2) despliegue de la red, (3) casos de uso vía subvenciones en concurrencia competitiva a pymes madrileñas.
- **Presupuesto máximo**: 8.923.758 € (Madrid 6.738.000 €; Alastria 2.185.758 € valorados en su cartera de activos).
- **Vigencia**: hasta el **31-dic-2025, sin prórrogas** (cláusula novena); incumplir los paquetes 1 y 2 a esa fecha implica devolución del 100 % más intereses.
- **Gobernanza del convenio**: Comisión de Seguimiento paritaria, preside la Consejería, secretario el presidente de Alastria, mayoría simple con voto dirimente del presidente.
- **Titularidad**: cotitularidad a partes iguales de los resultados y de la red ISBE, concebida como infraestructura descentralizada con nodos operados por múltiples entidades.
- **Hallazgos que importan al marco**:
  - El **modelo de gobernanza de la red "se desarrollará durante el proyecto"**: no estaba definido en el convenio.
  - **No regula un mecanismo formal de adhesión de otras administraciones**; solo prevé nodos en Madrid y "las regiones que así lo manifiesten". El exponendo menciona que el proyecto se presentó con Asturias y Canarias.
  - Ejemplo real del patrón de §7.3: una CCAA + una asociación privada, con la adhesión territorial sin resolver. Aquí encajaría el problema foral (Navarra, Euskadi).
- **Sin contrastar**: qué ocurrió tras el 31-dic-2025 (continuidad, nuevo convenio, traspaso de la gobernanza). Buscarlo.

### 12.3 Postura de Alastria sobre MiFID (respuesta del Comité Legal a una consulta de la CNMV sobre un proyecto de Circular de publicidad de criptoactivos; fecha sin verificar)
- Los tokens que sean instrumentos financieros se rigen por **MiFID II** y la normativa de mercado primario; propone un test tipo **Howey** para delimitar el ámbito.
- Lo relevante es **si el token se presenta como inversión**, no su tipología técnica.
- Considera la **gobernanza de las redes DLT** esencial y poco tratada en la propuesta europea: estructura del protocolo, identidad digital del titular, riesgos operativos incluido el **"apagado eventual" de la red**. Sugiere considerar a los administradores de redes permisionadas según ISO/TC 307 e ITU-T.
- **No analiza** la responsabilidad de nodos o del consorcio ni el valor probatorio de los registros en blockchain.
- → Alastria identifica el mismo hueco que este marco: gobernanza y operación de la red son lo menos regulado.

---

## Pendientes / a discutir

- [x] Instrumento jurídico de ISBE → convenio Ley 40/2015 Madrid-Alastria (§12.2). Sigue abierto cómo se adhieren otras CCAA y las forales.
- [ ] Averiguar qué pasó con ISBE tras el fin del convenio (31-dic-2025): continuidad, gobernanza definitiva, nueva entidad
- [ ] Confirmar con el autor qué texto de MiFID leyó y qué le pareció relevante (¿valores tokenizados? ¿deuda pública? ¿otra cosa?)
- [x] Elección tecnológica → **Besu + IBFT 2.0** (estándar de facto en EBSI, Alastria y LACChain)
- [x] Caso de uso principal → credenciales de formación (§5). Puede haber más ("muchas cosas", dijo el autor).
- [ ] Definir quién sería el/los organismo(s) acreditador(es) raíz del árbol de confianza
- [ ] Criterios de entrada al consorcio (¿quién puede tener nodo? ¿validador vs lector?)
- [ ] Estudiar ISBE en detalle: arquitectura, gobernanza actual, cómo entrar como nodo
- [ ] ¿Quién sería el QTSP para emitir QEAA de formación? ¿Uno existente (FNMT?) o certificar el propio ledger (Sección 11 eIDAS)?
- [ ] Cómo se adhieren otras CCAA a ISBE y cómo encajan las forales (el convenio de §12.2 no lo regula)
- [ ] Diseñar el mecanismo de "épocas" de gobernanza para actualizaciones de red (ISBE/Besu no lo trae de fábrica)
- [ ] Definir política de re-sellado (archive timestamping) y agilidad criptográfica ante debilitamiento de algoritmos a largo plazo
- [x] Nivel de descentralización deseado → desdoblado en **eje infraestructura vs. eje finalidad** (§9.6). Infraestructura puede descentralizarse; la finalidad legal, no.
- [ ] Diseñar el procedimiento administrativo concreto que autoriza emitir una transacción de corrección (¿quién firma, con qué competencia, iniciado de oficio o a instancia de parte?)
