class Tank:
    Model = 'Tank'
    def __init__(self, power):
        self.power = power


class T34(Tank):
    tank_model = 'T34'
    def shoot(self):
        print(self.tank_model, ' - Бах')


class Tiger(Tank):
    tank_model = 'Tiger'
    def shoot(self):
        print(self.tank_model, ' - Ба-бах')


class Abrams(Tank):
    tank_model = 'Abrams'
    def shoot(self):
        print(self.tank_model, ' - Ба-ба-бах')


while True:
    t = input('Введите одну из мощностей выстрела: 30 - 80 - 90   ')
    if t.lower() == 'stop':
        print('Выход из программы')
        break
    elif t == '30':
        tnk1 = T34(30)
        tnk1.shoot()
    elif t == '80':
        tnk2 = Tiger(80)
        tnk2.shoot()
    elif t == '90':
        tnk3 = Abrams(90)
        tnk3.shoot()

