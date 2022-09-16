def my_dec(fun):
    def inner_fun(*args, **kwargs):
        print("===========")
        print(fun(*args, **kwargs))
        print("===========")
        return None

    return inner_fun


@my_dec
def my_fun(x, y):
    return x + y


my_fun(3, 5)
