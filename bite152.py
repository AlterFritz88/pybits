from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'




from functools import wraps

def strip_range(start, end):
    def somedec_outer(fn):
        @wraps(fn)
        def somedec_inner(text):
            # do stuff with somearg, someopt, args and kwargs
            new_arg = ''
            for i, char in enumerate(text):
                if i in range(start, end):
                    new_arg += DOT
                else:
                    new_arg += char
            return fn(new_arg)
        return somedec_inner
    return somedec_outer


@strip_range(2, 5)
def gen_output(text):
    return text

print(gen_output(DEFAULT_TEXT))