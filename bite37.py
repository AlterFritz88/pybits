def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    i = start
    if i == 0:
        print('time is up')
        return 0
    print(i)
    countdown_recursive(i-1)


countdown_recursive(10)