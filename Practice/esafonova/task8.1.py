#Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно.
class Iterator:

    def __init__(self, f, simbol):
        self._f = f
        self._simbol = simbol

    def __iter__(self):
        return self

    def __next__(self):
        a = " "
        b = ""
        while a != "":
            a = self._f.read(1)
            if a == self._simbol:
                break
            else:
                b += a
        return b

with open("text") as f:
    text = Iterator(f, "@")
    print(next(text))
    print(next(text))
    print(next(text))
    print(next(text))