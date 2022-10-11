class Tank:
    def __init__(self, power, model):
        self.power = power
        self.model = model

class T34(Tank):
    def shoot(self):
        print(self.model, ' - Бах')

class Tiger(Tank):
    def shoot(self):
        print(self.model, ' - Ба-бах')

class Abrams(Tank):
    def shoot(self):
        print(self.model, ' - Ба-ба-бах')

while True:
    t = input('Введите одну из мощностей выстрела: 30 - 80 - 90   ')
    if t.lower() == 'stop':
        print('Выход из программы')
        break
    elif t == '30':
        tnk1 = T34(30, 'T34')
        tnk1.shoot()
    elif t == '80':
        tnk2 = Tiger(80, 'Tiger')
        tnk2.shoot()
    elif t == '90':
        tnk3 = Abrams(90, 'Abrams')
        tnk3.shoot()
