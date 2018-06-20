import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

while True:
    numbercon = int(input("Скільки контейнерів?"))
    container = int(input("Який об'єм контейнера?"))

    if container <= 1:
        d = 0.10
    else:
        d = 0.25
    
    doplatasum = numbercon * container * d
   

    print( "Доплата составляет: ", f"{doplatasum:.2f}", "$")
