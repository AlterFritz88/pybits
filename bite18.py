import os
import urllib.request

import string
from collections import Counter

# data provided
stopwords_file = os.path.join('temp', 'stopwords')
harry_text = os.path.join('temp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(stopwords_file, 'r') as f:
        stops = f.read().split('\n')
    with open(harry_text, 'r') as f2:
        harry_lines = f2.read().split('\n')
    harry_words = []

    for line in harry_lines:
        words = line.split(' ')
        for word in words:
            harry_words.append(word)
    harry_words_filterd = [s.translate(str.maketrans('', '', string.punctuation)) for s in harry_words]
    harry_words_filterd = [x.lower() for x in harry_words_filterd if x != '' and x.lower() not in stops]
    count_words = Counter(harry_words_filterd)
    return count_words.most_common(1)[0]

print(get_harry_most_common_word())