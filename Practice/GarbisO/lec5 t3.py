def replace(s,dict):
    for key in dict:
        s = s.replace(str(key), str(dict[key]))
    return s


s1 = "Иванов - 2, Петров - 3, Сидоров - 4, Васильев - 5"
dict1 = {2: "неудовлетворительно", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
print(f"Результаты: {s1})")
res = replace(s1,dict1)
print(f"Результаты после замены: {res}")