# Glosario de términos

## OSCAL (Open Security Controls Assessment Language)

Lenguaje estándar, desarrollado por el NIST (National Institute of Standards and Technology), para representar de forma estructurada (JSON, XML o YAML) controles de seguridad, catálogos de cumplimiento, planes de seguridad (SSP) y evaluaciones de riesgo. Su objetivo es permitir que la información de cumplimiento normativo se pueda leer, validar y transformar de forma automatizada, en lugar de mantenerla en documentos manuales (PDF/Word).

**Herramientas que lo soportan:**

- **NIST OSCAL CLI** — herramienta oficial que convierte entre JSON, XML y YAML, y valida documentos contra el esquema oficial.
- **Trestle (compliance-trestle)**, de Red Hat/CISA — la herramienta más usada para trabajar con catálogos OSCAL en Python, generar SSP (System Security Plan), profiles, etc.
- **OpenControl** y **GovReady-Q** — también consumen documentos OSCAL.
- Al ser JSON/XML/YAML estándar, cualquier parser genérico (Python, `jq`, JavaScript...) puede leerlo sin necesidad de tooling especializado si solo se quiere extraer datos.

**Referencia:** [pages.nist.gov/OSCAL](https://pages.nist.gov/OSCAL/)

---

## EDIC (European Digital Infrastructure Consortium) — Europeum

Figura jurídica creada por la Comisión Europea para que varios Estados miembros implementen conjuntamente proyectos digitales transfronterizos. "Europeum" es el EDIC constituido específicamente para el desarrollo y despliegue de infraestructura blockchain europea (vinculado a EBSI, European Blockchain Services Infrastructure).

**Referencia:** [digital-strategy.ec.europa.eu — Blockchain: creation of Europeum EDIC](https://digital-strategy.ec.europa.eu/es/news/blockchain-creation-europeum-edic)

---

## QBFT (Quorum Byzantine Fault Tolerant)

Algoritmo de consenso de tolerancia a fallos bizantinos (BFT) basado en Prueba de Autoridad (PoA), utilizado en redes blockchain permisionadas (p. ej. Hyperledger Besu). Un conjunto de validadores conocidos propone y valida bloques mediante rondas de votación; la red tolera hasta *f* validadores maliciosos o caídos de un total de *3f+1*.

**Referencia:** [Documentación de Hyperledger Besu — QBFT](https://besu.hyperledger.org/private-networks/how-to/configure/consensus/qbft)

## IBFT 2.0 (Istanbul Byzantine Fault Tolerant 2.0)

Predecesor de QBFT, también basado en PoA y con propiedades de tolerancia a fallos bizantinos. Especificado originalmente en el EIP-650. Ambos algoritmos (QBFT e IBFT 2.0) garantizan finalidad inmediata de los bloques (a diferencia de Proof of Work), lo que los hace habituales en consorcios y redes gubernamentales/empresariales.

**Referencia:** [EIP-650: Istanbul Byzantine Fault Tolerance](https://github.com/ethereum/EIPs/issues/650)
