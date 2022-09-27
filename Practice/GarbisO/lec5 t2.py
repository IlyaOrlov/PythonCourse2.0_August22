def check_symbol(my_lst):
    lst1 = []
    for i in range(len(my_lst)):
        if my_lst[i] in lst1:
            print(f"Первый повторившийся символ: {my_lst[i]}")
            break
        else:
            lst1.append(my_lst[i])


lst = [2, 3, 4, 5, 3, 2]
res = check_symbol(lst)
