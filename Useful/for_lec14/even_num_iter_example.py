class EvenNumbers:
    def __init__(self, limit):
        self.start = 0
        self.step = 2
        self.cnt = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < self.limit:
            res = self.start
            self.start += self.step
            self.cnt += 1
            return res
        else:
            raise StopIteration


for i in EvenNumbers(10):
    print(i)
print("==============")
for i in EvenNumbers(100):
    print(i)
