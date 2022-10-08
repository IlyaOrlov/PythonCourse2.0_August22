def decorator(fun):
    def in_decorator(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res

    return in_decorator


@decorator
def my_example(x):
    return x * x


res = my_example(10) * 2
print(res)

