 s = ""
while True:
    x = input("Введите символ: ")
    if x.upper() == "STOP":
        print("Программа завершена")
        break
    elif not x.isdecimal():
        print("Некорректный ввод")
    else:
        s += x
        print(f"Ваше число {s}")
