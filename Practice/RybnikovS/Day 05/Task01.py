def find_min_in_arr(array):
    min_ind = 0
    for index, value in enumerate(array):
        if value < array[min_ind]:
            min_ind = index
    return min_ind


arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)-1):
    min_index = find_min_in_arr(arr[i:])
    if i != min_index:
        arr[i], arr[i+min_index] = arr[i+min_index], arr[i]
print(arr)
