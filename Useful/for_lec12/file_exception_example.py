def write_to_file(filename, value):
    try:
        print("открываем файл")
        f = open(filename, "w")
        print("записываем в файл")
        f.write(value)
        print("Исключений не произошло")
    except Exception as ex:
        print(ex)
    finally:
        print("закрываем файл")
        f.close()


write_to_file("1.txt", 10)
