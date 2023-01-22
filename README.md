# Implementacion de Linux Shell en Python

Se implemento una shell de linux en python para una version de linux siguiendo el manual de LFS.

## Made with:

![Image](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## API Reference:


### Copy
___
```
copy dirsrc dirdst
dirsrc=origen
dirdst=destino
```
  


#### Copy (dirsrc,dirdst)

#### ejemplo: copy archivo carpeta

Copia el archivo de la direccion especificada a la direccion de destino, si no se ingresa una direccion de destino la copia se hace en la misma direccion.


### Move
___
```
  move dirsrc dirdst
  dirsrc=origen archivo/directorio
  dirdst=destino
```

#### move (dirsrc,dirdst)
#### ejemplo: move carpeta carpeta

Mover un archivo/directorio de la direccion especificada a la direccion de destino.


### Rename
___
```
  rename src dst
  src=nombre actual archivo/directorio
  dirdst=nombre a cambiar archivo/directorio
```

#### move (dirsrc,dirdst)
#### ejemplo: rename hola.txt hola1.txt

Renombrar archivos/directorios.\ En caso de algun error, se lanza una excepcion.


### List
___
```
  list 
  list dirPATH
  list= listar directorio actual
  dirPATH= direccion de la carpeta a listar
```

#### list dirPATH
#### ejemplo: list carpeta

Listar un directorio.\ En caso de algun error o directorio inexistente, se lanza una excepcion.

### Makedir
___
```
  makedir dirnames 
  dirNAMES= nombre(s) de carpetas a crear
```

#### makedir dirnames
#### ejemplo: makedir a

Crear un directorio. 
En caso de algun error o el directorio ya existe, se lanza una excepcion.


### Ir
___
```
  ir dirPATH 
  dirPATH=direccion para cambiar de directorio 
```

#### ir dirPATH
#### ejemplo: ir carpeta

Cambiar de directorio.\
En caso de algun error o el directorio no existe, se lanza una excepcion.


### Permisos
___
```
  permisos perPATH 
  perPATH=contiene los permisos y el archivo/directorio que desea cambiar sus permisos. 
```

#### permisos perPATH
#### ejemplo: permisos 777 a.txt

Cambiar los permisos sobre un archivo o un directorio.\
En caso de algun error o el archivo/directorio no existe, se lanza una excepcion.


### Propietario
___
```
  propietario cad 
  cad=contiene el usuario/grupo y el archivo/directorio. 
```

#### propietario usuario:grupo archivo/carpeta
#### ejemplo: propietario erika:erikaGroup a.txt

Cambiar los propietarios sobre un archivo.\
En caso de algun error o el archivo/directorio no existe, se lanza una excepcion.


### Contraseña
___
```
  setPass usuario
  usuario = nombre de usuario

```
Recibe el nombre de usuario, luego verfifica si existe y cambia la contraseña \
en el formato correspondiente. En caso de algun error se lanza una excepcion.

### Agregar Usuario
___
```
  addsuario usuario
  usuario = nombre de usuario a ser creado.
```
Recibe el nombre de usuario, luego verfifica si existe,lanza una excepcion si es asi, \
y crea el usuario y su direccion de Home si es que no existe un usuario con ese nombre.

Agregar usuario, se registran los datos personales del mismo incluyendo
su horario de trabajo y posibles lugares de conexión
En caso de algun error se lanza una excepcion.


### Imprimir directorio
___
```
  printdir  
```

#### printdir
#### ejemplo: printdir

Imprime el directorio en el que se encuentra la shell actualmente.
En caso de algun error, se lanza una excepcion.


### Kill
___
```
  kill PIDs señal 
  PIDs = lista de procesos a ser terminados
  señal = 3 señales disponibles KILL, STOP, TERMINATE
```

Terminar procesos con señales determinadas.
En caso de algun error, se lanza una excepcion.


### Grep
___
```
  fgrep gpath
  gpath= Contiene el string a buscar y el archivo
  
```

#### fgrep gpath
#### ejemplo: fgrep mar new.txt

Buscar un string en un archivo .
En caso de algun error, archivo inexistente o palabra no encontrada, se lanza una excepcion.


### History
___

```
  history
```

#### history
#### ejemplo: historial

Imprime el historial de comandos.
En caso de algun error, se lanza una excepcion.


### Daemons
___

```
    daemonControl daemonPATH accion 
    deamon = direccion del daemon a ser ejecutado
    accion = accion a ser tomada start|stop|restart
  
```

Levantar y apagar demonios dentro del sistema.
En caso de algun error, se lanza una excepcion.

### Transferencia ftp
___

```
  ftpTransferencia b
  b= Contiene hostname, username y archivo a enviar/descargar.
```

#### ftpTransferencia b
#### ejemplo para probar: ftpTransferencia ftp.dlptest.com dlpuser rNrKYTX9g7z3RgJRmxWuGHbeu

Ejecutar una transferencia, bajar o subir archivo.
En caso de algun error, se lanza una excepcion.

## ARCHIVOS LOGS 

#### usuario_horarios_log.log

- Guarda los horarios de los usuarios que ingresan fuera de horario laboral.

#### Shell_transferencias.log

- Guarda las trasnferecias realizadas.

#### comandosDiarios.log

 * Guarda los comandos diarios realizados.

#### sistema_error.log

* Guarda los errores que se obtuvieron.


#### Implementación del LFS y SHELL

```
    Ingresamos en /sources y clonamos el repositorio.
    Luego copiamos o movemos el repositorio clonado a una carpeta creada llamada SO1 ubicada en /.
    chmod -R 777 /SO1 (todos los permisos)
    luego dentro de / realizamos vi shell.sh y escribimos:
     
      #!/bin/bash
      cd /SO1/SO1_CARDOZO_MONZON
      python3 main.py

    Despues ingresamos a /etc/profile y escribimos:
      bash /shell.sh
    
    Y por ultimo, en / realizar mkdir var/log/shell (crear carpeta shell para los logs) 
    chmod -R 777 /var/log/shell (todos los permisos) y listo.
  
```

## Autores

- [Martin Monzon](https://www.github.com/c4russian)
- [Erika Cardozo](https://github.com/erikacardozo)


