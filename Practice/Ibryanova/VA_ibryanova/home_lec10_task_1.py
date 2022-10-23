lst = ["10", "5", "a", "3", "b"]
new_lst = [x*x for i in lst if i.isdecimal() and (x := int(i)) * 2]

print(new_lst)