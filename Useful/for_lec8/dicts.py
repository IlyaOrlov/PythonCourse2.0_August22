b = {'one': [1, 1], 'two': 1, 'three': 1}
for key, value in b.items():
   print(f"{key=}, {value=}")
print(b.keys())

d = dict(b)

b['one'][0] = 100500

print(f"{b=}")
print(f"{d=}")
