import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

x = "X"

print("       ", x*3)
print("    ", x*9)
print("  ", x*13)
print(" ", x*15)
print("", x*17)
print("", x*17)
print(" ", x*15)
print("  ", x*13)
print("    ", x*9)
print("       ", x*3)
