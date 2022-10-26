predlogenie = 'Вася играл Adagio, когда произведение было написано Andante'
print("The original string is : " + str(predlogenie))

#словарь
dict_muzica = {"Adagio" : "медленно", "Andante" : "спокойно"}

res1 = predlogenie
for e in dict_muzica:
    res1 = res1.replace(e,dict_muzica[e])
print(res1)