def palindrom(x):
    return x == x[::-1]

word = input("Введите слово: ")
wordLow = word.lower()
print(palindrom(wordLow))
