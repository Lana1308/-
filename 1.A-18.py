import datetime
from math import sqrt

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

d = int(input("Какая длина высотки(в метрах)? "))
if d < 0:
    print ("ОШИБКА")
else:
    vi = 0
    a = 9.8
    vf = sqrt(vi**2 + 2 * a * d)
    print(vf)
