import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

b = []
while True:
    a = input("Введите число: ")
    if a == "0": break
    b.append(a)
print(sorted(b))
