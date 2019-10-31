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

def _get_ds(board):
    ds = []
    for i, y in enumerate(board):
        for j, x in enumerate(y):
            if board[i][j] == 'd':
                ds.append((i, j))
    return ds


def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy] == 'd':
        print('CLEAN')
        return None
    ds = _get_ds(board)
    possible_steps = _possible_moves(posx, posy, board)
    ds_distance = {}
    for d in ds:
        squard = sqrt((d[0] - posx) ** 2 + (d[1] - posy) ** 2)
        ds_distance[d] = squard
    d = sorted(ds_distance, key=lambda x: ds_distance[x])[0]
    steps_results = {}
    for step in possible_steps:
        y, x = steps_dict[step](posx, posy)
        squard = sqrt((d[0] - y)**2 + (d[1] - x)**2)
        steps_results[step] = squard
    print(sorted(steps_results, key=lambda x: steps_results[x])[0].upper())

if __name__ == "__main__":
    #pos = [int(i) for i in input().strip().split()]
    #dim = [int(i) for i in input().strip().split()]
    #board = [[j for j in input().strip()] for i in range(dim[0])]
    #print(board)
    pos = [1, 1]
    dim = [5, 5]
    board = [['-', 'd', '-', '-', '-'], ['-', 'b', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]
    for i in board:
        print(i)
    next_move(pos[0], pos[1], dim[0], dim[1], board)