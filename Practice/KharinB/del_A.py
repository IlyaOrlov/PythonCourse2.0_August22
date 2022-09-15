word = input("Введите слово: ")
while True:
    if word.find("a") == -1 and word.find("A") == -1:
        break
    word = word.replace("a", "*")
    word = word.replace("A", "*")
print(word)
