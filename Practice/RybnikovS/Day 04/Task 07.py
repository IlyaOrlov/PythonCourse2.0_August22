def wrap_output(func):

    def inside(a):
        print("===========")
        func(a)
        print("===========")

    return inside


def plus_three(argument):
    print(argument + 3)


@wrap_output
#  Первый способ декорирования функции
def plus_two(argument):
    print(argument + 2)
plus_two(5)


#  Второй способ декорирования функции
plus_three = wrap_output(plus_three)
plus_three(7)
