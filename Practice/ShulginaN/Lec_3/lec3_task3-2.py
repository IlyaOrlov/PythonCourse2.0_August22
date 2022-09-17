code = input("Введите шифр: ")
key = 14071995
res = int(code) ^ key
print(f"Ваш пароль: {res}")