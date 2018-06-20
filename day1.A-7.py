import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

temp = int(input("Введите температуру в Цельсия: "))
tempf = temp*1.8 + 32
tempk = temp + 273.15
print("Температура в Кельвина: ", tempk)
print("Температура в Фаренгейта: ", tempf)
