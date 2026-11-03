# Relaciones entre eIDAS, DG CONNECT, ETSI y CEN/CENELEC

## Esquema

```text
Parlamento Europeo + Consejo
  adoptan, a propuesta de la Comisión
        │
        ▼
Reglamento eIDAS (910/2014, modificado por 2024/1183)
  ley: servicios, efectos jurídicos, requisitos generales
        │
        │ faculta a la Comisión
        ▼
Comisión Europea (redacta DG CONNECT)
  actos de ejecución, con dictamen de un comité de Estados miembros
  obligatorios, fijan las normas técnicas de referencia
        │                                   ▲
        │ encarga normas                    │ cita normas ya existentes
        │ (solicitud de normalización)      │
        ▼                                   │
ETSI · CEN · CENELEC  (y fuera de la UE, ISO)
  organismos de normalización independientes
  redactan normas técnicas, voluntarias por sí solas
```

## Quién es cada uno

- eIDAS: la ley. Dice qué servicios de confianza existen y qué efectos jurídicos tienen, pero no entra en el detalle técnico
- DG CONNECT: el departamento de la Comisión Europea que lleva eIDAS. Prepara las propuestas de reglamento y redacta los actos de ejecución
- Actos de ejecución: reglamentos de la Comisión que concretan eIDAS. Son obligatorios, y es en ellos donde se dice qué norma técnica hay que cumplir
- ETSI, CEN y CENELEC: los tres organismos europeos de normalización reconocidos por el Reglamento (UE) 1025/2012. ETSI hace la mayoría de las normas de servicios de confianza (serie EN 319). CEN se ocupa, entre otras cosas, de los dispositivos de firma (serie EN 419)
- ISO: organismo internacional. Sus normas también pueden citarse directamente en un acto de ejecución

## Cómo se relacionan

- No hay jerarquía entre DG CONNECT y ETSI o CEN: estos no forman parte de la Comisión ni reciben órdenes de ella
- La Comisión puede encargarles una norma con una solicitud de normalización (artículo 10 del Reglamento 1025/2012). El organismo decide si la acepta
- La Comisión también puede citar en un acto de ejecución normas que ya existen
- Lo que hace obligatoria una norma es el acto de ejecución que la cita, no el organismo que la redacta

## Ejemplo: libro mayor electrónico cualificado

```text
eIDAS, artículos 45 duodecies y 45 terdecies
        │
        ▼
Reglamento de Ejecución (UE) 2025/2531  (Comisión, DG CONNECT)
        │ cita
        ▼
ETSI EN 319 401             → ETSI
ISO 23257 · ISO/TS 23635    → ISO
```

El 2025/2531 lo adopta la Comisión en virtud de eIDAS, no ETSI ni CEN. Lo que hacen ETSI e ISO es redactar las normas que ese reglamento cita.
