# Написать генератор для построчного чтения файла.
def read_file(a):
    with open(a, 'r') as f:
        a = ' '
        b = ''
        while a != '':
            a = f.read(1)
            if a == '/n':
                yield b
            else:
                b += a
        if b!= '':
            yield b

# Как уложить в 4 строчки
# def read_file(a):
#     with open(a, 'r') as f:
#         for i in f:
#             yield i


v = read_file('text')
for i in v:
    print(i)





