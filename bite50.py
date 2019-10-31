from collections import namedtuple
import datetime
from datetime import date


import feedparser

FEED = 'http://projects.bobbelderbos.com/pcc/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)"""
    pass


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)"""
    rss = feedparser.parse(FEED)
    for value in rss['entries']:
        print(value)
        print(value['published'], value['title'], value['link'], value['tags'])

        date = datetime.datetime.strptime(value['published'][5:16], '%d%m%Y').date()


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
    pass

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term, exit on 'q', try again upon empty input
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the date+title+link of each match ordered by date desc
       6. Secondly, print the number of matches"""
    get_feed_entries()
    while 1:
        inputed = input('Search for (q for exit):')

        if inputed == None:
            print('Please provide a search term')
        if inputed == 'q':
            break


if __name__ == '__main__':
    main()