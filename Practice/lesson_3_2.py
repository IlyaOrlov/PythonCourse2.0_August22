def average_speed(way, time):
    return (way/time)


w = int(input('Введите сколько вы проехали км: '))
t = float(input('Введите сколько часов вы затратили в пути: '))
wt = average_speed(w, t)
print(f'Средняя скорость в пути составляет: {wt}')