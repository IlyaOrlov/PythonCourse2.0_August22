def superfun(fun, *args): # (1, 2, 3, 5)
    lst = []
    for i in args:
        lst.append(fun(i))
    return lst


def square(x):
    return x * x


lst = [1, 2, 3, 5]
lst_new = superfun(lambda x: x * x, *lst)
print(lst_new)
lst_new = superfun(lambda x: x * 2, *lst)
print(lst_new)
