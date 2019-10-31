def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    dates = calendar_output.split('\n')[2:]
    days_dict = {
        0: 'Su',
        1: 'Mo',
        2: 'Tu',
        3: 'We',
        4: 'Th',
        5: 'Fr',
        6: 'Sa'
    }
    date_dict = {}
    for line in dates:
        line_date = [line[i:i+3] for i in range(0, len(line), 3)]

        for i, date in enumerate(line_date):

            try:

                date_dict[int(date)] = days_dict[i]
            except:
                continue
    return date_dict



april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

month = get_weekdays(jan_1986)
print(month[16])