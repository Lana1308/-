import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

a = int(input("Довжина 1 сторони: "))
b = int(input("Довжина 2 сторони: "))
c = int(input("Довжина 3 сторони: "))

if a == b == c:
    print("Рівносторонній")
elif a == b or b == c or a == c:
    print("Рівнобедрений")
elif a < 0 or b < 0 or c < 0:
    print("ОШИБКА")
else:
    print("Нерівносторонній")
