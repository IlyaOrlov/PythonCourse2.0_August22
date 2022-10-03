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
            print(f"Вес {other.name} - большей утки: {other.weight}")
        else:
            print(f"Вес {self.name} - большей утки: {self.weight}")

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        print(f"Общий вес уток: {self.weight + other.weight}")
        return None

Duck1 = Duck("Луи", 1)
Duck2 = Duck("Дьюи", 2)
Duck3 = Duck("Хьюи", 3)
Duck4 = Duck("Скрудж", 4)
lst = [Duck1, Duck2, Duck3, Duck4]
print(lst)
print(Duck1.col())
print(Duck2.say())
print(Duck3 > Duck4)
print(Duck1 != Duck2)
print(Duck2 + Duck4)

