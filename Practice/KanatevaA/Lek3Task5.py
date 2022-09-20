s = input("введите слово содержащее букву А:")
s1 = " "
for i in s:
    if i == "A" or i == "a":
        s1 += "*"
    else:
        s1 += i
print(s1)




