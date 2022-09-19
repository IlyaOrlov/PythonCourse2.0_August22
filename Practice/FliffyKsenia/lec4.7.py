def decorator(fun):
    def funs(*agrs, **kwargs):
        print("======================: ")
        res = fun(*agrs, **kwargs)
        print("======================: ")
        return res
    return funs

@decorator
def summ(x, y):
    print("ya krevedko")
    return x+y

print(summ(7, 9))
