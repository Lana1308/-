import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

house = input("Человечек, где ты живешь? (будинок/квартира/гуртожиток) ")
time = int(input("Человечек, сколько ты проводишь времени дома? "))

if house == "будинок" and time >= 18:
    print ("В’єтнамське порося")
elif house == "будинок" and 10 <= time <= 18:
    print ("Собака")
elif house == "будинок" and time < 10:
    print ("Змія")
elif house == "квартира" and time >= 10:
    print ("Кішка")
elif house == "квартира" and time < 10:
    print ("Хом’як")
elif house == "гуртожиток" and time >= 6:
    print ("Рибки")
elif house == "гуртожиток" and time < 6:
    print ("Мурашник")
elif house == "будинок" and time < 0:
    print ("ОШИБКА")
elif house == "квартира" and time < 0:
    print ("ОШИБКА")
else:
    print ("ОШИБКА")
