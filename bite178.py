from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join('temp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def _get_int(ins_del_str):
    return int(ins_del_str.split()[0])


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commits, 'r') as f:
        comm = {}
        for line in f:
            if '{} {}'.format(line.split()[2], line.split()[5]) not in comm.keys():

                if len(line) < 14:
                    comm['{} {}'.format(line.split()[2], line.split()[5])] = int(line.split()[11])
                else:
                    comm['{} {}'.format(line.split()[2], line.split()[5])] = int(line.split()[11]) + int(line.split()[-2])
            else:
                if len(line) < 14:
                    comm['{} {}'.format(line.split()[2], line.split()[5])] += int(line.split()[11])
                else:
                    comm['{} {}'.format(line.split()[2], line.split()[5])] += int(line.split()[11]) + int(line.split()[-2])



    comm_parse = {YEAR_MONTH.format(y=parse(x).year, m=parse(x).month): y for x, y  in comm.items()}
    if year == None:
        co_year = Counter(comm_parse)
        return co_year.most_common()[-1][0], co_year.most_common()[0][0]
    else:
        co_year = Counter({x:y for x, y in comm_parse.items() if year == int(x.split('-')[0])})
        return co_year.most_common()[-1][0], co_year.most_common()[0][0]


print(get_min_max_amount_of_commits(year=2017))