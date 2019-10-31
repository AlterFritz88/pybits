from datetime import datetime

BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
die_time = datetime.strptime('2020-04-12 0:0:0', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left():
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth"""
    time_last = die_time - BITE_CREATED_DT
    time_last_days = round((time_last.days * 24 + time_last.seconds / 3600), 2)
    return time_last_days


def py2_miller_min_left():
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller"""
    x_hours = round((py2_earth_hours_left() / (7 * 365 * 24)) * 60, 2)
    return x_hours

py2_earth_hours_left()

py2_miller_min_left()