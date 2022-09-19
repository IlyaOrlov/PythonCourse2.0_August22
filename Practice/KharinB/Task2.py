while not (x := input("Введите число:")).isdecimal:
    print("Введено не число!")
else:
    print(x)
    for i in range(len(x)):
        print(f"{i + 1} цифра равна {x[i]}")
