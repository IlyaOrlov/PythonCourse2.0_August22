def fun(a):
    new_set = set()
    for i in lst:
        if i in new_set:
            print(f"Первый повторившийся элемент: {i}")
            break
        else:
            new_set.add(i)


lst = [2, 3, 4, 5, 3, 2]
fun(lst)
