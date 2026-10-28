# De las tablillas cuneiformes al Cartulario: historia de la contabilidad y origen de las RJT

Post: <https://inza.blog/2026/10/23/de-las-tablillas-cuneiformes-al-cartulario-historia-de-la-contabilidad-y-origen-de-las-rjt/>

Fecha: 2026-10-23

El post recorre cinco mil años de registro contable para defender que lo que replica una blockchain es un libro diario (journal), no un libro mayor (ledger). También sostiene que buena parte de sus garantías se consiguen con firma electrónica y un registro fehaciente, incluso en un servidor centralizado.

En Mesopotamia, las fichas de arcilla guardadas en bullas selladas, con su contenido impreso en la superficie, ya eran un mecanismo de integridad, y las tablillas de Uruk y Ur III anotaban cada hecho con fecha, responsable, sello y archivo. Con los números indoarábigos llegó la partida doble a Italia, y Luca Pacioli la sistematizó en 1494 con tres libros: memorial, diario y mayor. En España, la Pragmática de Cigales (1549) la hizo obligatoria.

La partida doble anota cada hecho en el debe y en el haber por el mismo importe, así que el cuadre es un control de integridad incorporado al método, de la familia de la prueba del nueve o el CRC. Como ellos, no resiste la manipulación intencionada, para la que hacen falta hash criptográfico, sellos de tiempo y firma.

El diario registra los asientos en orden cronológico y no se borran; el mayor es una vista derivada por cuentas. El Código de Comercio exige el diario, no el mayor, porque lo que tiene valor probatorio es el orden.

Antes de Bitcoin ya existían casi todas las piezas: tarjetas, SWIFT, SEPA, el dinero electrónico de Chaum, el sellado de tiempo encadenado de Haber y Stornetta y la prueba de trabajo de Hashcash. En España, el proyecto PISTA (2002) gestionaba letras de cambio electrónicas con una fuente de verdad centralizada que garantizaba la «unicidad de fin», el mismo problema que el doble gasto ([Antecedentes de Blockchain en España](https://judiciaryblockchain.org/2017/08/31/antecedentes-de-blockchain-en-espana/)).

El Reglamento eIDAS 2 y el [Reglamento de Ejecución (UE) 2025/2531](https://www.boe.es/doue/2025/2531/L00001-00007.pdf) hablan de «libros mayores electrónicos», ya tratados en la entrada sobre [servicios cualificados con orden cronológico (qDLT)](https://inza.blog/2026/09/18/de-la-conservacion-cualificada-de-firmas-y-sellos-a-los-servicios-cualificados-de-archivo-con-orden-cronologico-qdlt/). Pero una cadena de bloques es una sucesión cronológica de asientos encadenados por hash, y cada nodo calcula el mayor a partir de ella. De ahí el término RJT, Replicated Journal Technology ([Blockchaintrust](http://blockchaintrust.eu/rjt-replicated-journal-technologies-como-llamar-a-blockchain/), [No es DLT: es RJT](https://inza.blog/2019/06/15/no-es-dlt-es-rjt/)).

Bajo blockchain hay dos técnicas: la firma electrónica, que acredita quién autoriza cada operación, y una fuente de verdad que fija el orden y resuelve contradicciones, como el protocolo notarial con su matriz. El consenso sustituye a un tercero de confianza; cuando existe un prestador cualificado, basta un registro centralizado con firmas, sellos de tiempo y encadenamiento de hash ([registros con orden cronológico en eIDAS 2.0](https://judiciaryblockchain.org/2024/07/07/eidas-2-0-el-reconocimiento-europeo-de-los-registros-electronicos-con-orden-cronologico-y-un-nuevo-recurso-para-la-justicia-digital/), [unicidad de fin](https://judiciaryblockchain.org/2021/04/15/unicidad-de-fin-en-el-documento-electronico/)).

El autor propone SJT, Signed Journal Technology: firma electrónica más un diario que actúa como fuente de verdad. Admite una variante centralizada y otra replicada (RJT), de la que blockchain es un caso concreto; en un texto jurídico, el equivalente sería «diario fehaciente». Como ejemplo cita el Cartulario de EADTrust, un registro centralizado de titularidad y estado de documentos con sellos de tiempo al milisegundo, que hoy se presta como servicio no cualificado.

En una frase: blockchain replica un diario firmado y no un mayor, y sus garantías pueden obtenerse con firma electrónica y una fuente de verdad centralizada operada por un prestador de confianza.

---
