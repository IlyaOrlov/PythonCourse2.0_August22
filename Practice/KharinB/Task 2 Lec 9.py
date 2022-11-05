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

def calculator_days(s="18/9/2022", f="22/10/2022" ):
    a = True
    start_date, start_day = vvod("Введите дату начала отсчёта(День/Месяц/Год): ", 0, s)
    while a:
        finish_date, finish_day = vvod("Введите дату окончания отсчёта(День/Месяц/Год): ", 0, f)
        if finish_date < start_date:
            print("Введена некорректная дата окончания отсчёта")
            print(f"Дата окончания отсчёта должна быть позже чем: {start_date}")
            continue
        a = False

    else:
        return calculation(start_date, start_day, finish_date, finish_day)


def calculation(start_date, start_day, finish_date, finish_day):
        start_monday = start_date - dt.timedelta(days=start_day)
        finish_monday = finish_date - dt.timedelta(days=finish_day)
        if start_day > 4:
            if finish_day > 4:
                delta = 0
            else:
                delta = finish_day-5
        else:
            delta = finish_day-start_day
        if start_monday == finish_monday:
            res = finish_day - start_day
        else:
            res = ((finish_monday - start_monday) - (finish_monday - start_monday)/7*2).days - delta
        return res

# По крайней мере именно так считает сайт, которым я регулярно пользуюсь: https://fincalculator.ru/kalkulyator-dnej


print(calculator_days()) #25
print(calculator_days("19/10/2022", "22/10/2022")) #3
print(calculator_days("16/10/2022", "22/10/2022")) #5
print(calculator_days("16/10/2021", "22/10/2022")) #265
