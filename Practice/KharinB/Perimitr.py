while True:
    a = input("Введите первую сторону прямоугольника")
    b = input("Введите вторую сторону прямоугольника")
    try:
        a = int(a)
        b = int(b)
        break
    except:
        print("Введены некоректные данные.")
print(f"Площадь прямоугольника равна:{a * b}")
