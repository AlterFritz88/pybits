import requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

print(data)
# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    if cap[-1] == 'M':
        return float(cap[1:-1])
    if cap[-1] == 'B':
        return float(cap[1:-1])*1000

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    return round(sum([_cap_str_to_mln_float(x['cap']) for x in data if x['industry'] == industry]), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    return sorted(data, key= lambda x: _cap_str_to_mln_float(x['cap']))[-1]['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    from collections import defaultdict
    di = defaultdict(list)
    for stock in data:
        if stock['sector'] != 'n/a':
            di[stock['sector']].append(_cap_str_to_mln_float(stock['cap']))
    di_sum = {x: sum(y) for x, y in di.items()}
    di_sum = sorted(di_sum.items(), key=lambda x: x[1])
    return (di_sum[-1][0], di_sum[0][0])


print(_cap_str_to_mln_float('$20.9B'))
print(get_industry_cap("Real Estate Investment Trusts"))
print(get_stock_symbol_with_highest_cap())
print(get_sectors_with_max_and_min_stocks())