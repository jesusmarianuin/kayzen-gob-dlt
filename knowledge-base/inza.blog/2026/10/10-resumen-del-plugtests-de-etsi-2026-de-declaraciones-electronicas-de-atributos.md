# Resumen del Plugtests de ETSI 2026 de declaraciones electrónicas de atributos

Post: <https://inza.blog/2026/10/10/resumen-del-plugtests-de-etsi-2026-de-declaraciones-electronicas-de-atributos/>

Fecha: 2026-10-10

ETSI publicó en julio de 2026 el [informe técnico de su primer Plugtests de declaraciones electrónicas de atributos](https://portal.etsi.org/Portals/0/TBpages/CTI/Docs/EAA_Plugtests_2026_Technical_Report_1.0.pdf), celebrado en remoto entre el 4 de mayo y el 30 de junio de 2026. Fabricantes, prestadores de servicios de confianza y laboratorios probaron entre sí declaraciones generadas según la especificación ETSI TS 119 472-1 V1.2.1. Son la pieza que permite a la Cartera de Identidad Digital Europea ir más allá de la identificación, y deben funcionar igual con independencia de quién las emita.

El Centro de Pruebas e Interoperabilidad de ETSI (CTI) organizó el ejercicio en un portal sin pruebas en tiempo real. Se probaron los dos perfiles de la especificación, SD-JWT VC (JSON) e ISO/IEC mdoc (CBOR, incluido el permiso de conducir móvil), en sus variantes no cualificada, cualificada y de organismo público responsable de una fuente auténtica. Hubo tres tipos de prueba: generación y verificación cruzada sobre 54 casos, 24 declaraciones deliberadamente defectuosas que debían rechazarse y un verificador de conformidad en beta. Por confidencialidad, el informe solo publica estadísticas globales y anónimas.

Se inscribieron 116 organizaciones de 41 países. Alemania (14) y España (13) aportaron más organizaciones; entre las españolas, el Ministerio para la Transformación Digital y de la Función Pública. Se generaron 959 declaraciones y 11.172 informes de verificación, unas 12 verificaciones por declaración, y SD-JWT VC concentró casi dos tercios de la actividad.

El informe recoge 17 cuestiones que ETSI trasladará a su comité técnico ESI:

- Desajustes normativos: el espacio de nombres mdoc que exige ETSI no coincide con el del PID Rulebook del ARF; la posición de `x5chain` en ISO/IEC 18013-5 impide firmas mdoc conformes con CB-AdES, y el Reglamento de Ejecución (UE) 2026/248 choca con la especificación en las firmas JAdES cualificadas
- Certificados de firma: se pide un perfil específico para firmar declaraciones y admitir funciones resumen distintas de SHA-256 en la referencia al certificado
- Estado y validez: el servicio de estado se especifica distinto en cada formato y el RFC 9901 remite a una versión antigua de Token Status List
- Codificación: errores como usar base64url en lugar de base64 en `vct#integrity` o colocar los parámetros del certificado del titular fuera del `jwk` anidado en `cnf`
- Verificador de conformidad: 9 incidencias notificadas, 7 resueltas durante el evento; todavía no comprueba el perfil mdoc

El autor concluye que el ecosistema tiene masa crítica, pero que la interoperabilidad exige que ETSI, ISO, IETF, el ARF y los actos de ejecución digan lo mismo. Destaca tres mensajes: alinear con urgencia la TS 119 472-1 con el ARF y los actos de ejecución, incorporar la criptoagilidad y la criptografía postcuántica al diseño, y cuidar los detalles de codificación, que bastan para que otro verificador rechace una declaración válida.

En una frase: el primer Plugtests de ETSI demuestra que las declaraciones electrónicas de atributos funcionan, pero que las normas que las rigen aún no están alineadas entre sí.

---
