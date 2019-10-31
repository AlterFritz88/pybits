from functools import wraps



def make_html(argument):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            return '<{0}>{1}</{0}>'.format(argument, function(*args, **kwargs))
        return wrapper
    return real_decorator








@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


print(get_text())