#Реализовать итератор,
class Fragment:

    def __init__(self, text, sml):
        self.text = text
        self.sml = sml

    def __iter__(self):
        return self

    def __next__(self):
        my_str = ' '
        new_str = ''
        while my_str != '':
            my_str = self.text.read(1)
            if my_str == self.sml:
                break
            else:
                new_str += my_str


        if new_str != '':
            return new_str
        else:
            raise StopIteration

with open('fragment.txt', 'r') as f:
    for i in Fragment(f, '+'):
        print(i)
