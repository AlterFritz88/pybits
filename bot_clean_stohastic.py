from math import sqrt
go_variants = {
    'all':          ('up', 'down', 'right', 'left'),
    'top_constr':   ('down', 'right', 'left'),
    'down_constr':  ('up', 'right', 'left'),
    'left_constr':  ('up', 'down', 'right'),
    'right_constr': ('up', 'down',  'left'),
    'top_left':     ('right', 'down'),
    'top_right':    ('down', 'left'),
    'down_right':   ('up', 'left'),
    'down_left':    ('up', 'right')
}

def _possible_moves(y, x, board):
    if y+1 == len(board):
        if x+1 == len(board[0]):
            return go_variants['down_right']
        if x-1 < 0:
            return go_variants['down_left']
        else:
            return go_variants['down_constr']

    elif y-1 < 0:
        if x+1 == len(board[0]):
            return go_variants['top_right']
        if x-1 < 0:
            return go_variants['top_left']
        else:
            return go_variants['top_constr']


    elif x+1 == len(board[0]):
        return go_variants['right_constr']
    elif x-1 < 0:
        return go_variants['left_constr']
    else:
        return go_variants['all']


def _get_d(board):
    for i, y in enumerate(board):
        for j, x in enumerate(y):
            if board[i][j] == 'd':
                return i, j

def _down(y, x):
    return y+1, x

def _top(y, x):
    return y-1, x

def _right(y, x):
    return y, x+1

def _left(y, x):
    return y, x-1

steps_dict = {
    'down':       _down,
    'up':      _top,
    'right':    _right,
    'left':     _left
}

def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print('CLEAN')
        return None
    dy, dx = _get_d(board)
    possible_steps = _possible_moves(posr, posc, board)
    steps_results = {}
    for step in possible_steps:
        y, x = steps_dict[step](posr, posc)
        squard = sqrt((dy - y)**2 + (dx - x)**2)
        steps_results[step] = squard
    print(sorted(steps_results, key=lambda x: steps_results[x])[0].upper())


if __name__ == "__main__":
    #pos = [int(i) for i in input().strip().split()]
    #board = [[j for j in input().strip()] for i in range(5)]
    #nextMove(pos[0], pos[1], board)
    board = [['-', 'b', '-', '-', 'd'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    pos = [4, 4]
    for i in board:
        print(i)
    print(nextMove(pos[0], pos[1], board))