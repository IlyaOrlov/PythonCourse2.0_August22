d = dict()
while True:
    i = input("Input something: ")
    if i == "stop":
        break
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
