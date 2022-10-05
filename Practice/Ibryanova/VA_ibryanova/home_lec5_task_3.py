s = 'Правильно поставленная цель уже наполовину достигнута'
d = {'Правильно': 'Right', 'цель': 'goal', 'достигнута': 'achieved'}
print(s)

for i, value in d.items():
    s = s.replace(str(i), str(d[i]))
print(s)

