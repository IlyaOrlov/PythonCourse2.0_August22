class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, *args, **kwargs):
        for i in args:
            print(i * self.n)


fun = Multiplier(10)
fun(5) #50
fun(2) #20
fun(3) #30
