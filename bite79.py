import csv

import requests

from collections import Counter

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        return [row[2] for row in my_list[1:]]

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    conten_count = Counter(content).most_common()
    conten_sorted = sorted(conten_count, key=lambda x: x[0])

    for county in conten_sorted:

        print('{:<21}| {}'.format(county[0], '+' * county[1]))

create_user_bar_chart(get_csv())