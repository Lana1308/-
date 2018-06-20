import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

name = printTimeStamp("Lana")

while True:
    gol = input("Напиши англ літеру: ")

    if gol == "a":
        print("Голосна  літера")
    elif gol == "e":
        print("Голосна  літера")
    elif gol == "i":
        print("Голосна  літера")
    elif gol == "o":
        print("Голосна  літера")
    elif gol == "u":
        print("Голосна  літера")
    elif gol == "y":
        print("Голосна  літера, але інколи - приголосна")
    
    else:
        print("Приголосна")
