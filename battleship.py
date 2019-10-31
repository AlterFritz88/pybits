from random import choice

go_variants = {
    'all': ('up', 'down', 'right', 'left', 'left-down', 'left-top', 'right-top', 'right-down'),
    'top_constr': ('down', 'right', 'left', 'left-down', 'right-down'),
    'down_constr': ('up', 'right', 'left', 'left-top', 'right-top'),
    'left_constr': ('up', 'down', 'right', 'right-top', 'right-down'),
    'right_constr': ('up', 'down', 'left', 'left-top', 'left-down'),
    'top_left': ('right', 'down', 'right-down'),
    'top_right': ('down', 'left', 'left-down'),
    'down_right': ('up', 'left', 'left-top'),
    'down_left': ('up', 'right', 'right-top')
}

h_variants = {
    'all': ('up', 'down', 'right', 'left'),
    'top_constr': ('down', 'right', 'left'),
    'down_constr': ('up', 'right', 'left'),
    'left_constr': ('up', 'down', 'right'),
    'right_constr': ('up', 'down', 'left'),
    'top_left': ('right', 'down'),
    'top_right': ('down', 'left'),
    'down_right': ('up', 'left'),
    'down_left': ('up', 'right')
}


def _possible_moves(y, x, board, variants):
    if y + 1 == len(board):
        if x + 1 == len(board[0]):
            return variants['down_right']
        if x - 1 < 0:
            return variants['down_left']
        else:
            return variants['down_constr']

    elif y - 1 < 0:
        if x + 1 == len(board[0]):
            return variants['top_right']
        if x - 1 < 0:
            return variants['top_left']
        else:
            return variants['top_constr']


    elif x + 1 == len(board[0]):
        return go_variants['right_constr']
    elif x - 1 < 0:
        return go_variants['left_constr']
    else:
        return go_variants['all']


def _down(y, x):
    return y + 1, x


def _top(y, x):
    return y - 1, x


def _right(y, x):
    return y, x + 1


def _left(y, x):
    return y, x - 1


def _left_top(y, x):
    return y - 1, x - 1


def _left_down(y, x):
    return y + 1, x - 1


def _right_top(y, x):
    return y - 1, x + 1


def _right_down(y, x):
    return y + 1, x + 1


steps_dict = {
    'down': _down,
    'up': _top,
    'right': _right,
    'left': _left,
    'left-down': _left_down,
    'left-top': _left_top,
    'right-top': _right_top,
    'right-down': _right_down
}


def _get_ds(board):
    ds = []
    for i, y in enumerate(board):
        for j, x in enumerate(y):
            if board[i][j] == 'd':
                ds.append((i, j))
    return ds


def _get_bitten_ships(board):
    bitten_ships = []
    for y, vertical in enumerate(board):
        for x, horizontal in enumerate(vertical):
            if board[y][x] == 'h':
                bitten_ships.append((y, x))
    return bitten_ships


def _update_board_with_dead_ships(board):
    ds = _get_ds(board)
    for d in ds:
        possible_shoots = _possible_moves(d[0], d[1], board, go_variants)
        for shoot in possible_shoots:
            shot_y, shot_x = steps_dict[shoot](d[0], d[1])
            board[shot_y][shot_x] = 'm'


def __get_opt_shoots():
    shoot_list = []
    n = 3
    for coll in range(10):
        for i in range(n, 10, 4):
            shoot_list.append((i, coll))
        n -= 1
        if n < 0:
            n = 3
    n = 1
    for coll in range(10):
        for i in range(n, 10, 4):
            shoot_list.append((i, coll))
        n -= 1
        if n < 0:
            n = 3

    return shoot_list


def _get_possible_shoots(board):
    possible_shoots = []
    for y, vertical in enumerate(board):
        for x, horizontal in enumerate(vertical):
            if board[y][x] == '-':
                possible_shoots.append((y, x))
    return possible_shoots


def _get_optimal_shoots(board):
    opt_shoots = __get_opt_shoots()
    for shoot in opt_shoots:
        if board[shoot[0]][shoot[1]] == '-':
            return shoot

    pos_shoot = _get_possible_shoots(board)
    return choice(pos_shoot)


def _get_directions_hs(hs):
    if hs[0][1] == hs[1][1]:
        return 'vertical'
    else:
        return 'horizontal'


def _shoot_in_h(board, hs):
    if len(hs) == 1:
        possible_shoots = _possible_moves(hs[0][0], hs[0][1], board, h_variants)
        for shoot in possible_shoots:
            shoot_y, shoot_x = steps_dict[shoot](hs[0][0], hs[0][1])
            if board[shoot_y][shoot_x] not in ('d', 'm'):
                return (shoot_y, shoot_x)
    else:
        where_go = _get_directions_hs(hs)

        print(where_go)
        if where_go == 'vertical':
            sorted_hits = sorted(hs, key=lambda x: x[1])
            max_posible_hit = sorted_hits[-1]
            min_posible_hit = sorted_hits[0]
            possible_shoots_max = _possible_moves(max_posible_hit[0], max_posible_hit[1], board, h_variants)
            possible_shoots_min = _possible_moves(min_posible_hit[0], min_posible_hit[1], board, h_variants)

            if 'down' in possible_shoots_max:
                y, x = steps_dict['down'](max_posible_hit[0], max_posible_hit[1])
                if board[y][x] == '-':
                    return (y, x)
            if 'up' in possible_shoots_min:
                y, x = steps_dict['up'](min_posible_hit[0], min_posible_hit[1])
                if board[y][x] == '-':
                    return (y, x)

        else:
            sorted_hits = sorted(hs, key=lambda x: x[1])
            max_posible_hit = sorted_hits[-1]
            min_posible_hit = sorted_hits[0]
            possible_shoots_max = _possible_moves(max_posible_hit[0], max_posible_hit[1], board, h_variants)
            possible_shoots_min = _possible_moves(min_posible_hit[0], min_posible_hit[1], board, h_variants)

            if 'right' in possible_shoots_max:
                y, x = steps_dict['right'](max_posible_hit[0], max_posible_hit[1])
                if board[y][x] == '-':
                    return (y, x)
            if 'left' in possible_shoots_min:
                y, x = steps_dict['left'](min_posible_hit[0], min_posible_hit[1])
                if board[y][x] == '-':
                    return (y, x)


def fire(board):
    # _update_board_with_dead_ships(board)
    hs = _get_bitten_ships(board)

    if hs == []:
        possible_shoots = _get_optimal_shoots(board)
        return possible_shoots
    else:
        shoot = _shoot_in_h(board, hs)
        return shoot


if __name__ == "__main__":
    board_size = int(input())
    board = [[j for j in input().strip()] for i in range(board_size)]
    # print(board)
    # board = [['-', '-', '-', '-', '-', 'd', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', 'm', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', 'd', '-', '-', '-', '-', '-', 'm', '-'], ['-', '-', '-', 'm', '-', 'm', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', 'm', '-', '-', '-'], ['-', 'm', '-', '-', '-', 'm', 'm', '-', '-', '-'], ['-', '-', 'm', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', 'm', '-', '-', '-']]
    # for i in board:
    #    print(i)

    shoot = fire(board)
    print(shoot[0], shoot[1])