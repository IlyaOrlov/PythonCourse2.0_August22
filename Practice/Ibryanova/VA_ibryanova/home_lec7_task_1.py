class Tanks:

    def __init__(self, classes, pluses):
        #print(self)
        self.classes = classes
        self.pluses = pluses


player1 = Tanks('Тяжелый танк', 'мощная броня')
#print(player1.__dict__)

player2 = Tanks('Средний танк', 'роль авангарда')
#print(player2.__dict__)

player3 = Tanks('Легкий танк', 'высокая скорость')
#print(player3.__dict__)

player4 = Tanks('ПТ-САУ', 'высокий урон')
#print(player4.__dict__)

player5 = Tanks('САУ', 'огромная дальность стрельбы')
#print(player5.__dict__)

lst = [player1, player2, player3, player4, player5]
for i in lst:
    print(f'Краткое описание: {i.classes} {i.pluses}')