def print_matrix(matrix):
    for i in matrix:
        print (i)


matrix = [[1,2,3,5,2],[4,5,6,2,1],[7,3,9,2,6],[1,2,3,4,5],[5,6,7,8,9]]
print("Bylo:")
print_matrix(matrix)
#удаляем поля, где встречается цифра 2
delet = 2
my = len(matrix)
if my > 0:
    mx = len(matrix[0])

    # заходим в цикл и осуществляем перебор с конца

    for indx in range(my):
        for indy in range(mx-1,-1,-1):
            if matrix[indx][indy] == delet:
                for i in range(my):
                    matrix[i].pop(indy)
                mx = mx - 1


    print("---------------------------")
    print("Stalo:")
    print_matrix(matrix)



