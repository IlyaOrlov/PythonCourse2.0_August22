import math
word = input("Введите слово для проверки: ")
_lower = word.lower()
word_length = int(len(_lower))
k = word_length / 2
if word_length % 2 == 0:
    z = int(k)
else:
    z = k.__ceil__()
left = _lower[0 : z]
rights = _lower[-1 : int(k) - 1 : -1]
if left == rights:
    print("True")
else:
    print("False")


