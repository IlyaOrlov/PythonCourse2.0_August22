s = 'My card CVV is 111'
key = 555

lst = list(s) #форм-м список
print(lst)
lst = [ord(x) for x in lst]# форм-м список чисел из строки символов, ord(x) фун-я кот-я позволяет получить номер символа в табл аскен
print(lst)
code_lst = [x ^ key for x in lst]# затем к кажд числу применяем операцию искл
print(code_lst)
code_s = '.'.join([str(x) for x in code_lst])
print(code_s)
with open('1.txt.txt', 'w') as f:
    f.write(code_s)