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
        try:
            while a != "":
                a = self._f.read(1)
                if a == self._simbol:
                    break
                else:
                    b += a
            return b
        except StopIteration:
            pass

    def __del__(self):
        self._f.close()



text = Iterator("text","@")
print(next(text))
print(next(text))
print(next(text))
print(next(text))

