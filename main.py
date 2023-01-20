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

# from usefunctions import *

#!/usr/bin/env python
"""A simple shell application."""
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
BOLD = '\033[1m'
WHITE = '\033[37m'
MAGENTA='\033[35m'
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
    def __init__(self):
        super().__init__()
        username = getpass.getuser()
        homedir = os.getcwd()
        hostname = socket.gethostname()
        
        self.default_to_shell = True #use default shell commands
        self.prompt =OKGREEN+username+"@"+hostname+":"+OKBLUE+homedir.replace('/root','~')+WHITE+"$ "
        self.maxrepeats = 3
        self.poutput("\nWelcome to So1_Shell_2022. \nMade by: Cardozo & Monzon.")
 
  
    def onecmd( self, s, **kwargs): #  **kwargs simplemente captura todos los argumentos de palabras clave y los pasa al método de la clase base. 
        print(s.raw)
        comando=s.raw
        ubi='historialFINAL.txt'
        f = open (ubi,'a')
        f.write(f'{comando}\n')
        f.close()
        return cmd2.Cmd.onecmd(self, s ,**kwargs)
    

    def logRegistroDiario(self,ch):
        direccion='/var/log/comandosDiarios.log'
        #if os.path.exists('var/log')==False:
        #    print("Directory doesn't exist.")
        #    cwd=os.getcwd()
        #    path=os.path.join(cwd,'var','log')
        #    os.makedirs(path)
        
        file = open(direccion, 'a')
        
        logger = logging.getLogger('RegistroDiario')
        logger.setLevel(logging.DEBUG)
       
        fileHandler = logging.FileHandler(direccion, mode='a')# envía la salida de registro a un archivo de disco
        fileHandler.setLevel(logging.DEBUG)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
       
        logger.debug(ch)
        logger.removeHandler(fileHandler)
        fileHandler.close()

    def logRegistroUsuario(self,ch):
        direccion='/var/log/registrosUsuarios.log'
        #if os.path.exists('var/log')==False:
        #    print("entra en no existeee")
        #    cwd=os.getcwd()
        #    path=os.path.join(cwd,'var','log')
        #    os.makedirs(path)

        file = open(direccion, 'a')

        logger = logging.getLogger('RegistroUsuario')
        logger.setLevel(logging.DEBUG)

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
        direccion='/var/log/(usuario_horarios_log).log'
        #if os.path.exists('var/log')==False:
        #    print("entra en no existeee")
        #    cwd=os.getcwd()
        #    path=os.path.join(cwd,'var','log')
        #    os.makedirs(path)

        file = open(direccion, 'a')

        logger = logging.getLogger('RegistroFueraHorario')
        logger.setLevel(logging.WARNING)

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
        direccion='/var/log/Shell_transferencias.log'
        #if os.path.exists('var/log')==False:
        #    print("Directory doesn't exist.")
        #    cwd=os.getcwd()
        #    path=os.path.join(cwd,'var','log')
        #    os.makedirs(path)
        
        file = open(direccion, 'a')
        
        logger = logging.getLogger('ShellTransferencia')
        logger.setLevel(logging.DEBUG)
       
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
        direccion='/var/log/shell/sistema_error.log'
        #if os.path.exists('var/log/shell')==False:
        #    # print("entra en no existe")
        #    cwd=os.getcwd()
        #    path=os.path.join(cwd,'var/log/shell')
        #    os.makedirs(path)
        
        file = open(direccion, 'a')
        
        logger = logging.getLogger('RegistroError')
        logger.setLevel(logging.ERROR)
       
        fileHandler = logging.FileHandler(direccion, mode='a')
        fileHandler.setLevel(logging.ERROR)
       
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formato)
        logger.addHandler(fileHandler)
       
        logger.error(ch)
        logger.removeHandler(fileHandler)
        fileHandler.close()

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
            self.logRegistroDiario(' '.join(guardarParam))
        
        # If src and dst are same
        except shutil.SameFileError:
            self.poutput("Source and destination represents the same file.")
            self.logRegistroError(' '.join(guardarParam))
        
        # If there is any permission issue
        except PermissionError:
            self.poutput("Permission denied.")
            self.logRegistroError(' '.join(guardarParam))
        
        # For other errors
        except:
            self.poutput("Error occurred while copying file/s.")
            self.logRegistroError(' '.join(guardarParam))
    
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
            self.logRegistroDiario(' '.join(guardarParam))
        elif src==dst:
            self.poutput("Source and destination represents the same file.")
            self.logRegistroError(' '.join(guardarParam))
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
        self.logRegistroDiario(' '.join(guardarParam))
        if src!=dst: #if name different rename
            os.rename(src,dst)
            self.poutput("File renamed successfully.")
            self.logRegistroDiario(' '.join(guardarParam))
        elif src==dst: #if name same show error
            self.poutput("Name has to be different to current.")
            self.logRegistroError(' '.join(guardarParam))
        else:
            self.logRegistroError(' '.join(guardarParam))
     
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
            self.logRegistroDiario(' '.join(guardarParam))
            print("entro en misma carpeta")
            list=os.listdir(cwd)
            lenlist=len(list)
            for i in range(lenlist):
                if i+1==lenlist:
                    self.poutput(f"{list[i]}")
                else:
                    self.poutput(f"{list[i]}",end=" - ")
        else:
            dir=dirPATH[0:len(dirPATH)]
            
            if dirPATH[0]=='/':
                dir=dirPATH[1:len(dirPATH)]
            
            guardarParam=(name,dir)#historial
            self.guardar(guardarParam)

            if os.path.exists(dir)==True:
                guardarParam1 = name+' '+dir
                self.logRegistroDiario(guardarParam1)
                print("entro en dist")
                list=os.listdir(dir)
                lenlist=len(list)
                for i in range(lenlist):
                    if i+1==lenlist:
                        self.poutput(f"{list[i]}")
                    else:
                        self.poutput(f"{list[i]}",end=" - ")
            elif os.path.exists(dir)==False:
                print("El archivo", dir ,"no existe")
                self.logRegistroError(' '.join(guardarParam))

    ###4.5. Crear un directorio - creardir
    ###4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
    ## ver historial!!!!!!!!!!!!!
    def do_makedir(self,dirnames):
        name = "makedir"
        guardarParam=(name, dirnames)
        cwd=os.getcwd()
        dirlen=len(dirnames.arg_list)
        self.guardar(guardarParam)
        try:
            for i in range(dirlen):
                dirname=f"{dirnames.arg_list[i]}"
                path=os.path.join(cwd,dirname)
                os.mkdir(path)
                #guardarParam.append(dirnames.arg_list[i])
            self.logRegistroDiario(' '.join(guardarParam))
        except:
            print("error")
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
                #print("cwd con barra",cwd2)
                
            
            elif dirPATH!=cwd1: # si queremos salir, ejemplo: ir .. o ir directorio sin /
                #print("entro en else")
                os.chdir(dirPATH)
                cwd2 = os.getcwd()
            
            self.logRegistroDiario(' '.join(guardarParam))
            hostname = socket.gethostname()
            self.prompt =OKGREEN+username+"@"+hostname+":"+OKBLUE+cwd2+"$ "+MAGENTA
        
        except:
            guardarParam=(name,dirPATH+" file not such directory")
            print("ERROR : ",dirPATH," file not such directory ")
            self.logRegistroError(' '.join(guardarParam))
            
            
    ####4.7. Cambiar los permisos sobre un archivo o un directorio - permisos//// falta
    def do_permisos(self,perPATH):
        ##separar la cadena y ver como cambiar el numero de permisos
        ##El primer dígito corresponde a los permisos del usuario, el segundo a los del grupo y el tercero a los del resto de usuarios.
        ## split separador y cuantas divisiones en total
        name = "permisos"
        newCAD=perPATH.split(' ', 2)
        guardarParam=(name,newCAD[0],newCAD[1])
        self.guardar(guardarParam)
        self.logRegistroDiario(' '.join(guardarParam))
        try:
            os.chmod(newCAD[1],int(newCAD[0],8)) ## convierte cadena octal a decimal por ej 777 a 511 y el decimal se envia como parametro
            ## binario = ' '.join(format(c, 'b') for c in bytearray(newCAD[0], "utf-8"))
            ## binario = bin(newCAD[0])
        except:
            print("Error a cambiar permisos")
            self.logRegistroError(' '.join(guardarParam))

    ###4.8. Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    ###4.8.1. Debe usar el formato USUARIO:GRUPO
    ##cambiar propietario// que hacer si no existe ese usuario o grupo?????se crea o se imprime mensaje de error
    def do_propietario(self,cad):
        name="propietario"
        guardarParam=(name,cad)
        self.guardar(guardarParam)
        #self.logRegistroDiario(' '.join(guardarParam))
        i=":"
        j=" "
        indice=cad.index(i)
        indice1=cad.index(j)                                                                                        ##FIX
        user=cad[0:indice]
        group=cad[indice+1:indice1]
        propPATH=cad[indice1+1:len(cad)]
        try:
            shutil.chown(propPATH, user, group)
            self.logRegistroDiario(' '.join(guardarParam))
        except :
            self.logRegistroError(' '.join(guardarParam))
        shutil.chown(propPATH, user, group)
        
    
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
        
        with open('test.txt', 'r') as file:
             # read a list of lines into data
             data = file.readlines()
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
        self.popout('Password set.')

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
        band=False
        i=0
        username = getpass.getuser()
        if os.path.exists('var/log/registrosUsuarios.log')==True:
            for line in open('var/log/etc/passwd', 'r'):
                i=i+1
                if re.search(username, line):
                    print("en la linea:",i,  line)
                    band=True
            cadena=line.split(' ', 4)

        entrada=cadena[2].split(':', 2)
        salida=cadena[3].split(':', 2)
        if (int(entrada[0])>actualHora or int(entrada[1])>actualMin) or (int(salida[0])<actualHora or int(salida[1])<actualMin): #ver 
            print("FUERA DE HORARIO LABORAL")
            ip=socket.gethostbyname(socket.gethostname())#obtener ip
            guardarParam=(username, cadena[2],cadena[3],ip)
            self.logRegistroHorario(''.join(guardarParam))
            

    ### 4.11. Imprimir el directorio en el que se encuentra la shell actualmente - pwd
    def do_printdir(self):
        name = 'printdir'
        cwd=os.getcwd()
        guardarParam = (name,cwd)
        self.logRegistroDiario(''.join(guardarParam))
        self.guardar(guardarParam)
        self.poutput(cwd)

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
        pids=[]
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
        self.guardar(guardarParam)
        #self.logRegistroDiario(' '.join(guardarParam))
        band=False
        i=0
        if os.path.exists(gpath[1])==True:
            for line in open(gpath[1], 'r'):
                i=i+1
                if re.search(gpath[0], line):
                    print("en la linea:",i,  line)
                    band=True
            self.logRegistroDiario(' '.join(guardarParam))       
            if band==False:
                print("Error: El string no existe")
                self.logRegistroError(' '.join(guardarParam))
        else:
            print("Error: El archivo no existe")
            self.logRegistroError(' '.join(guardarParam))
        
    ###4.14. Imprimir un historial de comandos - history
    def do_historial (self,arg):
        name = 'historial'
        self.guardar(name)
        self.logRegistroDiario(''.join(name))
        f = open ('historial.txt','r')
        for linea in f:
           print (linea)

    ###4.15 El usuario debe poder levantar y apagar demonios dentro del sistema,
    ###     utilizando una herramienta como service de CentOS. (no puede ser una
    ###     llamada a sistema a la función service o systemctl)

    ###4.16. Proveer la capacidad de poder ejecutar comandos del sistema, que no 
    ###      sean los comandos mencionados arriba.- falta agregar a historial

    ###4.17. Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar
    ###      con los registros de su horario cada vez que inicia/cierra la sesión y si esta
    ###      fuera del rango escribir en el archivo de log (usuario_horarios_log) un
    ###      mensaje que aclare que está fuera del rango y deben agregar el lugar desde
    ###      donde realizó la conexión que también puede estar fuera de sus IPs habilitado.
        # controller
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)

    ###4.18. Ejecutar una transferencia por ftp o scp, se debe registrar en el log
    ###      Shell_transferencias del usuario.

    def do_ftpTransferencia(self,b): # hostname user file
        aux=b.split(' ', 3)
        hostname = aux[0]
        username = aux [1]
        filename = aux [2]
        print (hostname)
        print (username)
        print (filename)
        passw = "eUj8GeW55SvYaswqUyDSm5v6N"
        while b==' ':
            hostname = input("ingrese hostname novacio")
            username = input("ingrese username novacio")
            filename = input("ingrese filename novacio")
            passw = "eUj8GeW55SvYaswqUyDSm5v6N"
       # passw = getpass.getpass()
        while (os.path.exists(filename)==False):
            filename=input("ingrese archivo existente")
        
        ftp_server = ftplib.FTP(hostname, username, passw) 
        ftp_server.encoding = "utf-8"
        typ = input("Ingrese S para subir o B para bajar: ")
        while typ!='s' or typ!='b':
            typ = input("Ingrese s para subir o b para bajar: ")
        try:
            if typ=='s':
                with open(filename, "rb") as file: 
                    ftp_server.storbinary(f"STOR {filename}", file)
                ftp_server.dir()
                ftp_server.quit()
            elif typ =='b':
                with open(filename, "wb") as file: 
                    ftp_server.retrbinary(f"RETR {filename}", file.write)
                
                file= open(filename, "r") 
                print('File Content:', file.read()) 
                ftp_server.quit()
        except: 
            print("Error al hacer TransferenciaFTP")

    def do_clean(self,args):
        name = 'clean'
        self.guardar(name)
        self.logRegistroDiario(''.join(name))
        _ = system('clear')  
        
    
    def do_exit(self,e): 
        self.logRegistroDiario(''.join('exit'))
        check=input('Are you sure you want to exit?. y/n: ')
        print(check)
        if check in ["y","Y"]: 
            print("EXIT!")
            self.verificarHorario(datetime.now().time())
            return True
        
    
    def do_shutdown(self,e): #ver
        self.verificarHorario(datetime.now().time())
        return os.system("shutdown /s /t 1")
        

if __name__ == '__main__':
    import sys
    c = shell()
    #c.verificarHorario(datetime.now().time()) # para inicio sesion
    sys.exit(c.cmdloop())