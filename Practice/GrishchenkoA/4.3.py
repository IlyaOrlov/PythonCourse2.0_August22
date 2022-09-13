symbol = input("Введите числовой символ: ")
numbers=""
while symbol.lower() != "stop":
    if symbol.isdecimal():
        numbers += symbol
        symbol = input("Введите числовой символ: ")
    else:
        print("Введен нечисловой символ")
        symbol = input("Введите числовой символ: ")
else:
    print(f"Сформированное число: {int(numbers)}")





