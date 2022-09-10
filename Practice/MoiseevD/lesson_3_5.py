def palindrom(line):
    return line == line[::-1]


word_line = input('Введите слово: ')
low_letters = word_line.lower()
print(palindrom(low_letters))
