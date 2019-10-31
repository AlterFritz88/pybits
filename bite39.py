from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    list_times = []
    with open(COURSE_TIMES, 'r') as f:
        for line in f:
            list_times.append(re.findall(r'\d\d?:\d\d', line))

    list_times = [x[0] for x in list_times if x != []]
    return list_times



def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    deltas = [timedelta(minutes = int(x.split(':')[0]), seconds = int(x.split(':')[1])) for x in timestamps]
    time = timedelta(seconds=0)
    for t in deltas:
        time += t
    return str(time)

print(get_all_timestamps())
print(calc_total_course_duration(get_all_timestamps()))