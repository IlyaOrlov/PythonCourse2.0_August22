text1 = open("text1.txt", "r")
text_read = text1.read()
text1.close()
request = input("Введите tab, если нужно заменить табуляцию на 4 пробела, если наоборот введите four: ")
text1 = open("text1.txt", "w")
if request == "tab":
    text1.write(text_read.replace('\t', '    '))
elif request == "four":
    text1.write(text_read.replace('    ', '\t'))
else:
    print("Неизвестный запрос")
text1.close()





