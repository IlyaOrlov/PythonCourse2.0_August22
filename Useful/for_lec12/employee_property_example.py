class SalaryException(Exception):
    pass


class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        if isinstance(salary, int) or salary.isdigit():
            self._salary = int(salary)
        else:
            raise SalaryException()

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"{self._name} {self._surname}"

    def say_hello(self):
        print(f"Hello, I'm {self._name}")


class Manager(Employee):
    def __init__(self, name, surname, salary):
        # Employee.__init__(self, name, surname, salary)
        super().__init__(name, surname, salary)
        self.__employees = []

    @property
    def employees(self):
        return self.__employees.copy()

    @employees.setter
    def employees(self, emp):
        if isinstance(emp, Employee):
            self.__employees.append(emp)

    @employees.deleter
    def employees(self):
        self.__employees.clear()

    def say_hello(self):
        print(f"Hello, I'm manager {self._name}")


while True:
    try:
        e = Employee("Ivan", "Ivanov", input("Input salary: "))
    except SalaryException:
        print("Incorrect salary. Try again")
        pass
    except Exception as ex:
        print(ex)
        break
    else:
        break

e2 = Employee("Semen", "Semenov", 3000)
e3 = Employee("Ilya", "Orlov", 3000)
print(e)
m = Manager("Petr", "Petrov", 5000)
m.employees = e
m.employees = e2
m.employees = e3
print(f"Employee name {e.name}")
print(f"Manager name {m.name}")

print(m.employees)
lst = m.employees
lst.append('Timofei Tapkin')
print(m.employees)

del m.employees
print(m.employees)


