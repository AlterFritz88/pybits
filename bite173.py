from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> datetime:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):

    """
    delay_time = delay_time.replace(' ', '')
    regex = re.compile(r'((?P<days>\d+?)d)?((?P<hours>\d+?)h)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)(s|$))?')
    parts = regex.match(delay_time).groupdict()
    delta_time = {k: int(v) if v != None else 0 for k, v in parts.items()}
    delta_time = timedelta(days=delta_time['days'], hours=delta_time['hours'], minutes=delta_time['minutes'], seconds=delta_time['seconds'])
    new_date = start_time + delta_time
    return task + ' @ ' + str(new_date)

print(add_todo("45", "Finish this Test"))