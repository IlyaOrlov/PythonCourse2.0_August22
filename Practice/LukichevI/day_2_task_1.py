# 1.Расположить инструкции программы для вычисления площади круга в правильном порядке:
import math


def square(r):


    return math.pi * r ** 2
radius = input("Введите радиус: ")
result = square(int(radius))
print(f"Площадь круга: {result}")




