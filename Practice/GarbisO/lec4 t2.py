while not (s := input("Введите пятизначное число: ")).isdecimal ():
    print("Вы ввели не число. Введите пятизначное число")
else:
    print(s)
    for i in range(len(s)):
        print(f"{i + 1} цифра равна {s[i]}")