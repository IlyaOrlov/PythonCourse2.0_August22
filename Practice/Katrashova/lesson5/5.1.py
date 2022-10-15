
def arr_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        if i != m:
            arr[i], arr[m] = arr[m], arr[i]

array = [0, 3, 24, 2, 3, 7]

arr_sort(array)
print(array)