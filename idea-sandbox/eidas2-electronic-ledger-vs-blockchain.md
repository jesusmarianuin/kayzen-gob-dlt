# ¿eIDAS2 mata por ley la implementación como blockchain?

eIDAS2 crea un nuevo servicio de confianza, el qualified electronic ledger, y a primera vista parece la entrada de la blockchain en el marco legal europeo. Pero el modelo legal exige que la confianza la respalde un prestador cualificado: el protocolo de la red no basta por sí solo. Este documento resume qué exige la ley, qué no regula y qué consecuencia tiene eso para una red blockchain.

## Qué exige la ley

La ley define el electronic ledger como "una secuencia de registros electrónicos de datos que garantiza su integridad y la exactitud de su orden cronológico". La definición es tecnológicamente neutra: no menciona nodos, consenso ni descentralización. Esos conceptos aparecen en los documentos técnicos de ETSI que analizan cómo aplicar la ley a los ledgers distribuidos, no en la ley.

Para que un ledger sea cualificado, y sus registros tengan presunción legal de integridad y orden, la ley exige que:

- Sea creado y gestionado por uno o varios prestadores cualificados de servicios de confianza (QTSP).
- Establezca el origen de los registros.
- Garantice un orden cronológico secuencial único de los registros.
- Registre los datos de forma que cualquier cambio posterior se detecte de inmediato.

Un ledger que no es cualificado no está prohibido ni pierde valor legal, pero no tiene esa presunción.

## De dónde sale la confianza

En una blockchain la confianza sale del protocolo. Muchos nodos independientes llegan a un consenso y ninguno controla el resultado por sí solo. Cuantos más nodos independientes hay, más difícil es manipular el ledger y menos depende la red de un único actor. ETSI lo recoge como una propiedad esencial de un ledger distribuido: sus propiedades "do not depend on a single point of failure in the functionality or security of a ledger service provider".

En eIDAS2 la confianza la respalda el QTSP. El prestador puede usar el protocolo para cumplir los requisitos de integridad y orden, pero la ley no lo acepta como garantía si no hay un prestador que responda. El QTSP es una entidad auditada, supervisada por un organismo nacional y responsable jurídicamente del servicio. ETSI EN 319 401, la norma con los requisitos generales para cualquier prestador, establece que el prestador sigue siendo el responsable aunque otras organizaciones hagan parte del trabajo, por ejemplo operar un nodo:

- El prestador mantiene la responsabilidad global aunque parte del servicio la ejecuten terceros (REQ-6.3-05 y REQ-7.1.1-08).
- Debe tener un acuerdo documentado con cualquier tercero que participe en el servicio (REQ-7.1.1-07).
- Debe definir la responsabilidad de esos terceros y obligarles a aplicar los controles que él exija (REQ-6.3-06).
- Su declaración de prácticas debe identificar las obligaciones de todas las organizaciones externas que soportan el servicio (REQ-6.1-04).

## Lo que eIDAS2 no regula

ETSI, el organismo europeo que redacta las normas técnicas de los servicios de confianza, analizó eIDAS2 frente a los ledgers distribuidos permisionados en el [informe ETSI GR PDL 017](https://www.etsi.org/deliver/etsi_gr/PDL/001_099/017/01.01.01_60/gr_PDL017v010101p.pdf) (julio de 2024). Sus conclusiones, en las tablas 2 y 3 y el apartado 6.1.2:

- "PDL is always multiparty. Whereas eIDAS 2 only addresses requirements of one QTSP". Un ledger distribuido siempre es de varias partes, pero eIDAS2 solo regula los requisitos de un prestador.
- "Decentralised decisions not addressed by eIDAS 2". La toma de decisiones descentralizada no está regulada.
- La lista de confianza identifica si un QTSP presta el servicio, pero "does not identify the PDL community", es decir, no identifica la comunidad de nodos.
- La rendición de cuentas se asegura frente a los requisitos de eIDAS2, "but not against PDL governance requirements", no frente a la gobernanza de la red.
- La naturaleza multiparte y la gobernanza de una comunidad de proveedores quedan "outside the scope of eIDAS 2".

ETSI propone completar la ley con una segunda capa de gobernanza para la comunidad de nodos, con reglas sobre consenso, admisión y auditoría de los operadores. En esa propuesta, los miembros de la comunidad son "Qualified Electronic Ledger Providers", y la lista de confianza sirve para comprobar si cada miembro cumple los requisitos del ledger cualificado.

El informe solo trata redes permisionadas. Las redes abiertas no entran en el análisis.

El informe no contempla nodos operados por organizaciones que no sean QTSP, como una universidad o un organismo público. Solo habla de comunidades de prestadores cualificados. No los prohíbe, pero tampoco los menciona.

## Quién puede operar los nodos

La ley no habla de nodos. Exige que el ledger lo creen y gestionen uno o varios QTSP. De ahí salen dos lecturas posibles, y las dos llevan al mismo sitio:

- Cada nodo es un proveedor del ledger y tiene que ser QTSP. Es el modelo que plantea ETSI. Los QTSP son pocos, porque cualificarse exige auditoría y supervisión, así que la red tendría pocos nodos.
- Los nodos los operan terceros que no son QTSP. En ese caso son terceros del servicio: necesitan un acuerdo con el prestador, aplican sus controles y responden ante él.

En los dos casos todos los nodos funcionan bajo la misma política de seguridad, los mismos controles y la misma cadena de responsabilidad. La independencia entre operadores, que es lo que da seguridad a una blockchain, queda muy reducida. Y una red homogénea tiende a compartir fallos: un error en una política o en un procedimiento común afecta a todos los nodos a la vez. La ley impone controles comunes, no un software único, pero la gobernanza es la misma para todos.

## Conclusión

eIDAS2 no prohíbe la blockchain, pero no la regula como modelo de confianza. Trata un ledger distribuido como el servicio de un prestador y deja fuera justo lo que distingue a una blockchain: las decisiones descentralizadas y la gobernanza entre participantes independientes. Así lo señala ETSI, el organismo que redacta las normas técnicas del propio reglamento.

La consecuencia práctica es que, en el servicio cualificado, el protocolo deja de ser la garantía y pasa a ser una herramienta del prestador, que es quien responde. Una blockchain cualificada acaba siendo una red de pocos operadores bajo las mismas normas y la misma responsabilidad, con un punto único de confianza legal en el prestador. Técnicamente sigue siendo una blockchain, pero pierde lo que la hace más segura que un sistema centralizado: muchos operadores independientes sin un responsable único.

El Reglamento (UE) 2025/2531 exige documentar la arquitectura, la gobernanza y los mecanismos de seguridad de los registros cualificados. Pero no he identificado una obligación explícita de diversidad de clientes, sistemas operativos o calendarios de actualización. ETSI EN 319 401 tampoco la pide. Al contrario, exige que los terceros apliquen los controles que fije el prestador.

eIDAS2 abre a las organizaciones una vía para que sus servicios tengan reconocimiento legal. Pero, en el caso de la blockchain, creo que comete un error grave. Pongamos que una entidad como Alastria obtiene la cualificación para un ledger sobre la red ISBE. Como responde de todo el servicio, es ella quien fija cómo se operan los nodos: requisitos claros, pero en la práctica todos aplican los mismos parches, las mismas actualizaciones, el mismo cliente y el mismo sistema operativo. El día que aparezca un exploit para esa combinación, caerán todos los nodos a la vez. ¿Diremos entonces que la blockchain no funciona? El fallo no sería de la tecnología, sino de un modelo que eliminó la diversidad que la hace segura.

Puedes refutar esta interpretación abriendo un issue en el repositorio, y cualquier comentario será atendido. Pero, de inicio, es la interpretación más plausible. Y a las pruebas me remito: EBSI, la infraestructura blockchain que impulsan la Comisión Europea y los Estados miembros, es una red permisionada cuyos nodos operan entidades públicas de los Estados, no prestadores cualificados. No funciona como un qualified electronic ledger. Es decir, la red blockchain de referencia de la propia Unión Europea, con muchos operadores independientes, no usa el modelo cualificado que define eIDAS2.


//todo  https://ebsi.eu/blog/ebsi-business-launch pesee a esto EBSI se lanza en PRO

Europa está construyendo un sistema de confianza jurídica, pero todavía tiene que demostrar que ese sistema puede aprovechar una descentralización efectiva sin neutralizar sus ventajas.

¿Podemos separar la confianza jurídica, la confianza criptográfica y la confianza en el operador de infraestructura?

## Referencias

- [Reglamento (UE) 2024/1183, eIDAS2](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento de Ejecución (UE) 2025/2531 sobre libros mayores electrónicos cualificados](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj)
- [Informe ETSI GR PDL 017 sobre ledgers distribuidos y servicios cualificados de eIDAS2](https://www.etsi.org/deliver/etsi_gr/PDL/001_099/017/01.01.01_60/gr_PDL017v010101p.pdf)
- [Norma ETSI EN 319 401, requisitos generales para prestadores de servicios de confianza](https://www.etsi.org/deliver/etsi_en/319400_319499/319401/02.03.01_60/en_319401v020301p.pdf)
