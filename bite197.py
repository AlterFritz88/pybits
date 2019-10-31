from datetime import date


import calendar
def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    Cal = calendar.Calendar()
    line = Cal.itermonthdates(year, 5)
    sundays = 0
    for l in line:
        if calendar.weekday(l.year, l.month, l.day) == 6:
            sundays += 1
        if sundays == 2:
            return l


print(get_mothers_day_date(2017))