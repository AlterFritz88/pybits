from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    deck = []
    for suit in SUITS:
        deck.append(UnoCard(suit, 0))
        for num in range(1, 10):
            for _ in range(2):
                deck.append(UnoCard(suit, num))
        for another in ('Draw Two', 'Skip', 'Reverse'):
            for _ in range(2):
                deck.append(UnoCard(suit, another))
    for _ in range(4):
        deck.append(UnoCard(None, 'Wild'))
        deck.append(UnoCard(None, 'Wild Draw Four'))
    return deck

print(len(create_uno_deck()))