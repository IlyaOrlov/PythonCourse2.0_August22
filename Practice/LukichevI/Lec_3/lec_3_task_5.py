# word = input("Введите слово для проверки на палиндромность: ")
# if word.lower()[::] == word.lower()[::-1]:    # word[::] - проверка(срез) с начала строки, word[::-1] - срез с конца строки
#     print('True')             # s[start:stop:step] - делает срез, начиная с индекса start до индекса stop с шагом step
# else:
#     print('False')


word = input("Введите слово для проверки на палиндромность: ")
word = word.lower()
print(word[::] == word[::-1])



