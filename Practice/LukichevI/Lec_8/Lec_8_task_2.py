def my_gen(file):
    with open(file, 'r', encoding='utf8') as f:
        for string in f:
            yield string


for i in my_gen('text.txt'):
    print(i)
