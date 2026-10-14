# Funciones hash

Una función hash es un algoritmo matemático que transforma cualquier cantidad de datos en una cadena de longitud fija. Según los bits del algoritmo, el SHA-256 es de 256 bits o 32 bytes. Cada byte permite dos números hexadecimales, es decir, representación de posición fija de 64 caracteres.

```text
SHA-256: 256 bits = 32 bytes = 64 caracteres hex
Input: "blockchain"
Output: ef7797e13d3a75526946a3bcf00daec9fc9c9c4d51ddc7cc5df888f74dd434d1
        |<---------------------- 64 caracteres ---------------------->|
```

El input alimenta a la función de hash y tiene como resultado el digest o digestión (como el hash de la comida). Es una función unidireccional: fácil calcular hash desde mensaje, imposible calcular mensaje desde hash.

## Historia y Evolución de las Funciones Hash

Las funciones hash criptográficas han evolucionado significativamente desde sus orígenes:

Década de 1970 - Fundamentos Teóricos:

El trabajo seminal de Merkle-Damgård en la década de 1970 sentó las bases para la construcción de funciones hash criptográficas. La construcción Merkle-Damgård divide el mensaje en bloques y los procesa iterativamente, creando una cadena de dependencias que garantiza que cualquier cambio en el input afecte al output final.

Década de 1990 - MD5 y SHA-1:

- MD5 (Message Digest Algorithm 5): Diseñado por Ronald Rivest en 1991, produce hashes de 128 bits. Ampliamente utilizado durante años, pero en 2004 se demostraron ataques de colisión prácticos: dos mensajes diferentes pueden producir el mismo hash. Actualmente obsoleto y no debe usarse.

- SHA-1 (Secure Hash Algorithm 1): Desarrollado por la NSA en 1995, produce hashes de 160 bits. En 2017, Google demostró el primer ataque de colisión práctico (SHAttered attack). Deprecado para usos criptográficos.

2001 - SHA-2:

Lanzado por la NSA, incluye variantes de diferentes longitudes:

- SHA-224 (224 bits)
- SHA-256 (256 bits) - el más usado en blockchain
- SHA-384 (384 bits)
- SHA-512 (512 bits)

SHA-256 es el estándar actual en Bitcoin y la mayoría de blockchains. No se conocen vulnerabilidades prácticas.

2012 - SHA-3 (Keccak):

Ganador de la competencia de hash organizada por NIST. Diseño completamente diferente basado en el principio de esponjas criptográficas, ofreciendo una alternativa robusta a SHA-2. Ethereum utiliza una variante llamada Keccak-256 (ligeramente diferente de SHA-3 estándar).

2020 - BLAKE3:

Algoritmo moderno extremadamente rápido, basado en BLAKE2 pero optimizado para paralelización. Diseñado para ser resistente a ataques cuánticos y mucho más eficiente que SHA-2.

## Propiedades Fundamentales

Una función hash criptográfica debe cumplir:

1. Determinismo:

Mismo input siempre produce mismo output. Esto es fundamental para verificación.

```text
SHA-256("bitcoin") = 6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b
# Siempre, en cualquier computadora, en cualquier momento
```

2. Resistencia a Preimagen (Unidireccionalidad):

Dado un hash H, es computacionalmente imposible encontrar un mensaje M tal que hash(M) = H. Esto protege contra ingeniería inversa.

3. Resistencia a Segunda Preimagen:

Dado un mensaje M1, es imposible encontrar otro mensaje M2 diferente tal que hash(M1) = hash(M2). Esto previene suplantación.

4. Resistencia a Colisiones:

Es computacionalmente imposible encontrar dos mensajes diferentes M1 y M2 tal que hash(M1) = hash(M2). Esta propiedad fue vulnerada en MD5 y SHA-1, por eso se consideran inseguros.

5. Efecto Avalancha:

Un cambio mínimo en el input produce un hash completamente diferente. Esto es crucial para detectar modificaciones.

```text
# Ejemplos del efecto avalancha con SHA-256:

Input: "blockchain"
Hash:  ef7797e13d3a75526946a3bcf00daec9fc9c9c4d51ddc7cc5df888f74dd434d1

Input: "Blockchain"  # Solo la 'B' mayúscula
Hash:  625da44e4eaf58d61cf048d168aa6f5e492dea166d8bb54ec06c30de07db57e1
       ^  Completamente diferente

Input: "blockchain "  # Un espacio al final
Hash:  8cc0f1f8c7c3c20ab7c8e5fa52d81f3c5a8d2b8a9c8f2e5c1f3c6a7b8c9d0e1f2
       ^  Totalmente distinto

Input: "blockchaio"   # Cambio de 'n' por 'o'
Hash:  3f9c4a8e6d2f1b5a7c8e9d0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
       ^  Hash radicalmente diferente
```

Este efecto avalancha garantiza que incluso la modificación más pequeña en un bloque de blockchain sea inmediatamente detectable.

## Aplicaciones en Blockchain

1. Encadenamiento de Bloques:

Cada bloque contiene el hash del bloque anterior, creando una cadena inmutable:

```text
Bloque 1:
- Datos: "Transacción A"
- Hash anterior: 0000000000000000
- Hash propio: abc123...

Bloque 2:
- Datos: "Transacción B"
- Hash anterior: abc123...  ← Hash del Bloque 1
- Hash propio: def456...

Bloque 3:
- Datos: "Transacción C"
- Hash anterior: def456...  ← Hash del Bloque 2
- Hash propio: ghi789...
```

Si alguien intenta modificar el Bloque 1:

1. Su hash cambiaría de `abc123...` a algo diferente
2. El Bloque 2 seguiría apuntando al hash antiguo `abc123...`
3. La cadena estaría rota y sería detectable inmediatamente
4. Para ocultar el cambio, el atacante debería recalcular todos los bloques posteriores
5. En una red descentralizada con miles de nodos, esto es prácticamente imposible

2. Proof of Work (Minería):

Los mineros buscan un nonce que produzca un hash que cumpla cierto objetivo (target). Por ejemplo, en Bitcoin el hash debe comenzar con cierto número de ceros:

```text
# Target: hash debe comenzar con 4 ceros
Hash("Bloque + nonce=1")    = 8a3f2c...  ✗ No válido
Hash("Bloque + nonce=2")    = 7b2e1d...  ✗ No válido
Hash("Bloque + nonce=3")    = 9c4f3e...  ✗ No válido
...
Hash("Bloque + nonce=42857") = 0000a1b2...  ✓ Válido!
```

3. Direcciones de Wallets:

Las direcciones criptográficas se derivan aplicando funciones hash a claves públicas:

- Bitcoin: RIPEMD-160(SHA-256(clave_pública))
- Ethereum: Keccak-256(clave_pública), tomando últimos 20 bytes

4. Verificación de Integridad:

Los hashes permiten verificar que archivos, transacciones o bloques no han sido alterados sin necesidad de comparar todo el contenido, solo el hash.

## Checksum

Valor calculado a partir de datos para detectar errores de transmisión o corrupción accidental. No es criptográficamente seguro, solo detecta errores aleatorios.

En blockchain, las direcciones incluyen checksum para prevenir errores de tipeo. Bitcoin usa Base58Check con 4 bytes de doble SHA-256. Ethereum usa EIP-55 con capitalización como checksum.

Más información: [Suma de verificación](https://es.wikipedia.org/wiki/Suma_de_verificaci%C3%B3n)
