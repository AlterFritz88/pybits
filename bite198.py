import datetime


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    dates = reboots.strip().split('\n')
    dates_parsed = []
    for date in dates:
        d = '2019 ' + date.split('~')[1].strip()
        parsed = datetime.datetime.strptime(d, '%Y %a %b %d %H:%M')
        dates_parsed.append(parsed)
    min_dif = (datetime.timedelta(days=0), None)
    for i, date in enumerate(dates_parsed):
        if i > 0:
            if (dates_parsed[i-1] - date).days > min_dif[0].days:
                min_dif = (dates_parsed[i-1] - date, str(dates_parsed[i-1].date()))

    return min_dif[0].days, min_dif[1]

print(calc_max_uptime(MAC1))