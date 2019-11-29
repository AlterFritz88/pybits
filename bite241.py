import pytest

from typing import List


def list_to_decimal(nums: List[int]) -> int:
    """Accept a list of positive integers in the range(0, 10)
       and return a integer where each int of the given list represents
       decimal place values from first element to last.  E.g
        [1,7,5] => 175
        [0,3,1,2] => 312
        Place values are 10**n where n represents the digit position
        Eg to calculate 1345, we have 5 1's, 4 10's, 3 100's and 1 1000's
        1,     3  ,  4  , 5
        1000's, 100's, 10's, 1's
    """
    if not all(isinstance(num, int) for num in nums):
        raise TypeError

    if not all(num in range(0, 11) for num in nums):
        raise ValueError

    return int(''.join(map(str, nums)))


def test_type_error():
    with pytest.raises(TypeError) as excinfo:
        answer = list_to_decimal(["1", 1])

def test_value_error():
    with pytest.raises(ValueError) as excinfo:
        list_to_decimal([9, 1, 10, 5])

def test_value_error_1():
    with pytest.raises(ValueError) as excinfo:
        list_to_decimal([9, 1, 123, 5])

def test_float():
    with pytest.raises(TypeError) as excinfo:
        answer = list_to_decimal([11.3, 1, 123, 5])

def test_minus():
    with pytest.raises(ValueError) as excinfo:
        answer = list_to_decimal([-3, 1])

def test_norm():
    assert 145 == list_to_decimal([1, 4, 5])
    assert 105 == list_to_decimal([1, 0, 5])