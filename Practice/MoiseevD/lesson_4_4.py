import random


s = ('Ты сам-то понял, что написал?', 'Аргументируй', 'И?')

while True:
    answers = random.choice(s)
    question = input('Задайте вопрос: ')

    if question.lower() == 'хватит':
        print('---Выход из программы---')
        break
    else:
        print(answers)
