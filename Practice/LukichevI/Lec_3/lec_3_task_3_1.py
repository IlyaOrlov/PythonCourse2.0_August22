password = int(input('Введите пароль: '))
key = int(input('Введи ключ:'))
res = password ^ key
print(f'Пароль в зашифрованном виде: {res}')