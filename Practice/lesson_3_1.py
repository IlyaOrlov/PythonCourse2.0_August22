def rectangle(x,y):
    return ((x + y) * 2)


x = float(input('Введите длину прямоугольника в мм  - x: '))
y = float(input('Введите высоту прямоугольниеп в мм - y:'))
result = rectangle(x, y)
print(f'Периметр прямоугольника: {result}')