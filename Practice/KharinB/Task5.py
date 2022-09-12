import random

flag = True
while flag:
    range_min = input("Введите минимальное число: ")
    while range_min.isdecimal():
        range_max = input("Введите максимальное число: ")
        if range_max.isdecimal():
            if range_max > range_min:
                range_min = int(range_min)
                range_max = int(range_max)
                flag = False
                break
            elif range_max < range_min:
                qv = input("Минимальное число больше максимального, хотите поменять их местами и продолжить?(да)")
                if qv.lower() == "да":
                    range_min, range_max = int(range_max), int(range_min)
                    flag = False
                    break
                else:
                    continue
        else:
            print("Введено не число, повторите ввод")

    else:
        print("Введено не число, повторите ввод")
print("А теперь сыграем!!!")
num = random.randint(range_min, range_max)
while True:
    answer = input("Угадайте число которое загадал компьютер: ")
    if answer.isdecimal():
        answer = int(answer)
        if answer == num:
            print("Вы угадали!!!")
            break
        elif range_max > answer > num:
            print("Почти, но загаданное число меньше")
        elif num > answer > range_min:
            print("Почти, но загаданное число больше")
        elif answer > range_max or answer < range_min:
            print(f"Вы загадали диапазон от {range_min} до {range_max}, держите себя в руках и не выходите за рамки.")
    else:
        print("Это вообще не число...")
