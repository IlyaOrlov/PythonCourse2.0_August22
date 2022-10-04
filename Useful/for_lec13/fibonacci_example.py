class Fibonacci:

    def __init__(self, N):
        self.n, self.a, self.b, self.max = 0, 0, 1, N

    def __iter__(self):
        # сами себе итератор: в классе есть метод next()
        return self

    def __next__(self):
        if self.n < self.max:
            # a = self.a
            # self.a = self.b
            # self.b += a
            # self.n += 1
            a, self.n, self.a, self.b = self.a, self.n + 1, self.b, self.a + self.b
            return a
        else:
            raise StopIteration


for i in Fibonacci(10):
    print(i, end=' ')


