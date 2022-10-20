# Написать функцию для подсчета количества рабочих дней между двумя датами (даты передаются в качестве параметров).

import datetime as dt


def work_days(d1, d2):
    d1_new = dt.datetime.strptime(d1, "%Y.%m.%d")
    d2_new = dt.datetime.strptime(d2, "%Y.%m.%d")
    count = 0
    while d1_new < d2_new:
        if d1_new.isoweekday() < 6:
            count += 1
        d1_new += dt.timedelta(days=1)
    return count


print(work_days("2022.10.14", "2022.10.20"))





