def palindrom(line):
    return line == line[::-1]


word_line = input('Введите слово: ')
low_letters = word_line.lower()
if palindrom(low_letters):
    print(palindrom(low_letters))
else:
    print(palindrom(low_letters))