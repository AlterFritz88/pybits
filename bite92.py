from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if type(date) != datetime or date > NOW:
        raise ValueError
    time_in_sec = (NOW - date).days * DAY + (NOW - date).seconds
    for time in TIME_OFFSETS:
        if time_in_sec < time.offset:
            if time.divider == None:
                return time.date_str.format(time_in_sec)
            else:
                return time.date_str.format(time_in_sec//time.divider)
    return date.strftime('%m/%d/%y')


print(pretty_date((NOW - timedelta(seconds=15))))