class Coordinates:
    def __init__(self):
        self.a = 0
        self.b = 0

    def __add__(self, other):
        m = Coordinates()
        m.a = self.a + other.a
        m.b = self.b + other.b
        return m

    def __str__(self):
        return f"Coordinates: a = {self.a}, b = {self.b}"

    # неудобная и неочевидная реализация
    def add_method(self, another):
        m = Coordinates()
        m.a = self.a + another.a
        m.b = self.b + another.b
        return m


x = Coordinates()
x.a = 10
x.b = 20
y = Coordinates()
y.a = 100
y.b = 200
print(x + y + y + y)


#print(x.add_method(x.add_method(x.add_method(x.add_method(x.add_method(y))))))
