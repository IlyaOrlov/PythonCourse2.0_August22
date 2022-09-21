roster = []

for i in range(1,101):
    if i % 15 == 0:
        roster.append('FizzBizz')
    elif i % 3 == 0:
        roster.append('Fizz')
    elif i % 5 == 0:
         roster.append('Bizz')
    else:
        roster.append(i)
print(roster)