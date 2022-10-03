# type -> класс (объект типа type) -> экземпляр (объект класса)
class Pizza:
    def __init__(self):
        self._status = "Not ready"

    def make_base(self):
        print("Base ready")

    def add_ingredients(self):
        print("Ingredients added")

    def bake(self):
        self._status = "Ready"
        print("Baking done")

    def show_status(self):
        print(self._status)


class MeatPizza(Pizza):
    def add_ingredients(self):
        print("Meat added")


class VegPizza(Pizza):
    def add_ingredients(self):
        print("Vegs added")


class MushPizza(Pizza):
    def add_ingredients(self):
        print("Mushs added")


lst = [MeatPizza(), VegPizza(), MushPizza()]
for p in lst:
    p.make_base()
    p.add_ingredients()
    p.bake()
    p.show_status()
