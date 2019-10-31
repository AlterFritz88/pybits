'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('temp', 'log')
#urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    date_time_p = line.split(' ')[1].split('T')
    date = tuple(int(x) for x in date_time_p[0].split('-'))
    time = tuple(int(x) for x in date_time_p[1].split(':'))
    return datetime(date[0], date[1], date[2], time[0], time[1], time[2])

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    first_err = None
    last_err = None
    for log in loglines:
        event = log.split(' ')
        print(event)
        if event[3] == 'Shutdown' and event[4] == 'complete.\n':
            if first_err == None:
                first_err = convert_to_datetime(log)
            else:
                last_err = convert_to_datetime(log)
    return last_err - first_err



#print(convert_to_datetime(6))
print(type(time_between_shutdowns(loglines)))