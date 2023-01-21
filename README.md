
# Implementacion de Linux Shell en Python

Se implemento una shell de linux en python para una version de linux siguiendo el manual de LFS.


## API Reference

### Copy

```http
  copy dirsrc dirdst
  dirsrc=origen
  dirdst=destino
```

#### Copy (dirsrc,dirdst)
#### ejemplo: copy archivo carpeta

Copia el archivo de la direccion especificada a la direccion de destino, si no se ingresa una direccion de destino la copia se hace en la misma direccion.


#### Move

```http
  move dirsrc dirdst
  dirsrc=origen archivo/directorio
  dirdst=destino
```

#### move (dirsrc,dirdst)
#### ejemplo: move carpeta carpeta

Mover un archivo/directorio de la direccion especificada a la direccion de destino.


#### Rename

```http
  rename src dst
  src=nombre actual archivo/directorio
  dirdst=nombre a cambiar archivo/directorio
```

#### move (dirsrc,dirdst)
#### ejemplo: rename hola.txt hola1.txt

Renombrar archivos/directorios
En caso de algun error, se lanza una excepcion.


#### List

```http
  list 
  list dirPATH
  list= listar directorio actual
  dirPATH= direccion de la carpeta a listar
```

#### list dirPATH
#### ejemplo: list carpeta

Listar un directorio 
En caso de algun error o directorio inexistente, se lanza una excepcion.

#### Makedir

```http
  makedir dirnames 
  dirNAMES= nombre(s) de carpetas a crear
```

#### makedir dirnames
#### ejemplo: makedir a

Crear un directorio 
En caso de algun error o el directorio ya existe, se lanza una excepcion.


#### Ir

```http
  ir dirPATH 
  dirPATH=direccion para cambiar de directorio 
```

#### ir dirPATH
#### ejemplo: ir carpeta

Cambiar de directorio 
En caso de algun error o el directorio no existe, se lanza una excepcion.


#### Permisos

```http
  permisos perPATH 
  perPATH=contiene los permisos y el archivo/directorio que desea cambiar sus permisos. 
```

#### permisos perPATH
#### ejemplo: permisos 777 a.txt

Cambiar los permisos sobre un archivo o un directorio  
En caso de algun error o el archivo/directorio no existe, se lanza una excepcion.


#### Propietario

```http
  propietario cad 
  cad=contiene el usuario/grupo y el archivo/directorio. 
```

#### propietario usuario:grupo archivo/carpeta
#### ejemplo: propietario erika:erikaGroup a.txt

Cambiar los propietarios sobre un archivo  
En caso de algun error o el archivo/directorio no existe, se lanza una excepcion.


#### Contraseña

```http
  setPass /// 
  // que recibe
```

#### como es el comando
#### un ejemplo

Cambiar contraseña  
En caso de algun error se lanza una excepcion.

#### Agregar Usuario

```http
  addsuario /// 
  // que recibe
```

#### como es el comando
#### un ejemplo

Agregar usuario, se registran los datos personales del mismo incluyendo
su horario de trabajo y posibles lugares de conexión
En caso de algun error se lanza una excepcion.


#### Imprimir directorio

```http
  printdir  
```

#### printdir
#### ejemplo: printdir

Imprime el directorio en el que se encuentra la shell actualmente.
En caso de algun error, se lanza una excepcion.


#### Kill

```http
  kill //  
  que recibe //
``

#### kill
#### ejemplo para kill: //

Terminar procesos con señales determinadas.
En caso de algun error, se lanza una excepcion.


#### Grep

```http
  fgrep gpath
  gpath= Contiene el string a buscar y el archivo
  
```

#### fgrep gpath
#### ejemplo: fgrep mar new.txt

Buscar un string en un archivo .
En caso de algun error, archivo inexistente o palabra no encontrada, se lanza una excepcion.


#### History

```http
  history
```

#### history
#### ejemplo: history

Imprime el historial de comandos.
En caso de algun error, se lanza una excepcion.


#### Daemons

```http
  
  
```

#### daemons
#### ejemplo: 

Levantar y apagar demonios dentro del sistema.
En caso de algun error, se lanza una excepcion.

#### Transferencia ftp

```http
  ftpTransferencia b
  b= Contiene hostname, username y archivo a enviar/descargar.
```

#### ftpTransferencia b
#### ejemplo para probar: ftpTransferencia ftp.dlptest.com dlpuser rNrKYTX9g7z3RgJRmxWuGHbeu

Ejecutar una transferencia, bajar o subir archivo.
En caso de algun error, se lanza una excepcion.

#### ARCHIVOS LOGS ####

usuario_horarios_log.log

```http
  Guarda los horarios de los usuarios que ingresan fuera de horario laboral.
```

Shell_transferencias.log

```http
  Guarda las trasnferecias realizadas.
```

comandosDiarios.log

```http
  Guarda los comandos diarios realizados.
```

sistema_error.log

```http
  Guarda los errores que se obtuvieron.
```






















## Autores

- [Martin Monzon](https://www.github.com/c4russian)
- [Erika Cardozo](https://github.com/erikacardozo)

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Appendix

Any additional information goes here

