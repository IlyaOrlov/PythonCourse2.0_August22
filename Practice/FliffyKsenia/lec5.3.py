predlogenie = 'Вася играл Adagio, когда произведение было написано Andante'
print("The original string is : " + str(predlogenie))

#словарь
dict_muzica = {"Adagio" : "медленно, плавно", "Andante" : "не спеша, спокойно"}

res = " ".join(dict_muzica.get(ele, ele) for ele in predlogenie.replace('.','').replace(',','').split())

print("Replaced Strings : " + str(res))