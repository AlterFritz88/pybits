from urllib.request import urlretrieve

import json
from pathlib import Path
from datetime import datetime

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('temp')


file_name = f'bite_scores{2}.json'
file_path = TMP / file_name
remote = 'https://bites-data.s3.us-east-2.amazonaws.com/'
#if not TMP.exists():
urlretrieve(f'{remote}{file_name}', file_path)

# with open(file_path) as f:
#     print(f.readlines()[:10])


def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    total_score = 0
    current_belt = 0
    ans = {}

    with open(data) as f:
        data = json.load(f)
    for item in data:
        item['date'] = datetime.strptime(item['date'], "%m/%d/%Y")
    data = sorted(data, key=lambda x: x['date'])


    for item in data:
        total_score += item['score']
        if total_score >= 1000:
            ans['red'] = item['date'].strftime("%B %d, %Y")
            break
        if total_score >= SCORES[current_belt]:
            ans[BELTS[current_belt]] = item['date'].strftime("%B %d, %Y")
            current_belt += 1


    return ans

print(get_belts('temp/bite_scores2.json'))