import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

hleb = int(input("Кількість буханок вчорашнього хліба, які бажає придбати покупець? "))

money = 8.50
zn = 0.6

vart = hleb * money
vartzn = vart * zn

print("Звичайна вартість товару: ", "{:.2f}".format(vart))
print("Загальна сума покупки(з урахуванням знижки): ", "{:.2f}".format(vartzn))
