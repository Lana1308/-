import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

dob = int(input("Введите длину поля в метрах: "))
shur = int(input("Введите ширину поля в метрах: "))

s = dob * shur
sa = s * 0.01
sg = s * 0.0001

print("Площа в арах: ", sa)
print("Площа в гектарах: ", sg)
