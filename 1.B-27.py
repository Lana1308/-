import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

for i in range(1,11):
    for j in range(1,11):
        print("%4d" % (i*j), end='')
    print()
