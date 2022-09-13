import random

n = int(input("Введи диапозон от 0 до: "))
number = random.randint(0, n)

while True:
    answer = input('Угадай число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdecimal():
        print("Введи правильное число")
        continue

    if int(answer) == number:
        print('Верно!')
        break
    elif int(answer) > number:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')