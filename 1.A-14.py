import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

m = str(input("Введите название месяца: "))


if m == "январь":
    print ("31 день")
elif m == "февраль":
    print ("28 или 29 дней")
elif m == "март":
    print("31 день")
elif m == "апрель":
    print ("30 дней")
elif m == "май":
    print ("31 день")
elif m == "июнь":
    print("30 дней")
elif m == "июль":
    print ("31 день")
elif m == "август":
    print ("31 день")
elif m == "сентябрь":
    print("30 дней")
elif m == "октябрь":
    print ("31 день")
elif m == "ноябрь":
    print("30 дней")
elif m == "декабрь":
    print ("31 день")
else:
    print("Ошибка")
