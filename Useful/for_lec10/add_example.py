class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinates {self.x, self.y}"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinates(new_x, new_y)


c1 = Coordinates(10, 20)
c2 = Coordinates(100, 200)

print(f"{c1} + {c2} = {c1 + c2}")
