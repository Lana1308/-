import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

a = int(input("Введите тиск у кПА: "))

a1 = a * 0.14503773773022
a2 = a * 7.5006375541921
a3 = a * 0.0098692326671601

print("тиск у фунтах на квадратний дюйм: ", a1)
print("тиск у міліметрах ртутного стовчика: ", a2)
print("тиск у атмосферах: ", a3)
