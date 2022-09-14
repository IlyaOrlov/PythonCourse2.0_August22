import random


a = int(input("Введите начальное число диапазона: "))
b = int(input("Введите конечное число диапазона: "))
number = random.randint(a, b)

while True:
    c = input("Угадай число, которое я загадал: ")
    if not c.isdecimal():
        print("Вы ввели не число!")
        break
    elif int(c) > number:
        print("Нет, число меньше загаданного")
    elif int(c) < number:
        print("Нет, число больше загаданного")
    else:
        print("Угадал!")
        break
