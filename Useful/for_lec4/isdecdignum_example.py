def spam(s):
    for attr in 'isnumeric', 'isdecimal', 'isdigit':
        print(attr, getattr(s, attr)())

spam('5')
spam('³')
spam('½')

