import math #добавил 2 пустых строки


def square(r):
    return math.pi * r ** 2


radius = input("Введите радиус: ")
result = square(int(radius))
print(f"Площадь круга: {result}")
