import os
from collections import Counter
import urllib.request
import feedparser

# prep

tempfile = os.path.join('tmp', 'feed')
'''
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)
'''
with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    rss = feedparser.parse('http://bit.ly/2zD8d8b')
    list_tag = []
    for i in rss['entries']:
        for d in i['tags']:
            list_tag.append(d['term'].lower())
    c = Counter()
    for word in list_tag:
        c[word] += 1
    di = dict(c)
    new_list = []
    for k, v in di.items():
        new_list.append((k, v))
    new_list = sorted(new_list, key=lambda x: x[1], reverse=True)
    return new_list[:n]

print(get_pybites_top_tags())