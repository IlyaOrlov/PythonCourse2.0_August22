# word = input('Введите слово для замены всех букв "Аа" на "*": ')
# if word.islower() == True:    # проверка на то, что все буквы строчные
#     word = word.replace('а', '*')
#     print(f'Буквы "а" в веднном слове заменены.\nРезультат: {word}')
# else:    # На тот случай, если пользователь введет несколько прописных букв в слове
#     word = word.lower()    # Для начала уменьшим все буквы до строчных
#     word_1 = word[0:1:]    # Срез первой буквы в веденном слове
#     word_1 = word_1.replace('а', 'А')    # Заменяем строчную букву на прописную
#     word_1 = word_1.replace('А', '*')    # Заменяем прописную букву  на символ "*"
#     word_2 = word[1:len(word):]    # Cрез введенного слова с второго символа и до конца
#     word_2 = word_2.replace('а', '*')    # Замена строчной буквы "а" на символ "*"
#     word = word_1 + word_2    # Конкатенация  строковых параметров
#     print(f'Буквы "Аа" в веднном слове заменены.\nРезультат: {word}')

word = input('Введите слово для замены всех букв "А,а" на "*": ')
word = word.replace('А', '*').replace('а', '*')
print(word)