class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary

    # метод для чтения - гЕтер
    def get_salary(self):
        return self.salary

    # метод управляющий изменением атри-в - сЕтер
    def set_salary(self, new_salary):
        if type(new_salary) is int:
            self.salary = new_salary
        else:
            print('Incorrect salary')


    def show(self):
        print(f'Сотрудник: {self.name} {self.surname} с з/п {self.salary}')


e1 = Employee('Anton', 'Antonov', 130000)
e2 = Employee('Ivan', 'Antonov', 150000)
e1.show()
e2.show()
print(e1 < e2)
print('=================')
# з/п одного сотр-ка
e1.set_salary(e1.salary + 20000)# вместо e1.salary += 20000
#e1.salary += 20000
e1.set_salary(e1.get_salary() + 20000)
e2.set_salary('100000')# вместо e2.salary = '100000'
#e2.salary = '100000'# спец-но укажет строку, чтобы избежать
# некотрол-е изменение атрибутов экземпляров испол-т инкапсуляцию,
# для этого делают апрет на прямой доступ к salary с помощью метода def set и
# можно закрвыть доступ для чтения с помощью метода def get
e1.show()
e2.show()
print(e1 < e2)
