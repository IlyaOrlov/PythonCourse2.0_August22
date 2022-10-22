class Money:

    def __init__(self, rubbles, pennies):
        self.rub = rubbles
        self.pen = pennies

    def __repr__(self):
        return f"{self.rub},{self.pen}"

    def __add__(self, other):
        temp_pen = self.pen + other.pen
        temp_rub = self.rub + other.rub
        if temp_pen >= 100:
            temp_rub += 1
            temp_pen -= 100
        return Money(temp_rub, temp_pen)

    def __sub__(self, other):
        temp_pen = abs(self.pen - other.pen)
        temp_rub = self.rub - other.rub
        return Money(temp_rub, temp_pen)

    def __ge__(self, other):
        if self.rub > other.rub:
            return True
        elif self.rub == other.rub:
            if self.pen >= other.pen:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.rub > other.rub:
            return True
        elif self.rub == other.rub:
            if self.pen > other.pen:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return True if self.rub == other.rub and self.pen == other.pen else False


one = Money(50, 20)
two = Money(100, 60)
print(f"{one=}")
print(f"{two=}")
print(f"one + two", one + two)
print(f"one - two", one - two)
print("one == two", one == two)
print("one != two", one != two)
print("one >= two", one >= two)
print("one > two", one > two)