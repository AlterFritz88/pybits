from itertools import islice


from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    now_date = PYBITES_BORN
    days_100 = 0
    while 1:
        now_date += timedelta(days=1)
        days_100 += 1
        if days_100 == 100:
            days_100 = 0
            yield now_date
        if now_date.month == 12 and now_date.day == 19:
            yield now_date

gen = gen_special_pybites_dates()
dates = list(islice(gen, 100))

print(dates[:10])