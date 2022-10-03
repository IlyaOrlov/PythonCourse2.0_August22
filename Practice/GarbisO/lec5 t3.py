# изменила имя переменных dict и dict1
def replace(s, mydict):
    for key in mydict:
        s = s.replace(str(key), str(mydict[key]))
    return s


s1 = "Иванов - 2, Петров - 3, Сидоров - 4, Васильев - 5"
mydict1 = {2: "неудовлетворительно", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
print(f"Результаты: {s1})")
print(f"Результаты после замены: {replace(s1, mydict1)}")