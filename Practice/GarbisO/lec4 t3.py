while not(x := input("Введите числовой символ: ")).isnumeric():
    if x.lower() == "stop":
        print("The end!")
        break
    print("Вы ввели не числовой символ. Введите числовой символ")
else:
    x = int(x)
    print(f"Ваше число: {x}")

