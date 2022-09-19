def repeat(lst):
    lst_new = []
    for i in lst:
        if not i in lst_new:
            lst_new.append(i)
        else:
            print(i)
            return i


lst_1 = [2, 3, 4, 5, 3, 2]
repeat(lst_1)



