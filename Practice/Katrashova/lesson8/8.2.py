def my_gen(file):
    with open(file, 'r', encoding='utf8') as f:
        for s in f:
            yield s


for i in my_gen('text.txt'):
    print(i)