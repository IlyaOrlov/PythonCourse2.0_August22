my_string = 'Иван родил дитенка велел тащить пеленки'
my_string = my_string.split()
my_dict = {'родил': 'купил', 'дитенка': 'самогонки', 'пеленки': 'закуски'}
for i in range(len(my_string)):
    word = my_string[i]
    for a in my_dict:
        if a == word:
            my_string[i] = my_dict[a]
my_string = ' '.join(my_string)
print(my_string)
