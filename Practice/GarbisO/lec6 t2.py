class Duck:
    color = "белый"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def say ():
        return "Кря-кря"

    @classmethod
    def col(cls):
       cls.color = Duck.color
       return f"Цвет уток: {Duck.color}"

    def __repr__(self):
        return f"Имя утки: {self.name}, вес утки: {self.weight}"

    def __lt__(self, other):
        if self.weight < other.weight:
            return f"Вес {other.name} - большей утки: {other.weight}"
        else:
            return f"Вес {self.name} - большей утки: {self.weight}"

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        print(f"Общий вес уток: {self.weight + other.weight}")
        return None

duck1 = Duck("Луи", 1)
duck2 = Duck("Дьюи", 2)
duck3 = Duck("Хьюи", 3)
duck4 = Duck("Скрудж", 4)
lst = [duck1, duck2, duck3, duck4]
print(lst)
print(duck1.col())
print(duck2.say())
print(duck3 > duck4)
print(duck1 != duck2)
print(duck2 + duck4)

