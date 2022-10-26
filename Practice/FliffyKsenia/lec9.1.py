import re

find_git = r'(git\ )([a-zA-Z\d\_\/\.\@\:\-\ ]+)+(\".+\")?'  # формируем строку регулярного выражения для поиска команд git
with open('../README.md', 'rt') as file_readme:             # открываем файл в котором надо производить поиск
    for line in file_readme:                                # запускаем цикл для построчного чтения
        res = re.findall(find_git, line)                    # применяем регулярное выражение и ищем все совпадения
        for r in res:                                       # пробегаемся по регультату работы модуля ре
            print(''.join(r))                               # объединяем группы в единую строку для вывода.
