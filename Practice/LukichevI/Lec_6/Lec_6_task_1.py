class Tank:
    class_tank = ('Легкий танк', 'Средний танк', 'Тяжелый танк')
    @classmethod
    def my_tank(cls):
        cls.my_tank = class_tank



tank = int(input('Выберите тип танка: 0 - Легкий танк 1 - Средний танк 2 - Тяжелый танк: '))

tank1 = Tank()
tank2 = Tank()
tank3 = Tank()

if tank == 0:
    print(f'{tank1.class_tank[0]}: Танк - Врум - врум')
elif tank == 1:
    print(f'{tank2.class_tank[1]}: Танк - бах бах!')
else:
    print(f'{tank3.class_tank[2]}: - Танк БаБаХа!')