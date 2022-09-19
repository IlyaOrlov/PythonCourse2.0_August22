word = input("Введите слово для проверки палиндрома: ")
word = word.lower()
print(word == word[::-1])