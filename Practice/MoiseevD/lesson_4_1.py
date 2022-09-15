i = 0
while i < 100:
    i += 1
    if i % 15 == 0:
        print('FizzBizz')
    elif i % 5 == 0:
        print('Bizz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)