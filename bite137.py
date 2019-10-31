#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator


CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

def _similarity(st1, st2):
    str1_list = Counter(list(st1.lower()))
    str2_list = Counter(list(st2.lower()))
    points = 0
    for letter in max([str1_list.keys(), str2_list.keys()]):
        if letter in str1_list.keys() and letter in str2_list.keys():
            if str1_list[letter] == str2_list[letter]:
                points += str1_list[letter]
            else:
                points += min(str1_list[letter], str2_list[letter])
    return points / (1 + pow((len(st1) - len(st2)), 2))

def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    wines_dict = {'all': SPARKLING_WINES + WHITE_WINES + RED_WINES, 'red': RED_WINES, 'white': WHITE_WINES, 'sparkling': SPARKLING_WINES}
    if wine_type not in ('all', 'white', 'red', 'sparkling'):
        raise ValueError
    wines = wines_dict[wine_type]
    best_case = (None, None, 0)
    for wine in wines:
        for cheese in CHEESES:
            if _similarity(wine, cheese) > best_case[2]:
                best_case = (wine, cheese, _similarity(wine, cheese))
    return best_case



def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    wines = sorted(SPARKLING_WINES + WHITE_WINES + RED_WINES)
    wines_cheese = []
    for wine in wines:
        wine_list = [wine, {}]

        for cheese in CHEESES:
            wine_list[1][cheese] = _similarity(wine, cheese)
        wine_items = sorted(wine_list[1].items(), key= lambda x: x[0])
        sorted_list = sorted(wine_items, key= lambda x: x[1], reverse=True)[:5]
        wine_list[1] = [x[0] for x in sorted_list]
        wines_cheese.append(wine_list)
    return wines_cheese


print(_similarity('roosters-do-sound', 'cocka-doodle-doo'))
print(best_match_per_wine("sparkling"))
print(match_wine_5cheeses())