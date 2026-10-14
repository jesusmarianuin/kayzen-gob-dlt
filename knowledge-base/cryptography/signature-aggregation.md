# Agregación de firmas: BLS y Schnorr

## BLS Signatures (Boneh-Lynn-Shacham)

Esquema de firma criptográfica basado en emparejamientos bilineales (bilinear pairings) sobre curvas elípticas que permite agregación eficiente de firmas, crítico para escalabilidad y eficiencia en sistemas blockchain modernos.

Fundamentos Matemáticos:

A diferencia de ECDSA que opera sobre curvas elípticas estándar (secp256k1, secp256r1), BLS utiliza curvas con propiedades de emparejamiento como BLS12-381. Un emparejamiento bilineal es una función matemática e: G₁ × G₂ → Gₜ que satisface:

- Bilinealidad: e(aP, bQ) = e(P, Q)^(ab)
- No-degeneración: e(G₁, G₂) ≠ 1
- Computabilidad eficiente

Estas propiedades permiten verificar firmas agregadas sin necesidad de verificar cada firma individual.

Proceso de Firma:

1. Generación de Claves:
   - Clave privada: x ∈ Zₚ (número aleatorio)
   - Clave pública: PK = x·G₂ (punto en curva G₂)

2. Firma de Mensaje:
   - Hash del mensaje a punto de curva: H(m) ∈ G₁
   - Firma: σ = x·H(m)

3. Verificación:
   - Comprobar: e(σ, G₂) = e(H(m), PK)
   - Si la ecuación se cumple, la firma es válida

Agregación de Firmas:

La propiedad más poderosa de BLS es la agregación:

- Dadas n firmas σ₁, σ₂, ..., σₙ sobre mensajes m₁, m₂, ..., mₙ
- Firma agregada: σₐgg = σ₁ + σ₂ + ... + σₙ (suma de puntos en la curva)
- Claves públicas agregadas: PKₐgg = PK₁ + PK₂ + ... + PKₙ
- Verificación agregada: e(σₐgg, G₂) = ∏ e(H(mᵢ), PKᵢ)

Crucialmente, el tamaño de σₐgg es idéntico al de una firma individual (48 bytes en BLS12-381), sin importar cuántas firmas se agreguen.

Aplicaciones en Blockchain:

Ethereum Beacon Chain (Consenso PoS):

Ethereum 2.0 utiliza BLS signatures como componente fundamental del consenso:

- Agregación de attestations: En cada época, miles de validadores firman attestations (votos sobre bloques válidos). Agregar estas firmas reduce drásticamente el ancho de banda:
  - Sin agregación: 10,000 validadores × 96 bytes/firma = 960 KB
  - Con BLS agregado: 1 firma = 96 bytes (reducción >99%)

- Sync committees: Comités de 512 validadores que firman headers de bloques para light clients. Una firma agregada representa el consenso de todo el comité.

- Slashing proofs: Evidencia de comportamiento malicioso puede incluir múltiples firmas agregadas de forma compacta.

Ethereum usa la curva BLS12-381 con firmas de 96 bytes y claves públicas de 48 bytes. [EIP-2537](https://eips.ethereum.org/EIPS/eip-2537) añadió precompiles para operaciones BLS eficientes en contratos inteligentes.

Optimistic Rollups y ZK-Rollups:

L2 solutions utilizan BLS para agregar firmas de múltiples transacciones en un batch:

- Arbitrum: Validadores firman bloques. Firmas agregadas reducen costo de verificación on-chain.
- zkSync y StarkNet: Aunque usan ZK-proofs como método principal, BLS complementa para firmas de operadores en data availability.

Multisig Eficiente:

Tradicional multisig en Ethereum (Safe/Gnosis) requiere incluir todas las firmas ECDSA individuales en la transacción, incrementando linealmente el gas:

- 3-of-5 multisig con ECDSA: ~5 firmas × 65 bytes = 325 bytes + lógica verificación
- Mismo esquema con BLS: 1 firma agregada = 96 bytes

Ahorro de gas significativo en organizaciones con múltiples firmantes.

Ventajas:

- Agregación de firmas: Múltiples firmas → una firma del mismo tamaño. Reducción dramática de ancho de banda y storage.
- Verificación batch eficiente: Verificar n firmas agregadas es más rápido que verificar n firmas individuales.
- Umbral nativo: Esquemas threshold (t-of-n) son naturalmente implementables sin complejidad adicional.
- Determinismo: Como ECDSA, la generación de firma es determinista (no requiere nonce aleatorio).

Desventajas:

- Emparejamientos costosos: Operaciones de pairing son computacionalmente más caras que multiplicación escalar de ECDSA (aunque el ahorro en agregación compensa en casos de múltiples firmas).
- Claves públicas más grandes: 48 bytes en BLS12-381 vs 33 bytes en ECDSA comprimido.
- Rogue key attacks: Sin medidas de protección, un atacante puede elegir clave pública maliciosa PK* = PK - PKₘₐₗ para cancelar la firma honesta en agregación. Solución: proof-of-possession (PoP) donde cada firmante demuestra conocimiento de su clave privada.
- Implementación compleja: Requiere aritmética de curvas con pairing, bibliotecas especializadas, superficie de ataque mayor.

Implementaciones y Herramientas:

- py_ecc: Implementación Python de BLS12-381 usada en especificación de Ethereum beacon chain.
- blst: Biblioteca C/C++ de alta performance usada por clientes Ethereum (Prysm, Lighthouse).
- noble-curves: Implementación JavaScript/TypeScript auditable de BLS12-381.
- Apache Milagro: Suite criptográfica multi-lenguaje con soporte BLS.

Seguridad:

- Nivel de seguridad: BLS12-381 ofrece ~128 bits de seguridad, equivalente a AES-128 o RSA-3072.
- Resistencia cuántica: Como ECDSA, BLS es vulnerable a algoritmo de Shor en computadoras cuánticas. No es post-cuántico.
- Auditorías: Implementaciones deben ser exhaustivamente auditadas. Bugs en aritmética de pairing pueden ser catastróficos.

Recursos Adicionales:

- [BLS Signatures for Beginners](https://ethresear.ch/t/pragmatic-signature-aggregation-with-bls/2105) - Ethereum Research
- [BLS12-381 For The Rest Of Us](https://hackmd.io/@benjaminion/bls12-381) - Ben Edgington
- [Pairing-Based Cryptography](https://www.iacr.org/archive/asiacrypt2008/53500001/53500001.pdf) - Paper académico fundacional
- [EIP-2537 Specification](https://eips.ethereum.org/EIPS/eip-2537) - BLS precompiles en Ethereum

## Schnorr Signatures y MuSig

Esquema de firma digital basado en el problema del logaritmo discreto, conocido por su simplicidad matemática, eficiencia y propiedades de agregación. Schnorr fue patentado hasta 2008, lo que retrasó su adopción. Bitcoin lo integró en 2021 mediante Taproot (BIP-340).

Fundamentos de Schnorr:

A diferencia de ECDSA que requiere aritmética modular compleja y nonces críticos, Schnorr tiene estructura matemática más elegante:

Generación de Claves:

- Clave privada: x ∈ Zₙ (escalar aleatorio)
- Clave pública: P = x·G (punto en curva elíptica)

Proceso de Firma:

1. Generar nonce aleatorio: k ∈ Zₙ
2. Calcular R = k·G
3. Calcular challenge: e = H(R || P || m) donde m es el mensaje
4. Calcular s = k + e·x
5. Firma: (R, s)

Verificación:

1. Recalcular: e = H(R || P || m)
2. Verificar: s·G = R + e·P
3. Si la ecuación se cumple, la firma es válida

Linealidad y Agregación:

La propiedad fundamental de Schnorr es la linealidad:

- Si σ₁ = (R₁, s₁) firma mensaje m con clave x₁
- Y σ₂ = (R₂, s₂) firma el mismo mensaje m con clave x₂
- Entonces σₐgg = (R₁ + R₂, s₁ + s₂) es firma válida para clave agregada x₁ + x₂

Esto habilita signature aggregation y multisig nativo sin smart contracts.

MuSig: Multisignatures con Schnorr:

MuSig (Multi-Signature) es un protocolo que permite a múltiples partes colaborar para producir una única firma Schnorr indistinguible de una firma individual.

Variantes de MuSig:

MuSig1 (Original):

- Requiere tres rondas de comunicación
- Vulnerable a rogue-key attacks sin medidas de protección
- Implementación inicial, no recomendado para producción

MuSig2 (Actual estándar):

- Dos rondas de comunicación
- Resistente a rogue-key attacks mediante key aggregation coefficient
- Usado en Bitcoin Taproot
- Proceso:

1. Ronda 1 (Compromiso de nonce):
   - Cada participante genera nonce rᵢ y comparte compromiso H(Rᵢ)

2. Ronda 2 (Revelación de nonce):
   - Cada participante revela Rᵢ
   - Todos verifican compromisos y calculan R = ∑Rᵢ

3. Firma:
   - Calcular clave pública agregada: P̃ = ∑aᵢ·Pᵢ donde aᵢ = H(L || Pᵢ) y L es lista de todas las claves
   - Cada participante calcula sᵢ = rᵢ + H(R || P̃ || m)·aᵢ·xᵢ
   - Firma final: s = ∑sᵢ

MuSig-DN (Deterministic Nonces):

- Elimina requisito de generación de nonces aleatorios
- Nonces derivados determinísticamente de clave privada y mensaje
- Previene ataques de reutilización de nonce

FROST (Flexible Round-Optimized Schnorr Threshold):

- Extensión de MuSig para firmas threshold (t-of-n)
- Permite que subconjunto de participantes firme sin revelar quiénes específicamente
- Mejor privacidad que MuSig simple

Implementación en Bitcoin Taproot (BIP-340, BIP-341, BIP-342):

Taproot, activado en Bitcoin en noviembre 2021, introdujo Schnorr signatures como método de firma estándar:

Ventajas para Bitcoin:

- Indistinguibilidad: Transacciones multisig son idénticas a transacciones single-sig on-chain. Mejor privacidad.
- Eficiencia: Una firma Schnorr agregada (64 bytes) vs múltiples firmas ECDSA (65 bytes × n firmantes).
- Menor costo: Transacciones multisig usan menos block space → fees más bajos.
- Script paths ocultos: Taproot permite condiciones de gasto complejas (timelocks, hashlocks) que solo se revelan si se usan, no por defecto.

Ejemplo Comparativo:

- Pre-Taproot multisig 3-of-5: Transacción incluye script explícito con 5 claves públicas (33 bytes cada una) y 3 firmas ECDSA (65 bytes cada una). Total visible on-chain: ~360 bytes.

- Post-Taproot MuSig 3-of-5: Transacción incluye 1 clave pública agregada (32 bytes) y 1 firma Schnorr (64 bytes). Total: 96 bytes. Reducción ~73%.

Además, observadores externos no pueden determinar que es multisig, mejorando privacidad.

Threshold Signatures con Schnorr:

Esquemas t-of-n donde cualquier subconjunto de t participantes puede generar firma válida:

- FROST: Protocolo threshold optimizado, 2 rondas, sin trusted dealer
- Uso en custodia institucional: Fondos que requieren aprobación de, por ejemplo, 5 de 9 ejecutivos
- Privacidad mejorada: No se revela on-chain cuántos firmantes participaron ni quiénes específicamente

Ventajas de Schnorr sobre ECDSA:

- Linealidad matemática: Agregación de firmas y claves es trivial (suma de puntos).
- Simplicidad de implementación: Menos propenso a bugs que ECDSA.
- Seguridad demostrable: Prueba de seguridad en modelo random oracle, asumiendo dureza del logaritmo discreto.
- Batch verification: Verificar múltiples firmas Schnorr simultáneamente es más eficiente que verificarlas individualmente.
- No-maleabilidad nativa: ECDSA sufre de transaction malleability (firma puede modificarse sin invalidarla), Schnorr no.

Desventajas:

- Adopción limitada: Solo Bitcoin Taproot y algunos proyectos (Polkadot, Cardano usan Ed25519 que es variante de Schnorr). Ethereum sigue usando ECDSA.
- Requerimiento de coordinación: MuSig requiere interacción entre firmantes (múltiples rondas), mientras ECDSA multisig puede ser asíncrono.
- Rogue-key attacks: Sin protección adecuada (key aggregation coefficients), atacante puede manipular clave agregada.

Aplicaciones Más Allá de Bitcoin:

Lightning Network:

- Canales de pago aprovechan Schnorr para transacciones multisig eficientes
- Schnorr/Taproot permite channel factories y splice-in/out más eficientes

Monero (RandomX):

- Usa ring signatures basadas en Schnorr para privacidad
- Permite ofuscar quién específicamente firmó entre múltiples posibles firmantes

Zcash Orchard:

- Usa RedDSA (variante de Schnorr sobre curva Jubjub) en shielded transactions

Comparación BLS vs Schnorr:

| Característica | BLS | Schnorr |
| --- | --- | --- |
| Base matemática | Emparejamientos bilineales | Logaritmo discreto |
| Agregación | Nativa, cualquier combinación | Requiere coordinación (MuSig) |
| Tamaño firma | 96 bytes (BLS12-381) | 64 bytes (secp256k1) |
| Tamaño clave pública | 48 bytes | 32 bytes |
| Verificación agregada | Eficiente via pairings | Batch verification disponible |
| Adopción blockchain | Ethereum PoS, L2s | Bitcoin Taproot, Polkadot |
| Complejidad implementación | Alta (pairings) | Media (aritmética curva) |
| Rondas de comunicación multisig | 0 (no interactivo) | 2 (MuSig2) |
| Threshold nativo | Sí | Sí (FROST) |
| Privacidad multisig | Firmas indistinguibles | Firmas indistinguibles |

Recursos Adicionales:

- [BIP-340: Schnorr Signatures for secp256k1](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki)
- [BIP-341: Taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)
- [MuSig2 Paper](https://eprint.iacr.org/2020/1261.pdf) - Especificación académica
- [FROST Paper](https://eprint.iacr.org/2020/852.pdf) - Threshold signatures
- [Taproot Workshop](https://bitcoinops.org/en/schorr-taproot-workshop/) - Bitcoin Optech
- [Schnorr Signatures Overview](https://github.com/sipa/bips/blob/bip-schnorr/bip-schnorr.mediawiki) - Pieter Wuille
