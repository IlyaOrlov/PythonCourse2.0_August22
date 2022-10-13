import random
# рандомное формирование имени и фамилии

 "АБЕОЗЩМЮ"

    class Employee:
        s =
    def __init__(self):
        self.name = self.name_generator(4)
        self.surname = self.name_generator(6)

    def show(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    @staticmethod
    def name_generator(name_len):
        #s = "АБЕОЗЩМЮ"
        name = ''
        for i in range(name_len):
            name += random.choice(Employee.s)
        return name

# чтобы не совершалась лишняя операция мы строку s = "АБЕОЗЩМЮ" вынесли в класс


class EnglichEmployee(Employee):# сгенерируем список имен на англ яз
    s = 'AMDBTOEEH'


print(Employee.name_generator(10))
#def name_generator факт=ки мы может эту ф-ю вынести из класса,
# но она нам в классе нужна, она логич-ки связана с ним. Этот класс исп-т эту фун-ю.
#Методы кот-е логически связаны с классами, но ни как не испол-т его атрибуты
# назы=ся статич-ми методами.На такие методы вешается спец декоратор - @staticmethod


emp1 = Employee()
emp2 = Employee()
print(Employee.__dict__)


lst = [emp1, emp2]
print(f'Выдать премию: ')
for i in lst:
    i.show()# можно записать Employee.show(i)





