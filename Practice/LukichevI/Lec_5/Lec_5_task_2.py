def fun(my_list):
    new_list = set()
    for i in range(len(my_list)):
        if my_list[i] in new_list:
            print(f'Первый повторившийся символ: {my_list[i]} ')
            break
        else:
            new_list.add(my_list[i])


lst = [2, 3, 4, 5, 3, 2]
fun(lst)