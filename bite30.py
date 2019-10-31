import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = 'temp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
#urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = {}
    with open(local, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            try:
                if int(row['title_year']) < MIN_YEAR:
                    continue
                else:
                    movie_year = int(row['title_year'])
                    score = float(row['imdb_score'])
            except:
                continue

            if len(row['director_name']) > 0:
                if row['director_name'] not in directors.keys():
                    directors[row['director_name']] = [Movie(row['movie_title'][:-1], movie_year, score)]
                else:
                    directors[row['director_name']].append(Movie(row['movie_title'][:-1], movie_year, score))
        return directors

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    all_score = 0
    for movie in movies:
        all_score += movie.score
    return round(all_score / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    dir_list = []
    for key, value in directors.items():
        if len(value) >= MIN_MOVIES:
            dir_list.append((key, calc_mean_score(value)))
    dir_list.sort(key=lambda tup: tup[1], reverse=True)
    return dir_list

print(get_movies_by_director())

cameron_list = get_movies_by_director()['James Algar']
print(cameron_list)
print(calc_mean_score(cameron_list))

print(get_average_scores(get_movies_by_director()))