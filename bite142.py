from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    for dice in scores:
        if dice not in DICE_VALUES:
            raise ValueError
    return sum([x for x in scores if x >= MIN_SCORE])


def get_winner(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    max_len = max([len(x.scores) for x in players])
    for player in players:
        if len(player.scores) != max_len:
            raise ValueError
    top_player = Player(name='player 1', scores=[1, 1, 1, 1])
    for player in players:
        if calculate_score(player.scores) > calculate_score(top_player.scores):
            top_player = player
    return top_player


players = [
      Player(name='player 1', scores=[4, 3, 5, 5, 4]),
      Player(name='player 2', scores=[4, 4, 6, 6, 3, 2]),  # 1 more
      Player(name='player 3', scores=[4, 5, 6, 6, 5]),
    ]

print(get_winner(players))