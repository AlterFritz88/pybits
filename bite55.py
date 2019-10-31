from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    rss = feedparser.parse(FEED_URL)
    list_ans = []
    for value in rss['entries']:
        list_ans.append(Game(value['title'], value['link']))
    return list_ans

print(get_games())