from collections import namedtuple
import random

from string import ascii_uppercase

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    if n > 26:
        return ValueError

    deck = []

    for char in range(n):
        temp_deck = []
        for number in NUMBERS:
            card = ascii_uppercase[char] + str(number)
            temp_deck.append(PawCard(card=card, action=None))

        index = random.choice(range(0, 4))
        temp_deck[index] = PawCard(card=temp_deck[index].card, action=random.choice(ACTIONS))
        deck += temp_deck
    return deck

print(create_paw_deck(n=8))

deck  = create_paw_deck(n=8)
for i in deck:
    print(i)