# Есть список списков (матрица). Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.


def search(ls, a):
    ind = set()
    for i in range(len(ls)):
        for m in range(len(ls)):
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

res = search(lst, 4)
res2 = delete(lst, res)
print(res2)





