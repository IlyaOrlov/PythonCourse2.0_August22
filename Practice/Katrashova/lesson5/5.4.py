def search(ls, a):
    ind = set()
    for i in range(len(ls)):
        for m in range(len(ls[i])):
            if a == ls[i][m]:
                ind.add(m)
    ind = list(ind)
    return ind


def delete(my_lst, lst_to_remove):
    for i in range(len(my_lst)):
        for n in reversed(lst_to_remove):
            del my_lst[i][n]
    return my_lst


lst = [
    [1, 2, 3, 4, 5, 6, 7],
    [1, 1, 1, 2, 3, 4, 4],
    [2, 2, 1, 3, 3, 5, 6]
]

d = int(input("Ведите цифру для удаления стобцов( от 1 до 7): "))
res = search(lst, d)
res2 = delete(lst, res)
print(f"Удалил: {res2}")