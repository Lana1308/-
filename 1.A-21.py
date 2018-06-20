import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

n = int(input("Введите число: "))

if n < 0:
    print("Ошибка")
else:
    suma = (n * (n + 1))/2
    print("Сумма всех целых чисел от 1 до n: ", int(suma))
