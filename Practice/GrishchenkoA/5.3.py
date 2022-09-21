str = "Петров - 2 , Иванов - 5 , Сидоров - 4"
lst = list(str.split())
dict_1 = {2: "неудовлетворительно", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
for y, b in enumerate(lst):
    for i, d in enumerate(dict_1):
        if b.isdigit():
            if int(b) == d:
                lst[y] = dict_1[d]
str_1 = ""
for i in lst:
    print(str_1.join(i), end=" ")



