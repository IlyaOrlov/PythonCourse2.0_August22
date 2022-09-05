def coding():
    current_pass = int(input("Введите текущий пароль: "))
    encription_key = int(input("Введите секретный код: "))
    encripted_pass = current_pass ^ encription_key
    return (print(f"Ваш зашифрованный пароль {encripted_pass}"))


print("Программа шифрования пароля")
coding()
exit("Работа с шифрованием завершена")
