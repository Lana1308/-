import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

moneyFood = int(input("Введите сумму заказанной в ресторане еды: "))

tea = moneyFood * 0.14
nalog = moneyFood * 0.18

print("Cумма заказа: ", moneyFood + tea + nalog)
print("Размер налога: ", f"{nalog:.2f}")
print("Размер чаевых: ", f"{tea:.2f}")
