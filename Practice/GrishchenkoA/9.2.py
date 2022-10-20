# #-*- coding: utf-8 -*-
import datetime as dt

def search_days(start, stop):

    day = (start + dt.timedelta(x) for x in range((stop - start).days + 1))
    work_day = sum(1 for day in day if day.weekday() < 5)
    print(work_day)

start_day = dt.date(2020,1,1)
stop_day = dt.date(2020,2,1)

search_days(start_day, stop_day)





