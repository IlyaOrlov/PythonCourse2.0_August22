cvv = int(input("введите цифровой пароль:"))
key = int(input("введите ключ:"))
res = cvv^key
print (f"Шифр введенного пользователем пароля code: {res}")

code = int(input("введите сообщенный code"))
key = int(input("введите ключ:"))
res = code^key
print (f"восстановленный пароль: {res}")


