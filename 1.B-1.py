import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

p = int(input("Введите тиск: "))
v = int(input("Введите об'єм: "))
t = int(input("Введите температуру: "))

n = (p * (v / 1000)) / (8.314 * (t + 273.15))

print("Молярна маса газу: ", n)
