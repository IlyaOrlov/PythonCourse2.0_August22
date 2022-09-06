import  random


s = str(input('Введиде слово: '))
b = s.find('А')
c = s.find('а')
rep_A = s.replace('А', '*')
result_rep_Aa = rep_A.replace('а', '*')
if b != -1 or c != -1:
    print(f'В слове "{s}" буквы "А" и "а" будут заменены на "*"')
    print(f'Результат: "{result_rep_Aa}"')
else:
    print(f'В слове "{s}" нет букв "А" и "а"')
