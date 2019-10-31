from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        for i in args:
            if type(i) != int:
                raise TypeError
            if i < 0:
                raise ValueError
        return func(*args)
    return wrapper

@int_args
def sum_numbers(*numbers):
    return sum(numbers)


print(sum_numbers(1, 'lolo', 3))