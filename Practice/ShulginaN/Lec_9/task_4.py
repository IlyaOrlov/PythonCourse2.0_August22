# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров, сериализовывала их и сохраняла в файл
# human.data, и другую функцию, которая бы читала файл human.data, десериализовывала его содержимое и выводила
# результат на печать. Примечание: чтоб у экземпляров Human были разные значения атрибутов, можно воспользоваться
# функциями random.randint() и random.choice().


import random
import pickle


class Human:

    def __init__(self, name, surname, patronymic, age, place):
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._age = age
        self._place = place


def generator_name_ser(s):
    lst = []
    name = ("Иван", "Антон", "Олег", "Дмитрий", "Сергей")
    surname = ("Иванов", "Антонов", "Дмитров", "Петров", "Егоров")
    patronymic = ("Иванович", "Антонович", "Петрович", "Владимирович", "Сергеевич")
    place = ("Москва", "Нижний Новгород", "Семенов", "Иваново", "Владимир")
    for i in range(s):
        h = Human(random.choice(name),
                  random.choice(surname),
                  random.choice(patronymic),
                  random.randint(20, 45),
                  random.choice(place))
        lst.append(h)
    with open("human.data", "wb") as f:
        pickle.dump(lst, f)


def human_deser():
    with open("human.data", "rb") as f:
        return pickle.load(f)


generator_name_ser(5)
print(human_deser())



