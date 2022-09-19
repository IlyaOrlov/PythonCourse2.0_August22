def decorator1(func):
    def equality(*args, **kwargs):
        print("===========")
        res = func(*args, **kwargs)
        print("===========")
        return res
    return equality


@decorator1
def func():
    print("Привет")

func()


