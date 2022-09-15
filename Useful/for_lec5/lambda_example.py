def super_code(x, y, make_choice):
    z = make_choice(x, y)
    print(z)


def find_max(a, b):
    return a if a > b else b


x = int(input("Input x: "))
y = int(input("Input y: "))
super_code(x, y, lambda a, b: a if a > b else b)
super_code(x, y, lambda a, b: a if a < b else b)



