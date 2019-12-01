from collections import namedtuple
from datetime import datetime
from operator import itemgetter
from typing import List

Sign = namedtuple('Sign', 'name compatibility famous_people sun_dates')


def get_signs(data: list) -> List[Sign]:
    ret = []
    for sign in data:
        name = sign['name']
        compatibility = sign['compatibility']
        famous_people = sign['famous_people']
        sun_dates = sign['sun_dates']
        sign = Sign(name, compatibility, famous_people, sun_dates)

        print(type(sign))
        ret.append(
            sign
        )
    return ret


def get_sign_with_most_famous_people(signs: list):
    """Get the sign with the most famous people associated"""
    famous_people = [
        (s.name, len(s.famous_people)) for s in signs
    ]
    return max(famous_people, key=itemgetter(1))


def signs_are_mutually_compatible(signs: list, sign1: str, sign2: str) -> bool:
    """Given 2 signs return if they are compatible (compatibility field)"""
    ret = False
    for sign in signs:
        if sign.name == sign1:
            ret = sign2 in sign.compatibility
        elif sign.name == sign2:
            ret = sign1 in sign.compatibility
    return ret


def get_sign_by_date(signs: list, date: datetime) -> str:
    """Given a date return the right sign (sun_dates field)"""
    year = date.year
    for sign in signs:
        start, end = sign.sun_dates
        start_dt = datetime.strptime(start, '%B %d').replace(year=year)
        end_dt = datetime.strptime(end, '%B %d').replace(year=year)
        if start_dt <= date <= end_dt:
            return sign.name



from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest


# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "temp")
print(TMP)
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_data(signs):
    assert type(signs[0]).__name__ == "Sign"

def test_most_famous(signs):
    assert ('Scorpio', 35) == get_sign_with_most_famous_people(signs)


def test_sign_comp_1(signs):
    assert not signs_are_mutually_compatible(signs, "Cancer", "Virgo")


def test_sign_comp_2(signs):
    assert signs_are_mutually_compatible(signs, "Aries", "Aquarius")

def test_sign_comp_3(signs):
    assert signs_are_mutually_compatible(signs, "Aquarius", "Aries")


def test_date_1(signs):
    date = datetime.strptime("30/03/06 00:00", "%d/%m/%y %H:%M")
    assert "Aries" == get_sign_by_date(signs, date)

def test_date_2(signs):
    date = datetime.strptime("21/03/06 00:00", "%d/%m/%y %H:%M")
    assert "Aries" == get_sign_by_date(signs, date)

def test_date_3(signs):
    date = datetime.strptime("19/04/06 00:00", "%d/%m/%y %H:%M")
    assert "Aries" == get_sign_by_date(signs, date)

def test_date_4(signs):
    date = datetime.strptime("20/03/06 00:00", "%d/%m/%y %H:%M")
    assert 'Pisces' == get_sign_by_date(signs, date)

def test_date_5(signs):
    date = datetime.strptime("20/04/06 00:00", "%d/%m/%y %H:%M")
    assert "Taurus" == get_sign_by_date(signs, date)