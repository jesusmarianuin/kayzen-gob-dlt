# Estructuras de Merkle

Las estructuras de Merkle permiten resumir un conjunto grande de datos en un único hash, la raíz, y demostrar que un dato concreto forma parte del conjunto sin entregar el resto. En una blockchain son la base para que un nodo, un cliente ligero o un smart contract verifiquen datos sin descargar ni confiar en toda la cadena.

Este documento cubre tres piezas:

- El Merkle tree binario, la estructura base
- El Merkle Patricia trie, la estructura con la que Ethereum y Besu guardan el estado
- Las pruebas de estado (`eth_getProof`), la forma de usar esas estructuras desde fuera del nodo

## Merkle tree

Un Merkle tree es un árbol binario de hashes:

- Cada hoja es el hash de un dato (una transacción, un documento)
- Cada nodo interno es el hash de la concatenación de sus dos hijos
- La raíz resume todo el conjunto: si cambia un solo dato, cambia la raíz

```text
                Raíz = H(H_AB + H_CD)
               /                     \
        H_AB = H(H_A + H_B)    H_CD = H(H_C + H_D)
         /         \             /         \
       H_A         H_B         H_C         H_D
        |           |           |           |
     Dato A      Dato B      Dato C      Dato D
```

### Prueba de inclusión

Para demostrar que el dato A está en el árbol basta con entregar los hashes hermanos del camino hasta la raíz, en este caso `H_B` y `H_CD`. Quien verifica recalcula `H_A`, después `H_AB` y después la raíz, y la compara con la raíz que ya conoce.

El tamaño de la prueba crece con el logaritmo del número de hojas: para un millón de documentos bastan 20 hashes.

### Uso en la administración: anclaje de documentos por lotes

Registrar en la cadena el hash de cada documento cuesta una transacción por documento. Con un Merkle tree se registra solo la raíz de un lote, y cada documento se verifica después con su prueba. Es el patrón habitual para sellar en blockchain registros de entrada, actas o certificados emitidos.

El árbol se construye fuera de la cadena. En Node.js, con la librería de OpenZeppelin:

```bash
# Ejecutar en la carpeta del proyecto de scripts
npm install @openzeppelin/merkle-tree
```

```javascript
// scripts/build-batch.mjs
import { StandardMerkleTree } from "@openzeppelin/merkle-tree";

// Hashes SHA-256 de los documentos del lote, calculados previamente
const values = [
  ["0x9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"],
  ["0x60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752"],
];

const tree = StandardMerkleTree.of(values, ["bytes32"]);

console.log("Raíz del lote:", tree.root);
console.log("Prueba del documento 0:", tree.getProof(0));
```

La raíz se registra en un contrato, y cualquiera puede verificar un documento con su prueba. Ejemplo con OpenZeppelin Contracts 5.x:

```solidity
// contracts/DocumentBatchRegistry.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {MerkleProof} from "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract DocumentBatchRegistry is Ownable {
    mapping(bytes32 => bool) public isRegisteredRoot;

    event BatchRegistered(bytes32 indexed root);

    constructor(address initialOwner) Ownable(initialOwner) {}

    function registerBatch(bytes32 root) external onlyOwner {
        isRegisteredRoot[root] = true;
        emit BatchRegistered(root);
    }

    function verifyDocument(
        bytes32 root,
        bytes32 documentHash,
        bytes32[] calldata proof
    ) external view returns (bool) {
        // Doble hash de la hoja, igual que StandardMerkleTree
        bytes32 leaf = keccak256(bytes.concat(keccak256(abi.encode(documentHash))));
        return isRegisteredRoot[root] && MerkleProof.verify(proof, root, leaf);
    }
}
```

Implicaciones de seguridad:

- Doble hash de las hojas: si la hoja y el nodo interno se calculan igual, un atacante puede presentar un nodo interno (64 bytes) como si fuera una hoja y obtener una prueba válida para un dato que no existe (ataque de segunda preimagen). El doble hash separa los dos dominios. Por eso el contrato tiene que calcular la hoja exactamente igual que la librería que construye el árbol
- Control de acceso al registro: sin `onlyOwner`, cualquiera podría registrar raíces propias y "certificar" documentos falsos
- Qué prueba el anclaje: que el documento existía con ese contenido cuando se registró la raíz. No prueba quién lo emitió; para eso hace falta una firma electrónica sobre el documento

## Merkle Patricia trie

Ethereum no usa un Merkle tree binario para su estado, sino un Merkle Patricia trie (MPT). Combina dos ideas:

- Trie de Patricia: un árbol de búsqueda por clave en el que el camino desde la raíz deletrea la clave, y los tramos sin bifurcaciones se comprimen en un solo nodo. Permite leer, insertar y borrar por clave
- Merkle: cada nodo se identifica por el hash Keccak-256 de su contenido codificado en RLP, así que la raíz resume todo el árbol

La diferencia práctica con un Merkle tree es que el MPT es un mapa clave-valor que se actualiza bloque a bloque, no una lista fija de datos.

### Tipos de nodo

Las claves se recorren en nibbles (dígitos hexadecimales, 4 bits). Hay tres tipos de nodo:

- Branch: 16 posiciones, una por nibble posible, más un valor opcional
- Extension: un tramo de clave compartido y el hash del siguiente nodo
- Leaf: el resto de la clave y el valor

Un nodo cuya codificación RLP ocupa menos de 32 bytes se incrusta en su padre en lugar de referenciarse por hash.

### Los tries de un bloque

Cada cabecera de bloque contiene la raíz de varios tries:

- `stateRoot`: estado global. La clave es `keccak256(dirección)` y el valor es la cuenta: `[nonce, balance, storageRoot, codeHash]`
- `transactionsRoot`: transacciones del bloque, indexadas por su posición
- `receiptsRoot`: recibos de las transacciones (estado, gas usado, logs)

Además, cada contrato tiene su propio storage trie, cuya raíz es el `storageRoot` de su cuenta. La clave es `keccak256(slot)`.

Las claves del estado y del storage se hashean para que el árbol quede equilibrado: nadie puede elegir direcciones o slots que alarguen a propósito un camino y encarezcan las lecturas.

Las raíces se pueden consultar en cualquier nodo Besu:

```bash
# Ejecutar en una máquina con acceso al endpoint JSON-RPC del nodo
curl -s -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest",false],"id":1}' \
  http://127.0.0.1:8545 | jq '.result | {number, stateRoot, transactionsRoot, receiptsRoot}'
```

### Almacenamiento en Besu: Forest y Bonsai

Besu puede guardar el MPT en disco de dos formas, con la opción `--data-storage-format`:

- Forest: guarda cada nodo del trie por su hash. Conserva el estado de todos los bloques, pero ocupa mucho disco y las lecturas son más lentas
- Bonsai: guarda el estado actual de forma plana, por cuenta y slot, y reconstruye las raíces cuando las necesita. Ocupa mucho menos y lee más rápido. Para estados anteriores guarda "trie logs" que permiten retroceder un número limitado de bloques

Las versiones recientes de Besu usan Bonsai por defecto. El límite de bloques históricos se controla con `--bonsai-historical-block-limit` (512 por defecto). Comprueba ambos valores en la documentación de la versión que despliegues.

El formato es una decisión de cada nodo, no de la red: en una red QBFT pueden convivir validadores con Bonsai y un nodo de archivo con Forest, que es lo habitual cuando hay que consultar o auditar estados antiguos.

## Pruebas de estado con eth_getProof

El método `eth_getProof`, definido en [EIP-1186](https://eips.ethereum.org/EIPS/eip-1186), devuelve el camino del MPT desde la `stateRoot` de un bloque hasta una cuenta y, si se piden, hasta slots concretos de su storage. Con esa prueba y la `stateRoot` del bloque, un tercero comprueba el saldo, el nonce o un valor de storage sin fiarse del nodo que le respondió.

Usos relevantes en una red de la administración:

- Auditoría: demostrar el valor de un registro en un bloque concreto ante alguien que solo confía en las cabeceras de bloque
- Interoperabilidad entre redes: un contrato o un puente verifica en otra red el estado de esta a partir de una `stateRoot` conocida

```bash
# Ejecutar en una máquina con acceso al endpoint JSON-RPC del nodo
# Prueba de la cuenta del contrato y de su slot 0 en el último bloque
curl -s -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_getProof","params":["0xDIRECCION_DEL_CONTRATO",["0x0"],"latest"],"id":1}' \
  http://127.0.0.1:8545 | jq '.result | {balance, nonce, storageHash, accountProof, storageProof}'
```

La respuesta incluye:

- `accountProof`: los nodos RLP del camino desde la `stateRoot` hasta la cuenta
- `storageHash`: el `storageRoot` de la cuenta
- `storageProof`: para cada slot pedido, su valor y los nodos del camino desde el `storageHash`

## Evolución: Verkle trees y árboles binarios

En Ethereum mainnet se estudia sustituir el MPT por una estructura con pruebas más pequeñas, para que los clientes puedan verificar bloques sin guardar el estado (clientes stateless). Primero se propusieron los Verkle trees y después árboles binarios basados en hash. Ninguno está activado en mainnet.

Una red privada QBFT no se ve afectada mientras no cambie de versión de cliente y de hard fork, pero conviene seguir esta evolución: cambiará el formato de las pruebas de estado y cualquier contrato o servicio que las verifique.

## Resolución de problemas

### eth_getProof devuelve un error en un bloque antiguo

Con Bonsai, el nodo solo puede reconstruir el estado de los últimos bloques que permite `--bonsai-historical-block-limit`. Para bloques más antiguos hay que consultar un nodo de archivo con Forest, o aumentar el límite en el nodo, a costa de más disco.

### El método eth_getProof no está disponible

El endpoint JSON-RPC tiene que exponer el espacio de nombres `ETH`, que va incluido por defecto en `--rpc-http-api`. Si el nodo se arrancó con una lista explícita de APIs, comprueba que incluye `ETH`.

### MerkleProof.verify devuelve false con una prueba correcta

Casi siempre la hoja no se calcula igual en el contrato y en el script. Con `StandardMerkleTree` la hoja es el doble hash de los valores codificados con `abi.encode` y los tipos declarados al crear el árbol. Si cambias los tipos o usas `abi.encodePacked`, la raíz no coincide.

## Referencias

- [Merkle Patricia trie en ethereum.org](https://ethereum.org/es/developers/docs/data-structures-and-encoding/patricia-merkle-trie/)
- [Formatos de almacenamiento de Besu](https://besu.hyperledger.org/public-networks/concepts/data-storage-formats)
- [EIP-1186: método eth_getProof](https://eips.ethereum.org/EIPS/eip-1186)
- [MerkleProof de OpenZeppelin Contracts 5.x](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof)
- [Librería merkle-tree de OpenZeppelin](https://github.com/OpenZeppelin/merkle-tree)
