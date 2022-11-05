class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'User: name={}, age={}'.format(self.name, self.age)
