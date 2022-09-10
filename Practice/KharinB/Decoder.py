key = input("Введите ключ: ")
code = input("Введите код: ")

print(f"Ваш пароль: {int(code) ^ int(key)}")
