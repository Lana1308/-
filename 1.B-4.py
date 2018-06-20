import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

minut = int(input("Количество минут за месяц: "))
text = int(input("Количество смс за месяц: "))


if 0 <= minut <= 200 and 0 <= text <= 50:
    tarif = 15
    fond = 0.44
    podatok = tarif * 0.05
    rah = tarif + fond + podatok
    
elif minut > 200 and text > 50:
    tarif = (((minut - 200) * 0.17) + ((text - 50) * 0.15)) + 15
    fond = 0.44
    podatok = tarif * 0.05
    rah = tarif + fond + podatok

elif minut > 200 and 0 <= text <= 50:
    tarif = ((minut - 200) * 0.17) + 15
    fond = 0.44
    podatok = tarif * 0.05
    rah = tarif + fond + podatok

elif 0 <= minut <= 200 and text > 50:
    tarif = ((text - 50) * 0.15) + 15
    fond = 0.44
    podatok = tarif * 0.05
    rah = tarif + fond + podatok
    
else:
    print("ERROR")



print ("Базова плата за користування(без внесків та податків): ", f"{tarif:.2f}")
print("Загальний рахунок: ", f"{rah:.2f}")
