#t = (1, 4, 'hello', 5, [100, 200, 300])
#t[4].pop(0)
#t[4].append(400) # добавили элемент четвертый в список
#print(t)
#print(t[1:4])
import random

t = ('лимон', 'клубничка', 'вишенка', 'банан', '7')
while True:
    s = input('нажмите кнопку (stop для остановки): ')
    if s == "stop":
        break

    print(f'{random.choice(t)}|{random.choice(t)}|{random.choice(t)}')
