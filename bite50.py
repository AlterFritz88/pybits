from collections import namedtuple
import datetime
#from datetime import date
from time import mktime


import feedparser

FEED = 'http://projects.bobbelderbos.com/pcc/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)"""
    df = datetime.datetime.fromtimestamp(mktime(stime)).date()
    return df

def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)"""
    rss = feedparser.parse(feed)
    #rss = MOCK_ENTRIES
    content = []
    for value in rss['entries']:
        date = datetime.datetime.strptime(value['published'][5:16], '%d %b %Y').date()     #strftime('%Y-%m-%d')
        title = value['title']
        link = value['link']
        tags = value['tags']

        tag_to_tuple = []
        for tag in tags:
            tag_to_tuple.append(tag['term'].lower())
        content.append(Entry(date=date, title=title, link=link, tags=tag_to_tuple))
    return content


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags"""


    if '&' in search:
        match = search.lower().split('&')
        if set(match).issubset(entry.tags):
            return True
    elif '|' in search:
        match = search.lower().split('|')
        if any(x in match for x in entry.tags):
            return True
    else:
        if search.lower() in entry.tags:
            return True
    return False

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term, exit on 'q', try again upon empty input
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the date+title+link of each match ordered by date desc
       6. Secondly, print the number of matches"""
    get_feed_entries()
    entries = get_feed_entries(FEED)
    while 1:
        inputed = input('\nSearch for (q for exit): ')

        if inputed == '':
            print('Please provide a search term')
            continue
        if inputed == 'q':
            print('Bye')
            break

        for_print = []
        for entry in entries:
            if filter_entries_by_tag(inputed.lower(), entry):
                for_print.append(entry)

        for_print = sorted(for_print, key=lambda x: x.date)
        for result in for_print:
            print(str(result.date), result.title, result.link)

        if len(for_print) == 1:
            print('\n{} entry matched "{}"'.format(len(for_print), inputed))
        else:
            print('\n{} entries matched "{}"'.format(len(for_print), inputed))



class AttrDict(dict):
    """feedparser lets you access dict keys as attributes, hence a bit of
       mocking, got this from https://stackoverflow.com/a/14620633"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

dt1 = datetime.datetime(2018, 2, 18, 19, 52, 0).timetuple()
dt2 = datetime.datetime(2017, 1, 6, 11, 0, 0).timetuple()


MOCK_ENTRIES = {'entries':
                [AttrDict({'author': 'PyBites',
                           'link':
                           'https://pybit.es/twitter_digest_201808.html',  # noqa E501
                           'published': 'Sun, 18 Feb 2018 20:52:00 +0100',  # noqa E501
                           'published_parsed': dt1,
                           'summary': '<p>Every weekend we share ...',
                           'tags': [AttrDict({'term': 'twitter'}),
                                    AttrDict({'term': 'Flask'}),
                                    AttrDict({'term': 'Python'}),
                                    AttrDict({'term': 'Regex'})],
                           'title': 'Twitter Digest 2018 Week 08'}),
                 AttrDict({'author': 'Julian',
                           'link': 'https://pybit.es/pyperclip.html',
                           'published': 'Fri, 06 Jan 2017 12:00:00 +0100',  # noqa E501
                           'published_parsed': dt2,
                           'summary': '<p>Use the Pyperclip module to ...',
                           'tags': [AttrDict({'term': 'python'}),
                                    AttrDict({'term': 'tips'}),
                                    AttrDict({'term': 'tricks'}),
                                    AttrDict({'term': 'code'}),
                                    AttrDict({'term': 'pybites'})],
                           'title': 'Copy and Paste with Pyperclip'})]}

if __name__ == '__main__':
    main()




