import datetime as dt


def work_days(date1, date2):
    date_s = dt.datetime.strptime(date1, '%d.%m.%Y')
    date_e = dt.datetime.strptime(date2, '%d.%m.%Y')
    count = 0
    while date_s < date_e:
        if date_s.isoweekday() < 6:
            count += 1
        date_s += dt.timedelta(days=1)
    return count

print(work_days('01.10.2022', '20.10.2022'))