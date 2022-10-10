FILENAME = '1.txt.txt'
#t = ('hello', 'bye', 'good luck')

#f_out = open(FILENAME, 'w')
#for i in t:
#    f_out.write(f'{i}\n')
#f_out.close()

f_in = open(FILENAME, 'r')
#while s := f_in.read(1): # чтение файла посимвольно или
#так
#while True:
#    s = f_in.read(2)
#   if not s:
#       break
# или считать весь файл
s = f_in.read()
print(s)
f_in.close()

# менеджер констпекта позволяет файл закрывать автомат-ки,
# в этом случае на пишем f_in.close()

with open(FILENAME, 'r') as f_in:
    print(f'{f_in.closed=}')
    s = f_in.read()
    print(s)
print(f'{f_in.closed=}')