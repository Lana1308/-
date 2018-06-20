import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

datam = input("Введите месяц своего рождения: ")
datad = int(input("Введите день своего рождения: "))

if datam == "декабрь"and 22 <= datad <= 31:
    print("Capricon")
elif datam == "январь"and 1 <= datad <= 19:
    print("Capricon")
elif datam == "январь"and 20 <= datad <= 31:
    print("Aquarius")
elif datam == "февраль"and 1 <= datad <= 18:
    print("Aquarius")
elif datam == "февраль"and 19 <= datad <= 28:
    print("Pisces")
elif datam == "март"and 1 <= datad <= 20:
    print("Pisces")
elif datam == "март"and 21 <= datad <= 31:
    print("Aries")
elif datam == "апрель"and 1 <= datad <= 19:
    print("Aries")
elif datam == "апрель"and 20 <= datad <= 31:
    print("Taurus")
elif datam == "май"and 1 <= datad <= 20:
    print("Taurus")
elif datam == "май"and 21 <= datad <= 31:
    print("Gemini")
elif datam == "июнь"and 1 <= datad <= 20:
    print("Gemini")
elif datam == "июнь"and 21 <= datad <= 31:
    print("Cancer")
elif datam == "июль"and 1 <= datad <= 22:
    print("Cancer")
elif datam == "июль"and 23 <= datad <= 31:
    print("Leo")
elif datam == "август"and 1 <= datad <= 22:
    print("Leo")
elif datam == "август"and 23 <= datad <= 31:
    print("Virgo")
elif datam == "сентябрь"and 1 <= datad <= 22:
    print("Virgo")
elif datam == "сентябрь"and 23 <= datad <= 31:
    print("Libra")
elif datam == "октябрь"and 1 <= datad <= 22:
    print("Libra")
elif datam == "октябрь"and 23 <= datad <= 31:
    print("Scorpio")
elif datam == "ноябрь"and 1 <= datad <= 21:
    print("Scorpio")
elif datam == "ноябрь"and 22 <= datad <= 31:
    print("Sagittarius")
elif datam == "декабрь"and 1 <= datad <= 22:
    print("Sagittarius")
else:
    print("ОШИБКА")
