import random

password = input("Введите цифровой пароль: ")
key = ""

for i in range(len(password)):
   key += str(random.randint(0, 9))

print(f"ключ: {key}")
print(f"код: {int(password) ^ int(key)}")
