class Human:
    def __init__(self):
        self._children = []

    @property
    def children(self):
        return self._children.copy()

    @children.setter
    def children(self, child):
        if type(child) is list:
            self._children = child
        else:
            self._children.append(child)


m = Human()
try:
    m.children = "Ivan"
    m.children = "Petr"

    w = Human()
    w.children = m.children

    print(m.children)
    print(w.children)

    m.children = "Sergey"

    print(m.children)
    print(w.children)
except HumanError:
    print("Бывает")