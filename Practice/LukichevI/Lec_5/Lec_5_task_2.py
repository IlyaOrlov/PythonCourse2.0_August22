def fun():
    for i in range(len(lst1) - 1):
        if (lst1[i] in lst2) == False:
            lst2.append(lst1[i])
        else:
            print(f'Первый повторившийся символ: {lst1[i]} ')


lst1 = [2, 3, 4, 5, 3, 2]
lst2 = []
fun()