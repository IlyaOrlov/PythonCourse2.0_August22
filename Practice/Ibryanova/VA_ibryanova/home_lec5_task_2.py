def fun(lst):
    for i in range(len(lst)):
        if lst[i] in lst[:i:]:
            return lst[i]

lst = [2, 3, 4, 5, 3, 2]
print(fun(lst))