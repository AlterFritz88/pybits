from itertools import accumulate
def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sums = enumerate(list(accumulate(sequence)))
    return [round(y/(x+1), 2) for x, y in sums]
print(running_mean([3, 4, 6, 2, 1, 9, 0, 7, 5, 8]))