class Employee:
    company = "Yandex"

    def __init__(self, n, s, salary):
        self.name = n
        self.surname = s
        self.salary = salary

    def set_salary(self, value):
        self.salary = value

    def set_company(self, new_company):
        self.company = new_company

    def show_info(self):
        print(f"{self.name} {self.surname} at {self.company}")

    @classmethod
    def say_hello(cls):
        print(f"Hello from {cls.__name__}s")

    @staticmethod
    def information():
        print('Данный класс позволяет узнать зарплату работников')


class SuperEmployee(Employee):
    pass


e1 = SuperEmployee("Ivan", "Ivanov", 100000)
e1.say_hello()
e2 = Employee("Petr", "Petrov", 50000)
e2.say_hello()

print(e1.__dict__)
print(Employee.__dict__)
