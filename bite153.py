import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        return [math.ceil(x) for x in transactions]
    else:
        return [math.floor(x) for x in transactions]

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
print(round_up_or_down(transactions1, False))