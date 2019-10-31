from dataclasses import dataclass
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.bites < other.bites

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.bites > other.bites

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.bites == other.bites

    def __repr__(self):
        return '[{}] {}'.format(self.bites, self.name)



@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    def __init__(self):
        self.rankings = []

    def add(self, ninja):
        self.rankings.append(ninja)

    def dump(self):
        minim = min(self.rankings)
        self.rankings.remove(minim)
        return minim

    def highest(self, high=1):
        return sorted(self.rankings, reverse=True)[:high]

    def lowest(self, low=1):
        return sorted(self.rankings, reverse=False)[:low]

    def pair_up(self, pairs=3):
        sorted_ninjas = sorted(self.rankings, reverse=True)
        ans_list = []
        for i in range(pairs):
            max_p = max(sorted_ninjas)
            min_p = min(sorted_ninjas)
            ans_list.append((max_p, min_p))
            sorted_ninjas.remove(max_p)
            sorted_ninjas.remove(min_p)
        return ans_list

    def __len__(self):
        return len(self.rankings)


FIRST_NINJAS = [Ninja(*ninja) for ninja in zip(names, bites)]


ranking = Rankings()
for ninja in FIRST_NINJAS:
    ranking.add(ninja)
ranking.dump()
print(ranking.pair_up())