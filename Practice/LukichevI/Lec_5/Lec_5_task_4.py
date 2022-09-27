def count(my_lst, x):
    idx_lst = []
    for i in range(len(my_lst) - 1, -1, -1):
        for a in range(len(my_lst) - 1, -1, -1):
            if x == my_lst[i][a]:
                idx_lst.append(a)
    return idx_lst


def del_num(my_lst, idx_lst):
    for i in range(len(my_lst)):
        for a in idx_lst:
            del my_lst[i][a]
    return my_lst


lst = [[1, 2, 2], [4, 5, 6], [7, 8, 9]]
#       0  1  2    0  1  2    0  1  2
#          0          1          2
a = int(input('Введите счисло на удаление от 1 до 9: '))
res = count(lst, a)
res2 = del_num(lst, res)
print(res2)