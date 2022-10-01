class Duck:
    _color = "коричневый"

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @staticmethod
    def crack_duck():
        print("Crack")

    @classmethod
    def color_print(cls):
        print(cls._color)

    def show_info(self):
        print(f"Вес утки по имени {self._name} равен {self._weight}")

    def __repr__(self):
        return self._name

    def __lt__(self, other):
        if self._weight < other._weight:
            res = other._name
        else:
            res = self._name
        return res

    def __ne__(self, other):
        return self._weight == other._weight

    def __add__(self, other):
        return self._weight + other._weight


a = Duck("Донни", 3)
b = Duck("Дональд", 5)

a.crack_duck()
a.color_print()
a.show_info()
print(a)
print(a > b)
print(a == b)
print(a + b)
