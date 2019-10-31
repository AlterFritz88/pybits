import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    for i in timezones:
        if i not in list(TIMEZONES):
            raise ValueError
    urs_dt = pytz.utc.localize(utc)
    local_time = [urs_dt.astimezone(pytz.timezone(x)).hour for x in timezones]
    true_no = [x in MEETING_HOURS for x in local_time]
    if False in true_no:
        return False
    else:
        return True

dt = datetime(2018, 4, 18, 13, 28)
timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

print(within_schedule(dt, *timezones))