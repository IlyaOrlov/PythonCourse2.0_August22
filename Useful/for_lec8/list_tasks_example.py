#      0  1  2  3  4  5  6  7
lst = [1, 2, 3, 4, 3, 4, 5, 6, 8]  # [1, 3, 3, 5]

# Создать новый список из нечётных элементов старого
lst2 = [i for i in lst if i % 2 != 0]

# Удалить из списка все чётные значения
# !!!Антипример 1
# for i in range(len(lst)):
#     print(i, lst)
#     if lst[i] % 2 == 0:
#         lst.pop(i)
# !!!Антипример 2
# for i in lst:
#     print(i, lst)
#     if i % 2 == 0:
#         lst.remove(i)
# !!!Антипример 3
# for i, d in enumerate(lst):
#     if d % 2 == 0:
#         lst.pop(i)
# print(lst)
#
# Пример 1
# i = len(lst) - 1
# while i >= 0:
#     if lst[i] % 2 == 0:
#         lst.pop(i)
#     i -= 1
# print(lst)
#
# Пример 2
# i = 0
# while i < len(lst):
#     if lst[i] % 2 == 0:
#         lst.pop(i)
#     else:
#         i += 1
# print(lst)

# Пример 3
for el in reversed(lst):
    if el % 2 == 0:
        lst.remove(el)
print(lst)
