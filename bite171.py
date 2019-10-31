from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    time_start = time()
    for n in cycle(SPINNER_STATES):
        if time() >= time_start + seconds:
            break
        print(n+'\r', end='')

        sleep(STATE_TRANSITION_TIME)
        sys.stdout.flush()
        #delete_last_lines()



if __name__ == '__main__':
    spinner(2)