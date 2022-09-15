def my_dec(fun):
    def inner_fun(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res

    return inner_fun


@my_dec
def my_fun(x, y):
    return x + y


print(my_fun(3, 5))
