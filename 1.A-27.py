import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

govor = input("Папугай что-то говорит? (да/нет) ")
time = float(input("Сколько сейчас времени? "))

if govor == "да" and 22.00 <= time <= 24.00 or 00.00 <= time <= 8.00:
    print("Накройте попугая")
elif govor == "нет":
    print("Это хорошо")
elif 8.00 < time <22.00:
    print("ПАПУГА РУЛИТ. ОРИ ВО ВСЕ ГОРЛО")
else:
    print("Ошибка")
