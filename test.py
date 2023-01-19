import os

# direccion='var/log/comandosDiarios.log'
# if os.path.exists('var/log')==False:
#     print("Directory doesn't exist.")

# cwd=os.getcwd()
# path=os.path.join(cwd,'var','log')
# print(path)

f = open("test.txt", "a")
f.write("Now the file has more content!\n")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())