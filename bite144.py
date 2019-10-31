from datetime import date

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def calc_months_passed(year, month, day):
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    if type(year) != int or type(month) != int or type(day) != int:
        raise ValueError
    try:
        end_date = date(year, month, day)
    except:
        raise ValueError
    if end_date < START_DATE:
        raise ValueError

    delta = relativedelta(end_date, START_DATE)
    extra_month = 1 if delta.days >= 10 else 0
    months = delta.years*MONTHS_PER_YEAR + delta.months + extra_month
    return months

print(calc_months_passed('a', 12, 11))