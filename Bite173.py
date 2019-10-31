from datetime import datetime, timedelta

import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> datetime:



    delta = _parse_time(delay_time)
    print(delta)
    return task + ' @ ' + str(start_time + delta)




def _parse_time(time_str):
    regex = re.compile(r'((?P<days>\d+?)d)\s((?P<hours>\d+?)h)\s((?P<minutes>\d+?)m)\s((?P<seconds>\d+?)s)?')
    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for (name, param) in parts.items():
        if param:
            time_params[name] = int(param)
    return timedelta(**time_params)

print(add_todo("5d 30m", "Go to Bed"))