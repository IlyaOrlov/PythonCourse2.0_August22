my_txt = open("text.txt", 'r', encoding='utf8')
read_txt = my_txt.read()
my_txt.close()
my_choice = input('Что заменить: 1 - табуляция / 2 - (4 пробела): ')
if my_choice == '1':
    my_txt = open("text.txt", 'w', encoding='utf8')
    my_txt.write(read_txt.replace('\t', '    '))
elif my_choice == '2':
    my_txt = open("text.txt", 'w', encoding='utf8')
    my_txt.write(read_txt.replace('    ', '\t'))
else:
    print('Ошибка. Повторите ввод.')

my_txt.close()

