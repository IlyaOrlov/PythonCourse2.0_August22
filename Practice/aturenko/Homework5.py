# 6.Написать и вызвать две функции, принимающие два числа.
# Первая функция должна вывести на экран большее из двух введённых чисел.
# Другая должна вернуть большее из двух введённых чисел по месту вызова.

def max1_num(a,b):
    if a > b:
        print(f"Большее из двух введёных чисел: {a}")
    else:
        print(f"Большее из двух введёных чисел: {b}")


x = int(input("Введите число: "))
y = int(input("Введите число: "))
max1_num(x, y)



def max2_num(c,d):
    return c if c > d else d


x2 = int(input("Введите число: "))
y2 = int(input("Введите число: "))
res = max2_num(x2, y2)
print(f"Большее из двух введёных чисел: {res}")
