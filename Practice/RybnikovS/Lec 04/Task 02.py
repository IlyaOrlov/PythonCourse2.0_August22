while not ((x := input("Введите пятизначное число: ")).isdecimal() and len(x) == 5):
    print("Ввод некорректный")
else:
    print(f"Число: {x}")
    for index, symbol in enumerate(x):
        print(f"{index+1} цифра равна {symbol}")
