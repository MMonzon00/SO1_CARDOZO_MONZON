import cmd2
import argparse

#!/usr/bin/env python
"""A simple cmd2 application."""
class shell(cmd2.Cmd):
    """A simple cmd2 application."""
    def __init__(self):
        super().__init__()

        self.prompt='Martinshell$'
        
    
    def do_copy(self,archcp,dirsrc,dirdst):
        src = r'dirsrc'
        dst = r'dirdst'
        try:
            os.sendfile(src, dst)
            self.("File copied successfully.")
        
        # If src and dst are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
        
        # If dst is a directory.
        except IsADirectoryError:
            print("Destination is a directory.")
        
        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")
        
        # For other errors
        except:
            print("Error occurred while copying file.")
        # 4.1. Copiar (no puede ser una llamada a sistema a la función cp) - copiar
        # 4.1.1. El input debe tener el siguiente formato: Archivo(s) DirectorioDestino
    def do_move(self,archcp,dirsrc,dirdst):
        # 4.2. Mover - mover
        # 4.2.1. El input debe tener el siguiente formato: Archivo(s)/Directorio(s)
        # DirectorioDestino.
        # 4.2.2. Ejemplos: https://linuxhandbook.com/mv-command/
    def do_rename(self):

    def do_listdir(self):
        #4.4. Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
        # 4.4.1. Si no recibe argumentos, debe listar los archivos/directorios de la
        # carpeta actual.
        # 4.4.2. En caso de recibir un directorio, listar archivos/directorios de ese
        # directorio.
    def do_makedir(self,*dirname):
        for dirname
        #4.5.1. Debe recibir 1 o más argumentos y crear un directorio por cada uno.
    def do_changedir(self,):
    def do_hello(self):
    def do_hello(self):
    def do_hello(self):
    
  



if __name__ == '__main__':
    import sys
    c = shell()
    sys.exit(c.cmdloop())