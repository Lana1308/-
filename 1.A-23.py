import datetime
from math import log10


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))

z1 = a+b
z2 = b-a
z3 = a*b
z4 = a/b
z5 = a%b
z6 = log10(a)
z7 = a**b

print("Сума а і b: ", z1)
print("Різниця, коли від b віднімається a: ", z2)
print("Добуток a на b: ", z3)
print("Частка від ділення a на b: ", z4)
print("Остача від ділення a на b: ", z5)
print("Значення log10(a): ", z6)
print("Значення a**b: ", z7)
