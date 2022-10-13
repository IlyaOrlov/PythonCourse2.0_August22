class MyIterator:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol

    def __iter__(self):
        return self

    def __next__(self):
        my_str = " "
        new_str = ""
        while my_str != "":
            my_str = self.text.read(1)
            if my_str == self.symbol:
                break
            else:
                new_str += my_str

        if new_str != '':
            return new_str
        else:
            raise StopIteration


with open("paragraph.txt", 'r', encoding="utf8") as f:
    for i in MyIterator(f, '$'):
        print(i)
