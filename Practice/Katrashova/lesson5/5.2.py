def fun(my_list):
    new_set = set()
    for i in my_list:
        if my_list[i] in new_set:
            print(f'Первый повторившийся символ: {my_list[i]} ')
            break
        else:
            new_set.add(my_list[i])


lst = [2, 3, 4, 5, 3, 2]
fun(lst)