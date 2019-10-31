from enum import Enum
from datetime import datetime
from collections import Counter


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    # complete this method
    def get_date(date, format):
        new_date = datetime.strptime(date, format.get_d_parse_formats(format.value))
        return '{}-{:02d}-{:02d}'.format(new_date.year, new_date.month, new_date.day)

    list_formats = []
    for date in dates:
        form = _maybe_DateFormats(date)
        for item in form:
            list_formats.append(item)
    most_form = Counter(list_formats).most_common()
    if most_form[0][1] == most_form[1][1] or most_form[0][0] == DateFormat.NONPARSABLE:
        raise InfDateFmtError
    main_form = most_form[0][0]
    ans_dates = []
    for date in dates:
        if main_form in _maybe_DateFormats(date):
            ans_dates.append(get_date(date, main_form))
        else:
            ans_dates.append('Invalid')
    return ans_dates




dates = [
        "04/3/79",
        "08/09/70",
        "08/04/10",
        "95/31/10",
        "06/13/34",
        "04/03/22",
        "67/12/17",
        "34/10/12",
        "04/05/94",
        "07/12/41",
        "88/11/05",
        "96/26/08",
    ]

print(get_dates(dates))