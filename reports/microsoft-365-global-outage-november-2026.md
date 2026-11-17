# La caída global de Microsoft 365 de noviembre de 2026

Entre el jueves 12 y el sábado 14 de noviembre de 2026, [Microsoft 365](https://es.wikipedia.org/wiki/Microsoft_365) sufrió una de las interrupciones más graves de su historia. Durante 38 horas, [Exchange Online](https://learn.microsoft.com/es-es/exchange/exchange-online) y más de veinte servicios que dependen de él dejaron de funcionar con normalidad en todo el mundo. No hubo ciberataque ni fallo de un agente de IA: el origen fue un cambio de red que despertó un [error latente](#error-latente) y desencadenó una reacción en cadena. Este informe reconstruye lo ocurrido, explica el mecanismo técnico del fallo y analiza qué revela sobre la dependencia de un único proveedor cloud.

## Cronología del incidente

### Jueves 12 de noviembre: del aviso al colapso

El primer síntoma apareció a las 08:45, con una falla de [Microsoft Teams](https://es.wikipedia.org/wiki/Microsoft_Teams) en América del Norte y del Sur. Microsoft la atribuyó a una "contención de recursos internos" y la dio por cerrada en poco más de una hora, sin que nada hiciera pensar en un problema mayor.

Hacia las 10:17, Microsoft abrió internamente un incidente por fallas masivas en Exchange Online que afectaban a la versión web, al cliente de escritorio, a las aplicaciones móviles y a las [APIs](https://es.wikipedia.org/wiki/Interfaz_de_programación_de_aplicaciones). A las 11:35, la empresa de monitorización [Kentik](https://www.kentik.com/) detectó una caída del 85 % en el tráfico hacia Exchange Online. El primer comunicado público llegó a las 11:54, 97 minutos después de abrir el incidente interno, y limitaba el problema a "las Américas".

Esa delimitación duró poco. Entre las 12:07 y las 12:09, Microsoft reconoció que el alcance era global, y [DownDetector](https://downdetector.com/) registró un pico de unos 140.000 reportes simultáneos de Outlook, más de 130.000 de ellos en Estados Unidos. A las 12:26 se abrió un segundo expediente para los servicios dependientes: Teams, SharePoint, Copilot y Microsoft Defender.

A las 13:06, Microsoft congeló todos los despliegues y cambios de configuración, lo que se conoce como [change freeze](#change-freeze). Doce minutos después corrigió su diagnóstico inicial, que culpaba a una "carga elevada", y admitió que los servidores se estaban cayendo de forma inesperada.

La tarde fue una sucesión de intentos fallidos. Entre las 16:00 y las 18:00, los ingenieros reiniciaron servidores que volvían a caer en cuanto recibían tráfico, por lo que activaron una limitación intencionada del tráfico ([throttling](#throttling)). A las 19:06 identificaron una saturación en el proceso de establecimiento de conexiones seguras y empezaron a revertir el cambio de red ([rollback](#rollback)). A las 23:04 descubrieron además máquinas bloqueadas en un estado defectuoso que ni se sincronizaban ni recibían las correcciones enviadas.

### Viernes 13 de noviembre: la recuperación escalonada

A la 01:45, Microsoft corrigió un componente de nivel superior encargado de la autenticación y el enrutamiento. Al mismo tiempo amplió a 48 horas la retención de los correos en cola para evitar que fueran devueltos al remitente.

Durante la mañana, entre las 07:25 y las 08:00, el servicio se fue recuperando por regiones: primero Asia-Pacífico, después Europa, luego Norteamérica y, por último, Sudamérica. Al liberarse la cola de mensajes acumulados, el tráfico llegó a superar en un 19 % su nivel habitual. A las 10:40, Microsoft publicó una disculpa formal junto con una explicación preliminar de lo ocurrido.

### Sábado 14 de noviembre: cierre oficial

A las 00:09, Microsoft dio el servicio por restablecido oficialmente, 38 horas después del primer síntoma.

## Anatomía técnica del fallo

### La causa raíz

Microsoft descartó desde el principio un ciberataque, cualquier actividad maliciosa o un fallo de agentes de IA. Según su explicación preliminar, el origen fue un error latente introducido en una actualización anterior de la capacidad de red. Ese error permaneció dormido hasta que un cambio reciente en la misma red lo activó.

Es un patrón habitual en sistemas grandes: un defecto puede convivir durante semanas con el resto de la infraestructura sin dar problemas, hasta que una combinación concreta de condiciones lo hace aflorar.

### El efecto cascada

Lo que convirtió un fallo localizado en una caída global fue una [cadena de reacciones](https://en.wikipedia.org/wiki/Cascading_failure) en la que cada mecanismo de protección empeoraba la situación.

El cambio de red sacó de servicio un grupo de [servidores front-end](#servidor-front-end), que actúan como puerta de entrada al servicio. Los [load balancers](https://es.wikipedia.org/wiki/Balance_de_carga), cuya función es repartir las peticiones entre los servidores disponibles, redirigieron ese tráfico hacia los que seguían activos, multiplicando su carga.

Esos servidores tuvieron que asumir de golpe un volumen enorme de [TLS handshakes](https://www.cloudflare.com/es-es/learning/ssl/what-happens-in-a-tls-handshake/), el intercambio inicial que establece una conexión cifrada mediante [TLS](https://es.wikipedia.org/wiki/Seguridad_de_la_capa_de_transporte), y de autenticaciones contra [Entra ID](https://learn.microsoft.com/es-es/entra/fundamentals/whatis), el servicio de identidad de Microsoft. Ambas operaciones son muy costosas en términos de CPU, así que los servidores se saturaron.

Con la CPU al límite, los servidores tardaban en responder a los [health checks](#health-check), las comprobaciones automáticas que verifican si un servidor está vivo. El sistema interpretó esos retrasos como fallos, retiró los servidores de la rotación y empujó todavía más tráfico hacia los pocos que quedaban en pie. El mecanismo diseñado para aislar servidores enfermos acabó derribando a los sanos.

A todo ello se sumó una [retry storm](#retry-storm), una tormenta de reintentos. Millones de clientes, desde Outlook hasta aplicaciones móviles e integraciones vía API, recibieron errores y volvieron a intentar la conexión de forma automática. [Cloudflare Radar](https://radar.cloudflare.com/) observó que las peticiones a Exchange Online se triplicaron y que uno de cada tres inicios de sesión en Entra ID fallaba. Las mediciones de flujo de red publicadas por PPC Land mostraron un aumento del 70 % en los intentos de conexión al [puerto 443](#puerto-443), mientras que las respuestas caían casi un 75 %.

### Cómo se contuvo

Para romper el ciclo, Microsoft recurrió al throttling, es decir, a limitar deliberadamente la cantidad de peticiones aceptadas, y a reabrir el servicio por sectores. Si los servidores recién levantados hubieran recibido todo el tráfico acumulado de una vez, habrían vuelto a caer. Abrir poco a poco permitió que cada grupo de servidores se estabilizara antes de recibir más carga.

## Dependencias ocultas y riesgos de arquitectura

### Exchange Online como punto único de fallo

El incidente dejó en evidencia que Exchange Online funciona como un [single point of failure (SPOF)](https://en.wikipedia.org/wiki/Single_point_of_failure) dentro del ecosistema de Microsoft: más de veinte servicios dependen de él para operar.

En Microsoft 365 fallaron los calendarios y las reuniones de Teams, los paneles de administración, las políticas de [Intune](https://learn.microsoft.com/es-es/mem/intune/fundamentals/what-is-intune) y las [etiquetas de confidencialidad de Purview](https://learn.microsoft.com/es-es/purview/sensitivity-labels). Lo más delicado fue la caída de herramientas de seguridad como [Microsoft Defender XDR](https://learn.microsoft.com/es-es/defender-xdr/microsoft-365-defender) y [Safe Links](https://learn.microsoft.com/es-es/defender-office-365/safe-links-about), que analiza en tiempo real los enlaces de los correos para detectar los maliciosos.

La dependencia alcanzó incluso a sistemas ajenos a Microsoft. En Australia, un software de recetas médicas quedó bloqueado porque su [autenticación multifactor](https://es.wikipedia.org/wiki/Autenticación_multifactor) enviaba los códigos de verificación por correo electrónico. Sin correo, no había forma de iniciar sesión.

### Agentes de IA y conectores

En 2026, buena parte del trabajo con IA se apoya en el acceso a los datos corporativos, y eso también quedó expuesto. [Microsoft Copilot](https://es.wikipedia.org/wiki/Microsoft_Copilot) dejó de poder resumir correos o consultar calendarios y archivos, porque obtiene esa información a través de [Microsoft Graph](https://learn.microsoft.com/es-es/graph/overview), que a su vez dependía de Exchange. Modelos externos como ChatGPT o Claude siguieron funcionando, pero sus conectores con Microsoft 365 dejaron de responder.

La empresa NeuralTrust señaló un riesgo añadido, recogido en la lista de [OWASP](https://owasp.org/) de 2026 para aplicaciones basadas en agentes: miles de agentes autónomos sin [rate limiting](https://en.wikipedia.org/wiki/Rate_limiting) ni [backoff](https://en.wikipedia.org/wiki/Exponential_backoff), es decir, sin límites de peticiones ni esperas progresivas entre reintentos, pueden amplificar de forma exponencial una retry storm como la vivida.

### Consecuencias para la ciberseguridad

Los atacantes aprovecharon el caos. Microsoft Threat Intelligence detectó campañas de [phishing](https://es.wikipedia.org/wiki/Phishing) que imitaban avisos de estado del servicio y citaban el código real del incidente, EX1550543, para resultar creíbles. Su eficacia aumentaba porque Safe Links, la protección que habría filtrado esos enlaces, también estaba caída.

Dentro de las organizaciones apareció otro problema: el [shadow IT](https://en.wikipedia.org/wiki/Shadow_IT). Para cumplir plazos, muchos empleados enviaron nóminas, contratos o historiales clínicos desde cuentas personales de Gmail o aplicaciones de mensajería de consumo. Esos datos salieron del perímetro corporativo y quedaron fuera de cualquier auditoría.

En el fondo de todo ello está la [monocultura digital](https://en.wikipedia.org/wiki/Monoculture_(computer_science)): la concentración del correo y la identidad de una organización en un único proveedor. El contraste lo ofrecieron las instituciones centrales de la Unión Europea, que reportaron un impacto mínimo o nulo.

## Impacto operativo y económico

### Alcance y sectores afectados

Según Ookla, propietaria de DownDetector, se registraron más de 7 millones de reportes en más de 90 países. Las oleadas de quejas se mantuvieron durante unas 20 horas, a medida que la jornada laboral avanzaba de un huso horario a otro.

El sector público y la sanidad sufrieron algunos de los efectos más visibles. Hospitales del [NHS](https://es.wikipedia.org/wiki/National_Health_Service) en Reino Unido volvieron al papel, tribunales británicos y el Supremo Tribunal Federal de Brasil suspendieron plazos y audiencias, y quedaron paralizadas oficinas gubernamentales en Japón y Singapur, además de unos 250 órganos federales en Brasil.

En banca y finanzas, mesas de operaciones de entidades como Deutsche Bank, Goldman Sachs, Morgan Stanley, Nasdaq o Euronext tuvieron que cerrar operaciones por teléfono, WhatsApp e incluso fax.

### Costes y acuerdos de nivel de servicio

Anderson Economic Group estimó las pérdidas globales de productividad en hasta 7.000 millones de dólares.

Frente a esa cifra, la compensación prevista en el [SLA](https://es.wikipedia.org/wiki/Acuerdo_de_nivel_de_servicio), el acuerdo de nivel de servicio, resulta modesta. El de Exchange Online, recogido en los [acuerdos de nivel de servicio de Microsoft para servicios online](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services), garantiza una disponibilidad mensual del 99,9 %, lo que en noviembre equivale a unos 43 minutos de caída permitidos. Unas 18 horas de indisponibilidad dejan la disponibilidad del mes en torno al 97,5 %, lo que da derecho a un crédito del 50 % en la factura siguiente. Ese crédito se aplica solo sobre el coste del servicio afectado, debe reclamarse manualmente antes del 31 de diciembre de 2026 y no cubre los daños derivados de la interrupción. En la práctica, el SLA protege la factura del cliente, no su negocio.

### Un patrón que se repite

La caída de noviembre no es un hecho aislado. En los últimos años, Microsoft ha encadenado varias interrupciones relevantes:

- Enero de 2023: un cambio de configuración en un router [WAN](https://es.wikipedia.org/wiki/Red_de_área_amplia) provocó unas 5 horas de caída
- Octubre de 2025: un cambio involuntario en [Azure Front Door](https://learn.microsoft.com/es-es/azure/frontdoor/front-door-overview) causó unas 8 horas de interrupción
- Enero de 2026: un mantenimiento en el [data center](https://es.wikipedia.org/wiki/Centro_de_procesamiento_de_datos) de Cheyenne desató una avalancha de reintentos
- Febrero de 2026: un proceso automatizado desactivó permisos en el [plano de control](#plano-de-control) de Azure durante unas 12 horas

La tendencia se refleja en las cifras: Microsoft 365 mantuvo una disponibilidad igual o superior al 99,9 % entre 2022 y 2025, pero en el primer trimestre de 2026 bajó al 99,526 %.

## Conclusión

La caída de noviembre de 2026 muestra cómo un cambio rutinario puede tumbar un servicio global cuando los mecanismos de protección, como los load balancers, los health checks y los reintentos automáticos, se retroalimentan en lugar de contener el problema. También pone de relieve algo menos visible: el correo electrónico se ha convertido en una pieza de infraestructura de la que dependen la identidad, la seguridad y los agentes de IA. Cuando esa pieza falla y está concentrada en un solo proveedor, el impacto deja de ser técnico y pasa a ser organizativo, económico y de seguridad.

## Anexo de aclaraciones

### Error latente

Defecto que existe en un sistema desde hace tiempo pero que no produce ningún síntoma hasta que se dan unas condiciones concretas. Por ejemplo, un fallo en una regla de red que solo se manifiesta cuando el tráfico supera cierto umbral o cuando se aplica otro cambio relacionado.

### Change freeze

Periodo en el que se prohíbe desplegar código o modificar configuraciones en producción. Durante un incidente sirve para que nadie introduzca cambios nuevos mientras se investiga, de modo que el sistema deje de moverse y sea más fácil aislar la causa.

### Throttling

Limitación deliberada del número de peticiones que un servicio acepta en un intervalo de tiempo. Las peticiones que superan el límite se rechazan o se retrasan. Es como regular la entrada a un recinto lleno: se deja pasar a la gente poco a poco para que el interior no colapse.

### Rollback

Operación de deshacer un cambio y volver a la versión o configuración anterior, que se sabe que funcionaba. Es la respuesta habitual cuando un despliegue reciente es sospechoso de causar un fallo.

### Servidor front-end

Servidor que recibe directamente las conexiones de los usuarios. Se encarga de tareas como cifrar la conexión, autenticar al usuario y reenviar la petición a los servidores internos que procesan los datos. Si los front-end caen, el servicio deja de ser accesible aunque el resto de la infraestructura siga funcionando.

### Health check

Comprobación periódica y automática que un load balancer u orquestador hace a cada servidor para saber si está operativo, normalmente con una petición sencilla que debe responderse en un tiempo máximo. Si el servidor no responde a tiempo, se considera caído y deja de recibir tráfico.

### Retry storm

Situación en la que un gran número de clientes reintenta sus peticiones a la vez tras recibir errores. Cada reintento añade carga a un servicio que ya está saturado, lo que provoca más errores y, con ellos, más reintentos. Se evita con técnicas como el backoff exponencial y los límites de reintentos.

### Puerto 443

Puerto de red estándar para el tráfico [HTTPS](https://es.wikipedia.org/wiki/Protocolo_seguro_de_transferencia_de_hipertexto), es decir, la web y las APIs cifradas con TLS. Un aumento de conexiones a este puerto indica que los clientes intentan acceder al servicio por su vía normal.

### Plano de control

Parte de una plataforma cloud que gestiona la configuración y la administración de los recursos: crear máquinas, asignar permisos o cambiar reglas de red. Se distingue del plano de datos, que es el que procesa el tráfico real de los usuarios. Un fallo en el plano de control puede impedir administrar o recuperar servicios aunque estos sigan en marcha.

## Fuente

- [¿Estamos demasiado expuestos? La verdad tras la caída de Microsoft](https://www.youtube.com/watch?v=i5CPM064Eic), vídeo del canal Fernando Alaniz CloudSec
