def decorator(fun):
    def inner_fun(*args, **kwargs):
        res = fun(*args, **kwargs)
        print('==============')
        return res

    return inner_fun


@decorator
def square(x, y):
    return x * y

s = square(5, 3)
print(f'площадь прямоугольника равна: {s}')
print('==============')