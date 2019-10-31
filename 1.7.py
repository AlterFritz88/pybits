
a = [-1, -3, 4, 2, 5, 7, 1, 77, -54]

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return [x for x in numbers if x%2 == 0 and x > 0]


filter_positive_even_numbers(a)