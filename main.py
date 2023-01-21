import subprocess
import cmd2
import os 
import shutil
import getpass
import socket
import re
import logging
import datetime
import socket
from os import system
from cmd2 import Cmd2ArgumentParser, with_argparser
import psutil
from datetime import datetime
import mutilities
import bcrypt
import hashlib
import base64
import ftplib
import string
import time
from daemonClass import daemon
import sys

#!/usr/bin/env python
"""A simple shell application."""
class shell(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        username = getpass.getuser() #user 
        homedir = os.getcwd() #cwd
        hostname = socket.gethostname() #hostname
        self.colors = mutilities.colors()
        
        self.default_to_shell = True #use default shell commands
        self.prompt =self.colors.OKGREEN+username+"@"+hostname+":"+self.colors.OKBLUE+homedir+self.colors.WHITE+"$ "
        self.maxrepeats = 3
        self.poutput("\nWelcome to So1_Shell_2022. \nMade by: Cardozo & Monzon.")
 
    def onecmd( self, s, **kwargs): #  **kwargs simplemente captura todos los argumentos de palabras clave y los pasa al método de la clase base. 
        #print(s.raw)
        comando=s.raw # obtenemos cada comando realizado
        ubi='/historialFINAL.txt'
        f = open (ubi,'a')
        f.write(f'{comando}\n') #guardamos para historial
        f.close()
        self.logRegistroDiario(''.join(comando)) #guardamos para logDiario
        return cmd2.Cmd.onecmd(self, s ,**kwargs)
    
    def logRegistroDiario(self,ch):
        direccion='var/log/shell/comandosDiarios.log'
        file = open(direccion, 'a')
        logger = logging.getLogger('RegistroDiario')
        logger.setLevel(logging.DEBUG) #DEBUG Reportar eventos que ocurren durante el funcionamiento normal de un programa
       
        fileHandler = logging.FileHandler(direccion, mode='a')# envía la salida de registro a un archivo de disco
        fileHandler.setLevel(logging.DEBUG)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
       
        logger.debug(ch)
        logger.removeHandler(fileHandler)
        fileHandler.close()

    def logRegistroUsuario(self,ch):
        direccion='/var/log/shell/registrosUsuarios.log'
        file = open(direccion, 'a')

        logger = logging.getLogger('RegistroUsuario')
        logger.setLevel(logging.DEBUG) # DEBUG Reportar eventos que ocurren durante el funcionamiento normal de un programa

        fileHandler = logging.FileHandler(direccion, mode='a')# envía la salida de registro a un archivo de disco
        fileHandler.setLevel(logging.DEBUG)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
        logger.debug(ch)
        
        logger.removeHandler(fileHandler)
        fileHandler.close()

    # def logRegistroHorario(self,ch): # log para guardar usuarios fuera de horario
    def logRegistroHorario(self,ch):
        direccion='/var/log/shell/usuario_horarios_log.log'
        file = open(direccion, 'a')

        logger = logging.getLogger('RegistroFueraHorario')
        logger.setLevel(logging.WARNING) #Un indicio de que algo inesperado sucedió

        fileHandler = logging.FileHandler(direccion, mode='a')# envía la salida de registro a un archivo de disco
        fileHandler.setLevel(logging.WARNING)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
        logger.warning(ch)
        
        logger.removeHandler(fileHandler)
        fileHandler.close()

    # log FTP
    def logShellTransferencia(self,ch):
        direccion='/var/log/shell/Shell_transferencias.log'
        file = open(direccion, 'a')
        
        logger = logging.getLogger('ShellTransferencia')
        logger.setLevel(logging.DEBUG) #DEBUG Información detallada
       
        fileHandler = logging.FileHandler(direccion, mode='a')# envía la salida de registro a un archivo de disco
        fileHandler.setLevel(logging.DEBUG)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
       
        logger.debug(ch)
        logger.removeHandler(fileHandler)
        fileHandler.close()
    #log error
    def logRegistroError(self,ch):
        direccion='var/log/shell/sistema_error.log'
        file = open(direccion, 'a')
        
        logger = logging.getLogger('RegistroError')
        logger.setLevel(logging.ERROR) #ERROR un problema más grave, el software no ha sido capaz de realizar alguna función.
       
        fileHandler = logging.FileHandler(direccion, mode='a')
        fileHandler.setLevel(logging.ERROR)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
       
        logger.error(ch)
        logger.removeHandler(fileHandler)
        fileHandler.close()
    
    ###4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
    ###4.1.1. El input debe tener el siguiente formato: Archivo(s) DirectorioDestino
    copyParser=Cmd2ArgumentParser()
    copyParser.add_argument('src',nargs=1,help='Source Path of file or directory.')
    copyParser.add_argument('dst',nargs=1,help='Destiny Path of file or directory.')\
    
    @with_argparser(copyParser)
    def do_copy(self,args):
        src=(os.path.abspath(os.path.expanduser(args.src[0])))
        dst=str(os.path.abspath(os.path.expanduser(args.dst[0])))
        name = "copy"
        guardarParam = (name,src,dst)
        if os.path.isfile(src)==True: # verificar si existe
            shutil.copy(src, dst)
            return 0
        file_names = os.listdir(src) # listar 
        try:   
            for file_name in file_names:
                shutil.copy(file_names[file_name], dst)
            self.poutput("File copied successfully.")
            #self.logRegistroDiario(' '.join(guardarParam))
            return 0
        
        # If src and dst are same
        except shutil.SameFileError:
            self.poutput(self.colors.FAIL+"Source and destination represents the same file.")
            self.logRegistroError(' '.join(guardarParam))
        
        # If there is any permission issue
        except PermissionError:
            self.poutput(self.colors.FAIL+"Permission denied.")
            self.logRegistroError(' '.join(guardarParam))
        
        # For other errors
        except:
            self.poutput(self.colors.FAIL+"Error occurred while copying file/s.")
            self.logRegistroError(' '.join(guardarParam))
    
    ###4.2. Mover - mover
    ###4.2.1. El input debe tener el siguiente formato: Archivo(s)/Directorio(s) DirectorioDestino.
    moveParser=Cmd2ArgumentParser()
    moveParser.add_argument('src',nargs=1,help='Source Path of file or directory.')
    moveParser.add_argument('dst',nargs=1,help='Destiny Path of file or directory.')
    
    @with_argparser(moveParser)
    def do_move(self,args):
        src=(os.path.abspath(os.path.expanduser(args.src[0])))
        dst=str(os.path.abspath(os.path.expanduser(args.dst[0])))
        name = "move"
        guardarParam = (name,src,dst)
        self.guardar(guardarParam)
        if os.path.isfile(src)==True: #verificar
            shutil.move(src, dst)
            return 0
        file_names = os.listdir(src) #listar
        try:   
            for file_name in file_names:
                shutil.move(file_names[file_name], dst)
            self.popout("File/s moved successfully.")
           # self.logRegistroDiario(' '.join(guardarParam))
            return 0
        except shutil.SameFileError:
            self.poutput("Source and destination represents the same file.")
            self.logRegistroError(' '.join(guardarParam))
        except PermissionError:
            self.poutput("Permission denied.")
            self.logRegistroError(' '.join(guardarParam))
    
    ###4.3. Renombrar - renombrar
    def do_rename(self,FILENAME): #these are the parameters needed
        cwd = os.getcwd() #Get current working directory
        src = f'{cwd}/{FILENAME.arg_list[0]}' #current name
        dst = f'{cwd}/{FILENAME.arg_list[1]}' #new name
        name = "rename"
        guardarParam = (name,src,dst)
        try:
            if src!=dst: #if name different rename
                os.rename(src,dst)
                self.poutput("File renamed successfully.")
        #elif src==dst: #if name same show error
          #  self.poutput("Name has to be different to current.")
         #   self.logRegistroError(' '.join(guardarParam))
        except:
            print("renaming Error")
            self.logRegistroError(' '.join(guardarParam))
     
    ###4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    ###4.4.1. Si no recibe argumentos, debe listar los archivos/directorios de la carpeta actual.
    ###4.4.2. En caso de recibir un directorio, listar archivos/directorios de esedirectorio.       
    #listar// okkkk // ver si se necesita -l o -la retcode = subprocess.call(['ls', '-l'])  
    def do_listar(self,dirPATH):
        name = "listar"
        try:
            if len(dirPATH)==0: #listar mismo cwd
                cwd=os.getcwd()
                guardarParam = (name,cwd)
                list=os.listdir(cwd)
                lenlist=len(list)
                for i in range(lenlist):
                    if i+1==lenlist:
                        self.poutput(f"{list[i]}")
                    else:
                        self.poutput(f"{list[i]}",end=" - ")
            else:
                dir=dirPATH[0:len(dirPATH)]
                
                if dirPATH[0]=='/': #si ingresamos por ej listar /test
                    dir=dirPATH[1:len(dirPATH)]
            
                guardarParam=(name,dir)
                
                if os.path.exists(dir)==True: #si existe listamos dir
                    guardarParam1 = name+' '+dir
                    #print("entro en dist")
                    list=os.listdir(dir)
                    lenlist=len(list)
                    for i in range(lenlist):
                        if i+1==lenlist:
                            self.poutput(f"{list[i]}")
                        else:
                            self.poutput(f"{list[i]}",end=" - ")
                
                elif os.path.exists(dir)==False: #si no existe
                   print(self.colors.FAIL+"El archivo", dir ,"no existe")
                   self.logRegistroError(' '.join(guardarParam))
        except: 
            print(self.colors.FAIL+"Error listar")
            self.logRegistroError(' '.join(guardarParam))
    
    ###4.5. Crear un directorio - creardir
    ###4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
    def do_makedir(self,dirnames):
        name = "makedir"
        guardarParam=(name, dirnames)
        cwd=os.getcwd() # obtenemos directorio actual
        dirlen=len(dirnames.arg_list) 
        try:
            for i in range(dirlen):
                dirname=f"{dirnames.arg_list[i]}" #con un for vamos creando uno o mas directorios
                path=os.path.join(cwd,dirname) # Une uno o mas directorios 
                os.mkdir(path)
                #guardarParam.append(dirnames.arg_list[i])
        except:
            print(self.colors.FAIL+"error makedir")
            self.logRegistroError(' '.join(guardarParam))
    
    ### 4.6. Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
    def do_ir(self,dirPATH):
        name = "ir"
        guardarParam=(name,dirPATH)
        cwd1 = os.getcwd()#current working directory
        username = getpass.getuser()
        try:
            if cwd1==dirPATH: # mismo directorio
                self.poutput("Path is the same as current directory. \n")
                cwd2=cwd1
            
            if dirPATH!=cwd1 and dirPATH[0]=='/': # si se ingresa directorio dif y con /
                i="/"
                indice=dirPATH.index(i)
                dirB=dirPATH[indice+1:len(dirPATH)]
                print("dir",dirB)
                os.chdir(dirB)
                cwd2 = os.getcwd()

            elif dirPATH!=cwd1: # si queremos salir, ejemplo: ir .. o ir directorio sin /
                os.chdir(dirPATH)
                cwd2 = os.getcwd()

            hostname = socket.gethostname()
            self.prompt =self.colors.OKGREEN+username+"@"+hostname+":"+self.colors.OKBLUE+cwd2+"$ "+self.colors.MAGENTA
        
        except:
            guardarParam=(name,dirPATH+" no such file directory")
            print(self.colors.FAIL+"ERROR : ",dirPATH," no such file directory ")
            self.logRegistroError(' '.join(guardarParam))
            
            
    ####4.7. Cambiar los permisos sobre un archivo o un directorio - permisos
    def do_permisos(self,perPATH):
        ##separar la cadena y ver como cambiar el numero de permisos
        ##El primer dígito corresponde a los permisos del usuario, el segundo a los del grupo y el tercero a los del resto de usuarios.
        ## split separador y cuantas divisiones en total
        name = "permisos"
        newCAD=perPATH.split(' ', 2)
        guardarParam=(name,newCAD[0],newCAD[1])
        try:
            os.chmod(newCAD[1],int(newCAD[0],8)) ## convierte cadena octal a decimal por ej 777 a 511 y el decimal se envia como parametro
            print(self.colors.OKGREEN+"changed")
        except:
            print(self.colors.FAIL+"error changing permissions")
            self.logRegistroError(' '.join(guardarParam))

    ###4.8. Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    ###4.8.1. Debe usar el formato USUARIO:GRUPO
    ##cambiar propietario// que hacer si no existe ese usuario o grupo?????se crea o se imprime mensaje de error
    def do_propietario(self,cad):
        name="propietario"
        guardarParam=(name,cad)
        i=":"
        j=" "
        indice=cad.index(i) #buscamos ':'
        indice1=cad.index(j)                                                                                        ##FIX
        user=cad[0:indice] #asignamos a user la cadena antes del :
        group=cad[indice+1:indice1]#asignamos a group la cadena despues del : 
        propPATH=cad[indice1+1:len(cad)]#archivo/directorio
        try:
            dirlen=len(cad.arg_list)
            for i in range(1,dirlen): # for para cambiar propietario de uno o mas archivos/directorios
                dirname=f"{cad.arg_list[i]}"
                shutil.chown(dirname, user, group)
        except :
            print(self.colors.FAIL+"error")
            self.logRegistroError(' '.join(guardarParam))
        
    ###4.9. Cambiar la contraseña - contraseña
    passparser = Cmd2ArgumentParser()
    passparser.add_argument('usr',nargs=1, help='Nombre de usuario')

    @with_argparser(passparser)
    def do_setPass(self,args):
        username=args.usr[0]
        lastchanged = mutilities.days_since()
        paths = ["/etc/passwd","/etc/shadow"]
        files = []
        files = mutilities.parseFile(files,paths)
        passwdFile = files[0]
        shadowFile = files[1]
        userlist = []
        for line in range(len(passwdFile)):
            userlist.append(passwdFile[line][0])
        for line in range(len(userlist)):
            if username not in userlist:
                timeNow = datetime.now()
                current_time = timeNow.strftime("%H:%M:%S")
                self.logRegistroError(f"Username: {username} doesn't exist. Time of error: {current_time}")
                self.poutput(f"Username: {username} doesn't exist.\nExiting...")
                return 
        password = getpass.getpass('New password:')
        passwordcheck = getpass.getpass('Retype new password:')
        if password == passwordcheck:
            password = password.encode("utf-8")
        else:
            self.poutput('Sorry, passwords do not match.')
            self.poutput('passSet: password unchanged.')
            return
        salt = bcrypt.gensalt(prefix=b"2a")
        saltstr = mutilities.rmquotes(salt)
        p_hashed = bcrypt.hashpw(base64.b64encode(hashlib.sha512(password).digest()),salt)
        passString= mutilities.rmquotes(p_hashed)
        passwordFormat=f'$6${saltstr}${passString}'
        
        for i in range(len(passwdFile)):
            currentusername =passwdFile[i][0] #username
            if args.usr[0] == currentusername:
                passwdFile[i][1] = passwordFormat
                passwdtextline=passwdFile[i]
                passwdtextline = str(passwdtextline)
                break
        for i in range(len(shadowFile)):
            currentusername=shadowFile[i][0]
            if args.usr[0] == currentusername:
                shadowFile[i][1] = passwordFormat
                shadowFile[i][2] = str(lastchanged)
                shadowtextline=shadowFile[i]
                shadowtextline=str(shadowtextline)
                break
        mutilities.writePass(paths[0],passwdFile)
        mutilities.writePass(paths[1],shadowFile)
        self.poutput('Password set.')

    ###4.10. Agregar usuario, y deben registrar los datos personales del mismo incluyendo su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost). - usuario
    userparser = Cmd2ArgumentParser()
    userparser.add_argument('usr',nargs=1, help='Nombre de usuario')

    #checkip
    @with_argparser(userparser)
    def do_addusuario(self,args):
        separator=','
        username = args.usr[0]
        paths = ["/etc/passwd","/etc/shadow","/etc/group"]
        files = []
        files = mutilities.parseFile(files,paths)
        # print(files)
        for path in range(len(files[2])):
            timeNow = datetime.now()
            current_time = timeNow.strftime("%H:%M:%S")
            if files[2][path][0] == username:
                self.logRegistroError(f"{username} already exists. {current_time}")
                self.poutput(f"{username} already exists.Try again")
                return 
        homeDIR=f'/home/{username}'
        flagP=mutilities.checkpath(homeDIR) #check if path exists
        if flagP==True:
            self.poutput('Path already exists. Exiting...')
            return
        shellPATH='/bin/bash'
        encrypted_pwd= 'x'
        groupID = os.getpgrp()
        userID = mutilities.getUID()
        fullname =input('Insert your Name and Surname: ')
        ipadresses = []
        exit=0
        while exit != '1':
            ip=input('Ingrese la ip por donde se puede conectar: ')
            if ip =='':
                ip=input('Ingrese una ip valida: ')
            ipadresses.append(ip)
            exit = input('Ingrese 1 si agrego las ip correspondientes:')
        ipadresses=mutilities.turnElementTostr(ipadresses)
        ipadresses=mutilities.joinList(ipadresses,separator)
        horario=mutilities.verifyTime()
        workphone=input("Teléfono del Trabajo:")
        homephone=input("Teléfono de casa: ")
        horario=mutilities.joinList(horario,',')
        GECOS = [fullname,workphone,homephone,horario,ipadresses]
        GECOS=mutilities.joinList(GECOS,',')
        for path in range(len(paths)):
            files[path] = open(paths[path],"a+") 
        files[0].write(f"{username}:{encrypted_pwd}:{userID}:{groupID}:{GECOS}:{homeDIR}:{shellPATH}\n")
        files[1].write(f"{username}:!:0:0:99999:7:::\n")
        files[2].write(f"{username}:{encrypted_pwd}:{groupID}:\n")
        for path in range(len(paths)):
            files[path].close()
        os.mkdir(homeDIR)
        self.poutput(f'Path {homeDIR} created.')
        self.poutput(f'User {username} created.\nSet password with passSet ''<username>''.\n ')
        return 0
    
    # verficar horario laboral-falta
    def verificarHorario(self,b):
        hora_actual = b
        print(hora_actual)
        actualHora=hora_actual.hour
        actualMin=hora_actual.minute
        i=0
        username = getpass.getuser()
        for line in open('/etc/passwd', 'r'):
            i=i+1
            if re.search(username, line):
                print("en la linea:",i,  line)
             
        cadena=line.split(' ', 5)

        entrada=cadena[2].split(':', 2)
        salida=cadena[3].split(':', 2)
        if (int(entrada[0])>actualHora or int(entrada[1])>actualMin) or (int(salida[0])<actualHora or int(salida[1])<actualMin): #ver 
            print("FUERA DE HORARIO LABORAL")
            ip=socket.gethostbyname(socket.gethostname())#obtener ip
            guardarParam=(username, cadena[2],cadena[3],ip)
            self.logRegistroHorario(''.join(guardarParam))
            
    ### 4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
    def do_printdir(self,c):
        name = 'printdir'
        try:
            cwd=os.getcwd()#obtener diretorio actual
            guardarParam = (name,cwd) 
            self.poutput(cwd)#imprimir directorio actual
        except:
            print(self.colors.FAIL+"Error printdir",cwd)
            self.logRegistroHorario(''.join(guardarParam))
    
    
    ###4.12. Terminar procesos con señales determinadas - kill
    ###4.12.1. Debe aceptar el input con el formato: PID(s) señal
    matarparser = Cmd2ArgumentParser()
    matarparser.add_argument('-9', '--SIGKILL', action='store_true', help='Kill signal.')
    matarparser.add_argument('-15', '--SIGTERM', action='store_true', help='Termination signal.')
    matarparser.add_argument('-19', '--SIGSTOP', action='store_true', help='Stop signal.')
    matarparser.add_argument('pids',type=int,nargs='+', help='Process ids.')
    
    @with_argparser(matarparser)
    def do_matar(self,args):
        name = 'matar'
        for pid in range(len(args.pids)):
            if args.SIGKILL:
                signal_ID=9   
                os.kill(args.pids[pid],signal_ID)
                process = psutil.Process(args.pids[pid])
                process_name = process.name()
                self.poutput(f'Process {process_name} killed. PID:{args.pids[pid]}\n')
            if args.SIGTERM:
                signal_ID=15
                os.kill(args.pids[pid],signal_ID)
                process = psutil.Process(args.pids[pid])
                process_name = process.name()
                self.poutput(f'Process {process_name} terminated. PID:{args.pids[pid]}\n')
            if args.SIGSTOP:
                signal_ID=19
                os.kill(args.pids[pid],signal_ID)
                process = psutil.Process(args.pids[pid])
                process_name = process.name()
                self.poutput(f'Process {process_name} stopped. PID:{args.pids[pid]}\n')

    ###4.13. Buscar un string en un archivo - grep
    def do_fgrep(self,gpath):
        gpath=gpath.split(' ', 2)
        name='fgrep'
        guardarParam = (name,gpath[0],gpath[1])
        band=False
        i=0
       
        if os.path.exists(gpath[1])==True: #si existe archivo
            for line in open(gpath[1], 'r'):
                i=i+1
                if re.search(gpath[0], line):
                    print("en la linea:",i,  line) #buscamos el string en todo el archivo
                    band=True
           
            if band==False: #si la bandera queda false, no se encontro string
                print(self.colors.FAIL+"Error: El string no existe")
                self.logRegistroError(' '.join(guardarParam))
        else:
            print(self.colors.FAIL+"Error: El archivo no existe") #archivo no existe
            self.logRegistroError(' '.join(guardarParam))
        
    ###4.14. Imprimir un historial de comandos - history
    def do_historial (self,arg):
        name = 'historial'
        f = open ('/historialFINAL.txt','r') #muestra en pantalla el historial
        for linea in f:
           print (linea)

    ###4.15 El usuario debe poder levantar y apagar demonios dentro del sistema,
    ###     utilizando una herramienta como service de CentOS. (no puede ser una
    ###     llamada a sistema a la función service o systemctl)
    class Cdaemon(daemon):
        def run(self):
                while True:
                        time.sleep(1)
        def quit(self):
                while True:
                    time.sleep(1)
                    
    daemonParser = Cmd2ArgumentParser()
    daemonParser.add_argument('daemon',nargs=1,type=str,help='Program to daemonize.')
    daemonParser.add_argument('sig', nargs=1,type=str, help='Signal to send.')

    @with_argparser(daemonParser)
    def do_daemonControl(self,args):
        daemonPath=(os.path.abspath(os.path.expanduser(args.daemon[0])))
        daemon = self.Cdaemon(daemonPath)
        sysargsv = [args.daemon[0],args.sig[0]]
        if len(sysargsv) == 2:
                if 'start' == sysargsv[1]:
                        daemon.start()
                elif 'stop' == sysargsv[1]:
                        daemon.stop()
                elif 'restart' == sysargsv[1]:
                        daemon.restart()
                else:
                        print('Unknown command')
                        return 1
                sys.exit(0)
        else:
                print(f"usage: {sysargsv[0]} start|stop|restart")
                return 1
        

    ###4.16. Proveer la capacidad de poder ejecutar comandos del sistema, que no 
    ###      sean los comandos mencionados arriba.- LISTO

    ###4.17. Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar
    ###      con los registros de su horario cada vez que inicia/cierra la sesión y si esta
    ###      fuera del rango escribir en el archivo de log (usuario_horarios_log) un
    ###      mensaje que aclare que está fuera del rango y deben agregar el lugar desde
    ###      donde realizó la conexión que también puede estar fuera de sus IPs habilitado.

    ###4.18. Ejecutar una transferencia por ftp o scp, se debe registrar en el log
    ###      Shell_transferencias del usuario.

    def do_ftpTransferencia(self,b): # hostname user file
        #datos para la prueba!!!!!!!!!!!!!!!!!
        #hostname = "ftp.dlptest.com"
        #username = "dlpuser"
        #passw = "rNrKYTX9g7z3RgJRmxWuGHbeu"
        #filename = "gfg.txt"
        passw = getpass.getpass()

        while len(b)==0: #si se ingresa vacio
            b = input("ingrese datos novacio, ej: hostname user file  ")
            passw = getpass.getpass()
            #passw = "rNrKYTX9g7z3RgJRmxWuGHbeu"
        
        aux=b.split(' ', 3) 
        hostname = aux[0]
        username = aux [1]
        filename = aux [2]
        guardarParam=("ftpTransferencia",b)
        ftp_server = ftplib.FTP(hostname, username, passw) #datos del sitio
        ftp_server.encoding = "utf-8"
        
        typ = input("Ingrese s para subir o b para bajar: ") #verificacion si desea subir o bajar archivos
        while typ!='s' and typ!='b':
            typ = input("Ingrese s para subir o b para bajar: ")

        try:
            if typ=='s':
                print("subir archivos")
                
                x=input("desea subir el archivo existente o crear? ingrese existente o nuevo: ") #verificacion si desea subir archivo existente o nuevo
                while(x!='existente' and x!='nuevo'):
                    x=input("desea subir archivo existente o crear? ingrese existente o nuevo: ")
                
                if x=='existente':
                    while (os.path.exists(filename)==False): # verificacion si existe archivo
                        filename=input("error ingrese archivo existente ")
                    with open(filename, "rb") as file: # subir archivo
                        ftp_server.storbinary(f"STOR {filename}", file) #obtiene nombre del archivo y archivo de ftp
                    ftp_server.dir()
                    ftp_server.quit()
                
                elif x=='nuevo':
                    filen=input("ingrese nombre del archivo nuevo: ") #crear archivo y editar par subir
                    contenido=input("ingrese texto para el archivo nuevo: ")
                    archivo=open(filen, "a")
                    archivo.write(contenido)
                    archivo.close()
                    guardarParam=("ftpTransferencia",hostname,username,filen)
                    with open(filen, "rb") as file: 
                        ftp_server.storbinary(f"STOR {filen}", file)#obtiene nombre del archivo y archivo de ftp
                    ftp_server.dir()
                    ftp_server.quit()
            
            elif typ =='b':
                print("bajar archivo")
                with open(filename, "wb") as file: 
                    ftp_server.retrbinary(f"RETR {filename}", file.write) #bajar archivo , obtiene nombre del archivo y archivo de ftp
                
                ftp_server.dir()
                file= open(filename, "r") 
                print('File Content:', file.read()) #imprime el contenido
                ftp_server.quit()
            
            print(self.colors.OKGREEN+"Transferencia OK")
            self.logShellTransferencia(' '.join(guardarParam))

        except: 
            print(self.colors.FAIL+"Error al hacer TransferenciaFTP") 
            self.logRegistroError(' '.join(guardarParam))

    def do_clean(self,args):
        name = 'clean'
        _ = system('clear')  #limpiar pantalla
        
    
    def do_exit(self,e): 
        check=input('Are you sure you want to exit?. y/n: ') #cerrar sesion y verificacion de horario
        print(check)
        if check in ["y","Y"]: 
            print("EXIT!")
           # self.verificarHorario(datetime.now().time()) # enviamos horario actual para verificar horario
            return True
        
    
    def do_shutdown(self,e): 
        #self.verificarHorario(datetime.now().time()) #enviamos horario actual para verificar horario si desea apagar la maquina
        return os.system("shutdown 0 /t 1")
    

if __name__ == '__main__':
    c = shell()
    #c.verificarHorario(datetime.now().time()) # para inicio sesion
    sys.exit(c.cmdloop())

