s = "dsfsfds1ytuyt45"

i = 0
while i < len(s):
    print(s[i])
    if s[i].isdecimal():
        print("Цифры есть!")
        break
    i += 1
else:
    print("Цифр нет!")