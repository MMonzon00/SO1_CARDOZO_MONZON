# SO1_CARDOZO_MONZON
Shell implementation in python
2. Desarrollo del Shell
2.1. Descripción
1. El Shell debe ser cargado de manera automática al iniciar la sesión.
2. Deben utilizar versionamiento de código y subir en GitLAB o GitHub los avances de
código.
3. Además, deben habilitar una cuenta en la plataforma Jira y utilizando metodología
ágiles para la implementación del proyecto, construyendo todo el escenario.
4. El usuario debe poder realizar un conjunto de comando básicos:
4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
4.1.1. El input debe tener el siguiente formato: Archivo(s) DirectorioDestino
4.1.2. Ejemplos:
https://www.ionos.com/digitalguide/server/configuration/linux-cp-com
mand/
4.2. Mover - mover
4.2.1. El input debe tener el siguiente formato: Archivo(s)/Directorio(s)
DirectorioDestino.
4.2.2. Ejemplos: https://linuxhandbook.com/mv-command/
4.3. Renombrar - renombrar
4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
4.4.1. Si no recibe argumentos, debe listar los archivos/directorios de la
carpeta actual.
4.4.2. En caso de recibir un directorio, listar archivos/directorios de ese
directorio.
4.4.3. Ejemplos:
https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-comma
nd/

4.5. Crear un directorio - creardir
4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
4.5.2. Ejemplo: https://www.educba.com/mkdir-command-in-linux/ (Mirar el
Ejemplo #3)

4.6. Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
4.7. Cambiar los permisos sobre un archivo o un directorio - permisos

4.8. Cambiar los propietarios sobre un archivo o un conjunto de archivos. -
propietario
4.8.1. Debe usar el formato USUARIO:GRUPO
4.8.2. Ejemplos:
https://phoenixnap.com/kb/linux-chown-command-with-examples

4.9. Cambiar la contraseña - contraseña
4.10. Agregar usuario, y deben registrar los datos personales del mismo incluyendo
su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost).
- usuario
4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
4.12. Terminar procesos con señales determinadas - kill
4.12.1. Debe aceptar el input con el formato: PID(s) señal
4.12.2. Ejemplos (con la lista de señales posibles):

https://linuxize.com/post/kill-command-in-linux/

4.13. Buscar un string en un archivo - grep
4.14. Imprimir un historial de comandos - history
4.15. El usuario debe poder levantar y apagar demonios dentro del sistema,
utilizando una herramienta como service de CentOS. (no puede ser una
llamada a sistema a la función service o systemctl)
4.16. Proveer la capacidad de poder ejecutar comandos del sistema, que no sean los
comandos mencionados arriba.
4.17. Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar
con los registros de su horario cada vez que inicia/cierra la sesión y si esta
fuera del rango escribir en el archivo de log (usuario_horarios_log) un
mensaje que aclare que está fuera del rango y deben agregar el lugar desde
donde realizó la conexión que también puede estar fuera de sus IPs habilitado.
4.18. Ejecutar una transferencia por ftp o scp, se debe registrar en el log
Shell_transferencias del usuario.

2.2. Requerimientos
1. Debe funcionar sobre el sistema LFS y sobre un Ubuntu.
2. Se debe registrar en el archivo de log del Shell nuevo todos los movimientos
realizados por un usuario de los comandos básicos mencionados en la descripción
del proyecto generando un timestamp (YYYY-MM-DD hh:min:sec), que debe
encontrarse al comienzo de cada línea.
3. Cuando el usuario tiene de retorno un error en el sistema. Ejemplo:
a. Un usuario que accede a un directorio no permitido
b. Error al copiar o renombrar un archivo
c. cambio de contraseña exitoso o equivocado
d. Servicio no inicializado

Estos registros deben ser almacenados en un archivo independiente, siempre dentro del
archivo log, pero que se llame sistema_error.log ubicado en el /var/log/shell
4. Perfectamente documentado el código del sistema, líneas y funciones. Dentro del
código, así como un manual de documentación.
5. Se debe entregar una copia digital y otra impresa. Y un manual de uso e
instalación del Shell.