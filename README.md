# DB_Patterns
1- Para utilizar la herramienta logminer se deberá tener activado el modo archive en la base de datos y además tener establecidos
los archives que se utilizaran para el analisis en caso de no utilizar los archives se puede utilizar directamente los log files.

2- Se debera provocar el modo archive en la base de datos,
 posteriormente se seleccionara el archive que desee este puede ser un solo archive donde se establecera su ubicacion o varios 
archives seleccionados manualmente o estableciendo un rango de fechas.

3- Establecer un diccionario de datos al iniciar sesion en logminer, el cual será utilizado para poder extraer 
la informarcion de los archives, este diccionario de datos puede ser creado a partir de los archivos redo log de la base de 
datos o seleccionar el diccionario online por defecto.

4- Una vez creada la vista v$logmnr_contents con los datos obtenidos de logminer se procedera a utilizar
software externo para realizar el analisis de patrones.

5- El software permitira automatizar algunos de los procesos para la creación de la tabla de logminer, una vez obtenido los datos 
se podrán realizar consultas al sistema para buscar patrones deseados de los registros obtenidos por logminer, para esto se podran establecer filtros las consultas que permitan mostrar información precisa.

6- El software mostrara los resultados en forma de graficos, lo cual facilitara la comprensión de los resultados 
obtenidos de las consultas con filtros que se realicen.

Algunos de los filtros que se pueden realizar en las consultas son:
Username transactions
Time Transactions
Table_name Transaction 
Tablespace_name Transactions
Date Transactions
Operations 
General View

7- Con esta información obtenida se podrán encontrar patrones en las transacciones realizadas por los usuarios, lo cual permitira encontrar posibles anomalias en la base de datos.
