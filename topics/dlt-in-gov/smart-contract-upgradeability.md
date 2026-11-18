# Inmutabilidad y evolución de los *smart contracts*

El código de un contrato desplegado no se puede modificar. Es la misma propiedad que da valor al *ledger*, pero un error en un contrato queda en producción para siempre, y una norma que cambia obliga a cambiar las reglas que el contrato aplica.

Hay que distinguir dos inmutabilidades. La del historial no se negocia: lo registrado no se altera. La de la lógica sí puede relajarse, siempre que el cambio sea visible, esté gobernado y quede registrado *on-chain*. Para ello existen tres mecanismos que se diseñan desde el principio, porque no se pueden añadir a un contrato ya desplegado.

## Proxies

Un *proxy* es un contrato que conserva la dirección y los datos, y delega la ejecución en un contrato de implementación que puede sustituirse. Quien interactúa con el sistema siempre usa la misma dirección, aunque la lógica haya cambiado por debajo.

Los patrones más extendidos son:

- *Proxy* transparente: la lógica de actualización vive en el *proxy* y solo puede invocarla un administrador.
- UUPS ([ERC-1822](https://eips.ethereum.org/EIPS/eip-1822)): la lógica de actualización vive en la implementación, lo que abarata el *proxy*, pero una implementación sin esa función bloquea para siempre futuras actualizaciones.
- *Beacon*: muchos *proxies* apuntan a un mismo contrato que indica la implementación vigente, útil cuando cada organismo tiene su propia instancia del mismo contrato y todas deben actualizarse a la vez.

## Paradas de emergencia

Una parada de emergencia (*circuit breaker*, patrón *pausable*) permite suspender las operaciones de un contrato ante un incidente de seguridad o un error grave, sin esperar a tener una corrección. Los datos no se tocan: solo se bloquean las funciones marcadas como pausables.

Su diseño plantea tres preguntas que corresponden a la [gobernanza](network-governance.md):

- Quién puede pausar: debe ser rápido, así que suele bastar con un único rol de guardián o una firma múltiple.
- Qué se pausa: las escrituras críticas, pero conviene mantener las consultas para que la información siga siendo verificable.
- Quién reanuda: reanudar debe exigir más acuerdo que pausar, para que el guardián no pueda abusar del mecanismo.

El rol que pausa no debe ser el mismo que actualiza. Pausar es una medida defensiva y acotada; actualizar cambia las reglas.

## Time locks

Un *time lock* introduce un retardo obligatorio entre la aprobación de una operación sensible (una actualización, un cambio de parámetros, un cambio de roles) y su ejecución. Durante ese plazo, la operación es pública y cualquier participante puede revisar el nuevo código, objetar por los cauces acordados o preparar sus sistemas.

En una red de la Administración el *time lock* es la traducción técnica de un plazo de información previa: ningún organismo puede cambiar las reglas comunes de un día para otro.

## Cómo se combinan

El esquema habitual reparte los poderes según su urgencia y su impacto:

- Actualizar la implementación exige firma múltiple de varios organismos y pasa siempre por el *time lock*.
- Pausar queda en manos de un guardián con efecto inmediato, pero sin capacidad de actualizar ni de reanudar por sí solo.
- Todo cambio deja rastro *on-chain*, de modo que la evolución de la lógica es tan auditable como los datos.

Cada contrato debe documentar qué es actualizable, quién tiene cada rol y qué plazos aplican. Un contrato actualizable sin esas reglas explícitas ofrece menos garantías que una base de datos centralizada, porque aparenta una inmutabilidad que no tiene.
