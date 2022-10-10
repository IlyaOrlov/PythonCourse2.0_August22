def superfun(fun, *args):
    lst = []
    for i in args:
        lst.append(fun(i))
    return lst

def square(x):
    return x * x


lst = [1, 2, 3, 5]
lst_new = superfun(square, *lst)# *lst распакует список
##lst_new = superfun(lambds x: x * x, *lst)
print(lst_new)