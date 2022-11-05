import itertools

lst_common = list(itertools.chain([1, 2, 3], [4, 5], [6, 7]))
print(lst_common)

my_lst = list(itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code']))
print(my_lst)

my_combinations = list(itertools.combinations('password', 4))
print(my_combinations)
