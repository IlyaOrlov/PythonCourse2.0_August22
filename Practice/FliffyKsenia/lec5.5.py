import os.path

filename_in = '\/'
vybor = ''
variant_vybora = ["0", "1"]
tabs = '\t'
probel = '    '

while not os.path.exists(filename_in):
    filename_in = input("Введите имя файла: ")

while not (vybor in variant_vybora):
    vybor = input(
        "Введите необходимую операцию: если необходимо выполнить замену табуляции (tab) четырмя пробелом, введите 0. Если необходимо заменить 4 пробела табуляцией (tab), введите 1: ")

# filename_in = "/media/data/python_ucheba/python_ucheba/project/PythonCourse2.0_August22/Practice/FliffyKsenia/in.txt"
filename_out = filename_in + '_temp'

if vybor == '0':
    old_str = tabs
    new_str = probel
else:
    old_str = probel
    new_str = tabs

with open(filename_in) as file_in, open(filename_out, 'w') as file_out:
    for line in file_in:
        file_out.write(line.replace(old_str, new_str))

os.rename(filename_out, filename_in)
