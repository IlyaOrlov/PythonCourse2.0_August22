s = 'Правильно поставленная цель уже наполовину достигнута'
d = {'Правильно': 'Right', 'цель': 'goal', 'достигнута': 'achieved'}
print(s)

for i in d:
    s = s.replace(str(i), str(d[i]))
print(s)

