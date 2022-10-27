#-*- coding: utf-8 -*-
import random

hello = ["Привет!", "Здравствуйте!", "Добрый день!"]
mood = ["Хорошо!", "Так себе", "Что-то не очень хорошо"]
weather = ["Сегодня ветренно", "Сегодня солнечно", "Дождь"]

while True:
    match input('Что Вы хотели спросить: '):
        case "Привет":
            print(random.choice(hello))
        case "Как дела?":
            print(random.choice(mood))
        case "Какая сегодня погода":
            print(random.choice(weather))
        case _:
            print("Вопрос некорректен, попробуйте сформулировать его по-другому")
