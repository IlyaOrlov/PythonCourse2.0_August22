import random

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Число загадано в указанном диапазоне")
c = random.randint(a, b)


while True:
    x = input("Попробуй отгадать моё число ")
    if not x.isdecimal():
        print("Введено не число")
        continue
    x = int(x)
    if x < c:
        print("Введённое число меньше загаданного.")
    elif x > c:
        print("Введённое число больше загаданного.")
    else:
        print("Поздравляю, Вы угадали!")
        break


