from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

print(data)
# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    car_per_year = [x['automaker'] for x in data if x['year'] == year]
    count = Counter(car_per_year)
    return count.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    cars = [x['model'] for x in data if x['year'] == year and x['automaker'] == automaker]
    return set(cars)

most_prolific_automaker(2008)
get_models('Volkswagen', 2008)