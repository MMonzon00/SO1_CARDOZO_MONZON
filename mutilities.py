from datetime import date
import datetime
import os

def checkpath(path):
    return os.path.exists(path)
def readFile(filePATH,separator):
        f = open(filePATH ,'r')
        fileList = f.readlines()
        resultMatrix=[]
        for i in range(len(fileList)):
            matrix=fileList[i].split(separator)
            resultMatrix.append(matrix)
        f.close()   
        return resultMatrix

def getUID():
    filePATH='/etc/passwd'
    separator=':'
    resultMatrix=readFile(filePATH,separator)
    UID_list = []
    GID_list = []
    for i in range(len(resultMatrix)):
        UID_list.append(resultMatrix[i][2])
        GID_list.append(resultMatrix[i][3])
    UID_list = list(map(int, UID_list))
    GID_list = list(map(int, GID_list))
    UID=max(UID_list)+1
    return UID

def getGID():
    filePATH='/etc/passwd'
    separator=':'
    resultMatrix=readFile(filePATH,separator)
    UID_list = []
    GID_list = []
    for i in range(len(resultMatrix)):
        UID_list.append(resultMatrix[i][2])
        GID_list.append(resultMatrix[i][3])
    UID_list = list(map(int, UID_list))
    GID_list = list(map(int, GID_list))
    GID=max(GID_list)+1
    return GID

def days_since():
    dateThen=date(1970,1,1) #Format: year, month, date.
    dateNow=date.today()
    days_since=dateNow - dateThen
    return days_since.days


def checkip(ip):
    ipFormat=0
    return True

def readFileLines(filename):
    with open(filename) as file:
        lines = file.readlines() 
        lines = [line.rstrip() for line in lines]
    return lines

def rmquotes(byteline):
    byteline = str(byteline).replace('b','').replace("'",'')
    return byteline

def processText(text):
    processedText = list(text)
    for i in range(len(processedText)):
        processedText[i] = processedText[i].split(':')
    return processedText

def parseFile(files,paths):
    for path in paths:
        files.append(readFileLines(path))
    for path in range(len(paths)):
        files[path] = processText(files[path])
    return files
    
def turnElementTostr(list):
    for element in range(len(list)):
        list[element]=(str(list[element]))
    return list

def writePass(path,file):
    fileo=open(path, 'w')
    for i in range(len(file)):
        lineparsed=joinList(file[i],':')
        fileo.write(f'{lineparsed}\n')

def joinList(list,separator):
    str=separator.join(list)
    return str

if __name__== '__main__':
    print(days_since())