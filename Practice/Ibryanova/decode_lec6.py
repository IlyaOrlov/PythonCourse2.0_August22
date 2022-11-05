key = 555

with open('1.txt.txt', 'r') as f:
    s = f.read()
    print(s)
    lst = s.split('.')
    print(lst)
    decode_lst = [int(x) ^ key for x in lst]
    print(decode_lst)
    decode_lst = [chr(x) for x in decode_lst]
    print(decode_lst)
    decode_s = ''.join(decode_lst)
    print(decode_s

