# Identidad y protección de datos

Una red de la Administración tiene que identificar con garantías a quien participa en ella y, a la vez, no exponer datos personales en un registro que no se puede borrar.

## Identidad

La gestión de la identidad es un pilar crítico. Una red de la administración exige la identificación fehaciente de cada nodo y de cada actor que firma una transacción. Esto requiere la integración con esquemas de PKI (*Public Key Infrastructure*), certificados electrónicos cualificados y marcos de Identidad Digital Descentralizada (mediante *Verifiable Credentials* y *Decentralized Identifiers* - DIDs, alineados con el reglamento eIDAS2 y las listas de confianza TSL). La custodia y gestión del ciclo de vida de las claves privadas institucionales se convierte en un requisito de alta seguridad, dado que la firma criptográfica vincula jurídicamente a la organización en el *ledger*.

## Protección de datos

La arquitectura debe ser plenamente respetuosa con la normativa de protección de datos (RGPD). Una DLT inmutable no debe utilizarse como almacenamiento primario de datos de carácter personal o confidencial, ya que la replicación masiva y la imposibilidad de alteración entran en conflicto directo con los derechos de supresión («derecho al olvido») y rectificación. El patrón arquitectónico correcto consiste en registrar *on-chain* exclusivamente *hashes*, evidencias criptográficas, estados o compromisos (*commitments*), manteniendo los datos personales *off-chain* en los sistemas de gestión tradicionales sujetos a sus correspondientes controles de acceso y políticas de borrado.

De este modo, la DLT actúa como un notario digital distribuido: permite demostrar la existencia, la integridad y la secuencia temporal de un documento o evento sin necesidad de exponer información subyacente.
