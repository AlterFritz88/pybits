from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = []
    for i, line in enumerate(data.split('\n')):
        if i in (0, 1, 2, 3, len(data.split('\n'))-1, len(data.split('\n'))-2):
            continue
        dates.append(datetime.strptime(line.strip().split('|')[1].strip(), '%Y-%m-%d').date())
    return sorted(set(dates))


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """

    streak = 0
    for i, date in enumerate(dates):
        if i == 0:
            continue
        if dates[i-1] + timedelta(days=1) == date:
            streak += 1
        if streak > 0 and dates[i-1] + timedelta(days=1) != date:
            streak = 0
    if dates[-1] != TODAY and dates[-1] + timedelta(days=1) != TODAY:
        streak = 0
    if TODAY == dates[-1] + timedelta(days=1):
        streak += 1
    if TODAY == dates[-1]:
        streak += 1

    return streak



data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-08 | pcc        | 1       |
    +------------+------------+---------+
    """

dates = extract_dates(data)
print(calculate_streak(dates))