from string import ascii_lowercase



def binary_search(sequence, target):
    low = 0
    mid = len(sequence) // 2
    max = len(sequence) - 1
    seq_2 = sequence[:]

    while sequence[mid] != target:
        if sequence[mid] > target:
            max = mid
            mid = ((max + low) // 2)
            seq_2 = sequence[low:max]
            if sequence[mid] == target:
                return mid
        if sequence[mid] < target:
            low = mid
            mid = ((max + low) // 2) + 1
            seq_2 = sequence[low:max]
            if sequence[mid] == target:
                return mid
        if len(seq_2) < 2:
            return None


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)



print(binary_search(PRIMES, 1))