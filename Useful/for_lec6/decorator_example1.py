import time
import decorator_example

def decorator(fun):
    def inner_fun(*args, **kwargs):
        print("Hello")
        res = fun(*args, **kwargs)
        print("Bye")
        return res

    return inner_fun

@decorator_example.superfun
@decorator
def mysum(x, y):
    return x + y



mysum = decorator_example.superfun(decorator(mysum))
print(mysum(100, 500))
print(mysum(1000, 5000))


