# 1.Расположить инструкции программы для вычисления площади круга в правильном порядке:
# result = square(int(radius))
#
# print(f"Площадь круга: {result}")
#
# def square(r):
#
#     return math.pi * r ** 2
#
# radius = input("Введите радиус: ")
#
# import math
import math
radius = input("Введите радиус: ")
def square(r):
    return math.pi * r ** 2
result = square(int(radius))
print(f"Площадь круга: {result}")

# 2.Следующая программа для вычисления среднего расхода бензина содержит различные ошибки. Необходимо их найти и исправить.
# start = input("Топлива было: "); end = input("Топлива осталось: ")
#
# distance = input("Расстояние: ")
#
# diff = int(start) - int(end)
#
# result = diff / distance
#
# print
start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = diff / int(distance)
print(f"Средний расход бензина составляет {result} л/км2")

