txt = str(input("Проверка на палиндром\nВведите слово\n"))
if txt.upper() == txt.upper()[::-1]:
    print('True')
else:
    print('False')
