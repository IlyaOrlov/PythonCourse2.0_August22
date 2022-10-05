class OldEmployee:
    def __init__(self, age):
        self._age = age

class Employee:  # _ protected, __ private
    def __init__(self, name, surname, salary):
        self.__name = name  # _Employee__name
        self.__surname = surname
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if type(new_salary) is int:
            self._salary = new_salary
        else:
            print("Incorrect salary")

    def show(self):
        print(f"Сотрудник {self.__name} {self.__surname} с з/п {self._salary}")


e1 = Employee("Ivan", "Ivanov", 100000)
print(e1.__dict__)
# print(e1.__name)
# print(e1.__salary)


class Manager(Employee, OldEmployee):
    def __init__(self, name, surname, salary, age):
        super().__init__(name, surname, salary)  # Employee.__init__(self, name, surname, salary)
        super(Employee, self).__init__(age)
        self._employees = []

    def show(self):
        print(f"Менеджер {self.__name} {self.__surname} с з/п {self._salary}")

    def add_employee(self, emp):
        self._employees.append(emp)


m = Manager("Petr", "Petrov", 120000, 30)
print(m._age)

