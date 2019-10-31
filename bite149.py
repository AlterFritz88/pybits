def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    digits = [x for x in words if x[0].isdigit()]
    words = [x for x in words if not x[0].isdigit()]
    words = sorted(words, key=str.lower) + sorted(digits)
    return words

words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()

print(sort_words_case_insensitively(words))