import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

byd = int(input("У тебя 1)выходной/отпуск или 2)работа? "))

if byd == 1:
    print("СПАТЬ/ГУЛЯТЬ")
elif byd == 2:
    print("ЧУВАК, РАБОТА ЖДЕТ!")
else:
    print("ERRRRRRRRROOOOOORRRR")
