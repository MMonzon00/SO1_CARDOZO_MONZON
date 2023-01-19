import os

direccion='var/log/comandosDiarios.log'
if os.path.exists('var/log')==False:
    print("Directory doesn't exist.")

cwd=os.getcwd()
path=os.path.join(cwd,'var','log')
print(path)
