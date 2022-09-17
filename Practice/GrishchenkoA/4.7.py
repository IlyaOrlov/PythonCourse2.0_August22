def decorator1(func):
    def equality(*args, **kwargs):
        print("===========")
        func(*args, **kwargs)
        print("===========")
        return func
    return equality()


def func1():
    print("Привет")


decorator1(func1)
