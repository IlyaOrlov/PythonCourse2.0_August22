def fun(a, b):
    for i in range(len(a)):
        if a[i] in b:
            print(f'Первый повторившийся символ: {a[i]} ')
            break
        else:
            b.add(a[i])


lst1 = [2, 3, 4, 5, 3, 2]
lst2 = set()
fun(lst1, lst2)