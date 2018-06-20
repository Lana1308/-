import datetime
from time import asctime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

print ("Поточний час та дата: ", asctime())
