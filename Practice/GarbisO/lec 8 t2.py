def mygen(text):
    with open("paragraph.txt", 'r', encoding="utf8") as f:
        for string in f:
            yield string


for i in mygen("paragraph.txt"):
    print(i)
