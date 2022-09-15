import random


while True:
    question = input('Задайте вопрос: ')
    s = ('Ты сам-то понял, что написал?', 'Аргументируй', 'И?')
    answers = random.choice(s)
    print(answers)

    if question.lower() == 'хватит':
        print('Выход из программы')
        break
