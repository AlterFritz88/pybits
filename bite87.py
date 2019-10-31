def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    nums = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
            }
    if type(decimal_number) != int or decimal_number < 0 or decimal_number >= 4000:
        raise ValueError
    ans = ''
    while decimal_number > 0:
        stop = 0
        for n, k in enumerate(nums.keys()):
            if decimal_number - k < 0:
                ans += nums[list(nums.keys())[n-1]]
                decimal_number -= list(nums.keys())[n-1]
                stop = 1
                break


        if n == 12 and stop == 0:
            ans += 'M'
            decimal_number -= 1000

    return ans

print(romanize(3500))