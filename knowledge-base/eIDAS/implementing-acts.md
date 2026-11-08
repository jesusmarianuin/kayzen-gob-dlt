# Actos de ejecución de eIDAS2

eIDAS2 establece las reglas generales del ecosistema de identidad digital europeo. Define qué es una cartera europea, qué servicios de confianza existen, qué garantías deben ofrecer y qué responsabilidades tienen los diferentes participantes, pero no desarrolla todos estos detalles. Los actos de ejecución son los documentos que concretan cómo deben cumplirse esas obligaciones.

Esto permite que los requisitos técnicos puedan evolucionar sin tener que modificar todo el reglamento principal cada vez que cambia una especificación.

> [Aclaración sobre las características de los actos de ejecución](#características-de-los-actos-de-ejecución).

Si desarrollas una cartera, no puedes limitarte a implementar las funcionalidades que consideres suficientes, porque debe estar certificada. El artículo 5 quater del Reglamento 910/2014 impone esa certificación y el [Reglamento de Ejecución (UE) 2024/2981](https://eur-lex.europa.eu/eli/reg_impl/2024/2981/oj) desarrolla sus requisitos y procedimientos.

Otro ejemplo es el [Reglamento de Ejecución (UE) 2024/2982](https://eur-lex.europa.eu/eli/reg_impl/2024/2982/oj), que establece los protocolos e interfaces que deben utilizarse para determinadas comunicaciones entre las carteras y los servicios que interactúan con ellas.

Para orientarse en esas especificaciones, la [DG CONNECT](dg-connect.md) publica guías cuando es relevante, como la [ARF (Architecture and Reference Framework)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework). No es una ley ni un estándar: se alinea con los actos de ejecución y da una visión de conjunto de lo que piden, así que seguirla facilita cumplirlos, pero no lo garantiza, porque el cumplimiento se comprueba contra el acto. Si difieren, manda el acto, y las especificaciones de la ARF solo obligan cuando un acto las incorpora como requisitos de referencia.

Por tanto, al desarrollar una solución EUDI conviene distinguir entre:

- La normativa obligatoria.
- Los estándares técnicos que la normativa incorpora o utiliza como referencia.
- Las especificaciones de arquitectura que sirven de orientación para implementar el ecosistema.

> Como se aclara en [por qué eIDAS2 depende de los actos de ejecución](#por-qué-eidas2-depende-de-los-actos-de-ejecución), seguirlos es un trabajo periódico para saber si hay cambios.

## Los estándares técnicos y su importancia

Muchos actos de ejecución hacen referencia a estándares publicados por [organismos de normalización](standardization-bodies.md) como ETSI, CEN/CENELEC o ISO.

Estos estándares contienen especificaciones técnicas que permiten implementar sistemas de forma interoperable y con requisitos comunes.

Por ejemplo, un acto puede exigir que un servicio utilice un determinado estándar ETSI para implementar una funcionalidad de seguridad.

En ese caso, el estándar deja de ser simplemente una recomendación técnica para convertirse en una referencia normativa que debe tenerse en cuenta al implementar el servicio.

Si la norma lo prevé, cumplir un estándar citado permite presumir que se cumplen los requisitos que ese estándar cubre, pero no todo eIDAS2.

Al usar una norma citada hay que tener en cuenta dos cautelas:

- Cada acto de ejecución fija una versión concreta de cada norma, y a veces adaptaciones. Hay que comprobarla en el [DOUE](https://eur-lex.europa.eu/oj/direct-access.html?locale=es) antes de usar la referencia en un pliego o una auditoría.
- El propio DOUE ha publicado algunas normas con el número mal escrito. Esos códigos no corresponden a ninguna norma tal cual, así que para usarlos hay que deducir a cuál se refiere realmente el acto de ejecución.

Esto también afecta a las auditorías y certificaciones. Los organismos responsables comprueban que los servicios cumplen los requisitos aplicables, utilizando las normas y especificaciones de referencia que correspondan.

## Dónde consultar las reglas técnicas

No hace falta recorrer EUR-Lex reglamento a reglamento. Según lo que se desarrolle, estos son los puntos de partida.

### Lista oficial de actos de ejecución

La Comisión Europea mantiene una página con los actos de ejecución de eIDAS2. Para cada uno indica el artículo que desarrolla, su estado (adoptado o en consulta) y el enlace a su texto en EUR-Lex. Es la referencia para comprobar si un acto se ha aprobado o modificado.

- [Lista de actos de ejecución de eIDAS2 (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation)

Igualmente, el desarrollador puede guiarse por otros referentes en la materia que comparten sus trabajos, como esta [lista de actos de ejecución de eIDAS2 y de las normas que citan](https://inza.blog/2026/08/30/los-actos-de-ejecucion-de-eidas2-al-dia-y-las-normas-etsi-y-cen-que-citan-the-eidas2-implementing-acts-up-to-date-and-the-etsi-and-cen-standards-they-cite/) y sobre todo [los actos de ejecución al día](https://inza.blog/2026/08/30/los-actos-de-ejecucion-de-eidas2-al-dia-y-las-normas-etsi-y-cen-que-citan-the-eidas2-implementing-acts-up-to-date-and-the-etsi-and-cen-standards-they-cite/).

### Cartera EUDI

Los actos de ejecución de la cartera fijan los requisitos obligatorios y remiten a estándares y especificaciones técnicas. Para el desarrollo, la documentación de referencia está en dos repositorios oficiales:

- [Architecture and Reference Framework (ARF)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework): arquitectura de referencia de la cartera.
- [Estándares y especificaciones técnicas (STS)](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications): relaciona cada estándar o especificación técnica con el acto de ejecución que lo exige.

Los actos de ejecución básicos de la cartera son:

- [Reglamento de Ejecución (UE) 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj): datos de identificación personal y atestaciones electrónicas de atributos.
- [Reglamento de Ejecución (UE) 2024/2979](https://eur-lex.europa.eu/eli/reg_impl/2024/2979/oj): integridad y funcionalidades básicas.
- [Reglamento de Ejecución (UE) 2024/2980](https://eur-lex.europa.eu/eli/reg_impl/2024/2980/oj): notificaciones a la Comisión sobre el ecosistema de la cartera (marco de confianza).
- [Reglamento de Ejecución (UE) 2024/2981](https://eur-lex.europa.eu/eli/reg_impl/2024/2981/oj): certificación.
- [Reglamento de Ejecución (UE) 2024/2982](https://eur-lex.europa.eu/eli/reg_impl/2024/2982/oj): protocolos e interfaces.

El [Reglamento de Ejecución (UE) 2026/1731](https://eur-lex.europa.eu/eli/reg_impl/2026/1731/oj) modifica los reglamentos 2024/2977, 2024/2979, 2024/2980 y 2024/2982, así que hay que leerlos junto con esa modificación.

Otros actos de 2026 que afectan a la cartera:

- [Reglamento de Ejecución (UE) 2026/798](https://eur-lex.europa.eu/eli/reg_impl/2026/798/oj): alta remota en la cartera hasta el nivel de seguridad alto.
- [Reglamento de Ejecución (UE) 2026/1730](https://eur-lex.europa.eu/eli/reg_impl/2026/1730/oj): registro de las partes usuarias.
- [Reglamento de Ejecución (UE) 2026/1735](https://eur-lex.europa.eu/eli/reg_impl/2026/1735/oj): atestaciones electrónicas cualificadas de atributos.

### Libros mayores electrónicos (Electronic Ledgers)

El [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj) fija las normas de referencia y especificaciones aplicables a los libros mayores electrónicos cualificados introducidos por eIDAS2. Se dirige a los prestadores cualificados de servicios de confianza (QTSP) que ofrezcan este servicio y concreta requisitos de seguridad, de origen e integridad de los registros, de orden cronológico y de mecanismos criptográficos. Cumplir su anexo da presunción de cumplimiento (artículo 45 terdecies, apartado 2), aunque el QTSP puede demostrarlo con otras prácticas.

Lo que garantiza un libro mayor cualificado es el origen de los registros, su orden cronológico y su integridad, de modo que ninguna entrada puede insertarse, borrarse o reordenarse sin que se detecte. Por eso el artículo 45 duodecies, apartado 2, otorga a sus registros la presunción de que su orden cronológico es exacto y de que están íntegros.

El reglamento no exige una blockchain. El orden puede construirlo un único prestador, en un registro centralizado, o una red de nodos que acuerdan la secuencia. El reglamento llama a la variante distribuida "libro mayor electrónico distribuido cualificado", y también se conoce como qDLT.

Las normas de referencia dependen de esa variante:

- Todos los libros mayores cualificados: ETSI EN 319 401, requisitos generales de los prestadores de servicios de confianza, y perfiles AdES adaptados para firmas y sellos.
- Solo la variante distribuida, además: ISO 23257:2022, arquitectura de referencia de blockchain y DLT, e ISO/TS 23635:2022, gobernanza de blockchain y DLT.

CEN ha publicado además la especificación técnica CEN/TS 18264:2026, dedicada a los libros mayores electrónicos. Es posterior al reglamento y este no la cita.

Como el servicio lo presta un QTSP, también le aplican los actos horizontales de los servicios de confianza cualificados:

- [Reglamento de Ejecución (UE) 2025/2530](https://eur-lex.europa.eu/eli/reg_impl/2025/2530/oj): requisitos de cumplimiento y seguridad de los prestadores cualificados.
- [Reglamento de Ejecución (UE) 2025/1572](https://eur-lex.europa.eu/eli/reg_impl/2025/1572/oj): inicio de la prestación de servicios de confianza cualificados.
- [Reglamento de Ejecución (UE) 2025/2162](https://eur-lex.europa.eu/eli/reg_impl/2025/2162/oj): acreditación de los organismos de evaluación de la conformidad; su anexo II reúne las normas con las que se evalúa cada servicio cualificado.

Conviene distinguir el libro mayor de otros dos servicios cualificados cercanos:

- Conservación de firmas y sellos cualificados ([Reglamento de Ejecución (UE) 2025/1946](https://eur-lex.europa.eu/eli/reg_impl/2025/1946/oj)): mantiene válida la evidencia criptográfica cuando caducan los certificados o envejecen los algoritmos.
- Archivo electrónico cualificado ([Reglamento de Ejecución (UE) 2025/2532](https://eur-lex.europa.eu/eli/reg_impl/2025/2532/oj)): custodia el documento, esté firmado o no, con integridad, legibilidad, trazabilidad de accesos y retención.
- Libro mayor electrónico cualificado (Reglamento de Ejecución (UE) 2025/2531): fija un orden cronológico verificable de los hechos registrados.

Referencias oficiales y documentación técnica:

- [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj) — requisitos técnicos de los libros mayores electrónicos cualificados.
- [Reglamento (UE) 910/2014, versión consolidada tras eIDAS2](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018) — artículos 45 duodecies y 45 terdecies, sobre los efectos jurídicos y los requisitos de los libros mayores electrónicos.
- [ETSI EN 319 401](https://www.etsi.org/deliver/etsi_en/319400_319499/319401/) — requisitos generales para prestadores de servicios de confianza.
- [ISO 23257:2022](https://www.iso.org/standard/75093.html) — arquitectura de referencia para blockchain y DLT.
- [ISO/TS 23635:2022](https://www.iso.org/standard/76480.html) — directrices de gobernanza para blockchain y DLT.
- [ETSI Electronic Signatures and Trust Infrastructures](https://www.etsi.org/technologies/electronic-signatures) — estándares técnicos de firmas, sellos y servicios de confianza.

Análisis de referencia:

- [De la conservación cualificada de firmas y sellos a los servicios cualificados de archivo con orden cronológico (qDLT)](../inza.blog/2026/09/18-de-la-conservacion-cualificada-de-firmas-y-sellos-a-los-servicios-cualificados-de-archivo-con-orden-cronologico-qdlt.md)
- [De las tablillas cuneiformes al Cartulario: historia de la contabilidad y origen de las RJT](../inza.blog/2026/10/23-de-las-tablillas-cuneiformes-al-cartulario-historia-de-la-contabilidad-y-origen-de-las-rjt.md)

### EBSI

[EBSI](ebsi.md) es una infraestructura técnica que opera un consorcio institucional (constituido bajo la figura jurídica de un EDIC, EUROPEUM-EDIC), no un objeto normativo. Por este motivo, no se regula de forma nominal en los actos de ejecución de eIDAS2 ni aparece en los anexos legales. Es una red DLT permisionada transfronteriza, pero eso no la convierte en un libro mayor cualificado. Para serlo, tendrían que crearlo y gestionarlo uno o varios QTSP y cumplir los requisitos del artículo 45 terdecies. Las reglas de arquitectura, el alta de nodos, la referencia de las APIs y las herramientas de validación de credenciales verificables no se publican en el [Diario Oficial de la Unión Europea (DOUE)](https://eur-lex.europa.eu/oj/direct-access.html?locale=es), sino directamente en su portal de desarrollo.

- [Portal para desarrolladores de EBSI (EBSI Hub)](https://hub.ebsi.eu/)

## Aclaraciones

### Características de los actos de ejecución

Los actos de ejecución los redacta y aprueba la Comisión Europea, pero los países de la UE participan en su elaboración y los controlan a través de un comité. Este procedimiento se llama comitología y lo regula el [Reglamento (UE) 182/2011](https://eur-lex.europa.eu/eli/reg/2011/182/oj). Sin entrar en el detalle jurídico, lo importante es que los requisitos técnicos de eIDAS2 no los decide unilateralmente un equipo técnico de la Comisión.

Para hacerlos, la Comisión no parte de cero, sino que se apoya en dos pilares:

- Expertos de los Estados miembros: representantes técnicos de cada país, reunidos en el grupo de expertos de eIDAS.
- Organismos de normalización: la Comisión puede pedir a entidades como ETSI, CEN o CENELEC que preparen [estándares y especificaciones técnicas](#los-estándares-técnicos-y-su-importancia), que los actos de ejecución pueden citar después como referencia.

El proceso general es el siguiente:

- Propuesta: la Comisión prepara los requisitos que necesita desarrollar. En eIDAS2 participa especialmente la [DG CONNECT](dg-connect.md), su departamento responsable de las políticas digitales.
- Consulta pública: es opcional. En el ecosistema EUDI, la Comisión la usa para recibir comentarios de empresas, desarrolladores, organizaciones y otras partes interesadas.
- Comité: el comité de eIDAS (artículo 48 del reglamento), formado por representantes de los países de la UE, examina la propuesta y emite un dictamen. Según el procedimiento aplicable, la Comisión puede adoptar el acto si obtiene el resultado favorable correspondiente.
- Adopción: la Comisión adopta el acto y se publica en el Diario Oficial de la Unión Europea (DOUE).
- Entrada en vigor: en la fecha que fije el propio reglamento, habitualmente a los veinte días de la publicación, aunque puede haber excepciones.

La Comisión publica los borradores por lotes. Un ejemplo es el acto de los libros mayores electrónicos cualificados:

- Septiembre de 2025: [consulta pública](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14752-Qualified-electronic-ledgers_en) del borrador dentro del quinto lote, con comentarios hasta el 2 de octubre.
- 16 de diciembre de 2025: adopción como Reglamento de Ejecución (UE) 2025/2531.
- 17 de diciembre de 2025: publicación en el DOUE.

Para quien desarrolla, este procedimiento explica que las especificaciones técnicas de eIDAS2 se publiquen progresivamente y que haya que estar atento a las nuevas versiones de los reglamentos.

Los actos de ejecución tienen estas características:

- Son normas obligatorias. No son recomendaciones, documentación técnica opcional ni buenas prácticas. Una vez entran en vigor, sus requisitos deben cumplirse dentro de su ámbito de aplicación.
- Se aplican en todos los países de la UE. No necesitan que cada país apruebe otra ley para que sean aplicables.
- Desarrollan eIDAS2, pero no pueden contradecirlo. No pueden eliminar obligaciones del reglamento ni inventar un marco legal incompatible con él.
- Pueden establecer requisitos técnicos concretos. Por ejemplo, formatos, protocolos, interfaces, procedimientos de seguridad o estándares que deben utilizarse.
- Pueden actualizarse. Si cambian las especificaciones técnicas de referencia, la Comisión puede aprobar modificaciones para adaptar los requisitos.

También es importante distinguir los actos de ejecución de los actos delegados.

Los actos delegados, regulados en el artículo 290 del Tratado de Funcionamiento de la Unión Europea (TFUE), permiten a la Comisión modificar o completar determinados elementos no esenciales de una ley.

Los actos de ejecución, regulados en el artículo 291, establecen condiciones uniformes para aplicar una ley que ya existe.

Para un desarrollador, lo importante es que ambos (actos de ejecución y actos delegados) pueden introducir cambios en el marco normativo, pero los actos de ejecución son especialmente relevantes porque concretan requisitos necesarios para implementar los servicios.

### Por qué eIDAS2 depende de los actos de ejecución

eIDAS2 entró en vigor el 20 de mayo de 2024.

Sin embargo, que el reglamento estuviera en vigor no significaba que ya estuvieran definidos todos los requisitos necesarios para desplegar los servicios.

Por ejemplo, un proveedor podía conocer la obligación de desarrollar una cartera europea, pero todavía necesitaba conocer las especificaciones definitivas de seguridad, los protocolos de comunicación y los procedimientos de certificación.

Por eso eIDAS2 establece plazos para que la Comisión apruebe los actos de ejecución que desarrollan sus diferentes artículos.

Los principales paquetes se han publicado en distintas fechas:

- Diciembre de 2024: requisitos fundamentales de la cartera europea, como los datos de identidad, la seguridad, la certificación y los protocolos.
- Mayo de 2025: requisitos adicionales del ecosistema de la cartera, como el registro de entidades que solicitan datos, las violaciones de seguridad y la interoperabilidad entre países.
- Julio a septiembre de 2025: requisitos para diferentes servicios de confianza, como certificados cualificados, dispositivos remotos de firma, sellos de tiempo, entrega electrónica certificada y conservación de firmas.
- Octubre de 2025: gestión de riesgos de los servicios de confianza no cualificados, acreditación de los organismos de evaluación de la conformidad y plantilla de las listas de confianza.
- Diciembre de 2025: requisitos de los prestadores cualificados, archivo electrónico, libros mayores electrónicos y certificados de autenticación de sitios web (QWAC). Con este paquete, los actos de ejecución publicados sumaban 29.
- 2026: nuevas especificaciones y actualizaciones de los requisitos técnicos de la cartera, además de otros aspectos del ecosistema.

Esto tiene una consecuencia práctica: desarrollar una solución compatible con eIDAS2 requiere seguir tanto el reglamento principal como los actos de ejecución que afectan a sus funcionalidades.

No es suficiente estudiar eIDAS2 una sola vez y considerar que los requisitos técnicos permanecerán invariables.

## Referencias

- [Reglamento (UE) 2024/1183 (eIDAS2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento (UE) 910/2014, versión consolidada tras eIDAS2, en EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018)
- [Reglamento (UE) 182/2011 sobre el control de las competencias de ejecución de la Comisión en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2011/182/oj)
- [Resumen del reglamento europeo de identidad digital y sus actos de ejecución (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation)
- [Aplicación de la cartera europea de identidad digital (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eudi-wallet-implementation)
- [Portal de consultas públicas de la Comisión (Have your say)](https://ec.europa.eu/info/law/better-regulation/have-your-say_es)