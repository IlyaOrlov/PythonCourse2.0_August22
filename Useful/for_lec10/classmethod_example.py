import random


class Employee:
    s = "АБЕОУЗМЦЮ"

    def __init__(self):
        self.name = self.name_generator(4)
        self.surname = self.name_generator(6)

    def show(self):
        print(f"Сотрудник {self.name} {self.surname}")

    @classmethod
    def name_generator(cls, name_len):
        print(f"{cls=}")
        name = ""
        for _ in range(name_len):
            name += random.choice(cls.s)
        return name


class EnglishEmployee(Employee):
    s = "ABCDEFGH"


emp1 = Employee()
emp2 = EnglishEmployee()
emp1.show()
emp2.show()