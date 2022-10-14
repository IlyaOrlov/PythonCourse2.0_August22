#-*- coding: utf-8 -*-
import datetime as dt

def search_days(start, stop):
    start = start.split('.')
    stop = stop.split('.')
    start_day = dt.date(int(start[2]), int(start[1]), int(start[0]))
    stop_day = dt.date(int(stop[2]), int(stop[1]), int(stop[0]))
    day = stop_day - start_day
    work_day = day/7*5
    print(work_day)


search_days("01.01.2020", "01.02.2020")