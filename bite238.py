def fib(n):
   if n < 0:
        raise ValueError
   elif n in (0, 1):
       return n
   else:
       return (fib(n - 1) + fib(n - 2))


#print(fib(16))

import pytest

def test_under_zero():
    with pytest.raises(ValueError) as excinfo:
        fib(-1)

def test_one():
    assert 1 == fib(1)

def test_zero():
    assert 0 == fib(0)

def test_4():
    assert 3 == fib(4)

# @pytest.mark.parametrize("test_input, expected", [(4, 3), (5, 5), (6, 8), (9, 34), (12, 144), (21, 10946)])
# def test_eval(test_input, expected):
#     print(test_input)
#     assert 1 == 2
#     assert fib(test_input) == expected
#     assert fib(test_input) != 0
#
# @pytest.mark.parametrize("test_input,expected", [(4, 3), (5, 5), (6, 8), (9, 34), (12, 144)])
# def test_eval(test_input, expected):
#     assert type(fib(test_input)) == int


