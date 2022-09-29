class Tank:
    def __init__(self, power):
        self._power = power

    def __add__(self, other):
        if isinstance(other, int):
            self._power += other
            return self
        else:
            return Tank(self._power + other._power)

    def __radd__(self, other):
        if isinstance(other, int):
            self._power += other
            return self

    def __repr__(self):
        return f"Tank(power: {self._power}) at {id(self)}"

    def __str__(self):
        return f"Tank(power: {self._power})"


t1 = Tank(10)
t2 = Tank(100)
t3 = 1000 + t1
print(t3)
