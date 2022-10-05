import random


s = ('Ты сам-то понял, что написал?', 'Аргументируй', 'И?')

while True:
    question = input('Задайте вопрос: ')

    if question.lower() == 'хватит':
        print('---Выход из программы---')
        break
    else:
        answers = random.choice(s)
        print(answers)
