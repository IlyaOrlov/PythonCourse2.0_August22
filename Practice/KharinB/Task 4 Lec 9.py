import random
import pickle

class Human:

    def __init__(self, name, surname, adres, age, marriage, child = False, hobbi = False, pet = False, conscripted = False, sleep_now = False):
        self._name = name
        self._surname = surname
        self._age = age
        self._adres = adres
        self._marriage = marriage
        self._child = child
        self._hobbi = hobbi
        self._pet=pet
        self._conscripted = False # Принципиально
        self._sleep_now = sleep_now


def gen_str():
    l = random.randint(3,10)
    res_str = ""
    for _ in range(l):
        res_str += random.choice("абвгдеёжзийклмнопрстуфхцчшщыьъэюя")
    return res_str


def human_ser(q):
    human_lst = []
    for _ in range(q):
        human_atr = [gen_str(), gen_str(), gen_str(), random.randint(1,100)] # создаём список с первыми четырьмя атрибутами
        atr = random.randint(1,6)
        for __ in range(atr):
            human_atr += [random.choice([True, False])] # Дополняем список атрибутов рандомным количеством атрибутов, но не меньше 1
        human_lst += [Human(*human_atr)]
    with open('human.data', 'wb') as f:
        pickle.dump(human_lst, f)


def human_deser():
    with open('human.data', 'rb') as f:
        return pickle.load(f)


human_ser(5)

print(human_deser())