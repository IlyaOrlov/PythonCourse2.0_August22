count = ""
while True:
    a = input("Введите число: ")
    if a.lower() == "stop":
        break
    elif not a.isdecimal():
        print("Не корректный ввод")
    else:
        count += str(a)
print(f"Ваше число: {count}")