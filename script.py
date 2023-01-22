import time
f=open('helloEveryone.txt','a+')
while True:
    f.write("Hello, World!")
    time.sleep(10)