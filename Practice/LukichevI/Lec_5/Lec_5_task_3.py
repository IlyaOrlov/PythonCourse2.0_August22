my_string = 'Иван родил дитенка велел тащить пеленки'
my_string = my_string.split()
my_dict = {'родил': 'купил', 'дитенка': 'самогонки', 'пеленки': 'закуски'}
for i in range(len(my_string)):
    if my_string[i] in my_dict:
        my_string[i] = my_dict[my_string[i]]
my_string = ' '.join(my_string)
print(my_string)
