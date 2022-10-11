import random
# рандомное формирование имени и фамилии

class Employee:
    s = "АБЕОЗЩМЮ"

    def __init__(self):
        self.name = self.name_generator(4)
        self.surname = self.name_generator(6)

    def show(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    @classmethod
    def name_generator(cls, name_len):# cls будет указывать на класс, кот-й нужно использовать
        print(f'{cls=}')
        name = ''
        for _ in range(name_len):
            name += random.choice(cls.s)
        return name


class EnglishEmployee(Employee):# сгенерируем список имен на англ яз
    s = 'AMDBTOEEHS'


#Методы кот-е использ=т классовые атрибуты, а не атриб-ты экземпляра
# назыв-ся классовый метод и вешается спец декоратор - @classmethod


emp1 = Employee()
emp2 = EnglishEmployee()
emp1.show()
emp2.show()
