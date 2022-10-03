def sort(arr):
    for i in range(len(arr)):
        min = i

        for a in range(i + 1, len(arr)):
            if arr[a] < arr[min]:
                min = a

        arr[min], arr[i] = arr[i], arr[min]
    return arr

arr = [0,3,24,2,3,7]
print(sort(arr))