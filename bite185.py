from difflib import SequenceMatcher
from os import path
from urllib.request import urlretrieve


DICTIONARY = path.join('temp', 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    matches_dict = {}
    for word in words:
        matches_dict[word] = SequenceMatcher(None, word, misspelled_word).ratio()
    sorted_by_value = sorted(matches_dict.items(), key=lambda kv: kv[1])
    return sorted_by_value[-1][0]

print(suggest_word('abberration'))