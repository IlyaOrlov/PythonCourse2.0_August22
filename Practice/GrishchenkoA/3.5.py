word = input("Введите слово для проверки: ")
_lower = word.lower()
left = _lower
rights = _lower[::-1]
print(left == rights)


