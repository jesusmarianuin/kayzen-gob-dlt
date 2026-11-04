# Actos de ejecución de eIDAS2

Los actos de ejecución concretan los detalles técnicos que [eIDAS2](README.md#eidas2) no define por sí solo.

Son especialmente importantes para los desarrolladores porque contienen requisitos técnicos que condicionan cómo deben construirse e integrarse los sistemas compatibles con eIDAS2. No basta con implementar una solución que funcione: hay que respetar las especificaciones que establece la normativa.

Este documento explica qué son los actos de ejecución, cómo afectan al desarrollo de software y qué reglamentos se han aprobado para la cartera europea, los servicios de confianza y los libros mayores electrónicos.

## Qué es un acto de ejecución

eIDAS2 establece las reglas generales del ecosistema de identidad digital europeo. Define qué es una cartera europea, qué servicios de confianza existen, qué garantías deben ofrecer y qué responsabilidades tienen los diferentes participantes.

Sin embargo, para construir esos servicios hacen falta decisiones técnicas mucho más concretas.

Por ejemplo, imaginemos que estamos desarrollando una cartera EUDI. Necesitamos saber:

- Qué información de identidad puede almacenar y presentar.
- Qué formatos deben tener las credenciales.
- Qué protocolos debe utilizar para comunicarse con otros sistemas.
- Cómo debe gestionar las claves criptográficas.
- Qué mecanismos de seguridad debe implementar.
- Cómo se comprueba que una cartera cumple los requisitos.
- Qué procedimiento debe seguirse para certificarla.

eIDAS2 establece las obligaciones generales, pero no desarrolla todos estos detalles. Los actos de ejecución son los documentos que concretan cómo deben cumplirse esas obligaciones.

La diferencia es importante: eIDAS2 establece qué debe conseguir el sistema y los actos de ejecución especifican requisitos concretos para implementarlo.

Esto permite que los requisitos técnicos puedan evolucionar sin tener que modificar todo el reglamento principal cada vez que cambia una especificación.

Formalmente, eIDAS2 (Reglamento (UE) 2024/1183) es un reglamento de modificación: reforma el Reglamento (UE) 910/2014. Por eso los actos de ejecución citan en su título el 910/2014 y los artículos que desarrollan, como el 45 terdecies, siguen la numeración de su [versión consolidada](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018).

Por ejemplo, eIDAS2 establece en su artículo 5 quater que las carteras europeas deben certificarse. Para desarrollar esa obligación, el [Reglamento de Ejecución (UE) 2024/2981](https://eur-lex.europa.eu/eli/reg_impl/2024/2981/oj) establece los requisitos y procedimientos relacionados con esa certificación.

Si desarrollas una cartera, no puedes limitarte a implementar las funcionalidades que consideres suficientes. Debes tener en cuenta los requisitos de certificación que establece ese reglamento.

Otro ejemplo es el [Reglamento de Ejecución (UE) 2024/2982](https://eur-lex.europa.eu/eli/reg_impl/2024/2982/oj), que establece los protocolos e interfaces que deben utilizarse para determinadas comunicaciones entre las carteras y los servicios que interactúan con ellas.

Esto tiene una consecuencia directa para el desarrollo: no puedes diseñar libremente las interfaces de integración de una solución EUDI ignorando las especificaciones oficiales.

Los actos de ejecución tienen estas características:

- Son normas obligatorias. No son recomendaciones, documentación técnica opcional ni buenas prácticas. Una vez entran en vigor, sus requisitos deben cumplirse dentro de su ámbito de aplicación.
- Se aplican en todos los países de la UE. No necesitan que cada país apruebe otra ley para que sean aplicables.
- Desarrollan eIDAS2, pero no pueden contradecirlo. No pueden eliminar obligaciones del reglamento ni inventar un marco legal incompatible con él.
- Pueden establecer requisitos técnicos concretos. Por ejemplo, formatos, protocolos, interfaces, procedimientos de seguridad o estándares que deben utilizarse.
- Pueden actualizarse. Si cambian las especificaciones técnicas de referencia, la Comisión puede aprobar modificaciones para adaptar los requisitos.

También es importante distinguir los actos de ejecución de los actos delegados.

Los actos delegados, regulados en el artículo 290 del Tratado de Funcionamiento de la Unión Europea (TFUE), permiten a la Comisión modificar o completar determinados elementos no esenciales de una ley.

Los actos de ejecución, regulados en el artículo 291, establecen condiciones uniformes para aplicar una ley que ya existe.

Para un desarrollador, lo importante es que ambos pueden introducir cambios en el marco normativo, pero los actos de ejecución son especialmente relevantes porque concretan requisitos necesarios para implementar los servicios.

Los actos de ejecución son redactados y aprobados por la Comisión Europea.

Para hacerlos, la Comisión no parte de cero, sino que se apoya en dos pilares:

- Expertos de los Estados miembros: representantes técnicos de cada país, reunidos en el grupo de expertos de eIDAS.
- Organismos de normalización: la Comisión puede pedir a entidades como ETSI, CEN o CENELEC que preparen [estándares y especificaciones técnicas](#los-estándares-técnicos-y-su-importancia), que los actos de ejecución pueden citar después como referencia.

### Los estándares técnicos y su importancia

Muchos actos de ejecución hacen referencia a estándares publicados por [organismos de normalización](standardization-bodies.md) como ETSI, CEN/CENELEC o ISO.

Estos estándares contienen especificaciones técnicas que permiten implementar sistemas de forma interoperable y con requisitos comunes.

Por ejemplo, un acto puede exigir que un servicio utilice un determinado estándar ETSI para implementar una funcionalidad de seguridad.

En ese caso, el estándar deja de ser simplemente una recomendación técnica para convertirse en una referencia normativa que debe tenerse en cuenta al implementar el servicio.

Hay un matiz importante: cumplir un estándar citado puede proporcionar una presunción de conformidad respecto a los requisitos que cubre, cuando así lo establece el marco normativo. No significa que cumplir un estándar cualquiera garantice automáticamente el cumplimiento de todo eIDAS2.

Al usar una norma citada hay que tener en cuenta dos cautelas:

- Cada acto de ejecución fija una versión concreta de cada norma, y a veces adaptaciones. Hay que comprobarla en el DOUE antes de usar la referencia en un pliego o una auditoría.
- El DOUE contiene erratas en algunas referencias, como "EN 3191 22-1" o "EN 310 401", que hay que asignar a la norma correcta.

Esto también afecta a las auditorías y certificaciones. Los organismos responsables comprueban que los servicios cumplen los requisitos aplicables, utilizando las normas y especificaciones de referencia que correspondan.

Un ejemplo es la ARF (Architecture and Reference Framework), la arquitectura de referencia de la cartera europea.

La ARF describe cómo se organiza técnicamente el ecosistema EUDI y sirve de referencia para implementar sus componentes. Sin embargo, no todo lo que aparece en ella tiene automáticamente carácter obligatorio. Cuando un acto de ejecución incorpora determinadas especificaciones de la ARF como requisitos de referencia, esas especificaciones pasan a tener relevancia normativa.

Por tanto, al desarrollar una solución EUDI conviene distinguir entre:

- La normativa obligatoria.
- Los estándares técnicos que la normativa incorpora o utiliza como referencia.
- Las especificaciones de arquitectura que sirven de orientación para implementar el ecosistema.

## Cómo se aprueba un acto de ejecución

Los actos de ejecución los aprueba la Comisión Europea. Sin embargo, los países de la UE participan en el procedimiento y pueden controlar las propuestas a través de un comité.

Este procedimiento se llama comitología.

No necesitas conocer el procedimiento jurídico en detalle. Lo importante es entender que los requisitos técnicos de eIDAS2 no los decide unilateralmente un equipo técnico de la Comisión: los países participan en su elaboración y control.

El proceso general es el siguiente:

- La Comisión Europea prepara una propuesta con los requisitos que necesita desarrollar. En el caso de eIDAS2, participa especialmente la [DG CONNECT](dg-connect.md), el departamento de la Comisión responsable de las políticas digitales.
- La propuesta puede someterse a consulta pública. En el ecosistema EUDI, la Comisión utiliza este proceso para recibir comentarios de empresas, desarrolladores, organizaciones y otras partes interesadas.
- El comité de eIDAS, creado por el artículo 48 del reglamento, participa en el procedimiento. Está formado por representantes de los países de la UE y examina las propuestas de la Comisión.
- El comité emite su opinión mediante una votación. Según el procedimiento aplicable, la Comisión puede adoptar el acto si obtiene el resultado favorable correspondiente.
- La Comisión adopta el acto de ejecución y se publica en el Diario Oficial de la Unión Europea (DOUE).
- Una vez publicado, entra en vigor en la fecha que establezca el propio reglamento. Habitualmente, estos actos establecen su entrada en vigor a los veinte días de su publicación, aunque pueden existir excepciones.

La regulación general de este procedimiento se encuentra en el [Reglamento (UE) 182/2011](https://eur-lex.europa.eu/eli/reg/2011/182/oj).

La Comisión publica los borradores por lotes. Un ejemplo es el acto de los libros mayores electrónicos cualificados:

- Septiembre de 2025: el borrador sale a [consulta pública](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14752-Qualified-electronic-ledgers_en) dentro del quinto lote, con plazo de comentarios hasta el 2 de octubre.
- 16 de diciembre de 2025: la Comisión lo adopta como Reglamento de Ejecución (UE) 2025/2531.
- 17 de diciembre de 2025: se publica en el DOUE.

Desde el punto de vista del desarrollo, este procedimiento explica por qué las especificaciones técnicas de eIDAS2 se publican progresivamente y por qué hay que estar atento a las nuevas versiones de los reglamentos.

## Por qué eIDAS2 depende de los actos de ejecución

eIDAS2 entró en vigor el 20 de mayo de 2024.

Sin embargo, que el reglamento estuviera en vigor no significaba que ya estuvieran definidos todos los requisitos necesarios para desplegar los servicios.

Por ejemplo, un proveedor podía conocer la obligación de desarrollar una cartera europea, pero todavía necesitaba conocer las especificaciones definitivas de seguridad, los protocolos de comunicación y los procedimientos de certificación.

Por eso eIDAS2 establece plazos para que la Comisión apruebe los actos de ejecución que desarrollan sus diferentes artículos.

Los principales paquetes se han publicado en distintas fechas:

- Diciembre de 2024: requisitos fundamentales de la cartera europea, como los datos de identidad, la seguridad, la certificación y los protocolos.
- Mayo de 2025: requisitos adicionales del ecosistema de la cartera, como el registro de entidades que solicitan datos, las violaciones de seguridad y la interoperabilidad entre países.
- Julio a septiembre de 2025: requisitos para diferentes servicios de confianza, como certificados cualificados, dispositivos remotos de firma, sellos de tiempo, entrega electrónica certificada y conservación de firmas.
- Diciembre de 2025: requisitos de los prestadores cualificados, archivo electrónico, libros mayores electrónicos y certificados de autenticación de sitios web (QWAC). Con este paquete, los actos de ejecución publicados sumaban 26.
- 2026: nuevas especificaciones y actualizaciones de los requisitos técnicos de la cartera, además de otros aspectos del ecosistema.

Esto tiene una consecuencia práctica: desarrollar una solución compatible con eIDAS2 requiere seguir tanto el reglamento principal como los actos de ejecución que afectan a sus funcionalidades.

No es suficiente estudiar eIDAS2 una sola vez y considerar que los requisitos técnicos permanecerán invariables.

## Dónde consultar las reglas técnicas

No hace falta recorrer EUR-Lex reglamento a reglamento. Según lo que se desarrolle, estos son los puntos de partida.

### Lista oficial de actos de ejecución

La Comisión Europea mantiene una página con todos los actos de ejecución de eIDAS2. Para cada uno indica el artículo que desarrolla, su estado (adoptado o en consulta) y el enlace a su texto en EUR-Lex. Es la referencia para comprobar si un acto se ha aprobado o modificado.

- [Lista de actos de ejecución de eIDAS2 (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation)

### Cartera EUDI

Los actos de ejecución de la cartera fijan los requisitos obligatorios y remiten a estándares y especificaciones técnicas. Para el desarrollo, la documentación de referencia está en dos repositorios oficiales:

- [Architecture and Reference Framework (ARF)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework): arquitectura de referencia de la cartera. La versión vigente es la última publicada en el repositorio; la 3.0.0 se alinea con las modificaciones de los actos de ejecución aprobadas en 2026.
- [Estándares y especificaciones técnicas (STS)](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications): relaciona cada estándar o especificación técnica con el acto de ejecución que lo exige.

Los actos de ejecución básicos de la cartera son:

- [Reglamento de Ejecución (UE) 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj): datos de identificación personal y atestaciones electrónicas de atributos.
- [Reglamento de Ejecución (UE) 2024/2979](https://eur-lex.europa.eu/eli/reg_impl/2024/2979/oj): integridad y funcionalidades básicas.
- [Reglamento de Ejecución (UE) 2024/2980](https://eur-lex.europa.eu/eli/reg_impl/2024/2980/oj): notificaciones a la Comisión sobre el ecosistema de la cartera (marco de confianza).
- [Reglamento de Ejecución (UE) 2024/2981](https://eur-lex.europa.eu/eli/reg_impl/2024/2981/oj): certificación.
- [Reglamento de Ejecución (UE) 2024/2982](https://eur-lex.europa.eu/eli/reg_impl/2024/2982/oj): protocolos e interfaces.

El [Reglamento de Ejecución (UE) 2026/1731](https://eur-lex.europa.eu/eli/reg_impl/2026/1731/oj) modifica los reglamentos 2024/2977, 2024/2979, 2024/2980 y 2024/2982, así que hay que leerlos junto con esa modificación. Los alinea con la ARF 3.0.0 e incorpora las especificaciones ETSI TS 119 472-1, -2 y -3, TS 119 412-6 y TS 119 432.

Otros actos de 2026 que afectan a la cartera:

- [Reglamento de Ejecución (UE) 2026/798](https://eur-lex.europa.eu/eli/reg_impl/2026/798/oj): alta remota en la cartera hasta el nivel de seguridad alto.
- [Reglamento de Ejecución (UE) 2026/1730](https://eur-lex.europa.eu/eli/reg_impl/2026/1730/oj): registro de las partes usuarias, con ETSI TS 119 411-8 para los certificados de acceso y TS 119 475 para los de registro.
- [Reglamento de Ejecución (UE) 2026/1735](https://eur-lex.europa.eu/eli/reg_impl/2026/1735/oj): firma o sello de las verificaciones de atributos frente a fuentes auténticas, con ETSI TS 119 471 y TS 119 478.

### Libros mayores electrónicos (Electronic Ledgers)

El [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj), que desarrolla el artículo 45 terdecies, apartado 3, fija los requisitos técnicos y las normas de referencia aplicables a los libros mayores electrónicos cualificados introducidos por eIDAS2. Establece las condiciones que deben cumplir los prestadores cualificados de servicios de confianza (QTSP) que ofrezcan este servicio, definiendo los requisitos de seguridad, la garantía de presunción de integridad, el orden cronológico exacto de los registros, los mecanismos criptográficos y el modelo de gobernanza exigido.

Lo que garantiza un libro mayor cualificado es el orden cronológico de los registros: ninguna entrada puede insertarse, borrarse o reordenarse sin que se detecte.

El reglamento no exige una blockchain. El orden puede construirlo un único prestador, en un registro centralizado, o una red de nodos que acuerdan la secuencia. La variante distribuida prestada como servicio cualificado se conoce como qDLT.

Las normas de referencia dependen de esa variante:

- Todos los libros mayores cualificados: ETSI EN 319 401, requisitos generales de los prestadores de servicios de confianza, y perfiles AdES adaptados para firmas y sellos.
- Solo la variante distribuida, además: ISO 23257:2022, arquitectura de referencia de blockchain y DLT, e ISO/TS 23635:2022, gobernanza de blockchain y DLT.

CEN ha publicado además la especificación técnica CEN/TS 18264, dedicada a los libros mayores electrónicos.

Como el servicio lo presta un QTSP, también le aplican los actos horizontales de los servicios de confianza cualificados:

- [Reglamento de Ejecución (UE) 2025/2530](https://eur-lex.europa.eu/eli/reg_impl/2025/2530/oj): requisitos de cumplimiento y seguridad de los prestadores cualificados (artículo 24).
- [Reglamento de Ejecución (UE) 2025/1572](https://eur-lex.europa.eu/eli/reg_impl/2025/1572/oj): inicio de la prestación de servicios de confianza cualificados.
- [Reglamento de Ejecución (UE) 2025/2162](https://eur-lex.europa.eu/eli/reg_impl/2025/2162/oj): acreditación de los organismos de evaluación de la conformidad; su anexo II reúne las normas con las que se evalúa cada servicio cualificado.

El libro mayor es el último de tres servicios cualificados que se apoyan unos en otros:

- Conservación de firmas y sellos cualificados ([Reglamento de Ejecución (UE) 2025/1946](https://eur-lex.europa.eu/eli/reg_impl/2025/1946/oj), ETSI TS 119 511 y TS 119 512): mantiene válida la evidencia criptográfica cuando caducan los certificados o envejecen los algoritmos.
- Archivo electrónico cualificado ([Reglamento de Ejecución (UE) 2025/2532](https://eur-lex.europa.eu/eli/reg_impl/2025/2532/oj), artículo 45 undecies, CEN/TS 18170): custodia el documento, esté firmado o no, con integridad, legibilidad, trazabilidad de accesos y retención.
- Libro mayor electrónico cualificado (Reglamento de Ejecución (UE) 2025/2531, CEN/TS 18264): fija un orden cronológico verificable de los hechos registrados.

Referencias oficiales y documentación técnica:

- [Reglamento de Ejecución (UE) 2025/2531](https://eur-lex.europa.eu/eli/reg_impl/2025/2531/oj) — requisitos técnicos de los libros mayores electrónicos cualificados.
- [Reglamento (UE) 910/2014, versión consolidada tras eIDAS2](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018) — artículos 45 duodecies y 45 terdecies (sección 11; 45k y 45l en la versión inglesa), relativos a los efectos jurídicos y requisitos de los libros mayores electrónicos.
- [ETSI EN 319 401](https://www.etsi.org/deliver/etsi_en/319400_319499/319401/) — requisitos generales para prestadores de servicios de confianza.
- [ISO 23257:2022](https://www.iso.org/standard/75093.html) — arquitectura de referencia para blockchain y DLT.
- [ISO/TS 23635:2022](https://www.iso.org/standard/76480.html) — directrices de gobernanza para blockchain y DLT.
- [ETSI Electronic Signatures and Trust Infrastructures](https://www.etsi.org/technologies/electronic-signatures) — estándares técnicos de firmas, sellos y servicios de confianza.

Análisis de referencia:

- [De la conservación cualificada de firmas y sellos a los servicios cualificados de archivo con orden cronológico (qDLT)](../inza.blog/2026/09/18-de-la-conservacion-cualificada-de-firmas-y-sellos-a-los-servicios-cualificados-de-archivo-con-orden-cronologico-qdlt.md)
- [De las tablillas cuneiformes al Cartulario: historia de la contabilidad y origen de las RJT](../inza.blog/2026/10/23-de-las-tablillas-cuneiformes-al-cartulario-historia-de-la-contabilidad-y-origen-de-las-rjt.md)

### EBSI

[EBSI](ebsi.md) es una infraestructura técnica y un consorcio institucional (constituido bajo la figura jurídica de un EDIC, EUROPEUM-EDIC), no un objeto normativo. Por este motivo, no se regula de forma nominal en los actos de ejecución de eIDAS2 ni aparece en los anexos legales. Es una red DLT permisionada transfronteriza y sirve de ejemplo de que la distribución es compatible con la confianza cualificada de los libros mayores, siempre que los nodos los operen entidades identificadas con anclas de confianza gubernamentales. Las reglas de arquitectura, el alta de nodos, la referencia de las APIs y las herramientas de validación de credenciales verificables no se publican en el [Diario Oficial de la Unión Europea (DOUE)](https://eur-lex.europa.eu/oj/direct-access.html?locale=es), sino directamente en su portal de desarrollo.

- [Portal para desarrolladores de EBSI (EBSI Hub)](https://hub.ebsi.eu/)

## Referencias

- [Reglamento (UE) 2024/1183 (eIDAS2) en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglamento (UE) 910/2014, versión consolidada tras eIDAS2, en EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02014R0910-20241018)
- [Reglamento (UE) 182/2011 sobre el control de las competencias de ejecución de la Comisión en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2011/182/oj)
- [Resumen del reglamento europeo de identidad digital y sus actos de ejecución (Comisión Europea)](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation)
- [Aplicación de la cartera europea de identidad digital (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/eudi-wallet-implementation)
- [Portal de consultas públicas de la Comisión (Have your say)](https://ec.europa.eu/info/law/better-regulation/have-your-say_es)