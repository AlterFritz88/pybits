"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join('temp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word_filtered = ''.join([x for x in word if x.isalnum()]).lower()
    if word_filtered[::-1] == word_filtered:
        return True
    else:
        return False



def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words == None:
        words = list(load_dictionary())

    polindroms = [x for x in words if is_palindrome(x)]
    return max(polindroms, key=len)


print(is_palindrome('No \'x\' in \'Nixon'))

print(get_longest_palindrome())