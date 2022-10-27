def repeat(lst):
    set_new = set()
    for i in lst:
        if not i in set_new:
            set_new.add(i)
        else:
            print(i)
            return i


lst_new = [2, 3, 4, 5, 3, 2]
repeat(lst_new)



