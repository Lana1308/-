import datetime
import random
from itertools import permutations

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

a = [1, 2, 5]
random.shuffle(a)
print(a)

b = list(permutations(a))
print(b)

c= [random.randint(1, 10) for i in range(8)]
print(c)

c = [random.choice([i for i in range(1000)]) for j in range(8)]
print(c)
