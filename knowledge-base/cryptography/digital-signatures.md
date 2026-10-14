# Firma digital

Se genera hash del contenido y se cifra con la clave privada. Como resultado está la cadena cifrada y la parte pública para su descifrado.

Propósito: mantener autenticidad e integridad del mensaje. También no repudio porque solo está en posesión del emisor firmante, siempre que incluya marca de tiempo.

Algoritmo típico: SHA para hash y RSA para cifrado de firma. En blockchain se usa SHA-256 o Keccak-256 con ECDSA.

Proceso:

1. Genera hash del mensaje (ej: SHA-256)
2. Cifra el hash con clave privada, produciendo la firma
3. Distribuye mensaje + firma + clave pública
4. Receptor descifra firma con clave pública y compara hashes

## ECDSA en Blockchain

Algoritmo de firma de curva elíptica (ECDSA). La clave pública se crea a partir de la clave privada: ECDSA es el algoritmo de curva elíptica que se utiliza en el protocolo Bitcoin para crear un par de claves privada y pública. La clave pública ECDSA se deriva de la clave privada, pero no se puede hacer el proceso inverso de derivar la clave privada a partir de la clave pública.

### Características Únicas

Este algoritmo es diferente a otros: permite generar (solo en esta dirección) en base a la private key el public key, y en base al public key la address.

Con la private key solo, es posible obtener los 2 elementos restantes (public key y addresses), varias de ellas. La generación es estrictamente unidireccional y determinista.

### Relación entre Claves y Direcciones

Relación 1:1 entre private key, public key y address en uso normal.

Pero en firma múltiple (multisig): una misma address tiene varias public keys asociadas. Sin embargo, para tu firma específica solo tienes una private key.

### Proceso de Generación

1. Private key: número aleatorio de 256 bits (debe generarse con fuente segura de entropía)
2. Public key: punto en curva elíptica = private_key × G (G es punto generador de la curva)
3. Address: hash de la public key

En Bitcoin: RIPEMD-160(SHA-256(public_key)) + prefijos + checksum, codificado en Base58Check.

En Ethereum: Keccak-256(public_key), tomando últimos 20 bytes, codificado en hexadecimal con EIP-55 checksum.

### Firma y Verificación

Para firmar transacción:

1. Hash del mensaje (transacción)
2. Generar nonce k único y aleatorio (CRÍTICO: debe ser único)
3. Calcular punto R = k × G en la curva
4. Calcular firma (r, s) usando matemática de curva elíptica

El nonce k DEBE ser único para cada firma. Reutilizarlo permite a un atacante extraer la clave privada matemáticamente. Esto causó el hack de PlayStation 3 y pérdidas de Bitcoin.

Para verificar:

Cualquiera puede verificar la firma con mensaje, firma (r, s) y clave pública. No necesitas clave privada para verificar, solo la pública. Esto es fundamental en blockchain: todos los nodos pueden verificar transacciones sin conocer claves privadas.
