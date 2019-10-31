def sum_numbers(numbers=None):
    if numbers == None:
        return sum(range(100))
    else:
        return sum(numbers)


print(sum_numbers(None))