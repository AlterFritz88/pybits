from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
TIM_BLOG = 'https://bit.ly/2NBnZ6P'


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content)
    books = []
    for a in soup.find_all('a', href=True):
        if AMAZON in a['href']:
            print(a.text)
            b = a.find('i')
            if b != None:
                books.append(b.find('span').text)

    co = Counter(books).most_common()
    return [x[0] for x in co[:limit]]



print(get_top_books(limit=5))