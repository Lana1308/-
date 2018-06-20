import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

timed = int(input("Напишите количество дней: "))
timeg = int(input("Напишите количество часов: "))
timeh = int(input("Напишите количество минут: "))
times = int(input("Напишите количество секунд: "))

sek = timed*24*60*60 + timeg*60*60 + timeh*60 + times

print("Общее количество секунд: ", sek)
