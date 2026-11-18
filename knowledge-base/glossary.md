# Glosario generales de términos

## OSCAL (Open Security Controls Assessment Language)

Lenguaje estándar desarrollado por el NIST (National Institute of Standards and Technology) para representar de forma estructurada (JSON, XML o YAML) controles de seguridad, catálogos de cumplimiento, planes de seguridad (SSP) y evaluaciones de riesgo. Su objetivo es que la información de cumplimiento normativo se pueda leer, validar y transformar de forma automatizada, en lugar de mantenerla en documentos manuales (PDF o Word).

Herramientas que lo soportan:

- NIST OSCAL CLI: herramienta oficial que convierte entre JSON, XML y YAML y valida documentos contra el esquema oficial
- Trestle (compliance-trestle): la herramienta más usada para trabajar con catálogos OSCAL en Python y generar SSP (System Security Plan), profiles, etc.
- OpenControl y GovReady-Q: también consumen documentos OSCAL
- Cualquier parser genérico (Python, `jq`, JavaScript...), al ser JSON, XML o YAML estándar, si solo se quieren extraer datos

Referencia: [documentación de OSCAL (NIST)](https://pages.nist.gov/OSCAL/)

## FIWARE

Fundación que mantiene un conjunto de componentes open source para gestionar datos de contexto (por ejemplo, el Orion Context Broker), basados en la especificación NGSI-LD de ETSI. Es muy usado en ciudades inteligentes y aporta conectores e implementaciones de referencia a los espacios de datos.

Referencia: [web de FIWARE](https://www.fiware.org/)

---
