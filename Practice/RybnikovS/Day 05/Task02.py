old_arr = [2, 3, 4, 5, 3, 2]

#Время выполнения O(n**2)
# min_index = len(arr)
# for i in range(len(arr)):  # O(n)
#     for j in range(i+1, len(arr)):  # O(n) => O(n**2)
#         if arr[i] == arr[j] and j < min_index:
#             min_index = j
#             break
# print(arr[min_index])

#Время выполнения O(n*log(n)) - лучшее
arr_second = []
arr = list(sorted(enumerate(old_arr), key=lambda x: x[1]))  # O(n*log(n)) > O(n) => O(n*log(n))
print(arr)
value_to_ignore = None
for i in range(len(arr)-1):  # O(n)
    if value_to_ignore == arr[i][1]:
        continue
    if arr[i][1] == arr[i+1][1]:
        arr_second.append(arr[i+1][0])
        value_to_ignore = arr[i][1]
print(old_arr[min(arr_second)])
