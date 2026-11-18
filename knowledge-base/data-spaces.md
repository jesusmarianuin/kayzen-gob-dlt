# Espacios de datos (data spaces)

Un espacio común europeo de datos (common European data space) es un concepto de la Unión Europea, introducido por la Comisión en la Estrategia Europea de Datos (2020), para que empresas y administraciones de un mismo sector económico compartan datos entre ellas sin cederlos a una plataforma que los centralice. Nace porque esas organizaciones apenas compartían datos, por miedo a perder el control sobre ellos, y su valor lo concentraban unas pocas plataformas, mayoritariamente no europeas.

Cada espacio corresponde a un sector: salud, movilidad, energía, agricultura, industria, finanzas, administración pública, Pacto Verde, entre otros. Lo forman las organizaciones de ese sector que aceptan unas reglas comunes:

- Legales: el Data Governance Act (Reglamento (UE) 2022/868), que prevé estos espacios por sectores, y el Data Act (Reglamento (UE) 2023/2854), cuyo artículo 33 fija requisitos de interoperabilidad para quienes ofrecen datos en ellos. Algunos sectores tienen además ley propia: el primero es el Espacio Europeo de Datos Sanitarios (Reglamento (UE) 2025/327)
- Técnicas: cada organización conserva sus datos en sus sistemas y los intercambia directamente con otra, normalmente mediante un software llamado conector, junto con unas condiciones de uso legibles por máquinas
- De gobernanza: una entidad del espacio decide quién entra, verifica su identidad y fija las reglas

El término "espacio de datos" también se usa fuera de este marco oficial para iniciativas privadas que siguen el mismo modelo. La más conocida es Catena-X, del sector del automóvil, impulsada desde 2020 por empresas como BMW, Bosch, SAP o Siemens. En ella, un fabricante pide a sus proveedores los datos de huella de CO2 de las piezas y cada proveedor se los envía directamente desde su conector, con la condición de que solo se usen para calcular CO2. Ningún dato pasa por un servidor central.

Los términos de este ámbito son de tipos muy distintos y conviene separarlos:

- Piezas técnicas, que explican cómo se intercambian los datos: conector, DSP, ODRL y el marco de confianza de Gaia-X
- Organizaciones que definen esas piezas: IDSA, Gaia-X, W3C y, como normalizadores oficiales, CEN y CENELEC
- Iniciativas de la Comisión Europea que reúnen esas piezas para los espacios comunes europeos: DSSC y Simpl
- Otros actores del ecosistema: BDVA

Referencia: [espacios comunes europeos de datos (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/data-spaces)

## Cómo funciona un intercambio de datos

Siguiendo el ejemplo de Catena-X, cuando un fabricante pide a un proveedor los datos de huella de CO2 de una pieza:

- Cada empresa tiene instalado en sus sistemas un conector, el software que se comunica con los conectores de los demás participantes
- Antes de intercambiar nada, cada parte comprueba la identidad de la otra y que cumple las reglas del espacio, mediante credenciales verificables (ver [Gaia-X](#gaia-x))
- El conector del fabricante consulta el catálogo del proveedor, negocia un contrato de uso y recibe los datos. Las reglas de esa comunicación entre conectores las fija el [DSP](#dsp-dataspace-protocol)
- La condición "solo para calcular CO2" viaja escrita en un formato legible por máquinas, [ODRL](#odrl-open-digital-rights-language)

### DSP (Dataspace Protocol)

Protocolo que define cómo se comunican los conectores de un espacio de datos: cómo publican un catálogo con los datos que ofrecen, cómo negocian el contrato de uso y cómo gestionan la transferencia. Las condiciones de uso se expresan en ODRL.

Lo creó IDSA, que en 2024 trasladó su mantenimiento al Eclipse Dataspace Working Group de la Eclipse Foundation, con el objetivo de convertirlo en estándar ISO/IEC.

Referencia: [versión estable del Dataspace Protocol (IDSA)](https://internationaldataspaces.org/idsa-releases-stable-version-of-the-dataspace-protocol/)

### ODRL (Open Digital Rights Language)

Recomendación del W3C para expresar políticas de uso (permisos, prohibiciones y obligaciones) de forma legible por máquinas. En un espacio de datos es el formato en el que se escriben las condiciones de uso de un conjunto de datos, por ejemplo "uso permitido solo para calcular CO2, durante un año".

Referencia: [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)

## Organizaciones que definen las piezas

### IDSA (International Data Spaces Association)

Asociación fundada en 2016 que creó el modelo técnico en el que se basan la mayoría de espacios de datos: la arquitectura de referencia (IDS-RAM), el modelo de conectores y su certificación, y el Dataspace Protocol. Catena-X, por ejemplo, se basa en este modelo. También mantiene el Data Spaces Radar, un mapa de las iniciativas de espacios de datos existentes en Europa.

Referencia: [web de IDSA](https://internationaldataspaces.org/)

### Gaia-X

Asociación europea sin ánimo de lucro que define un marco de confianza (Trust Framework) para servicios de datos y nube: qué reglas deben cumplir los participantes y cómo se comprueba, de forma automatizada, mediante credenciales verificables. En un espacio de datos aporta la respuesta a la pregunta "¿cómo sé que la otra parte es quien dice ser y cumple las reglas?".

Referencia: [web de Gaia-X](https://gaia-x.eu/)

## Iniciativas de la Comisión Europea

### DSSC (Data Spaces Support Centre)

Proyecto financiado por la Comisión Europea, dentro del programa Europa Digital, que actúa como centro de apoyo de los espacios comunes europeos de datos. Recoge el trabajo de IDSA, Gaia-X, FIWARE y otras iniciativas y lo ordena en un marco común, para que los espacios de cada sector usen las mismas piezas en lugar de desarrollar soluciones incompatibles. Publica:

- DSSC Blueprint: guía de cómo construir un espacio de datos, organizada en building blocks legales, técnicos y de gobernanza
- DSSC Toolbox: catálogo de componentes software que implementan esos building blocks
- Glosario: vocabulario común para que todas las iniciativas nombren igual los mismos conceptos

Referencia: [web del DSSC](https://dssc.eu/)

### Simpl

Software open source financiado por la Comisión Europea que reúne las piezas técnicas (gestión de identidades, catálogos, contratos e intercambio de datos) listas para usar en los espacios comunes europeos de datos, para que cada uno no tenga que desarrollar las suyas. DSSC dice cómo construir un espacio de datos; Simpl es software con el que construirlo.

Referencia: [Simpl (Comisión Europea)](https://digital-strategy.ec.europa.eu/es/policies/simpl)

## Otros actores

### BDVA (Big Data Value Association)

Asociación industrial europea que representa al sector privado en la colaboración público-privada con la Comisión Europea en materia de datos e inteligencia artificial. Influye en la agenda europea de investigación e innovación sobre espacios de datos, pero no aporta piezas técnicas.

Referencia: [web de BDVA](https://bdva.eu/)
