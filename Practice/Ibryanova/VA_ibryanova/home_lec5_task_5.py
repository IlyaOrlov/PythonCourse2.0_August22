FILENAME = 'my_text.txt'
#t = 'Не  бойся,  что не  получится. Бойся,    что    не    попробуешь!'

f_out = open(FILENAME, 'r')
s = f_out.read()
x = input('Меняем: 1 - символы табуляции на пробелы или  2 - пробелы на символ табуляции, Ваш выбор: ')
print(x)
f_out.close()

f_out = open(FILENAME, 'w')
if x == '1':
    #f_out = open(FILENAME, 'w')
    f_out.write(s.replace('\t', '    '))
    f_out.close()
else:
    #f_out = open(FILENAME, 'w')
    f_out.write(s.replace('    ', '\t'))
    f_out.close()



