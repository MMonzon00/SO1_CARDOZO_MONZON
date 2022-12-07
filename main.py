import cmd2
import argparse
import os 
import shutil
import getpass
import socket
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
    def do_copy(self,arguments):
        dirsrc=arguments.arg_list[0]
        dirdst=arguments.arg_list[1]
        src = f'{dirsrc}'
        dst = f'{dirdst}'
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
        # 4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
        # 4.1.1. El input debe tener el siguiente formato: Archivo(s) DirectorioDestino
    
    
    def do_move(self,arguments):
        dirsrc=arguments.arg_list[0]
        dirdst=arguments.arg_list[1]
        src = f'{dirsrc}'
        dst = f'{dirdst}'
        if src!=dst:
            shutil.move(src,dst)
            self.popout("File moved successfully.")
        elif src==dst:
            self.poutput("Source and destination represents the same file.")
        # except PermissionError:
        #     self.poutput("Permission denied.")
        # except:
        #     self.poutput("Error occurred while moving file/s.")
        # 4.2. Mover - mover
        # 4.2.1. El input debe tener el siguiente formato: Archivo(s)/Directorio(s)
        # DirectorioDestino.
        # 4.2.2. Ejemplos: https://linuxhandbook.com/mv-command/
    
    def do_rename(self,FILENAME): #these are the parameters needed
        cwd = os.getcwd() #Get current working directory
        src = f'{cwd}/{FILENAME.arg_list[0]}' #current name
        dst = f'{cwd}/{FILENAME.arg_list[1]}' #new name
        if src!=dst: #if name different rename
            os.rename(src,dst)
            self.poutput("File renamed successfully.")
        elif src==dst: #if name same show error
             self.poutput("Name has to be different to current.")



    def do_listdir(self,dirPATH):
            cwd=os.getcwd()
            dirPATH=f"{cwd}/{dirPATH}"
            if dirPATH!=cwd:
                list=os.listdir(cwd)
                lenlist=len(list)
                for i in range(lenlist):
                    if i+1==lenlist:
                        self.poutput(f"{list[i]}")
                    else:
                        self.poutput(f"{list[i]}",end=" - ")
            else:
                list=os.listdir(dirPATH)
                lenlist=len(list)
                for i in range(lenlist):
                    if i+1==lenlist:
                        self.poutput(f"{list[i]}")
                    else:
                        self.poutput(f"{list[i]}",end=" - ")

    #     #4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    #     #4.4.1. Si no recibe argumentos, debe listar los archivos/directorios de la
    #     #carpeta actual.
    #     #4.4.2. En caso de recibir un directorio, listar archivos/directorios de ese
    #     #directorio.
    
    def do_makedir(self,dirnames):
        cwd=os.getcwd()
        dirlen=len(dirnames.arg_list)
        for i in range(dirlen):
            dirname=f"{dirnames.arg_list[i]}"
            path=os.path.join(cwd,dirname)
            os.mkdir(path)
    
    #4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
    def do_changedir(self,dirPATH):
        username = getpass.getuser()
        if dirPATH==dirPATH:
            os.chdir(dirPATH)
            cwd = os.getcwd() #current working directory
            hostname = socket.gethostname()
            self.prompt = f"{username}@{hostname}:{cwd}$"

    def do_printdir(self,dirPATH):
        cwd=os.getcwd()
        self.poutput(cwd)

    def do_clean(self,args):
        _ = system('clear')

    def do_hello(self,statement):
            self.poutput(statement.arg_list)    


if __name__ == '__main__':
    import sys
    c = shell()
    sys.exit(c.cmdloop())