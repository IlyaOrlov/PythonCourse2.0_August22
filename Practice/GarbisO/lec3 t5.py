word = input("Введите слово: ")
#на случай, если слово с заглавной буквы, преобразуем все буквы в строчные
word = word.lower()
if (word == word[::-1]):
    print("True")
else:
    print("False")