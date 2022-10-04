class C:
    def __init__(self, attr):
        self._attr1 = attr


class A(C):
    def __init__(self, attr1, attr2):
        super().__init__(attr1)
        self._attr2 = attr2


class B(C):
    def __init__(self, attr):
        super().__init__(attr)
