# Написать генератор для построчного чтения файла.


def my_gen(file):
    with open(file, 'r') as f:
        for m in f:
            yield m


for i in my_gen("my_file.txt"):
    print(i)
