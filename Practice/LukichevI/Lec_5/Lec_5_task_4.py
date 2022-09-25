def del_num(my_lst):
    x = int(input('Введите счисло на удаление от 1 до 9: '))
    for i in range(len(my_lst)):
        for a in range(len(my_lst)):
            if x == my_lst[i][a]:
                my_lst[i].pop(a)
                return my_lst

lst = [[1, 2, 3 ], [4, 5, 6], [7, 8, 9]]
#       0  1  2     0  1  2    0  1  2
#          0           1          2
print(del_num(lst))
