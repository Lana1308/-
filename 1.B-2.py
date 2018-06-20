import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

m = float(input("Введите магнитуду: "))

if 0 <= m < 2.0:
    print ("Мікро (micro)")
elif m < 0:
    print ("ejsvdd")
elif 2.0 <= m <= 3.0:
    print ("Дуже слабкий (very minor)")
elif 3.0 < m <= 4.0:
    print ("Слабкий (minor)")
elif 4.0 < m <= 5.0:
    print ("Легкий (light)")
elif 5.0 < m <= 6.0:
    print ("Помірний (moderate)")
elif 6.0 < m <= 7.0:
    print ("Сильний (strong)")
elif 7.0 < m <= 8.0:
    print ("Дуже сильний (major)")
elif 8.0 < m < 10.0:
    print ("Дуже сильний (major)")
else:
    print ("Рідкісно великий (meteoric)")

print("Опис: ", m)
