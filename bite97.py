from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('temp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    Soup = BeautifulSoup(content)
    a = Soup.findAll('time')

    table = Soup.find(lambda tag: tag.name == 'table')
    rows = table.findAll(lambda tag: tag.name == 'a')

    for row, i in zip(rows, a):
        holidays[i['datetime'].split('-')[1]].append(row.text)
    return holidays



get_us_bank_holidays()