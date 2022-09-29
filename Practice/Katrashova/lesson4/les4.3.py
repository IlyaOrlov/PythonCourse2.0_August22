n = ""
while True:
    i = input("Введите символ: ")
    if i.lower() == "stop":
        break
    elif not i.isdecimal():
        print("Вы ввели не число")
    else:
        n += str(i)
print(f"Вы ввели число: {n}")