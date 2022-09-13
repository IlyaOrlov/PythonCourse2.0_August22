password = int(input("Введите пароль: "))
key = int(input("Введите код: "))
result = password^key
print(f"Пароль в зашифрованном виде:{result}")