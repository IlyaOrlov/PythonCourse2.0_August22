# while True:
#     a = input("Введите число: ")
#     if a.isdecimal():
#         break
#
# a = int(a)
# print(f"Квадрат числа: {a * a}")

while not (a := input("Введите число: ")).isdecimal():
    print("check nonstop")
    if a == 'nonstop':
        continue
    print("check stop")
    if a == 'stop':
        break
else:
    a = int(a)
    print(f"Квадрат числа: {a * a}")

print("The end")


