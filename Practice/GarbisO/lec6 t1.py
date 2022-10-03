class Tank:
    def __init__(self, name, speed, range_of_shot):
        self.name = name
        self.speed = speed
        self.range_of_shot = range_of_shot

    def show(self):
        print(f"Танк: {self.name}, скорость движения: {self.speed}, дальность выстрела: {self.range_of_shot}")

Tank1 = Tank("Pantera", "40", "1000")
Tank2 = Tank("Maus", "50", "900")
Tank3 = Tank("Leopard", "60", "1000")
lst = [Tank1, Tank2, Tank3]
print("В Вашем арсенале:")
for i in lst:
    i.show()