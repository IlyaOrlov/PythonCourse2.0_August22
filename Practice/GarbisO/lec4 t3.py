while not(x := input("Введите числовой символ: ")).isnumeric():
    print("Вы ввели не числовой символ. Введите числовой символ")
    if x == "STOP" or "Stop" or "stop":
        break
else:
    x = int(x)
    print(f"Ваше число: {x}")

