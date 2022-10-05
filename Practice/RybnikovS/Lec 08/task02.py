with open("task01_text.txt", encoding="utf") as f:
    x = (i[:-1] for i in f.readlines())
print(x)
print(next(x))
print(next(x))
