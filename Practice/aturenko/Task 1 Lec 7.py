# 1.Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.

class Tanks:
    def __init__(self, name, mass, speed):
        self._name = name
        self._mass = mass
        self._speed = speed
        
    @staticmethod   
    def is_shooting(shoot):
        if shoot == "Bah":
            print("Tank shooting!")
        else:
            print("The tank does not fire")
            
    def showTanks(self):
        print(f"Танк {self._name} имеет массу {self._mass} т и скорость {self._speed} км/ч")
        

tank1 = Tanks("T-90C", 48, 60)
tank2 = Tanks("Abrams M1A2", 69, 70)
tank3 = Tanks("Challenger 2", 62, 56)
tanklist = [tank1, tank2, tank3]
for i in tanklist:
    i.showTanks()
Tanks.is_shooting("Bah")





