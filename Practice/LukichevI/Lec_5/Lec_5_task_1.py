def sort_lst(b):
    for i in range(len(b)):
        minimum = i
        for a in range(i + 1, len(b)):
            if b[a] < b[minimum]:
                minimum = a
        if i != minimum:
            b[i], b[minimum] = b[minimum], b[i]


arr = [0,3,24,2,3,7]
sort_lst(arr)
print(f'Список отсортирован: {arr}')


