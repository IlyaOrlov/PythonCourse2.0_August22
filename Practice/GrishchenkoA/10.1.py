lst = ["10", "5", "a", "3", "b"]
lst1 = [x**2 for z in lst if z.isdigit() and (x := int(z))%5 == 0]
print(lst1)

