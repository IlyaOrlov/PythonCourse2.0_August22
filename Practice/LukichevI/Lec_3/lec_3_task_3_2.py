code = int(input('Введите пароль в зашифрованном виде: '))
key = int(input('Введи ключ:'))
res = code ^ key
print(f'Пароль в расшифрованном виде: {res}')