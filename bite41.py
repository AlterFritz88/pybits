known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    def wrapper(arg):
        '''Return a welcome message if logged in'''
        user = arg
        if user not in known_users:
            return f'please create an account'
        if user in known_users and user not in loggedin_users:
            return f'please login'
        if user in loggedin_users:
            return func(arg)

    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'

print(welcome('sue'))
print(welcome.__doc__)