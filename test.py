import os
from string import digits
# direccion='var/log/comandosDiarios.log'
# if os.path.exists('var/log')==False:
#     print("Directory doesn't exist.")
import datetime
from mutilities import verifyTime
# cwd=os.getcwd()
# path=os.path.join(cwd,'var','log')
# print(path)

# f = open("test.txt", "a")
# f.write("Now the file has more content!\n")
# f.close()

# #open and read the file after the appending:
# f = open("test.txt", "r")
# print(f.read())}


print(verifyTime())

# flag=True
# while flag==True:
#     hentrada=input('Debe ingresar el horario de entrada en formato H:M: ')
#     hsalida=input('Debe ingresar el horario de salida en formato H:M: ')
#     tlen=len(hsalida)+len(hentrada)
#     if hentrada and hsalida == f'{control}{control}:{control}{control}':
#         flag=False