import datetime
from math import pi

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

r = float(input("Введите радиус: "))

s = pi*(r**2)
v = (4/3)*pi*(r**3)

print("Площа круга: ", s)
print("Об'єм кулі: ", v)
