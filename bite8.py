from collections import deque

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string_deq = deque(string)
    #n = n + 1 if n>0 else n - 1
    string_deq.rotate(-n)
    string = ''.join(string_deq)
    return string

print(rotate('hallo', 2))

