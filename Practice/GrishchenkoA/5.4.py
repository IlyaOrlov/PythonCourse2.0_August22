def delete_column(lst, number):
    for d in lst:
        for y, v in enumerate(d):
            if number == int(v):
                for k in range(len(lst)):
                    del lst[k][y]
        for y, v in enumerate(d):
            if number == int(v):
                for k in range(len(lst)):
                    del lst_1[k][y]


lst_1 = [[1, 2, 2, 4], [7, 8, 9, 5], [5, 6, 7, 4], [1, 2, 9, 5]]
number_1 = int(input("Введите цифру: "))
delete_column(lst_1, number_1)
print(lst_1)



