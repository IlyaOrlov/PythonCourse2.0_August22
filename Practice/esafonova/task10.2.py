#Используя структурное сопоставление с шаблонами (match/case),
# написать чат-бота, отвечающего на вопросы «Привет», «Как дела?», «Какая сегодня погода?»
# заготовленными ответами, а на все остальные вопросы – «Вопрос некорректен, попробуйте сформулировать его по-другому».
while True:
    match input('Задайте Ваш вопрос: '):
        case 'Привет':
            print('Привет!')
        case 'Как дела?':
            print('Все ок!')
        case 'Какая сегодня погода?':
            print('Облачно, +9 градусов!')
        case _:
            print('Вопрос некорректен, попробуйте сформулировать его по-другому')
