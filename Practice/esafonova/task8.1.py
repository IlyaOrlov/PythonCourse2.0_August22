#Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно.
class Iterator:

    def __init__(self, name_file, simbol):
        self._f = open(name_file,'r')
        self._simbol = simbol

    def __iter__(self):
        return self

    def __next__(self):
        a = " "
        b = ""
        while a != "":
            a = self._f.read(1)
            if a == self._simbol:
                return b
            else:
                b += a
        # return b Вот в этом месте вопрос, как вернуть последнее значение в цикле до raise
        raise StopIteration

    def __del__(self):
        self._f.close()



text = Iterator("text","@")
print(next(text))
print(next(text))
print(next(text))
print(next(text))
print(next(text))
print(next(text))
print(next(text))


