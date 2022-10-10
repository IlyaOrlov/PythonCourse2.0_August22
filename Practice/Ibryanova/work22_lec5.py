import time


def superfun(fun):
    def inner_fun(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        stop = time.time()
        print(f'Execution time: {stop - start}')
        return res

    return inner_fun

@superfun
def mysum(x, y):
    return x + y

@superfun
def mymul(x, y):
    return x * y

@superfun
def supermul(x, y, z):
    return x * y * z



old_mysum = mysum
mysum = superfun(mysum)

mysum = superfun(mysum)
mymul = superfun(mymul)
supermul = superfun(supermul)



supermul(10, 20, 30)

print(mysum(100, 500))
print(mymul(10, 20))
p = mymul(2, mysum(30, 40))
print(p)
print(supermul)

print('===================')
mysum = old_mysum
print(mysum(1000, 2000))