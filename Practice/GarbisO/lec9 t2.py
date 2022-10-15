from datetime import date, timedelta


def work_days(d_start, d_end):
    days_sum = (d_start + timedelta(x + 1) for x in range((d_end - d_start).days))
    return sum(1 for day in days_sum if day.weekday() < 5)

d_start1 = date(2022, 10, 17)
d_end1 = date(2022, 12, 31)
res = work_days(d_start1, d_end1)
print(res)

