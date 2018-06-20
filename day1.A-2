import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

p = int(input("Вывести ИМТ в (кг и см)-1 или (футах и дюймах)-2: "))

if p == 1:
    weight1 = int(input("Введите свой вес в кг: "))
    height1 = int(input("Введите свой рост в см: "))
    if weight1 < 0 or height1 < 0:
        print ("ERROR")
    else:
        IMT1 = weight1 / ((height1/100)**2)
        print("Ваш ИМТ в кг и см: ", IMT1)
else:
    weight2 = int(input("Введите свой вес в футах: "))
    height2 = int(input("Введите свой рост в дюймах: "))
    if weight2 < 0 or height2 < 0:
        print ("ERROR")
    else:
        IMT2 = 703 * weight2 /(height2**2)
        print("Ваш ИМТ в футах и дюймах: ", IMT2)
