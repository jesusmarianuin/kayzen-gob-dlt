# De la conservación cualificada de firmas y sellos a los servicios cualificados de archivo con orden cronológico (qDLT)

Post: <https://inza.blog/2026/09/18/de-la-conservacion-cualificada-de-firmas-y-sellos-a-los-servicios-cualificados-de-archivo-con-orden-cronologico-qdlt/>

Fecha: 2026-09-18

El 14 de septiembre de 2026, en la sesión abierta de ETSI ESI para autoridades de certificación en Tallin, el autor sustituyó a Steffen Schwalm en un panel sobre la normalización de las DLT y del qDLT, el registro distribuido cualificado. Su tesis: el qDLT no es una revolución que llega de fuera, sino el tercer peldaño de una escalera que Europa lleva casi una década construyendo.

Primer peldaño, la conservación de firmas y sellos cualificados:

- ETSI TS 119 511 (política y seguridad) y TS 119 512 (protocolos), con el CIR 2025/1946 como acto de ejecución
- Mantiene viva la evidencia criptográfica frente a la caducidad de certificados y el envejecimiento de algoritmos, con nuevos sellos de tiempo o hashes encadenados
- Es una máquina para migrar de algoritmos, de ahí su relación con la criptoagilidad y la criptografía postcuántica

Segundo peldaño, el archivo electrónico cualificado, nuevo en eIDAS2:

- CEN/TS 18170 y el CIR 2025/2532 (artículo 45 undecies)
- Custodia el documento, esté firmado o no: integridad, legibilidad, trazabilidad de accesos y retención
- Se apoya en la conservación, no compite con ella, y migra de formatos igual que la conservación migra de algoritmos

Tercer peldaño, el registro electrónico cualificado:

- CEN/TS 18264 y el CIR 2025/2531 (artículo 45 terdecies)
- El autor lo define como un archivo de orden cronológico: garantiza que ninguna entrada se inserte, borre o reordene sin que se note
- Ese orden puede construirlo un único prestador o una red de nodos que acuerdan la secuencia; en el segundo caso, prestado como servicio cualificado, es un qDLT
- El CIR 2025/2531 exige a todos ETSI EN 319 401 y, a la variante distribuida, además ISO 23257:2022 (arquitectura de referencia DLT) e ISO/TS 23635:2022 (gobernanza)
- EBSI, gobernada por el Europeum-EDIC, muestra que la distribución es compatible con la confianza cualificada si los nodos los operan entidades identificadas con anclas gubernamentales

El autor propone llamarlo RJT (Replicated Journal Technology): en contabilidad, el orden cronológico se guarda en el libro diario (journal), no en el mayor (ledger).

Si el registro guarda también la titularidad, el estado y las relaciones de cada documento, habilita tres funciones:

- Transferibilidad o endosabilidad: anotar cambios de titular, como en los títulos de mercancías
- Obliterabilidad o cancelabilidad: anotar que un derecho se consumió, como una entrada o un matasellos, sin borrar la evidencia
- Completitud o "grapa electrónica": mantener unidos y en orden un documento, sus anexos y sus versiones

El patrón es el de las anotaciones en cuenta del mercado de valores. El servicio Cartulario de EADTrust se diseñó con esas premisas y añade sellos de tiempo con precisión de un milisegundo en cada solicitud. Hoy es un servicio no cualificado, pendiente de auditoría ([más información](https://www.eadtrust.eu)).

Un registro cronológico cualificado, centralizado o qDLT, puede servir de ancla de confianza para la EUDI Wallet y las declaraciones de atributos. La criptografía postcuántica hace esta arquitectura más necesaria.

En una frase: el qDLT es la tercera capa de una evolución normativa que va de conservar firmas a archivar documentos y a ordenar hechos de forma verificable, con normas ISO de DLT para la variante distribuida.

---
