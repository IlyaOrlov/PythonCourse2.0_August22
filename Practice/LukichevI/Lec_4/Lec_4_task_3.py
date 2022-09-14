count = ""
while True:
    a = input("Введите число: ")
    if a == "stop" or a == "Stop" or a == "STOP":
        break
    elif not a.isdecimal():
        print("Не корректный ввод")
        continue
    else:
        count += str(a)
print(f"Ваше число: {count}")