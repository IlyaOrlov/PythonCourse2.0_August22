import os

#os.makedirs('mydirectory/mydirectory')
def show_dir(cur_dir):
    for i in os.listdir(cur_dir):
        path = os.path.join(cur_dir, i)
        print(path)
        if os.path.isfile(i):
            print(f"Файл: {i}")
        else:
            print(f"Папка: {i}")
            show_dir(path)

show_dir('.')

# for i in os.walk('.'):
#     print(i)

# t = 'mydirectory'
# f = '1.txt'
# with open(os.path.join(t, f), 'w'):
#     pass



