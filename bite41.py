known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    pass


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    pass