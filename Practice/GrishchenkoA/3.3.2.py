code = int(input("Введите зашифрованный код :"))
key = 888
password = code ^ key
print(password)