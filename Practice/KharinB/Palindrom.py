word = input("Введите слово: ").lower()
len_w = len(word)
for i in range(len_w // 2):
    if word[i] != word[- i - 1]:
        print(False)
        break

else:
    print(True)
