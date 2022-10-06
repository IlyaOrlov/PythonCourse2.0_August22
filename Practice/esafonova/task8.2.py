# Написать генератор для построчного чтения файла.
def read_file(a):
    f = open(a, 'r')
    a = ' '
    b = ''
    try:
        while a != '':
            a = f.read(1)
            if a == '/n':
                break
            else:
                b += a
        yield b
    except StopIteration:
        pass


v = read_file('text')
for i in v:
    print(i)





