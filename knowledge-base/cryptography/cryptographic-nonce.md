# Nonce criptográfico

Number that can be only used once (número que solo puede usarse una vez).

Número aleatorio y a poder ser único, usado una sola vez destinado en un protocolo de autenticación para que autenticaciones antiguas no puedan re-usarse en replay attacks. Básicamente es una semilla o valor único que comunica el servidor al cliente para que sea usado en una autenticación.

Usos en blockchain:

Autenticación: el servidor envía nonce al cliente, quien debe incluirlo en respuesta firmada para prevenir replay attacks.

Firma ECDSA: el nonce k debe ser único por cada firma. Si se reutiliza, la clave privada puede ser extraída. Crítico para seguridad.

Proof of Work: en minería Bitcoin, el nonce es el valor que mineros incrementan buscando un hash válido que cumpla el target de dificultad.

Transacciones: en Ethereum, el nonce de cuenta es contador secuencial que previene replay de transacciones.

Más información: [Cryptographic nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce)
