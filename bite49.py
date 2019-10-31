from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')

def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT)
    title = str(soup.find_all("h2")[0]).replace('<h2>', '').replace('</h2>', '').strip()
    desc =  str([entry for entry in soup.find_all('div', class_="dotd-main-book-summary float-left")][0]).split('<div')[4][2:-7].strip()
    img = soup.findAll('img')[5]['src']
    link = soup.find_all('div',  class_="dotd-main-book-image float-left")

    for div in link:
        link_p = div.find('a')['href']
    return Book(title, desc, img, link)


print(get_book())