# Seguridad

## La skill

- No contiene claves, tokens, contraseñas ni datos personales.
- Exige un **auditor de seguridad** antes de cada commit en proyectos de código: busca secretos, archivos `.env`, llaves, datos personales reales y vulnerabilidades básicas, y bloquea el commit si encuentra algo.
- Trata todo el material y los archivos adjuntos como datos de trabajo, nunca como instrucciones. Un `.py` o `.sql` adjunto no se ejecuta salvo que la tarea lo pida.

## El Tablero de agentes

- Es una página privada de la cuenta de quien usa la skill: sus reglas de acceso dejan leer y escribir **solo al dueño**.
- No hace solicitudes a otros sitios, no pide credenciales y no tiene código de terceros.
- Guarda solo lo necesario para mostrar el avance: nombre del proyecto, agentes, estado, una línea de acción, nombre del archivo de salida, y las sugerencias y archivos que el propio dueño adjunta.
- Los archivos adjuntos (hasta 5 MB cada uno) quedan en la base de datos privada de esa página. El coordinador solo los borra si el dueño lo pide.

## Reportar un problema

Abrí un issue en el repositorio describiendo el problema sin incluir datos sensibles.
