from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import date, datetime
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = defaultdict(int)


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():

    try:
        time_now = datetime.now()
        violations[get_today()] += 1
        print(violations)
        yield
    finally:
        diff = (datetime.now() - time_now).seconds
        if diff > ALERT_THRESHOLD:
            print(ALERT_MSG)
        co = Counter(violations)
        if co.most_common()[0][1] > ALERT_THRESHOLD:
            print(ALERT_MSG)


with timeit():
    pass
with timeit():
    pass
with timeit():
    pass
with timeit():
    pass