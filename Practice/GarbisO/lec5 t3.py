# заменила mydict[key] на value. Но, как ни странно, код до замены работал
def replace(s, mydict):
    for key, value in mydict.items():
        s = s.replace(str(key), str(value))
    return s


s1 = "Иванов - 2, Петров - 3, Сидоров - 4, Васильев - 5"
mydict1 = {2: "неудовлетворительно", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
print(f"Результаты: {s1})")
print(f"Результаты после замены: {replace(s1, mydict1)}")