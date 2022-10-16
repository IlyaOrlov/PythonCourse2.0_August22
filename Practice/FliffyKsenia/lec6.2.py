# объявляем класс для уток.
class Duck:
    # пусть у нас все утки будут серыми
    COLOR = "серая"

    # инициализируем класс и вводим вес и имя утки.
    def __init__(self,name = "",weight = 0):
        self.weight = weight
        self.name = name

    # возвращаем цвет утки.
    def my_color(self):
        return self.COLOR

    # подменяем стандартный вывод информацию об утке.
    def __str__(self):
        return f"Меня зовут:{self.name}, мой вес:{self.weight}, и я {self.COLOR}"

    # подменяем процедуру сравнения уток, и выясняем самую тяжелую.
    def __lt__(self, other):
        nam = self.name
        if self.weight<other.weight:
            nam = other.name
        return nam

    # подменяем процедуру проверки на равенство по весу..
    def __eq__(self, other):
        return self.weight == other.weight

    # подменяем процедуру сложения уток.
    def __add__(self, other):
        return self.weight + other.weight

#статистический метод  Crack
    @staticmethod
    def speak():
        return 'Crack'
# задаем первую утку
p = Duck("Правая",40)
# задаем вторую утку
l = Duck("Левая",40)
# выводим информацию об утках.
print(f"Первая утка: {p}")
print(f"Вторая утка: {l}")
# выясняем кто тяжелее
print(f"Самая тяжелая утка: {p<l}")
# узнаем как они общаются
print(f"Утки разговаривают так: {p.speak()}")
# узнаем какого они цвета
print(f"Цвет уток: {p.my_color()}")
# узнаем общий вес уток.
print(f"Общий вес уток: {p+l}")
# узнаем, а одинаково ли весят утки
print(f"Одинаков ли у них вес? {p==l}")
