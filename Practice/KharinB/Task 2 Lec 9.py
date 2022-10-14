import datetime as dt


class DataError(Exception):
    pass


def vvod(s, n, d):
    try:
        data = dt.datetime.strptime((input(s) or d), "%d/%m/%Y")
        res = (data, dt.datetime.isoweekday(data))
    except ValueError:
        if n < 3:
            print("Введен некорректный формат даты, введите дату формата: День/Месяц/Год")
            print(f"У Вас осталось {3-n} попыток")
            res = vvod(s, n+1, d)
        else:
            raise DataError
    return res

def calculator_days():
    start = vvod("Введите дату начала отсчёта: ", 0, "10/9/2022")
    a = True
    while a:
        finish = vvod("Введите дату окончания отсчёта: ", 0, "28/10/2022")
        if finish[0] < start[0]:
            print("Введена некорректная дата окончания отсчёта")
            print(f"Дата окончания отсчёта должна быть позже чем: {start[0]}")
            continue
        a = False

    else:
        res = (finish[0] - start[0]).days - (7-start[1]) - finish[1]

        res =  res - res/7*2 + (-1 if start[1]>5 else 5 - start[1]) + (0 if finish[1]>5 else finish[1])
        return int(res)

# В строчке 36 в первом if мы возвращаем остаток рабочей недели, если начало отсчёта пришлось на середину рабочей недели, включая день старта отсчёта
# И возвращаем 0, если начало отсчёта пришлось на выходные (то есть не берём день начала отсчёта).
# Во втором if возвращаем 0, если конец отсчёта пришёлся на выходные
# и возвращаем количество прошедших дней на неделе, если конец отсчета пришёлся на середину рабочей недели
# ВКЛЮЧАЯ день окончания отсчёта.
# По крайней мере именно так считает сайт, которым я регулярно пользуюсь: https://fincalculator.ru/kalkulyator-dnej



print(calculator_days())