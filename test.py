from utilities import joinList
from utilities import turnElementTostr
ipadresses=[123,456,789]
ipadresses=turnElementTostr(ipadresses)
print(ipadresses)
ipadresses=joinList(ipadresses,',')
horario=['hentrada','hsalida']
horario=joinList(horario,',')
GECOS = ['fullname','workphone','homephone',horario]
GECOS=joinList(GECOS,',')
print(GECOS)
