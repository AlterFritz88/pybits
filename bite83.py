from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    urs_dt = utc.localize(naive_utc_dt)
    return urs_dt.astimezone(AUSTRALIA), urs_dt.astimezone(SPAIN)

print(what_time_lives_pybites(datetime(2018, 4, 27, 22, 55, 0)))