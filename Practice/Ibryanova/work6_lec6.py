# будем выдавать зарплату

class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    #переопределяем наш Employee, как будут выглядеть наши экземпляры
    def __str__(self):# переводит экземпляры в строковое состояние и
        # можно распечатать строку указав в списке lst = [str(emp1), str(emp2), str(emp3)]
        return f'Сотрудник: {self.name} {self.surname} '


    def __repr__(self):# print когда печатает элементы обращается к методу
    # __repr__ - этот метод тоже отвечает за строковое представление
        return f'Сотрудник: {self.name} {self.surname} с з/п {self.salary}'


    def show(self):
        print(f'Сотрудник: {self.name} {self.surname} с з/п {self.salary}')

emp1 = Employee('Petr', 'Petrov', 100000)
emp2 = Employee('Anton', 'Antonov', 150000)
emp3 = Employee('Ivan', 'Ivanov', 120000)
emp4 = Employee('Ivan', 'Antonov', 130000)


#предположим что сотруд-ки есть в неком списке

lst = [emp1, emp2, emp3]
lst.sort(key=lambda x: x.salary)# можем отсортировать сотр-ов, например по з/п
print(lst) # - метод __repr__ сработает
#print([str(i) for i in lst])# метод __str__сработает

# Итог: как правило def __str__(self) чаще используется для вывода на печать,
# в а методе def __repr__(self): пишется чуть более подробная инфо

