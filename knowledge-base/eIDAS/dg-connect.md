# DG CONNECT (Dirección General de Redes de Comunicación, Contenido y Tecnologías)

Departamento de la Comisión Europea responsable de la política digital: redes de telecomunicaciones, datos, inteligencia artificial, ciberseguridad e identidad digital, entre otros ámbitos.

Existe desde el 1 de julio de 2012, cuando la antigua DG INFSO (Sociedad de la Información y Medios) cambió de nombre para reflejar sus nuevas funciones. No la crea una norma propia: las direcciones generales son servicios internos que la Comisión organiza según su Reglamento interno, adoptado en virtud del artículo 249 del [TFUE](https://es.wikipedia.org/wiki/Tratado_de_Funcionamiento_de_la_Uni%C3%B3n_Europea).

Es la dirección general responsable de eIDAS: prepara las propuestas de reglamento, redacta los actos de ejecución y coordina con los Estados miembros el desarrollo de la cartera europea.

## Tipos de documentos que publica y dónde

DG CONNECT no publica canónicamente sino que participa en diferentes tipos de documentos de distinta naturaleza:

**Documentos de planificación estratégica (estrategias y planes)**:

- [Strategic Plans (planes estratégicos)](https://commission.europa.eu/publications/strategic-plan-2025-2029_en): documentos a cinco años que describen la contribución a los objetivos políticos.
- [Management Plans (planes de gestión)](https://commission.europa.eu/publications/management-plans-2016-2019_es): detallan las actividades y recursos anuales previstos.
- [Annual Activity Reports](https://commission.europa.eu/publications/annual-activity-reports-communication_en) (informes anuales): presentan los logros y recursos utilizados el año anterior.

**Documentos políticos y de iniciativa (comunicaciones y libros)**:

- Communications (comunicaciones): el formato oficial para presentar estrategias generales. [Ver Comunicación sobre los objetivos digitales para 2030 (Brújula Digital)](https://espanadigital.gob.es/sites/espanadigital/files/2022-06/Br%C3%BAjula%20Digital%202030.pdf)
- White Papers (libros blancos): contienen propuestas de acción comunitaria en un ámbito específico. [Ver Libro Blanco sobre Inteligencia Artificial](https://commission.europa.eu/publications/white-paper-artificial-intelligence-european-approach-excellence-and-trust_en)
- Green Papers (libros verdes): se publican para estimular la reflexión y lanzar consultas públicas. [Ver portal general de consultas públicas (Have your say)](https://ec.europa.eu/info/law/better-regulation/have-your-say_es)

**Legislación (normas)**:

- Regulations (reglamentos): normas vinculantes de aplicación directa en todos los Estados miembros. [Ver Reglamento de Servicios Digitales (DSA)](https://eur-lex.europa.eu/ES/legal-content/summary/digital-services-act.html)
- Directives (directivas): normas que establecen objetivos de obligado cumplimiento, dejando la forma legislativa a cada país. [Ver Directiva SRI 2 de ciberseguridad](https://digital-strategy.ec.europa.eu/es/policies/nis2-directive)

**Directrices, blueprints y hojas de ruta**:

- Guidelines / Recommendations (directrices): documentos no vinculantes que sugieren líneas de actuación. [Ver Recomendación sobre la ciberseguridad de las redes 5G](https://www.ceoexeuropa.es/comunicaciones/1094/)
- [Blueprints](https://employment-social-affairs.ec.europa.eu/policies-and-activities/skills-and-qualifications/working-together/blueprint-sectoral-cooperation-skills_en): no es una categoría jurídica oficial, sino un término operativo para esquemas, arquitecturas o marcos de trabajo altamente estructurados.
- Roadmaps (hojas de ruta): definen el camino a seguir para desarrollar una tecnología. [Ver Hojas de ruta estratégicas nacionales para la Década Digital](https://digital-strategy.ec.europa.eu/es/policies/national-strategic-roadmaps).

## Qué publica para eIDAS

Las piezas que publica para eIDAS son:

- [Actos de ejecución](implementing-acts.md): reglamentos de la Comisión que fijan requisitos técnicos y estándares, por ejemplo el 2024/2977 sobre datos de identificación personal y declaraciones electrónicas de atributos. Son obligatorios. [Ver Reglamento de Ejecución (UE) 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj)
- ARF: la arquitectura de referencia de la cartera europea. Lo elaboran la Comisión y expertos de los Estados miembros, a partir de la caja de herramientas común (toolbox) que pidió la Recomendación (UE) 2021/946. No es obligatorio. [Ver ARF](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/) y [Recomendación (UE) 2021/946](https://eur-lex.europa.eu/eli/reco/2021/946/oj)
- Implementación de referencia: código abierto que muestra cómo construir una cartera conforme al ARF y que los Estados pueden reutilizar. [Ver repositorios de la implementación de referencia](https://github.com/eu-digital-identity-wallet)
- Blueprints: soluciones completas para un caso de uso concreto, explicadas en el [apartado siguiente](#blueprint)

## Blueprint

Un blueprint es una solución de referencia para un caso de uso concreto: especificaciones técnicas, documentación y una app en código abierto. Un Estado o una empresa la adapta, le pone su marca y la publica. No es una norma, sino una forma de cumplirla ya construida y probada.

Ejemplos:

- Blueprint de verificación de edad: publicado en julio de 2025 para que las plataformas protejan a los menores, como exige el artículo 28 de la Ley de Servicios Digitales (DSA). Permite demostrar que se es mayor de 18 años sin revelar la fecha de nacimiento. Usa las mismas especificaciones que la cartera europea, así que funciona como app independiente o integrado en una cartera nacional. La versión 2, de octubre de 2025, permite obtener la prueba de edad con pasaporte o DNI. Lo desarrolló el consorcio T-Scy (Scytáles y T-Systems) y lo prueban Dinamarca, España, Francia, Grecia e Italia
- Implementación de referencia de la cartera europea: no se llama blueprint, pero cumple la misma función para la cartera completa

> En la UE, "blueprint" también se usa con el sentido de plan de actuación, sin código detrás. Por ejemplo, la Recomendación (UE) 2017/1584, sobre la respuesta coordinada a incidentes de ciberseguridad a gran escala, se conoce como el "blueprint" de ciberseguridad.

Referencias:

- [DG CONNECT (Comisión Europea)](https://commission.europa.eu/about/departments-and-executive-agencies/communications-networks-content-and-technology_es)
- [Recomendación (UE) 2021/946 sobre la caja de herramientas común en EUR-Lex](https://eur-lex.europa.eu/eli/reco/2021/946/oj)
- [blueprint de verificación de edad (Comisión Europea)](https://digital-strategy.ec.europa.eu/en/factpages/blueprint-age-verification-solution-help-protect-minors-online)
