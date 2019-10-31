from os import path
import statistics as st
from urllib.request import urlretrieve


STATS = path.join('tmp', 'testfiles_number_loc.txt')
if not path.isfile(STATS):
    urlretrieve('https://bit.ly/2Jp5CUt', STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    with open(STATS, 'r') as f:
        data = f.read().split('\n')
    data = [int(x.strip().split(' ')[0]) for x in data if x != '']
    return data


def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())

    # taking a sample for the last section
    sample = list(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(count=None,
                 min_=None,
                 max_=None,
                 mean=None,
                 pstdev=None,
                 pvariance=None,
                 sample_count=None,
                 sample_stdev=None,
                 sample_variance=None,
                 )
    stats['count'] = len(data)
    stats['min_'] = min(data)
    stats['max_'] = max(data)
    stats['mean'] = st.mean(data)
    stats['pstdev'] = st.pstdev(data)
    stats['pvariance'] = st.pvariance(data)
    stats['sample_count'] = len(sample)
    stats['sample_stdev'] = st.stdev(sample)
    stats['sample_variance'] = st.variance(sample)

    return STATS_OUTPUT.format(**stats)

print(create_stats_report(get_all_line_counts()))