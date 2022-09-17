x = "A"
y = "a"
print(ord(x))
print(ord("B"))
print(ord(y))
print(x > y)


s = "abc.def"
res = s.split(".") # разделитель строке, в этом случае деление идет по точке
print(res)


import random


s = "БВГД"
i = random.choice(s)# функция random внутри себя вызывает randint от 0 до длины
# строки и возврашает рез-т s[random.randint(0, len(s))]
#choice приминима к любым последовательностям
print(i)


s1 = "ЯАЕО"
s2 = "БВГД"
i = random.choice(s1) + random.choice(s2) + random.choice(s1) + random.choice(s2)
print(i)


s1 = "Hello"
s1 += "World" # в этом случае идет сложение строк s1 + "World" - это работает только со словами

print(s1)