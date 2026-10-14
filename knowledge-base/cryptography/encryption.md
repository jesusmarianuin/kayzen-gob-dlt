# Cifrado

## Tipos de Criptografía

### Criptografía Simétrica

Utiliza la misma clave para cifrar y descifrar. Ambas partes deben compartir la clave secreta previamente.

#### Cifrado por Bloques

Divide el mensaje en bloques de tamaño fijo y cifra cada bloque independientemente. Algoritmos comunes incluyen DES (obsoleto), 3DES (lento pero más seguro), y AES (estándar actual con claves de 128, 192 o 256 bits).

AES es el más utilizado actualmente por su balance entre seguridad y rendimiento. Opera en bloques de 128 bits y AES-256 es prácticamente imposible de romper por fuerza bruta.

#### Cifrado por Flujo

Cifra el mensaje bit a bit o byte a byte usando un flujo de claves pseudo-aleatorio. RC4 fue popular pero ahora es inseguro. ChaCha20 es moderno y eficiente, usado en TLS 1.3 y VPNs modernas.

### Criptografía Asimétrica

La más común por su versatilidad. Distribuye clave pública para funciones unidireccionales: lo que se cifra con una clave solo se puede descifrar con la otra.

Utiliza un par de claves matemáticamente relacionadas: clave pública (compartida abiertamente) y clave privada (mantenida en secreto). Este sistema resuelve el problema de distribución de claves. Puedes publicar tu clave pública libremente, y cualquiera puede usarla para enviarte mensajes cifrados que solo tú puedes descifrar con tu clave privada.

Algoritmos principales:

#### RSA (Rivest-Shamir-Adleman)

Basado en la dificultad de factorizar números primos grandes. Tamaños de clave típicos son 2048 o 4096 bits. Ampliamente usado para cifrado y firmas digitales en PKI tradicional.

#### ECDSA (Elliptic Curve Digital Signature Algorithm)

Basado en matemática de curvas elípticas. Una clave ECDSA de 256 bits tiene seguridad equivalente a RSA de 3072 bits. Es determinista en generación de clave pública en base a privada. Usado en Bitcoin, Ethereum, y la mayoría de certificados SSL/TLS modernos.

#### EdDSA (Edwards-curve Digital Signature Algorithm)

Variante moderna diseñada para evitar vulnerabilidades de implementación. Determinista, resistente a timing attacks. Usado en Solana, Polkadot, Cardano, y SSH moderno (ed25519).

## Cifrado Asimétrico

Se genera una serialización cifrada del contenido usando la clave pública del destinatario, para que el receptor pueda descifrarlo con su clave privada.

Algoritmo típico: SHA para hashing y RSA o ECDH para cifrado. Usado cuando necesitas enviar datos confidenciales a alguien sin haber compartido claves previamente.

## Casos de Uso por Algoritmo

Resumen de cuándo usar cada tipo:

### Firma y Cifrado con Simétrica

Si quieres firmar y cifrar es típico 3DES en simétrica, aunque AES-256 es preferible actualmente por rendimiento.

### Cifrar y Firmar con Asimétrica

Si es cifrar y firmar con asimétrica: RSA o ECDSA. ECDSA es determinista en generación de clave pública en base a privada, lo que lo hace ideal para blockchain.

### Solo Cifrado Simétrico

Si es cifrar y descifrar solo: AES con clave simétrica. AES-256-GCM es el estándar recomendado actualmente.
