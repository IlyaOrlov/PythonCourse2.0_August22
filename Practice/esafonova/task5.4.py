num = int(input('Введите значение цифры для удаления: '))
def mat(lst, num):
    for i in lst:
        j = 0
        while j < len(i):
            if i[j] == num:
                delete(lst, j)
                j -= 1
            j += 1
    return lst


def delete(lst, j):
    [lst[i].pop(j) for i in range(len(lst))]

lst = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
print(mat(lst, num))