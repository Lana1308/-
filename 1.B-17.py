import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

while True:
    year = int(input("Введите год: "))

    if year % 4 != 0:
        print("Обычный год")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("Высокосный год")
        else:
            print("Обычный год")
    else:
        print("Высокосный год")
