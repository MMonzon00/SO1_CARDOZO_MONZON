import cmd2
import argparse
import os 
import shutil
import os
import shutil
import getpass
import socket

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
        homedir = os.path.expanduser("~")
       
        hostname = socket.gethostname()
        
        self.default_to_shell = True #use default shell commands
        self.prompt = f"{username}@{hostname}:{os.path.expanduser('~')} $"
        shortcuts = {'?': 'help', '+': 'shell', '@': 'run_script', '@@': '_relative_run_script'}
        print(shortcuts)
    def do_copy(self,archcp,dirsrc,dirdst):
        src = r'dirsrc'
        dst = r'dirdst'
        try:
            os.sendfile(src, dst)
            self.popout("File copied successfully.")
        
        # If src and dst are same
        except shutil.SameFileError:
            self.poutput("Source and destination represents the same file.")
        
        # If dst is a directory.
        except IsADirectoryError:
            self.poutput("Destination is a directory.")
        
        # If there is any permission issue
        except PermissionError:
            self.poutput("Permission denied.")
        
        # For other errors
        except:
            self.poutput("Error occurred while copying file.")
        # 4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
        # 4.1.1. El input debe tener el siguiente formato: Archivo(s) DirectorioDestino
    #def do_move(self,archcp,dirsrc,dirdst):
        # 4.2. Mover - mover
        # 4.2.1. El input debe tener el siguiente formato: Archivo(s)/Directorio(s)
        # DirectorioDestino.
        # 4.2.2. Ejemplos: https://linuxhandbook.com/mv-command/
    # def do_rename(self):

    # def do_listdir(self):
    #     #4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    #     # 4.4.1. Si no recibe argumentos, debe listar los archivos/directorios de la
    #     # carpeta actual.
    #     # 4.4.2. En caso de recibir un directorio, listar archivos/directorios de ese
    #     # directorio.
        
    # def do_makedir(self,*dirname):
    #     for dirname
    #     return 0
    #4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
    # def do_changedir(self):
    #     return 0
    def do_hello(self,opt):
        opt=f"hello {opt} "
        self.poutput(opt)
        


if __name__ == '__main__':
    import sys
    c = shell()
    sys.exit(c.cmdloop())