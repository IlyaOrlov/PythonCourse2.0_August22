class MyNewIterator:
    def __init__(self, n):
        self._cur = 1
        self._step = 2
        self._n = n
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count < self._n:
            res = self._cur
            self._cur += self._step
            self._count += 1
            return res
        else:
            raise StopIteration


obj = MyNewIterator(10)
it = iter(obj)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))