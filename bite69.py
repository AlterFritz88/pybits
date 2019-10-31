import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    match = re.findall(r'\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d', f'r{text}')
    return True if len(match) > 0 else False


def is_integer(number):
    """Return True if number is an integer"""
    match = re.findall(r'[-]?[0-9]+', f'r{number}')
    return True if len(match) == 1 else False


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    match = re.findall(r'([a-z]+-[a-z]+)|([0-9]+-[0-9]+)', f'r{text}')
    print(match)
    return True if len(match) > 0 else False


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub('\s\((.*?)\)', '', text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    from string import punctuation
    r = re.compile(r'[{}]\s?'.format(re.escape(punctuation)))
    ans = [x for x in r.split(text) if x != '']
    return ans


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(' +', ' ', text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    voewels = 'aeuio'
    counter = 0
    for char in word:
        if char in voewels:
            counter += 1
    return True if counter > 2 else False


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    if '/' not in date:
        return date
    new_date = date.split('/')
    return '/'.join([new_date[1], new_date[0], new_date[2]])


print(split_string_on_punctuation('hi, how are you doing? blabla'))
print(split_string_on_punctuation(';String. with. punctuation characters!'))