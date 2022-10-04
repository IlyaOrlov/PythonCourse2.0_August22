f1 = open("1.txt", "r")
f2 = open("2.txt", "w")
s = f1.read()
f2.write(s)
f1.close()
f2.close()

f3 = open("1.txt", "r")
for x in f3:
    print(x)
f3.close()


with open("1.txt", "r") as f3:
    for x in f3:
        print(x)


