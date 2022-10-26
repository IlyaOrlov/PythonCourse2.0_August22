arr = ['0' ,'3', '24', '2', '3', '7']
# найти наименьший элемент в массиве
print(min(arr, key=lambda i: int(i)))
# поменять местами его и первый элемент в массиве
# вызываем функцию свопинга
def swapPositions(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

    return arr
# вызываем функцию драйвера
arr = [0, 3, 24, 2, 3, 7]

pos1, pos2 = 1, 3
print(swapPositions(arr, pos1-1, pos2-2))

# найти следующий наименьший элемент в массиве
def two_min(arr):
    m1, m2 = arr[0], None
    for a in arr[1:]:
        if a < m1:
            m1, m2 = a, m1
        elif m2 == None or a < m2:
            m2 = a
    return (m2)


print(two_min([0, 3, 24, 2, 3, 7]))

# и поменять местами его и второй элемент массива



# вызываем функцию свопинга

arr.sort()
print(arr)
#продолжать это пока весь массив не будет отсортирован
arr.sort()
print(arr)