import utilities
paths = ["/etc/shadow","/etc/passwd","/etc/group"]
files = []
for path in paths:
    files.append(utilities.readFile(path))
str=''
str=files.join()
print(str)