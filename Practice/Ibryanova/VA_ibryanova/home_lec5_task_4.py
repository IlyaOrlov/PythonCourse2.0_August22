def find(lst, x):
    lst_inx = set()
    for i in range(len(lst)):
        for number in range(len(lst)):
            if x == lst[i][number]:
                lst_inx.add(number)
    lst_inx = list(lst_inx)
    return lst_inx

def delete(lst, lst_inx):
    for i in range(len(lst)):
        for number in reversed(lst_inx):
            del lst[i][number]
    return lst



lst = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [9, 11, 13, 15],
    [10, 12, 14, 0]
]
number = int(input('Введите число от 0 до 15 для удаления столбца: '))
res = find(lst, number)
res2 = delete(lst, res)
print(res2)