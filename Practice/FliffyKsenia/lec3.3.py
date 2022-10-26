#программа по кодировке
kod = 325
stroka = input("Введие символ: ")
stroka1 = ""
for ind in stroka:
    kod_simvola = ord(ind)
    #print(kod_simvola)
    t = (kod_simvola+kod)%256
    stroka1 += chr(t)
print(stroka1)

#программа по раскодировке
stroka1 = input("Введите символ: ")
stroka2 = ""
for ind in stroka1:
    kod_simvola = ord(ind)
    #print(kod_simvola)
    e = (kod_simvola-325)%256
    stroka2 += chr(e)
print(stroka2)

