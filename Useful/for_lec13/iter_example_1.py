class MyIterator:
    def __init__(self, lst):
        self._lst = lst
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._lst):
            if self._lst[self._i] % 2 == 0:
                res = self._lst[self._i]
                self._i += 1
                return res
            else:
                self._i += 1

        raise StopIteration


lst = [2, 3, 4, 5, 7, 6, 9, 8]
# for i in lst:
#     print(i)

for i in MyIterator(lst):
    print(i)
