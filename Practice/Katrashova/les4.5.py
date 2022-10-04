a = input("Введите начало диапазона: ")
b = input("Введите конец диапазона: ")
print("Число загадано в указанном диапазоне")
c = random.randint(a, b)


while True:
    x = input("Попробуй отгадать моё число ")
    if not x.isdecimal():
        break
    x = int(x)
    if x < c:
        print("Введённое число меньше загаданного.")
    elif x > c:
        print("Введённое число больше загаданного.")
    else:
        print("Поздравляю, Вы угадали!")


