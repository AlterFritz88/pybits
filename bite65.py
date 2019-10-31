import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    li_comb = _get_permutations_draw(draw)
    li_words = [''.join(x).lower() for x in li_comb if ''.join(x).lower() in dictionary]
    calced_score = list(set([(x, _calc_word_value(x)) for x in li_words]))
    sorted_calc = sorted(calced_score, key= lambda x: x[1])
    ans = set([x[0] for x in sorted_calc if x[1] == sorted_calc[-1][1]])
    return ans

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    comb_li = []
    for i in range(1, len(draw)+1):
        comb_li += list(itertools.permutations(draw, i))
    return comb_li

def _calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    score = 0
    for letter in word:
        score += LETTER_SCORES[letter.upper()]
    return score

def _max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    max_word = words[0]
    max_score = 0
    for word in words:
        score = _calc_word_value(word)
        if score > max_score:
            max_score = score
            max_word = word
    return max_word

print(get_possible_dict_words(['B', 'R', 'C', 'O', 'O', 'E', 'O']))