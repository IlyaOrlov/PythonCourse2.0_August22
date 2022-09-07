import  random


s = input('Введиде слово: ')
if s.find('А') != -1 or s.find('а') != -1:
    rep_A = s.replace('А', '*')
    result_rep_Aa = rep_A.replace('а', '*')
    print(f'В слове "{s}" буквы "А" и "а" будут заменены на "*"')
    print(f'Результат: "{result_rep_Aa}"')
else:
    print(f'В слове "{s}" нет букв "А" или "а"')
