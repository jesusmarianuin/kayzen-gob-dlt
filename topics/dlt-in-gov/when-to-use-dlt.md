# Cuándo es interesante una DLT

Una DLT tiene sentido únicamente bajo condiciones de diseño muy concretas. Resulta relevante cuando concurren los siguientes factores:

- Existen múltiples organizaciones normativamente autónomas.
- Todos los participantes necesitan compartir y confiar en un estado común de la información.
- Ninguna entidad debe o puede asumir el control centralizado de la infraestructura.
- Existe un valor claro en la verificación independiente y auditable de los registros.
- La trazabilidad, la inmutabilidad y la resiliencia interorganizativa son requisitos del sistema.

En cambio, si existe una única autoridad competente, todos los participantes aceptan que dicho organismo administre la base de datos centralizada y no aporta valor distribuir la gobernanza, una base de datos convencional será una solución infinitamente más eficiente, económica y sencilla de mantener. Ocurre lo mismo cuando el sistema requiere un rendimiento extremo en transacciones por segundo (TPS), latencias de milisegundos o procesamiento analítico masivo (OLAP). Una DLT introduce mecanismos de replicación y consenso que conllevan inevitablemente una penalización en rendimiento.

Una prueba rápida es evaluar si por mantener un registro central surgen conflictos de autonomía, gobernanza, auditoría independiente, trazabilidad o puntos únicos de fallo. Si fuera el caso, entonces tendríamos que considerar una DLT.

Lo que una DLT pierde frente a una base de datos relacional se detalla en [retos de diseño con Besu](besu-design-challenges.md).
