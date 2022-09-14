#помогите, пжл, понять в чем ошибка: при вводе "хватит" на печать выводится ответ (из answers) и "До свидания!". Но ответ выводится не должен. Цикл должен завершаться
import random


request = " "
answers = ("Ты сам-то понял что написал?", "Аргументируй", "И?")
while True:
    if request == "хватит":
        break
    else:
        request = input("Введите запрос: ")
        n = random.choice(answers)
        print(n)
print("До свидания!")



