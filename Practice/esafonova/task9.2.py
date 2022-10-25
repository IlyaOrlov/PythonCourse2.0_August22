# Написать функцию для подсчета количества рабочих дней между двумя датами (даты передаются в качестве параметров).
import datetime as dt

def time_count(d_start, d_finish):
    time_gen = (d_start + dt.timedelta(i) for i in range((d_finish - d_start).days + 1))
    res = sum(1 for j in time_gen if j.weekday() < 5)
    print(res)

a = dt.date(2022,10,7)
b = dt.date(2022,10,10)
example = time_count(a, b)


# без учета рабочих дней
# def time_count(d_start, d_finish):
#     d_start = d_start.split('-')
#     d_finish = d_finish.split('-')
#     d_start_r = dt.date(int(d_start[0]), int(d_start[1]), int(d_start[2]))
#     d_finish_r = dt.date(int(d_finish[0]), int(d_finish[1]), int(d_finish[2]))
#     res = d_start_r - d_finish_r
#     print(res)
#
# example = time_count('2022-10-17', '1993-12-12')
