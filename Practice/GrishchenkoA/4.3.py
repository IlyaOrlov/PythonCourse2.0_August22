numbers=""
while (symbol := input("Введите числовой символ: ")).lower() != "stop":
    if symbol.isdecimal():
        numbers += symbol
    else:
        print("Введен нечисловой символ")
else:
    print(f"Сформированное число: {int(numbers)}")





