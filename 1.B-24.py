import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

m = float(input("Введите частоту: "))


if 0 <= m < 3*10**9:
    print ("Radio waves")
elif 3.9*10**12 <= m <= 3*10**12:
    print ("Microwaves")
elif 3*10**12 < m <= 4.3*10**14:
    print ("Infrared light")
elif 4.3*10**14 < m <= 7.5*10**14:
    print ("Visible light")
elif 7.5*10**14 < m <= 3*10**17:
    print ("Ultraviolet light")
elif 3*10**17 < m <= 3*10**19:
    print ("X-rays")
elif 3*10**19 < m:
    print ("Gamma rays")
else:
    print ("ОШИБКА")
