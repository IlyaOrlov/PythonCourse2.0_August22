while True:
    n = input("Введите число: ")
    if not n.isdigit():
        print("Ошибка введите ещё раз")
    else:
        break
for i in range(len(n)):
    print(f"{i+1} число равно {n[i]}")