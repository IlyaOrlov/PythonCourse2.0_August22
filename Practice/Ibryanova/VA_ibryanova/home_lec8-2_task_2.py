#Написать генератор

def my_gen(file):
    with open(file, 'r') as f:
        for i in f:
            yield i


for x in my_gen('fragment.txt'):
    print(x)