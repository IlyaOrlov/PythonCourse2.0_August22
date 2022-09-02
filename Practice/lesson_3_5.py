def revers(word):
    return word[::-1]


def palindrom(list):
    return list == revers(list)


word_list = str(input('Введите слово: '))
if palindrom(word_list):
    print(True)
else:
    print(False)