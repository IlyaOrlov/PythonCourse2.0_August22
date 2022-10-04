import itertools

def sum_lst(*args):
    return list(itertools.chain(*args))

def filtr_len(s):
    return len(s)<5

def filtr(lst):
    return list(itertools.filterfalse(filtr_len, lst))

def comb(s):
    return list(itertools.combinations(s, 4))

print(sum_lst([1, 2, 3], [4, 5], [6, 7]))
print(filtr(['hello', 'i', 'write', 'cool', 'code']))
print(comb("password"))
print("==============")

#Моя реализация.
def my_sum_lst(*args):
    args = list(args)
    while len(args)>1:
        args[0] += args.pop(1)
    return args[0]

def my_filtr(lst):
    res = []
    for i in lst:
        if len(i)>4:
            res.append(i)
    return res


def my_comb(s):
    s = list(s)
    res = []
    for i in range(len(s)):
        s2 = s[i::]
        a = s2.pop(0)
        for j in range(len(s2)):
            s3 = s2[j::]
            b = s3.pop(0)
            for l in range(len(s3)):
                s4 = s3[l::]
                c = s4.pop(0)
                for p in range(len(s4)):
                    res.append((a, b, c, s4[p]))
    return res




print(my_sum_lst([1, 2, 3], [4, 5], [6, 7]))
print(my_filtr(['hello', 'i', 'write', 'cool', 'code']))
print(my_comb("password"))
print(comb("password") == my_comb("password"))