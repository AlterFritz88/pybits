def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    sums = [((0, 0), (0,0 ))]

    for i, item in enumerate(numbers):
        for j, s_item in enumerate(numbers[i+1:]):
            if item + s_item == target:
                sums.append(((item, s_item), (i, j+i+1)))
    if len(sums) == 1:
        return None
    else:
        sums = sums[1:]
        sums = sorted(sums, key= lambda x: x[0][0])
        return sums[0][1]

numbers = [3, 10, 14, 8, 15, 5, 16, 13, 9, 2]
expected = (2, 6)
target = 30
NUMBERS = [
    2202, 9326, 1034, 4180, 1932, 8118, 7365, 7738, 6220, 3440, 1538, 7994, 465,
    6387, 7091, 9953, 35, 7298, 4364, 3749, 9686, 1675, 5201, 502, 366, 417,
    8871, 151, 6246, 3549, 6916, 476, 8645, 3633, 7175, 8124, 9059, 3819, 5664,
    3783, 3585, 7531, 4748, 353, 6819, 9117, 1639, 3046, 4857, 1981]


print(two_sums(NUMBERS, 11261))