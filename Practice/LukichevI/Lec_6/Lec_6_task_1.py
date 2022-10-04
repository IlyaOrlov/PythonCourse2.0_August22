class Tank:
    class_tank = ('Легкий танк', 'Средний танк', 'Тяжелый танк')
    def __init__(self, my_tank):
        self.my_tank = self.class_tank[my_tank]

tank = int(input('Выберите тип танка: 0 - Легкий танк 1 - Средний танк 2 - Тяжелый танк: '))

tank1 = Tank(tank)
tank2 = Tank(tank)
tank3 = Tank(tank)

if tank == 0:
    print(f'{tank1.my_tank}: Танк - Врум - врум')
elif tank == 1:
    print(f'{tank2.my_tank}: Танк - бах бах!')
else:
    print(f'{tank3.my_tank}: - Танк БаБаХа!')