def sort_lst(arr):
    for i in range(len(arr) - 1):
        min = i
        for a in range(i + 1, len(arr)):
            if arr[a] < arr[min]:
                min = a
        arr[i], arr[min] = arr[min], arr[i]


arr = [0,3,24,2,3,7]
sort_lst(arr)
print(f'Список отсортирован: {arr}')

