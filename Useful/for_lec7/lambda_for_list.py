# def prepare_to_compare(x):
#     return str(x)

lst = [2, 4, 5, 7, "hello", 10]
lst.append(100)
print(lst)
# el = lst[0]
# el1 = lst[1]
# str(el1) > str(el)
res = lst.sort(key=lambda x: str(x), reverse=True)
print(lst)
print(res)
