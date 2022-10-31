class Iter:

    def __init__(self, text, my_sim):
        self.text = text
        self.my_sim = my_sim

    def __iter__(self):
        return self

    def __next__(self):
        my_str = ' '
        new_str = ''
        while my_str != '':
            my_str = self.text.read(1)
            if my_str == self.my_sim:
                break
            else:
                new_str += my_str

        if new_str != '':
            return new_str
        else:
            raise StopIteration




with open('text.txt', 'r') as f:
    for i in Iter(f, '§'):
        print(i)