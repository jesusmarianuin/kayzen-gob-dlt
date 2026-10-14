# Hashes en smart contracts

Las funciones hash juegan un papel crítico en los contratos inteligentes, permitiendo automatización segura y verificación de condiciones sin revelar información sensible.

## Casos de Uso Prácticos

### 1. Commit-Reveal Schemes (Esquemas de Compromiso y Revelación)

Permiten hacer compromisos públicos sin revelar la información inmediatamente:

```solidity
// Fase 1: Commit (Compromiso)
// Usuario envía hash de su elección + secreto
function commit(bytes32 hashedChoice) public {
    commitments[msg.sender] = hashedChoice;
}

// Fase 2: Reveal (Revelación)
// Usuario revela su elección y secreto
function reveal(string memory choice, string memory secret) public {
    bytes32 hash = keccak256(abi.encodePacked(choice, secret));
    require(hash == commitments[msg.sender], "No coincide");
    // Procesar elección...
}
```

Aplicaciones:

- Votaciones on-chain donde no quieres que otros vean tu voto hasta que todos hayan votado
- Subastas ciegas donde las ofertas se revelan simultáneamente
- Juegos de azar descentralizados (piedra-papel-tijera, loterías)

### 2. Verificación de Identidad Sin Revelar Datos

```solidity
// Almacenar hash de credenciales en lugar de datos reales
mapping(address => bytes32) public credentialHashes;

function registerCredential(string memory credential) public {
    // Solo se almacena el hash, no la credencial real
    credentialHashes[msg.sender] = keccak256(abi.encodePacked(credential));
}

function verifyCredential(address user, string memory credential) public view returns (bool) {
    return keccak256(abi.encodePacked(credential)) == credentialHashes[user];
}
```

Ventaja: La información sensible (documento de identidad, certificado, etc.) nunca se almacena en la blockchain, solo su hash.

### 3. Gestión de Cadena de Suministro

```solidity
struct Product {
    bytes32 detailsHash;  // Hash de origen, fecha, certificaciones
    uint256 timestamp;
    address supplier;
}

mapping(uint256 => Product) public products;

function registerProduct(uint256 productId, bytes32 detailsHash) public {
    products[productId] = Product({
        detailsHash: detailsHash,
        timestamp: block.timestamp,
        supplier: msg.sender
    });
}

function verifyProduct(uint256 productId, string memory details) public view returns (bool) {
    return keccak256(abi.encodePacked(details)) == products[productId].detailsHash;
}
```

Aplicaciones:

- Trazabilidad de alimentos (origen, fecha de producción)
- Autenticidad de productos de lujo
- Certificaciones y cumplimiento normativo

### 4. Sistemas de Pago Condicional

```solidity
// Pago que se libera solo si se conoce la preimagen de un hash
struct HashedTimeLock {
    bytes32 hashLock;     // Hash del secreto
    uint256 timelock;     // Fecha límite
    uint256 amount;       // Cantidad bloqueada
    address recipient;
    bool claimed;
}

function createHTLC(bytes32 hashLock, address recipient, uint256 lockTime)
    public payable returns (uint256)
{
    uint256 id = nextId++;
    htlcs[id] = HashedTimeLock({
        hashLock: hashLock,
        timelock: block.timestamp + lockTime,
        amount: msg.value,
        recipient: recipient,
        claimed: false
    });
    return id;
}

function claim(uint256 id, string memory secret) public {
    HashedTimeLock storage htlc = htlcs[id];
    require(!htlc.claimed, "Ya reclamado");
    require(keccak256(abi.encodePacked(secret)) == htlc.hashLock, "Secreto incorrecto");
    require(block.timestamp <= htlc.timelock, "Expirado");

    htlc.claimed = true;
    payable(htlc.recipient).transfer(htlc.amount);
}
```

Aplicación: Atomic Swaps (intercambios atómicos entre blockchains diferentes) usando Hash Time Locked Contracts (HTLCs).

### 5. Almacenamiento Eficiente de Datos Grandes

En lugar de almacenar documentos completos on-chain (muy costoso), se almacena solo el hash:

```solidity
mapping(bytes32 => bool) public documentHashes;

function notarizeDocument(bytes32 documentHash) public {
    documentHashes[documentHash] = true;
    emit DocumentNotarized(documentHash, msg.sender, block.timestamp);
}

function verifyDocument(bytes32 documentHash) public view returns (bool) {
    return documentHashes[documentHash];
}
```

Casos de uso:

- Notarización de documentos legales
- Proof of existence (prueba de que un archivo existía en cierto momento)
- Registros médicos (almacenar hash, documento real off-chain)

## Diferencias entre Funciones Hash en Ethereum

Ethereum ofrece varias opciones:

```solidity
// Keccak-256 (SHA-3 variante) - Más usado en Ethereum
bytes32 hash1 = keccak256(abi.encodePacked("data"));

// SHA-256 (Bitcoin standard) - Disponible pero más caro en gas
bytes32 hash2 = sha256(abi.encodePacked("data"));

// RIPEMD-160 - Usado en generación de direcciones Bitcoin
bytes20 hash3 = ripemd160(abi.encodePacked("data"));
```

Costos de Gas (aproximados):

- `keccak256`: ~30 gas + 6 gas por palabra
- `sha256`: ~60 gas + 12 gas por palabra
- `ripemd160`: ~600 gas + 120 gas por palabra

Recomendación: Usar `keccak256` en Ethereum por ser más eficiente y nativo del protocolo.

## Commit-Reveal Schemes

Los esquemas commit-reveal son primitivas criptográficas que permiten comprometerse a un valor sin revelarlo inmediatamente, previniendo manipulación retroactiva. Son fundamentales para garantizar fairness en escenarios donde el orden de revelación podría ser explotado.

Funcionamiento básico:

1. Commit phase: Usuario calcula hash de su valor secreto: `commitment = hash(secret + salt)`. Publica commitment on-chain
2. Waiting period: Otros participantes publican sus commitments sin conocer valores de otros
3. Reveal phase: Cada participante publica su valor original + salt. Smart contract verifica `hash(revealed_value + salt) == commitment`
4. Execution: Solo valores válidos (cuyo hash coincide con commitment) se aceptan. Valores no revelados son descartados

Por qué funciona: Hash unidireccional imposibilita calcular `secret` desde `commitment`. Salt previene ataques de diccionario contra valores predecibles (ej. números 1-100). Una vez publicado commitment, usuario no puede cambiar su valor porque cualquier modificación produciría hash diferente.

Casos de uso en blockchain:

- NFT Fair Mints: Previene sniping. Usuarios commit durante mint window, reveal después. El contrato asigna NFTs basándose en reveals, no en velocidad de transacción
- Voting privado: DAOs permiten votar sin revelar opción hasta que periodo de votación termine. Previene bandwagoning donde votos tardíos copian mayoría
- Generación aleatoria descentralizada: Múltiples participantes commiten entropía, revelan, y XOR de todos los valores genera semilla aleatoria que nadie pudo predecir
- Time-locked secrets: Subastas ciegas donde bids se commitean durante periodo, revelan después. Ganador es mayor bid, pero nadie conoció bids de otros durante subasta
- Multiplayer gaming: Commits aseguran que movimientos simultáneos no puedan reaccionar a acciones de oponente (piedra-papel-tijera on-chain)

Limitaciones: Requiere dos transacciones on-chain (commit + reveal), duplicando costos de gas. Si usuario no revela, su participación es invalidada pero commitment consume espacio. Esquemas deben manejar non-revelation mediante timeouts o penalizaciones de stake.
