import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

a = int(input("Введите число: "))

if 106 < a < 130:
    print("Между шумами Jackhammer и Gas lawnmower")
elif a == 130:
    print("Jackhammer")
elif a == 106:
    print("Gas lawnmower")
elif 70 < a < 106:
    print("Между шумами Alarm clock и Gas lawnmower")
elif a == 70:
    print("Alarm clock")
elif 40 < a < 70:
    print("Между шумами Quiet room и Gas lawnmower")
elif a == 40:
    print("Quiet room")
else:
    print("Значение ниже за самый тихий шум или значение выше за самый громкий шум")
