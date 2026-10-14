# Certificados digitales

En criptografía asimétrica se utilizan soportes como X.509 o GPG llamados certificados, con estructura definida que contiene atributos específicos.

## Componentes de un Certificado

Un certificado digital contiene:

### Algoritmos

Algoritmo de hash y de firma (típicamente SHA-256 con RSA o ECDSA). Algoritmo y hash de cifrado utilizados para las operaciones criptográficas.

### Propósitos (Key Usage)

Define para qué puede usarse el certificado: firma digital, cifrado de datos, firma de certificados (solo CAs), autenticación de servidor/cliente, firma de código.

### Identificación

Sujeto: identifica al propietario del certificado (nombre, organización, email). Emisor: identifica a la Autoridad Certificadora que firmó el certificado. Número de serie: identificador único del certificado.

### Huella Digital

Hash generado en base a todo el contenido del certificado (incluido firmas de los emisores). SUPER importante para verificar autenticidad.

```text
# Ejemplo de huella digital SHA-256
59:3A:FB:72:44:49:1C:F7:E3:6E:41:B4:25:9F:87:3D...
```

### Validez y Revocación

Caducidad: fechas de inicio y expiración del certificado. Métodos de comprobación de revocación: CRL (Certificate Revocation List) y OCSP (Online Certificate Status Protocol).

### Claves

Clave privada: mantenida en secreto por el propietario. Clave pública: distribuida libremente en el certificado.

## Modelo de Confianza

El emisor firma el certificado para darle autenticidad si confiamos en una PKI con CA (Public Key Infrastructure con Certificate Authority).

Si no confiamos en la PKI, debemos confiar en el valor de la huella digital como auténtico, verificándola por un canal secundario confiable (en persona, teléfono, mensaje firmado previamente conocido).
