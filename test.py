import getpass
import socket
import mutilities
import cmd2
from datetime import datetime
class shell(cmd2.Cmd):
     nombre='carlos'

     
def controlHorario(a):
        c=shell()
        colors=mutilities.colors()
        username = a
        print(username)
        hostname = socket.gethostname()
        print(hostname)
        currentIP= socket.gethostbyname(hostname)  
        print(currentIP)
        passwdFile = "/etc/passwd"
        passwdFile = mutilities.readFileLines(passwdFile)
        print(passwdFile)
        for i in range(len(passwdFile)):
            lineList=passwdFile[i].split(':')
            if lineList[0]==username:
                 break
        textlineList=lineList[4].split(',')
        try:
            startHours = datetime.strptime(textlineList[1], '%H%M')
            endHours = datetime.strptime(textlineList[2], '%H%M')
        except ValueError:
            print('The user has no working hours set.')
            # self.logRegistroError(' '.join(f"User{username}, has no working hours set."))
            return 1
        now=datetime.now('%H%M')
        if (now>startHours and now<endHours): 
            c.self.poutput(f"User {username} is in range of working hours.")
        else:
            c.self.logRegistroHorario(f"User {getpass.getuser()} loggins outside working hours from IP:{currentIP}")
            c.self.poutput(colors.WARNING+"This incident will be reported.")

if __name__== '__main__':
    import sys
    controlHorario('gato')
    sys.exit()