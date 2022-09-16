def max_item(a, b):
    print(max(a, b))


def max_ret(a, b):
    return max(a, b)


high = int(input('Введите первое число: '))
low = int(input('Введите второе число: '))
max_item(high, low)
b = max_ret(high, low)
print(b)