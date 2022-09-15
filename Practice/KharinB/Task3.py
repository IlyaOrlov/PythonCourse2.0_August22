res = ""
while True:
    x = input("Введите число: ")
    if x.lower() == "stop":
        break
    elif x.isdecimal():
        res += x
    else:
        print("Введено не число!")
print("Введено: ", res)
