def choose_max(a, b):
    if a > b:
        max_1 = a
    else:
        max_1 = b
    print(f"Большее число из введенных: {max_1}")


def finds_max(a, b):
    if a > b:
        max_2 = a
    else:
        max_2 = b
    return max_2


a, b = map(int, input("Введите два числа: ").split())
choose_max(a, b)
finds_max(a, b)