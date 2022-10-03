# напишем ф=ю которая выводит на экран большее и меньшее из чисел введеных польз-лем
def super_code(x, y, make_choice):
    z = make_choice(x, y)
    print(z)


def find_max(a, b):
    return a if a > b else b


x =int(input("input x: "))
y =int(input("input y: "))
super_code(x, y, lambda a, b: a if a > b else b)
super_code(x, y, lambda a, b: a if a < b else b)