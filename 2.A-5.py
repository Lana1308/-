import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

slov = {2: 54, 5: 34, 3: 23, 4: 17}

print(sorted(slov.values(), reverse = True))
print(sorted(slov.values(), reverse = False))
