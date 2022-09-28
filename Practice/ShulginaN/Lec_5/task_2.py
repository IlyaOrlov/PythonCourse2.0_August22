def fun(a):
    for i in range(len(a)):
        if a[i] in a[:i:]:
            print(a[i])
            break


lst = [2, 3, 4, 5, 3, 2]
fun(lst)
