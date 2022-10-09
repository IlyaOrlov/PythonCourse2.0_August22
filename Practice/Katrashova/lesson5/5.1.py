array = [0, 3, 24, 2, 3, 7]

def arr_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

arr_sort(array)
print(array)