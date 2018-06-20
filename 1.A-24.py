import datetime
from math import pi, tan

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

s = float(input("Довжина сторони (c точкой): "))
n = int(input("Кількість сторін: "))
plo = (n*(s**2))/4*tan(pi/n)
print("Площа сконструйованого за даними значеннями полігону: ", plo)
