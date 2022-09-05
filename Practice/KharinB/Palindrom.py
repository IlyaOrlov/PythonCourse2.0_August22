word = input("Введите слово: ")
len_w = len(word)
for i in range(len_w // 2):
    if word[i] != word[len_w - (i + 1)]:
        print(False)
        break

    elif i + 1 == len_w // 2:
        print(True)
