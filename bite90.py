from collections import Counter, defaultdict
import csv
import re
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    data = [x.replace('""', '').replace('\n', ' ') for x in content.split('\n"\n')[1:] if x != '']
    persons = defaultdict(list)
    for phrase in data:
        b = phrase.split('"')[-1]
        print()
        print(b)
        a = _count(b.rstrip())
        #print(phrase)
        #print(re.findall(r'[a-zA-Z_]+', b))
        phrase = phrase.split(',')
        for i in range(a):
            persons[phrase[2]].append(phrase[1])
    #persons['Cartman'] = persons['Cartman'][3:]
    for k, v in persons.items():
        persons[k] = Counter(v)
    print(persons['Cartman'])
    return persons


def _count(word):


    #word = re.sub("[^a-zA-Z0-9' ]+",'', word).split(' ')
    word = word.split(' ')
    print([x for x in word if x != ''])
    a = len([x for x in word if x != ''])

    return a

#print(_count("All right. From everyone's accounts, I've narrowed down Eric's possible father... to the people in this room"))

print(get_num_words_spoken_by_character_per_episode(get_season_csv_file(1)))