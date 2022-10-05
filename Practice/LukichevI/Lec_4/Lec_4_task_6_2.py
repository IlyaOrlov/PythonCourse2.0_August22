def myfun(x, y):
    if x > y:
        return x
    else:
        return y


a = int(input('Введите число: '))
b = int(input('Введите число: '))
result = myfun(a, b)
print(result)