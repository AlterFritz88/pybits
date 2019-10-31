from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
    """Randomly select a move"""
    return choice(list(defeated_by.values()))


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if computer_choice == player_choice:
        return tie
    if (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'rock' and computer_choice == 'scissors'):
        return win.format(player_choice, computer_choice)
    else:
        return lose.format(computer_choice, player_choice)
def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    print('Welcome to Rock Paper Scissors')
    while 1:
        player_in = yield
        if player_in == 'q':
            raise StopIteration
        print(_get_winner(_get_computer_move(), player_in))
        yield


game = game()
next(game)
game.send('rock')
game.send('q')