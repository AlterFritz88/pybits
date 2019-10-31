from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from collections import defaultdict

# import the countries xml file
tmp = Path('temp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    with open(xml, 'r') as file:
        data = file.read()
    soup = BeautifulSoup(data)
    country_dic = defaultdict(list)
    for country in soup.findAll('wb:country'):
        c_name = country.text.split('\n')[2]
        class_inc = country.text.split('\n')[5]
        country_dic[class_inc].append(c_name)
    return country_dic

print(get_income_distribution())