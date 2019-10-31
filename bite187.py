from dataclasses import dataclass

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} when {movie} came out, e.g.:

       Wesley Snipes was 28 old when New Jack City came out.
    """
    age = relativedelta(parse(movie.release_date), parse(actor.born)).years
    print('{} was {} when {} came out.'.format(actor.name, age, movie.title))

act = Actor('Wesley Snipes', 'July 31, 1962')
mov = Movie('New Jack City', 'January 17, 1991')

get_age(act, mov)