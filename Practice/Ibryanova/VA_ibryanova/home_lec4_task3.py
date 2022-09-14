list = []
while True:
    number = int(input("Input a number: "))
    list.append(number)
    if number == "stop":
        break

print("list all elements",list)

even_list = []
odd_list = []

for i in number:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even list:",even_list)
print("Even list:",odd_list)