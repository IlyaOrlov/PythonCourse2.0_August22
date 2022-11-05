lst = ['10', '5', 'a', '3', 'b']
lst_new = [x**2 for i in lst if i.isdecimal() and (x := int(i)) % 5 == 0]
print(lst_new)
