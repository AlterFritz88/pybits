import calendar
from datetime import date

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    days_dict = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday0',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return days_dict[calendar.weekday(date.year, date.month, date.day)]

dt = date(1974, 11, 11)
print(weekday_of_birth_date(dt))