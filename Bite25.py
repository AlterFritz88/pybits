import random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
bites_done = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:

    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done

    def _pick_random_bite(self):
        if len(set(BITES.keys()) - self.bites_done) == 0:
            raise NoBitesAvailable

        sett = set(BITES.keys()) - self.bites_done
        print(sett)
        return random.choice(list(sett))

    def new_bite(self):
        self.bites_done.add(self._pick_random_bite())
        print(self.bites_done)

cl = Promo(bites_done)
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())
print(cl.new_bite())