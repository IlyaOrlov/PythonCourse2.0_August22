otvety = ['Ты сам-то понял, что написал? ', 'Аргументируй ', 'И? ']
# запрашиваем у пользователя ввод данных
fraza = input("Введите вопрос: ")
ind = 0 - 1
while fraza.upper() != "ХВАТИТ":
        ind = ind + 1
        fraza = input(f"{otvety[ind%3]}")