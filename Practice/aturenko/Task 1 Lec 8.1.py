class Man:
    def __init__(self, name):
        self._name = name
        
    def solve_task(self):
        print("I'm not ready yet")
        
myman = Man("Иван")

print(myman._name)
myman.solve_task()