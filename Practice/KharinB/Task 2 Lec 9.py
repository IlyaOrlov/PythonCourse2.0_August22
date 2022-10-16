import datetime as dt

class DataError(Exception):
    pass

def vvod(s, n, d):
    try:
        data = dt.datetime.strptime((input(s) or d), "%d/%m/%Y")
        day = dt.datetime.isoweekday(data)
        res = (data, day)
    except ValueError:
        if n < 3:
            print("Введен некорректный формат даты, введите дату формата: День/Месяц/Год")
            print(f"У Вас осталось {3-n} попыток")
            res = vvod(s, n+1, d)
        else:
            raise DataError
    return res

def calculator_days(s = "18/9/2022", f = "22/10/2022" ):
    a = True
    start = vvod("Введите дату начала отсчёта(День/Месяц/Год): ", 0, s)
    while a:
        finish = vvod("Введите дату окончания отсчёта(День/Месяц/Год): ", 0, f)
        if finish[0] < start[0]:
            print("Введена некорректная дата окончания отсчёта")
            print(f"Дата окончания отсчёта должна быть позже чем: {start[0]}")
            continue
        a = False

    else:
        start_m = start[0] - dt.timedelta(days=start[1])
        finish_m = finish[0] - dt.timedelta(days=finish[1])
        if start[1]>4:
            if finish[1]>4:
                delta = 0
            else:
                delta = finish[1]-5
        else:
            delta = finish[1]-start[1]
        if start_m == finish_m:
            res = finish[1] - start[1]
        else:
            res = ((finish_m - start_m) - (finish_m - start_m)/7*2).days - delta
        return res

# По крайней мере именно так считает сайт, которым я регулярно пользуюсь: https://fincalculator.ru/kalkulyator-dnej


print(calculator_days()) #25
print(calculator_days("19/10/2022", "22/10/2022")) #3
print(calculator_days("16/10/2022", "22/10/2022")) #5
print(calculator_days("16/10/2021", "22/10/2022")) #265
