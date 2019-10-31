def get_ordinal_suffix(number):
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    if len(str(number)) > 1 and str(number)[-2] == '1':
        return str(number) + 'th'
    if str(number)[-1] == '1':
        return str(number) + 'st'
    if str(number)[-1] == '2':
        return str(number) + 'nd'
    if str(number)[-1] == '3':
        return str(number) + 'rd'
    return str(number) + 'th'

print(get_ordinal_suffix(116))