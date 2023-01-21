# Documentación LFS

## Grupo: Erika Cardozo – Martin Monzón

### Capítulo 1: 
En el primer capítulo nos enseña cómo construir un sistema LFS, los cambios realizados y las novedades con respecto a la versión anterior.



### Capítulo 2: 
Con root instalamos las herramientas de host y paquetes necesarios para construir LFS. Se verifica si el sistema host tiene todas las versiones apropiadas y la capacidad de compilar programas.

- Describe cómo crear una nueva partición, un sistema de archivos y luego montarlos.

- Se realiza la configuración de la variable $LFS export LFS=/mnt/lfs donde construirá el sistema LFS.

- El tamaño del disco de Ubuntu tiene 10GB.

- El tamaño del disco para LFS tiene 35GB.



### Capítulo 3: 

- Explica qué paquetes y parches deben descargarse para construir un sistema LFS y cómo almacenarlos en el nuevo sistema de archivos.

- Se crea el directorio $LFS/sources la cual se puede utilizar como lugar para almacenar los tarballs, paquetes, parches y también como directorio de trabajo. Así al utilizar este directorio, todos sus elementos estarían disponible durante la construcción. 

- Para descargar los paquetes utilizamos wget wget-list-systemd (un enlace la cual contiene todos los paquetes y parches necesarios).

- Todo esto se realiza en root.



### Capítulo 4: 
Trata sobre la construcción de un sistema temporal. Se crean un conjunto de directorios donde se instalan herramientas temporales (etc, var, tools y otros).

- Como root cometer un solo error puede dañar un sistema entonces agregaremos un usuario sin privilegios llamado lfs y crearemos un entorno de compilación apropiado para ese usuario.

- También habla de cuánto tiempo se tarda aproximadamente en compilar e instalar cada paquete y sobre el conjunto de pruebas que se realizan.



### Capítulo 5: 
Explica la instalación de la cadena de herramientas inicial (binutils, gcc y glibc) utilizando técnicas de compilación cruzada para aislar las nuevas herramientas del sistema host y se instalan en el directorio $LFS/tools.

Como usuario lfs dentro del directorio /mnt/lfs/sources/ utilizamos tar -xvf paquete para extraer el paquete a construir.

Con cd Cambiamos al directorio creado cuando se extrajo el paquete, se siguen los pasos del libro para instalar y compilar. Luego volvemos al directorio /mnt/lfs/sources/ y eliminamos el directorio extraído con rm -Rf a menos que se indique lo contrario.

GCC puede tardar varios minutos, los demás paquetes normalmente son más rápidos.

Nos tomó alrededor de 1 hora o menos compilar los paquetes. 



### Capítulo 6: 
Este capítulo muestra cómo realizar una compilación cruzada de utilidades básicas utilizando la cadena de herramientas cruzada recién construida y debe realizarse como usuario lfs

Luego como en el Capítulo 5 con el usuario lfs dentro del directorio /mnt/lfs/sources/ utilizamos tar -xvf paquete para extraer el paquete a construir.

Con cd Cambiamos al directorio creado cuando se extrajo el paquete, se siguen los pasos del libro para instalar y compilar. Luego volvemos al directorio /mnt/lfs/sources/ y eliminamos el directorio extraído con rm -Rf a menos que se indique lo contrario.

GCC puede demorar mucho más que los demás paquetes.

Nos tomó alrededor de 2 horas o menos compilar los paquetes. 



### Capítulo 7: 
Ingresa a un entorno "chroot", donde usamos las nuevas herramientas para construir el resto de las herramientas necesarias para crear el sistema LFS.

Para que el entorno funcione correctamente, se deben los llamados sistemas de archivos de kernel virtual, que se montarán antes de ingresar al entorno chroot. Si se apaga la maquina o mejor dicho si es posible siempre se debe verificar que estén montados los sistemas de archivos de este capítulo con el comando findmnt | grep $LFS, ya que es importante para los siguientes capítulos.

Hasta el capítulo 7.4 trabajamos en el entorno root $LFS, luego directamente en el entorno chroot hasta el final.

Se crean directorios, archivos esenciales y enlaces simbólicos.

Se extraen paquetes con tar -xvf paquete y luego instalamos.

También se realiza una limpieza para liberar un poco de espacio y un respaldo por cualquier problema que ocurra.

Nos tomó alrededor de 30 minutos compilar los paquetes. 



### Capítulo 8: 
Se construye el sistema LFS completo. Se instalan paquetes con tar -xvf paquete, se compilan y luego se realizan pruebas de cada paquete, es importante verificar que no obtengamos errores ya que es un capítulo super importante para el sistema. Algunos errores el libro avisa la cual podrías ignorar, pero hay otros que se debe buscar la manera de solucionar. Lo malo de este capítulo es que te lleva como varios días (si Tenes actividades en el día) ya que son más de 70 paquetes por instalar y hay algunos que tardan bastante, uno de ellos es GCC.

Nos tomó 1 semana este capítulo. 

Se limpian algunos archivos adicionales sobrantes de la ejecución de pruebas y otros que ya no se necesitan.

Todo este capítulo se realiza en el entorno chroot.

Problemas y soluciones encontradas: Con los paquetes: man-pages, binutils y ncurses. Se soluciono volviendo a snapshots anteriores y volviendo a extraer, compilar y realizar las pruebas.



### Capítulo 9: 

Este capítulo trata sobre los archivos de configuración general necesarios para configurar la red, analizan los problemas que afectan la configuración adecuada de los dispositivos, configuración del reloj del sistema y la disposición del teclado, breve introducción a los scripts y archivos de configuración utilizados cuando el usuario inicia sesión en el sistema (Creación del archivo /etc/inputrc y /etc/shells), configuración del comportamiento de systemd.

Todo este capítulo se realiza en el entorno chroot.

Problemas y soluciones encontradas: No lograba conectar a internet, pero leyendo mejor el libro y editando los archivos de configuración general logramos conectar.


### Capítulo 10: 
Hacer que el sistema LFS sea de arranque. Todo este capítulo se realiza en el entorno chroot.

La creación del archivo /etc/fstab dónde se montarán los sistemas de archivos. 

La construcción de un núcleo para el nuevo sistema LFS donde extraemos el paquete, compilamos y configuramos el kernel a través de una interfaz con el comando make menuconfig donde habilitas o deshabilitas las funciones para que el sistema funcione. El comando que me ayudo bastante es make defconfig ya que te establece una configuración base y luego editas de acuerdo a lo que pide el libro en este capítulo.

Nos tomó alrededor de 1 hora o menos instalar y compilar. 

Tambien realizamos la instalación del cargador de arranque GRUB para que el sistema LFS pueda seleccionarse para arrancar al inicio. Es importante leer bien las Convenciones de nomenclatura de GRUB para que puedas crear el archivo de configuración de grub.

Hay un comando, grub-mkconfig, que puede escribir un archivo de configuración automáticamente y es super útil.

Problemas y soluciones encontradas: kernel panic, un error común por mala instalación del kernel. Después de varios días buscando la solución, instalando de vuelta Linux de capítulo 10.3 por decima vez y siguiendo los pasos correctamente/cuidadosamente y también teniendo en cuenta que en una sección de ese capítulo te dice que debes habilitar por orden se logró solucionar.

Problemas con Grub para el Dual boot: No encontraba el disco y otros errores, pero solucionamos al generar automáticamente el archivo grub del lfs en el grub Ubuntu.



### Capítulo 11: 
LFS instalado.  Se crea un /etc/lfs-release archivo para saber qué versión de LFS está instalada en el sistema.

Salimos del entorno chroot y luego desmontamos los sistemas de archivos virtuales, desmontar particiones y el sistema de archivos LFS. ¡¡¡Luego reiniciamos y todo LISTO!!!

Como ultimo podemos descargar wget, sudo y openssh en el lfs porque sería de mucha importancia.
