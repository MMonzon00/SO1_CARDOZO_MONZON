import cmd
import readline
import subprocess
from typing import Iterable
import cmd2
import argparse
import os 
import shutil
import getpass
import socket
import re
from os import system
# from usefunctions import *

#!/usr/bin/env python
"""A simple shell application."""

class shell(cmd2.Cmd):
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    """A simple cmd2 application."""
    def __init__(self):
        super().__init__()
        username = getpass.getuser()
        homedir = os.getcwd()
        hostname = socket.gethostname()
        
        self.default_to_shell = True #use default shell commands
        self.prompt = f"{username}@{hostname}:{homedir}$"
        # shortcuts = {'?': 'help', '+': 'shell', '@': 'run_script', '@@': '_relative_run_script'}
        # print(shortcuts)
        self.poutput("Welcome to So1_Shell_2022")
    
    def guardar(self,arguments):
        if arguments=="historial" or arguments=="contraseña" or arguments=="clean":
            arg=''.join(arguments)
        else:
            space=' '
            arg=space.join(arguments)
        
        ubi='historial.txt'
        f = open (ubi,'a')
        f.write(f'{arg}\n')
        f.close()
    
    ###4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
    ###4.1.1. El input debe tener el siguiente formato: Archivo(s) DirectorioDestino
    
    def do_copy(self,arguments):
        dirsrc=arguments.arg_list[0]
        dirdst=arguments.arg_list[1]
        src = f'{dirsrc}'
        dst = f'{dirdst}'
        name = "copy"
        guardarParam = (name,src,dst)
        self.guardar(guardarParam)
        try:

            shutil.copy(src, dst)
            self.poutput("File copied successfully.")
        
        # If src and dst are same
        except shutil.SameFileError:
            self.poutput("Source and destination represents the same file.")
        
        # If there is any permission issue
        except PermissionError:
            self.poutput("Permission denied.")
        
        # For other errors
        except:
            self.poutput("Error occurred while copying file/s.")
    
    ###4.2. Mover - mover
    ###4.2.1. El input debe tener el siguiente formato: Archivo(s)/Directorio(s) DirectorioDestino.
    
    def do_move(self,arguments):
        dirsrc=arguments.arg_list[0]
        dirdst=arguments.arg_list[1]
        src = f'{dirsrc}'
        dst = f'{dirdst}'
        name = "move"
        guardarParam = (name,src,dst)
        self.guardar(guardarParam)
        if src!=dst:
            shutil.move(src,dst)
            self.popout("File moved successfully.")
        elif src==dst:
            self.poutput("Source and destination represents the same file.")
        # except PermissionError:
        #     self.poutput("Permission denied.")
        # except:
        #     self.poutput("Error occurred while moving file/s.")
    
    
    ###4.3. Renombrar - renombrar
    def do_rename(self,FILENAME): #these are the parameters needed
        cwd = os.getcwd() #Get current working directory
        src = f'{cwd}/{FILENAME.arg_list[0]}' #current name
        dst = f'{cwd}/{FILENAME.arg_list[1]}' #new name
        name = "rename"
        guardarParam = (name,src,dst)
        self.guardar(guardarParam)
        if src!=dst: #if name different rename
            os.rename(src,dst)
            self.poutput("File renamed successfully.")
        elif src==dst: #if name same show error
             self.poutput("Name has to be different to current.")
    
    
    ###4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    ###4.4.1. Si no recibe argumentos, debe listar los archivos/directorios de la carpeta actual.
    ###4.4.2. En caso de recibir un directorio, listar archivos/directorios de esedirectorio.       
    #listar// okkkk // ver si se necesita -l o -la retcode = subprocess.call(['ls', '-l'])  
    def do_listar(self,dirPATH):
        name = "listar"
        if len(dirPATH)==0:
            cwd=os.getcwd()
            guardarParam = (name,cwd)
            self.guardar(guardarParam)
            print("entro en misma carpeta")
            list=os.listdir(cwd)
            lenlist=len(list)
            for i in range(lenlist):
                if i+1==lenlist:
                    self.poutput(f"{list[i]}")
                else:
                    self.poutput(f"{list[i]}",end=" - ")
        else:
            dir=dirPATH[1:len(dirPATH)]
            guardarParam = (name,dir)
            self.guardar(guardarParam)
            print("entro en dist")
            list=os.listdir(dir)
            lenlist=len(list)
            for i in range(lenlist):
                if i+1==lenlist:
                    self.poutput(f"{list[i]}")
                else:
                    self.poutput(f"{list[i]}",end=" - ")

    ###4.5. Crear un directorio - creardir
    ###4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
    ## okkkkk
    def do_makedir(self,dirnames):
        name = "makedir"
        guardarParam = []
        guardarParam.append(name)
        cwd=os.getcwd()
        dirlen=len(dirnames.arg_list)
        for i in range(dirlen):
            dirname=f"{dirnames.arg_list[i]}"
            path=os.path.join(cwd,dirname)
            os.mkdir(path)
            guardarParam.append(dirnames.arg_list[i])
        self.guardar(guardarParam)
    
    ### 4.6. Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir ///////LISTOOOOOOOOOOOOOO
    def do_ir(self,dirPATH):
        name = "ir"
        username = getpass.getuser()
        if dirPATH==dirPATH:
            guardarParam=(name,dirPATH)
            self.guardar(guardarParam)
            os.chdir(dirPATH)
            cwd = os.getcwd() #current working directory
            hostname = socket.gethostname()
            self.prompt = f"{username}@{hostname}:{cwd}$"
        else:
            print("no se encontro el archivo o directorio")
    ####4.7. Cambiar los permisos sobre un archivo o un directorio - permisos//// falta
    def do_permisos(self,perPATH):
        ##separar la cadena y ver como cambiar el numero de permisos
        ##El primer dígito corresponde a los permisos del usuario, el segundo a los del grupo y el tercero a los del resto de usuarios.
        ## split separador y cuantas divisiones en total
        name = "permisos"
        newCAD=perPATH.split(' ', 2)
        guardarParam=(name,newCAD[0],newCAD[1])
        self.guardar(guardarParam)
        os.chmod(newCAD[1],int(newCAD[0],8)) ## convierte cadena octal a decimal por ej 777 a 511
       ## binario = ' '.join(format(c, 'b') for c in bytearray(newCAD[0], "utf-8"))
       ## binario = bin(newCAD[0])
       

    ###4.8. Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    ###4.8.1. Debe usar el formato USUARIO:GRUPO
    ##cambiar propietario// que hacer si no existe ese usuario o grupo?????se crea o se imprime mensaje de error
    def do_propietario(self,cad):
        name="propietario"
        guardarParam=(name,cad)
        self.guardar(guardarParam)
        i=":"
        j=" "
        indice=cad.index(i)
        indice1=cad.index(j)
        user=cad[0:indice]
        group=cad[indice+1:indice1]
        propPATH=cad[indice1+1:len(cad)]
        shutil.chown(propPATH, user, group)
    
    ###4.9. Cambiar la contraseña - contraseña
    def do_contraseña(self,user):
        name="contraseña"
        guardarParam=(name)
        self.guardar(guardarParam)
        if user == '':
            user = getpass.getuser()
            subprocess.run(['passwd', user])


    ###4.10. Agregar usuario, y deben registrar los datos personales del mismo incluyendo su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost). - usuario

    ### 4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
    def do_printdir(self,dirPATH):
        name = 'printdir'
        cwd=os.getcwd()
        guardarParam = (name,cwd)
        self.guardar(guardarParam)
        self.poutput(cwd)
    
    ###4.12. Terminar procesos con señales determinadas - kill
    ###4.12.1. Debe aceptar el input con el formato: PID(s) señal


    ###4.13. Buscar un string en un archivo - grep
    def do_fgrep(self,gpath):
        gpath=gpath.split(' ', 2)
        name='fgrep'
        guardarParam = (name,gpath[0],gpath[1])
        self.guardar(guardarParam)
        band=False
        i=0
        if os.path.exists(gpath[1])==True:
            for line in open(gpath[1], 'r'):
                i=i+1
                if re.search(gpath[0], line):
                    print("en la linea:",i,  line)
                    band=True
            if band==False:
                print("Error: El string no existe")
        else:
            print("Error: El archivo no existe")
        
    
    ###4.14. Imprimir un historial de comandos - history
    
    
    def do_historial (self,arg):
        name = 'historial'
        self.guardar(name)
        f = open ('historial.txt','r')
        for linea in f:
           print (linea)

    ###4.15 y demas dsp voy a pensar ahora no quiero estresarme :)

    def do_clean(self,args):
        name = 'clean'
        self.guardar(name)
        _ = system('clear')  



if __name__ == '__main__':
    import sys
    c = shell()
    sys.exit(c.cmdloop())