s= ""
while True:
    i = input("Введите число: ")
    if i.lower() == "stop":
        break
    elif not i.isdecimal():
        print("Введите только числовые символы")
    else:
        s += str(i)
print(f"Ваше число: {s}")