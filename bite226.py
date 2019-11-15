from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    mydivs = soup.findAll("span", {"class": "smaller"})
    points = []
    comments = []
    titles = []
    answer = []
    for item in mydivs:
        if "point" in item.text:
            points.append(int(item.text.strip().split(" ")[0]))
            comments.append(int(item.text.strip().split("| ")[1].split(" ")[0]))
    mydivs = soup.findAll("span", {"class": "title"})
    for item in mydivs:

        titles.append(item.text.strip())

    for title, point, comment in zip(titles, points, comments):
        answer.append(Entry(title=title, points=point, comments=comment))
    answer = sorted(answer, key=lambda x: (-x.points, -x.comments))
    return answer[:top]


print(get_top_titles("https://bites-data.s3.us-east-2.amazonaws.com/"
            "news.python.sc/index.html"))