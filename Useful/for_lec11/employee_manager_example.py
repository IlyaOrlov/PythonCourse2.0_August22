class Employee:  # _ protected, __ private
    class_name = "Сотрудник"

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
        print(f"{self.class_name} {self.__name} {self.__surname} с з/п {self._salary}")


class Manager(Employee):
    class_name = "Менеджер"

    def __init__(self, name, surname, salary):
        super().__init__(name, surname, salary)
        self._employees = []

    def add_employee(self, emp):
        self._employees.append(emp)


lst = [Employee("Ivan", "Ivanov", 100000), Employee("Ivan", "Petrov", 100000), Manager("Petr", "Petrov", 120000)]

for i in lst:
    i.show()



