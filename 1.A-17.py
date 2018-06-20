import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

rah = int(input("Введите сумму денег: "))

rah1 = rah + (rah*0.14)
rah2 = rah1 + (rah1*0.14)
rah3 = rah2 + (rah2*0.14)

print("Сумма на счету через 1 год: ", f"{rah1:.2f}")
print("Сумма на счету через 2 года: ", f"{rah2:.2f}")
print("Сумма на счету через 3 года: ", f"{rah3:.2f}")
