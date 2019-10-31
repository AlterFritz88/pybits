def positive_divide(numerator, denominator):

    if type(numerator) not in (int, float):
        raise TypeError
    if type(denominator) not in (int, float):
        raise TypeError


    try:
        res = numerator / denominator
    except ZeroDivisionError:
        return 0

    if res < 0:
        raise ValueError

    return res


print(positive_divide(1,'4'))
