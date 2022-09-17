import random


a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print(f"Диапазон от {a} до {b}")
c = random.randint(a, b)


while True:
    d = input("Введите целое число из указанного диапазона: ")
    if d.isdecimal():
        d = int(d)
        if d == c:
            print(f"Поздравляем! Вы угадали: {c}")
            break
        elif d < c:
            print("Введите число меньше ")
        elif d > c:
            print("Введите число больше ")
    else:
        print("Введите число")