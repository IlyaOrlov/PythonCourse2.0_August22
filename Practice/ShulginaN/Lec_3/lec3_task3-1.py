pas = input("Введите пароль для шифрования: ")
key = 14071995
res = int(pas) ^ key
print(f"Зашифрованный пароль: {res}")