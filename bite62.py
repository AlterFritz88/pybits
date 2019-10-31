from functools import wraps
from time import time
from typing import List, Set
from string import ascii_lowercase


def timing(f):
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper


@timing
def contains(sequence: List[int], num: int) -> bool:
    for n in sequence:
        if n == num:
            return True
    return False


@timing
def contains_fast(sequence: Set[int], num: int) -> bool:
    return num in sequence


@timing
def ordered_list_max(sequence: List[int]) -> int:
    return max(sequence)


@timing
def ordered_list_max_fast(sequence: List[int]) -> int:
    return sequence[-1]


@timing
def list_concat(sequence: List[str]) -> str:
    bigstr = ''
    for i in sequence:
        bigstr += str(i)
    return bigstr


@timing
def list_concat_fast(sequence: List[str]) -> str:
    return ''.join(sequence)


@timing
def list_inserts(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst


@timing
def list_inserts_fast(n: int) -> List[int]:
    return [x for x in range(n-1, -1, -1)]


@timing
def list_creation(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@timing
def list_creation_fast(n: int) -> List[int]:
    return [x for x in range(n)]



# testst

alist = list(range(1000000))
aset = set(alist)
listofstrings = list(ascii_lowercase) * 1000
t1, res1 = ordered_list_max(alist)
t2, res2 = ordered_list_max_fast(alist)

assert res1 == res2
assert t1 > t2

t1, res1 = list_concat(listofstrings)
t2, res2 = list_concat_fast(listofstrings)

assert res1 == res2
assert t1 > t2

t1, res1 = list_inserts(10000)
t2, res2 = list_inserts_fast(10000)
print(res1)
print(res2)
assert list(res1) == list(res2)
assert t1 > t2

t1, res1 = list_creation(10000)
t2, res2 = list_creation_fast(10000)
assert list(res1) == list(res2)
assert t1 > t2