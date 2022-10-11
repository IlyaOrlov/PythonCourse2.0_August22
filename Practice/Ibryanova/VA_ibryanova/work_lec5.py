#фун=я которая будет находить макс символ в строке
def fun(s):
    m = s[0]
    for i in s:
        if i > m:
            m = i
    return m



s = 'BC DGTZP'
res = fun(s)
print(res)