# Identidad en la red

La red solo comprueba que una transacción está firmada con una clave. No sabe qué órgano responde de esa firma, ni quién tomó la decisión, ni si tenía competencia para tomarla. Diseñar la identidad consiste en unir esas piezas sin llenar el *ledger* de personas identificables.

## Cómo identifica la red

Cada participante tiene una clave privada, con la que firma, y una clave pública, con la que se comprueba la firma. La cuenta, o dirección, es un [identificador que se obtiene de la clave pública](https://www.aepd.es/guias/nota-tecnica-blockchain.pdf). El *ledger* solo guarda esa dirección: ni nombres ni cargos.

## Quién es quién

Una actuación en la red implica hasta cinco identidades distintas:

- Nodo: la máquina que participa en la red. En un validador QBFT, [la dirección del nodo es la dirección del validador](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft).
- Cuenta remitente: la dirección que firma la transacción. Es la única que aparece como autora.
- Órgano o Administración: quien responde jurídicamente. Puede [identificarse con un sello electrónico](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566#a40), basado en un certificado reconocido o cualificado que incluye su NIF y su denominación.
- Empleado público: la persona que actúa por el órgano. Fuera de las actuaciones automatizadas, la Administración actúa con la [firma del titular del órgano o del empleado](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566#a43).
- Ciudadano: el interesado en el procedimiento. La Administración [debe verificar su identidad](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a9), lo que no significa que tenga que figurar en la red.

## Quién firma la transacción

### Cuenta del órgano

Una aplicación del órgano firma con una clave institucional. Si no interviene directamente un empleado público, es una [actuación administrativa automatizada](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566#a41): hay que fijar antes qué órgano define y supervisa el sistema, y cuál responde a efectos de impugnación.

La dirección no identifica a ninguna persona y no cambia cuando cambia la plantilla. A cambio, el *ledger* no muestra quién decidió, de modo que ese dato debe quedar en los sistemas del órgano.

### Cuenta por empleado

Cada empleado firma con su propia clave. El *ledger* muestra quién actuó, pero la dirección [pasa a ser un dato personal](data-protection.md) y hay que dar y retirar permisos cada vez que alguien cambia de puesto.

### Cuenta del órgano y acto firmado fuera

El empleado firma el acto en el sistema del órgano, con su firma electrónica habitual, y la cuenta del órgano registra después la operación en la red. El acto mantiene su validez ordinaria, y la red aporta el registro compartido.

Es la opción que menos datos personales expone, porque separa dos firmas con funciones distintas: la del acto, que expresa la decisión, y la de la transacción, que la registra. Exige poder relacionar ambas sin publicar la identidad del firmante.

### Cuenta del ciudadano

El ciudadano firmaría directamente en la red. Su dirección sería un dato personal que [enlaza toda su actividad](https://www.aepd.es/guias/nota-tecnica-blockchain.pdf), así que no suele tener sentido en un registro permanente.

Lo habitual es que actúe a través del procedimiento y que el órgano registre el resultado. Si tiene que acreditar algo, puede presentar una credencial verificable, una declaración digital firmada por su emisor. EBSI, por ejemplo, identifica a las personas físicas con [`did:key`](https://hub.ebsi.eu/vc-framework/did/natural-person), un método que no describe ningún registro en el *ledger*.

## Cómo se une la dirección con el órgano

La dirección no dice a quién pertenece, y sin esa unión la firma no vincula a nadie. Hay dos vías:

### Registro propio

Un contrato guarda qué dirección corresponde a cada órgano. El alta se decide en la [gobernanza](network-governance.md) y se apoya en una declaración firmada con el sello electrónico del órgano. Es sencillo, pero el formato solo sirve dentro de esta red.

### Identificador descentralizado

Un identificador descentralizado (DID) es un identificador estándar asociado a un documento que indica qué claves puede usar su titular. En [`did:ebsi`](https://hub.ebsi.eu/docs/onboarding/legal-entity/did-ebsi-method), el método de EBSI para entidades jurídicas, ese documento se gestiona en el *ledger*. Es interoperable, pero añade una dependencia de ese método y de su evolución.

En cualquiera de los dos casos, tener la clave no otorga competencia. Un contrato puede comprobar que quien firma tiene un rol, pero no que el órgano sea competente para ese acto.

## Qué ocurre cuando cambia una clave

Como la dirección se obtiene de la clave, cambiar de clave significa cambiar de dirección. La nueva cuenta no hereda nada por sí sola: ni permisos, ni roles en los contratos, y empieza su propio [*nonce*](transaction-ordering.md). Por eso la identidad estable no puede ser la dirección.

Para mantenerla, los permisos se asocian a un identificador que no cambia, y ese identificador apunta a la clave vigente. [`did:ebsi` lo hace así](https://hub.ebsi.eu/vc-framework/guidelines/didr): permite añadir, revocar o caducar claves y conserva un registro cronológico. [ERC-1056](https://eips.ethereum.org/EIPS/eip-1056) sigue la misma idea, con un identificador fijo cuyo propietario puede cambiar, aunque es una propuesta estancada.

### Rotación planificada

La clave se sustituye por rutina. Se añade la nueva, se traspasan los permisos y se retira la antigua. Lo ya firmado no se ve afectado: según el [estándar DID](https://www.w3.org/TR/did-1.0/), la rotación no afecta a las firmas hechas con claves que ya no están en el documento, aunque comprobarlas puede exigir consultar su historial. EBSI [permite consultar el documento en una fecha concreta](https://hub.ebsi.eu/docs/onboarding/legal-entity/did-ebsi-method) y lo exige para validar una credencial en la fecha de su emisión.

### Clave comprometida

Alguien más pudo usar la clave. La revocación [no es retroactiva](https://www.w3.org/TR/did-1.0/): impide usarla en adelante, pero no invalida por sí sola lo anterior. El orden del *ledger* muestra qué se firmó antes y después de revocar, pero no separa lo legítimo de lo fraudulento en el periodo anterior. El órgano tiene que revisar ese periodo y [registrar las correcciones](transaction-ordering.md).

El plan para este caso debe existir antes del incidente: quién puede revocar, en qué plazo y con qué clave, ya que la comprometida no sirve para ello.

### Clave de un validador

Como la dirección del nodo es la del validador, cambiar la clave equivale a sustituir un validador por otro. Los validadores [votan el alta y la baja](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft), y conviene dar de alta el nuevo antes de retirar el antiguo: con cuatro validadores, retirar uno primero deja la red sin margen para tolerar fallos. Este procedimiento se deduce de cómo funcionan los validadores, así que debe ensayarse en la [red de pruebas](besu-design-challenges.md).

### Clave de un ciudadano

Con `did:key` el identificador [se deriva de la clave y no admite actualizaciones](https://hub.ebsi.eu/vc-framework/did/natural-person). Una clave nueva supone un identificador nuevo, y no hay nada que cambiar en el *ledger*.

## Custodia de las claves

Las claves deben guardarse en un [medio seguro](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf), con medidas también frente a cuentas comprometidas o empleados desleales. Lo habitual es usar un HSM, un dispositivo que guarda la clave y firma sin dejarla salir.

La clave de cada tipo se custodia de forma distinta:

- Clave de nodo o validador: Besu puede [guardarla en un HSM mediante un módulo de seguridad](https://docs.besu-eth.org/private-networks/how-to/configure/consensus/qbft).
- Clave de cuenta: se puede firmar fuera del nodo con un servicio como [Web3Signer](https://docs.web3signer.consensys.com/how-to/store-keys), que admite almacenes externos de claves.

Hay que decidir pronto la curva criptográfica. Besu usa `secp256k1` por defecto y [admite `secp256r1` en acceso anticipado](https://docs.besu-eth.org/private-networks/how-to/configure/curves), con la misma curva en todos los nodos. Si la curva se elige por compatibilidad con los dispositivos de firma de la Administración, hay que comprobar el resto de la cadena: [Web3Signer documenta firma de transacciones con `secp256k1`](https://docs.web3signer.consensys.com/), no con `secp256r1`.

## Cuestiones abiertas

Estas cuestiones deben resolverse antes del diseño final:

- Si la firma de una transacción puede considerarse por sí sola un sello electrónico, o si el valor jurídico debe venir siempre de un acto firmado fuera de la red.
- Si los prestadores de certificados cualificados y sus dispositivos admiten la curva elegida.
- Cómo se relaciona el acto firmado con la transacción sin revelar datos personales, lo que se trata en [protección de datos](data-protection.md).
