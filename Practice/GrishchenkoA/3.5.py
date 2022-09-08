import math
word = input("Введите слово для проверки: ")
_lower = word.lower()
left = _lower[0 : ]
rights = _lower[-1 : : -1]
print(left == rights)


