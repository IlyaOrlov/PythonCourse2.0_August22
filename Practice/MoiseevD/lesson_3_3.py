pasw = int(input('Введите пароль: '))
cod = int(input('Введите код: '))
w = pasw ^ cod
print(f'Зашифрованный пароль: {w}')
print()
pasw1 = int(input('Введите зашифрованный пароль: '))
cod1 = int(input('Введите пароль'))
w1 = pasw1 ^ cod1
print(f'Ваш код: {w1}')