import datetime
from collections import Counter

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")


a = [1, 4, 6, 5, 8, 1, 8, 6, 1, 56, 7, 5, 5, 5, 1, 1, 5, 1, 5, 8, 8, 8, 8]
d = {}


for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
#Если очередной элемент списка уже есть в качестве ключа словаря, то следует увеличить значение этого ключа на единицу.
# Если очередного элемента списка нет в качестве ключа в словаре, то такой ключ следует добавить и присвоить ему значение, равное единице.

for i in d:
    print("'%d':%d" % (i, d[i]))

print(C(d))
