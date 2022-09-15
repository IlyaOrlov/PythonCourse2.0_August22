while not (v := input("Введите скорость ")).isdecimal():
    pass

while not (t := input("Введите время ")).isdecimal():
    pass

d = int(v) * int(t)
print(d)
