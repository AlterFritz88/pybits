from datetime import date, timedelta

from dateutil import  parser

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    date_list = []
    now = TODAY
    while len(date_list) < 100:
        if parser.parse(str(now)).strftime("%A") != 'Sunday' and parser.parse(str(now)).strftime("%A") != 'Saturday':
            date_list.append(now)
        now += timedelta(days=1)
    return date_list


print(get_hundred_weekdays())