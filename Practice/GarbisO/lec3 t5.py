word = input("Введите слово: ")
#на случай, если слово с заглавной буквы, преобразуем все буквы в строчные
word = word.lower()
print(word == word[::-1])