import random
import pickle


class Human:
    def __init__(self):
        __first_name_lib = ("Petr", "Ivan", "Anton")
        __second_name_lib = ("Petrov", "Ivanov", "Antonov")
        __hair_lib = ("Black", "Brown", "Yellow", "Blue")
        self._first_name = random.choice(__first_name_lib)
        self._second_name = random.choice(__second_name_lib)
        self._age = random.randint(18, 60)
        self._year_of_birth = 2022 - self._age
        self._hair = random.choice(__hair_lib)


lst = []
for i in range(5):
    lst.append(Human())
with open("human.data", "wb") as file:
    pickle.dump(lst, file)

