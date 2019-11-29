import csv
import re
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('temp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = []
    with open(stats, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        for line in reader:
            if line['Difficulty'] == 'None':
                continue
            bit_number = re.findall(r'\d+\.', line[reader.fieldnames[0]])[0][:-1]
            bites.append(((bit_number, float(line['Difficulty']))))
    sorted_bites = sorted(bites, key=lambda x: (x[1], -int(x[0])))

    return [x[0] for x in sorted_bites[::-1][:N]]

if __name__ == '__main__':
    res = get_most_complex_bites(10)
    print(res)