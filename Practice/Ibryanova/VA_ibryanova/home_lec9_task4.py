import random
import pickle


class Human:

    def __init__(self, name, surname, age, place):
        self._name = name
        self._surname = surname
        self._age = age
        self._place = place


def generator_name(s):
    lst = []
    name = ("Иван", "Антон", "Олег", "Дмитрий", "Сергей")
    surname = ("Иванов", "Антонов", "Дмитров", "Петров", "Егоров")
    place = ("Москва", "Питер", "Севастополь", "Калининград", "Выборг")
    for i in range(s):
        h = Human(random.choice(name),
                  random.choice(surname),
                  random.randint(20, 50),
                  random.choice(place))
        lst.append(h)
    with open("human.data", "wb") as f:
        pickle.dump(lst, f)


def human_deser():
    with open("human.data", "rb") as f:
        return pickle.load(f)


generator_name(4)
print(human_deser())