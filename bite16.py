from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    date_now = PYBITES_BORN
    i = 0
    born = PYBITES_BORN
    while date_now.year != 2020:
        date_now += timedelta(days=1)
        i += 1
        if i == 100:
            i = 0
            yield date_now
        if (date_now.month, date_now.day) == (PYBITES_BORN.month, PYBITES_BORN.day):
            yield date_now

a = gen_special_pybites_dates()
dates = list(islice(a, 100))


print(dates)