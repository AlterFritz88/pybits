import os
import urllib.request

# PREWORK
DICTIONARY = 'temp/dictionary.txt'


urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', 'temp/dictionary.txt')
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}
print(LETTER_SCORES)

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    word_list = []
    with open(DICTIONARY, 'r') as file:
        for line in file:
            word_list.append(line[:-1])
    return word_list


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    score = 0
    for letter in word:
        score += LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    max_word = words[0]
    max_score = 0
    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score
            max_word = word
    return max_word

print(max_word_value(['dog', 'CaT', 'Friday']))