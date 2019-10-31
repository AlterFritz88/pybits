import itertools

def find_number_pairs(numbers, N=10):
    return [i for i in itertools.combinations(numbers, 2) if sum(i)==N]

print(find_number_pairs([2, 3, 5, 4, 6], 10))