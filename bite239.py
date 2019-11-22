def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

import pytest

def test_fizz_buzz():
    assert 'Fizz Buzz' == fizzbuzz(15)

def test_fizz():
    assert 'Fizz' == fizzbuzz(9)

def test_buzz():
    assert 'Buzz' == fizzbuzz(10)

def test_num():
    assert 8 == fizzbuzz(8)

@pytest.mark.parametrize("arg, ret", [
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16),
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret