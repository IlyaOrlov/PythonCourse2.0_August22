#Написать класс Man, который принимает имя в конструкторе.
# Имеет метод solve_task, который просто выводит "I'm not ready yet".
class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print("I'm not ready yet")

a = Man('Вася')
a.solve_task()
print(a.name)