# Закрытые методы не наследуются
class Pizza:
    def make_pizza(self):
        print("making pizza")
        self.__add_base()  # self._Pizza__add_base()
        self.__add_ingr()  # self._Pizza__add_ingr()

    def __add_base(self):  # _Pizza__add_base
        print("adding pizza base")

    def __add_ingr(self):  # _Pizza__add_ingr
        print("adding pizza ingredients")


class VegPizza(Pizza):
    def make_pizza(self):
        print("making super pizza")
        self.__add_base()  # self._VegPizza__add_base()
        self.__add_ingr()  # self._VegPizza__add_ingr()

    # не переопределяет закрытый метод базового класса
    def __add_ingr(self):  # _VegPizza__add_ingr
        print("adding veg pizza ingredients")


p = VegPizza()
p.make_pizza()

# Вывод на экран:
# making pizza
# adding pizza base
# adding pizza ingredients


