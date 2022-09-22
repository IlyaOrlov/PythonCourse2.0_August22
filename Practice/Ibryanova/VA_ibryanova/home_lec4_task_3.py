num = ""

while True:
    a = input("Введите число: ")
    if a.lower() == "stop":
        break
    if not a.isdecimal():
        print("Нужно ввести число: ")
    else:
        num += str(n)

print(f"Ваше число: {num}")