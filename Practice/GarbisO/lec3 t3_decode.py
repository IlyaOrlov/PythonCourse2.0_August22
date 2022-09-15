code = int(input("Введите пароль в зашифрованном виде: "))
key = int(input("Введите код: "))
result = code^key
print(f"Ваш пароль:{result}")