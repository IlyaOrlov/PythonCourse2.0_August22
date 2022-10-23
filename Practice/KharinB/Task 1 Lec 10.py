lst = ["10", "5", "a", "3", "b"]
lst_iter = iter(lst)
new_lst = []
i = 0
len_lst = len(lst)
while res:=next(lst_iter):
    if res.isdecimal():
        res = int(res)
        if res%5 == 0:
            new_lst.append(res)
    i += 1
    if i >= len_lst:
        break
print(new_lst)