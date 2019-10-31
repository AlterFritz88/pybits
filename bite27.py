import glob
import json
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = 'tmp_js'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))



def get_movie_data(files=files):
    films = []
    for file in files:
        with open(file, 'r') as f:
            st = f.read()
            film = json.loads(st)
        films.append(film)
    return films



def get_single_comedy(movies):
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies):
    num_award = {}
    for movie in movies:
        awards = sum([int(x) for x in movie['Awards'].split() if x.isdigit()])
        num_award[movie['Title']] = awards
    sort_awards = sorted(num_award.items(), key=lambda kv: kv[1])
    return sort_awards[-1][0]


def get_movie_longest_runtime(movies):
    num_award = {}
    for movie in movies:
        time = int(movie['Runtime'].split()[0])
        num_award[movie['Title']] = time
    sort_awards = sorted(num_award.items(), key=lambda kv: kv[1])
    return sort_awards[-1][0]

movies = get_movie_data(files)
print(get_single_comedy(movies))
print(get_movie_most_nominations(movies))
print(get_movie_longest_runtime(movies))