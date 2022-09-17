import random


a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
c = random.randint(a, b)


while True:
    d = input(f"Определите загаданное число из диапазона: {a, b} ")
    if not d.isdecimal():
        print(f"Введите число ")
        continue
    d = int(d)
    if c < d:
        print("Введите число поменьше ")
    elif c > d:
        print("Введите число побольше ")
    else:
        print("Верно!")
        break
