class Employee:
    attr = 200

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def show_employee(self):
        print(f"My name {self.name}")

