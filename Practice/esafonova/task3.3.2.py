code = int(input("Введите код: "))
key = 458
password = code ^ key
print(password)