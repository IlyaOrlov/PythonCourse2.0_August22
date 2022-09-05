def uncoding():
    encripted_pass = int(input("Введите зашифрованный пароль: "))
    encription_key = int(input("Введите секретный код: "))
    current_pass = encripted_pass ^ encription_key
    return (print(f"Ваш пароль {current_pass}"))


print("Программа шифрования пароля")
coding()
exit("Работа с шифрованием завершена")
