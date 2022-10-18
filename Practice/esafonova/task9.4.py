#Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров,
# сериализовывала их и сохраняла в файл human.data, и другую функцию, которая бы читала файл human.data,
# десериализовывала его содержимое и выводила результат на печать.
# чтоб у экземпляров Human были разные значения атрибутов, можно воспользоваться функциями random.randint() и random.choice().
import random
from dataclasses import dataclass
import pickle


@dataclass
class Human:
    name: str
    surname: str
    age: int
    city: str
    salary: int

def process_human_and_ser(n, file_name):
    names = ['Игорь', 'Петр', 'Антон', 'Иван', 'Алексей']
    surnames = ['Петров', 'Сидоров', 'Антонов', 'Белов', 'Иванов']
    cities = ['Москва', 'Самара', 'Владивосток', 'Уфа', 'Тамбов']
    humans = []
    for i in range(n):
        human = Human(
            random.choice(names),
            random.choice(surnames),
            random.randint(18,40),
            random.choice(cities),
            random.randint(35000, 85000)
        )
        humans.append(human)

    with open(file_name, 'wb') as f:
        for human in humans:
            pickle.dump(human, f, protocol=pickle.HIGHEST_PROTOCOL)


def deser_human(file_name, n):
    with open(file_name, 'rb') as f:
        humans = []
        for i in range(n):
            humans.append(pickle.load(f))
    return humans


process_human_and_ser(5, 'task9.4.1')
humans = deser_human('task9.4.1', 5)
for human in humans:
    print(human)


