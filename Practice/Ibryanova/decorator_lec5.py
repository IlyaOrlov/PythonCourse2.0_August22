import time


def decorator(fun):
    def inner_fun(*args, **kwargs):
        # новый код до основной фун-и
        print('hello')
        res = fun(*args, **kwargs)
        # новый код после основной фун-и
        print('bue')
        return res

    return inner_fun

def time_dec(fun):
    def inner_fun(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        stop = time.time()
        print(f'Execution time: {stop - start}')
        return res

    return inner_fun

@time_dec
@decorator
def mysum(x, y):
    return x + y

#old_mysum = mysum= вместо этой стр можно прописать decorator
#mysum = decorator(mysum)
print(mysum(100, 500))
#mysum = old_mysum = вместо этой стр можно прописать decorator

print(mysum(1000, 5000))

# также декоратор можно прописать ввиду стр
#mysum = time_dec(decorator(mysum))