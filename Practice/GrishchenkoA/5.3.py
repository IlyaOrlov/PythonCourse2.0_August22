str_new = "Петров - 2 , Иванов - 5 , Сидоров - 4"
lst = list(str_new.split())
dict_1 = {2: "неудовлетворительно", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
for y, b in enumerate(lst):
    if b.isdigit():
        b = int(b)
        if b in dict_1:
            lst[y] = dict_1[b]
str_1 = ""
for i in lst:
    print(str_1.join(i), end=" ")



