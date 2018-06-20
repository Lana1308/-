import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

n = int(input("Введите четырезначное число: "))

d1 = n % 10
#нахождение целого при делении нацело
n = n // 10
#нахождение остатка при делении нацело
d2 = n % 10
n = n // 10
d3 = n % 10
n = n // 10
d4 = n % 10


print("Сумма цифр числа:", d1 + d2 + d3 + d4)
