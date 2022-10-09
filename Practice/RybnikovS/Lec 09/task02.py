import datetime as dt


def work_days(start_day, end_day):
    date_format = "%d.%m.%Y"
    start = dt.datetime.strptime(start_day, date_format)
    end = dt.datetime.strptime(end_day, date_format)
    count = 0
    while start < end:
        if start.isoweekday() < 6:
            count += 1
        start += dt.timedelta(days=1)
    return count


print(work_days("03.10.2022", "10.10.2022"))
