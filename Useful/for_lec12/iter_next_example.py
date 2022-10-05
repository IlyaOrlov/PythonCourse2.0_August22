lst = [1, 2, 3, 4]
s = {7, 8, 4, 5}
st = "abcdef"
d = {"a": 1, "b": 2, "c": 3}

# С полиморфизмом весело:

# super_list = [lst, s, st]
# for el in super_list:
#     print("============")
#     for i in el:
#         print(i)

# it = iter(lst)  # lst.__iter__()
# print(it)
# i = next(it)  # it.__next__()
# print(i)
# i = next(it)
# print(i)
# i = next(it)
# print(i)
# i = next(it)
# print(i)
# i = next(it)
# print(i)
#
# for i in lst:
#     print(i)

# Без полиморфизма грустно:
super_list = [lst, s, st, d]
j = 0
while j < len(super_list):
    print("============")
    i = 0
    while i < len(super_list[j]):
        if type(super_list[j]) in (list, str):
            print(super_list[j][i])
        elif type(super_list[j]) is set:
            print(super_list[j].pop())
        elif type(super_list[j]) is dict:
            print(super_list[j].popitem())
        i += 1
    j += 1
#
# i = 0
# while i < len(s):
#     print(s.pop())
#     i += 1
#
# i = 0
# while i < len(st):
#     print(st[i])
#     i += 1
#
# i = 0
# while i < len(d):
#     print(d.popitem())
#     i += 1
