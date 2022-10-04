matrix = [[1,2,3],[4,5,6],[7,8,9],[1,2,3,4],[5,6,7,8,9]]
print(matrix)
#удаляем поля, где встречается цифра 2
delet = 2
# заходим в цикл и осуществляем перебор с конца
for a in range(len(matrix) -1,-1,-1):
    for c in matrix[a]:
        if c == delet:
            matrix.pop(a)


print(matrix)


