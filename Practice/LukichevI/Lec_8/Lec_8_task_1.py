class MyIter:

    def __init__(self, text, my_simbol):
        self.text = text
        self.my_simbol = my_simbol

    def __iter__(self):
        return self

    def __next__(self):
        my_string = ' '
        my_new_string = ''
        while my_string != '':
            my_string = self.text.read(1)
            if my_string == self.my_simbol:
                break
            else:
                my_new_string += my_string

        if my_new_string != '':
            return my_new_string
        else:
            raise StopIteration




with open('text.txt', 'r', encoding='utf8') as f:
    for i in MyIter(f, '&'):
        print(i)
