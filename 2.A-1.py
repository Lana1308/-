import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

a = [1, 4, 7, 1, 4, 5, 6, 10]
b = set(a)
print(b)

c = list(b)

del c[0]
del c[1]
del c[1]
print(c)
