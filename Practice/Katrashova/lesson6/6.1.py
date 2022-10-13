class Tank():
    def __init__(self, name, crew, weight):
        self.name = name
        self.crew = crew
        self.weight = weight

    def show(self):
        print(f"Танк {self.name}  экипажем {self.crew} человек(а), и массой {self.weight}")

    def __lt__(self, other):
        if self.weight > other.weight:
            print(f'У Игрока {self.name} больше шансов')
        elif self.weight == other.weight:
            print('Шансы равны')
        else:
            print(f'У Игрока {self.name} меньше шансов')


player1 = Tank('T-80', 3, 40)
player2 = Tank('T-34', 4, 30)
lst = [player1, player2]
for i in lst:
    i.show()
