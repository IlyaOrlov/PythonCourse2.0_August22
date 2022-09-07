import math
radius = input("Введите радиус: ")
def square(r):
    return math.pi * r ** 2
result = square(int(radius))
print(f"Площадь круга: {result}")