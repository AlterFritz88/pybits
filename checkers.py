from random import choice
from collections import defaultdict


def _cells_have_possible_step(cell_y, cell_x, cher, pos_steps) -> list:
    posible_moves = []
    for move in directions_dict[cher]:

        nex_pos_y, nex_pos_x = move(cell_y, cell_x)
        if nex_pos_x < 0 or nex_pos_x > len(board) - 1:
            continue
        if nex_pos_y < 0 or nex_pos_y > len(board) - 1:
            continue
        if board[nex_pos_y][nex_pos_x] in pos_steps:
            posible_moves.append((nex_pos_y, nex_pos_x))
    return posible_moves


def _down_right(y, x):
    return y + 1, x + 1


def _down_left(y, x):
    return y + 1, x - 1


def _up_right(y, x):
    return y - 1, x + 1


def _up_left(y, x):
    return y - 1, x - 1


def _get_cells_with_moves(board, cher) -> dict:
    steps = {}
    for y, vert in enumerate(board):
        for x, hor in enumerate(vert):
            if board[y][x] == cher:
                if _cells_have_possible_step(y, x, cher, ('_', opposite_color[color])) != []:
                    steps[(y, x)] = _cells_have_possible_step(y, x, cher, ('_', opposite_color[color]))

    return steps


def eat_all_dir(y, x, cher, board) -> list:
    dict_dirs = {'w': [_up_left, _up_right],
                 'b': [_down_left, _down_right],
                 'B': (_up_left, _up_right, _down_left, _down_right),
                 'W': (_up_left, _up_right, _down_left, _down_right)}
    dirs = dict_dirs[cher]
    list_posib_eat = []
    for d in dirs:
        try:
            pot_y, pot_x = d(y, x)
            if pot_x < 0 or pot_y < 0:
                continue
            if board[pot_y][pot_x] != opposite_color[color]:
                continue
            pot_y, pot_x = d(pot_y, pot_x)
            if pot_x < 0 or pot_y < 0:
                continue
            if board[pot_y][pot_x] == '_':
                list_posib_eat.append((pot_y, pot_x))
        except:
            continue
    return list_posib_eat


def _all_eats(color, board):
    ans_dict = {}
    for y, vert in enumerate(board):
        for x, hor in enumerate(vert):
            if board[y][x] == color:
                if eat_all_dir(y, x, color, board) != []:
                    ans_dict[(y, x)] = eat_all_dir(y, x, color, board)
    return ans_dict


def _dengerous_moves(moves: list) -> list:
    good_choise = []
    for move in moves:
        canditate = move[-1]
        up_left_y, up_left_x = _up_left(canditate[0], canditate[1])
        up_right_y, up_right_x = _up_right(canditate[0], canditate[1])
        down_left_y, down_left_x = _down_left(canditate[0], canditate[1])
        down_rigth_y, down_right_x = _down_right(canditate[0], canditate[1])
        if up_left_y < 0 or up_left_x < 0 or up_right_y < 0 or up_right_x > board_size - 1 or down_left_y > board_size - 1 or down_left_x < 0 or down_rigth_y > board_size - 1 or down_right_x > board_size - 1:
            good_choise.append(move)
            continue
        if (board[up_left_y][up_left_x] == opposite_color[color] and board[down_rigth_y][down_right_x] ==
            opposite_color[color]) or (
                board[up_left_y][up_left_x] == opposite_color[color] and board[down_rigth_y][down_right_x] ==
                opposite_color[color]):
            continue
        if (board[up_right_y][up_right_x] == opposite_color[color] and board[down_left_y][down_left_x] ==
            opposite_color[color]) or (
                board[up_right_y][up_right_x] == opposite_color[color] and board[down_left_y][down_left_x] ==
                opposite_color[color]):
            continue
        good_choise.append(move)
    if good_choise == []:
        test = moves[:]
        if len(test) == 1:
            return test[0]
        go = min_eaten(test)
        #print(moves, 'jutgjyhgyju')
        return go
    else:
        return good_choise[-1]


def min_eaten(steps):
    decision_list = []
    for move in steps:
        dirs = directions_dict[board[move[0][0]][move[0][1]]]
        temp_board = [[board[y][x] for x in range(len(board[0]))] for y in range(len(board))]
        for i, step in enumerate(move):
            if i == len(move) -1:
                continue
            for dir in dirs:
                y1, x1 = dir(move[i][0], move[i][1])
                y2, x2 = dir(y1, x1)
                if (y1 < 0 or y1 > board_size - 1 or x1 < 0 or x1 > board_size - 1) and (
                        y2 < 0 or y2 > board_size - 1 or x2 < 0 or x2 > board_size - 1):
                    continue
                if (y2, x2) == move[i+1]:
                    temp_board[move[i][0]][move[i][1]] = '_'
                    temp_board[y2][x2] = board[move[0][0]][move[0][1]]
                    temp_board[y1][x1] = '_'
        decision_list.append(eat_my_enemy(temp_board))
    a = decision_list.index(min(decision_list, key=lambda x: len(x)))
    return steps[a]

def eat_my_enemy(board_test):
    global color
    color = opposite_color[color]
    eat_liner_dir = _all_eats(color, board_test)
    eat_queen_dir = _all_eats(color.upper(), board_test)
    try:
        linear_eats = checker_eat(eat_liner_dir, color,board_test)
    except:
        linear_eats = []
    try:
        queen_eats = checker_eat(eat_queen_dir, color.upper(), board_test)
    except:
        queen_eats = []
    ans = sorted([linear_eats, queen_eats], key=lambda x: len(x))[-1]
    if ans[-1][0] == 7:
        if color == 'b':
            ans += add_bite(ans[-1], ans[-2], board_test)
    if ans[-1][0] == 0:
        if color == 'w':
            ans += add_bite(ans[-1], ans[-2], board_test)
    color = opposite_color[color]
    return ans

def _dangerous_moves_non_eat(steps: dict) -> dict:
    norm_moves = defaultdict(list)
    for key, value in steps.items():
        for step in value:
            temp_board = [[board[y][x] for x in range(len(board[0]))] for y in range(len(board))]
            temp_board[step[0]][step[1]] = color
            temp_board[key[0]][key[1]] = '_'

            up_left_y, up_left_x = _up_left(step[0], step[1])
            up_right_y, up_right_x = _up_right(step[0], step[1])
            down_left_y, down_left_x = _down_left(step[0], step[1])
            down_rigth_y, down_right_x = _down_right(step[0], step[1])
            if up_left_y < 0 or up_left_x < 0 or up_right_y < 0 or up_right_x > board_size - 1 or down_left_y > board_size - 1 or down_left_x < 0 or down_rigth_y > board_size - 1 or down_right_x > board_size - 1:
                norm_moves[key].append(step)
                continue
            if (temp_board[up_left_y][up_left_x] == opposite_color[color] and temp_board[down_rigth_y][down_right_x] ==
                '_') or (
                    temp_board[up_left_y][up_left_x] == '_' and temp_board[down_rigth_y][down_right_x] ==
                    opposite_color[color]):
                continue
            if (temp_board[up_right_y][up_right_x] == opposite_color[color] and temp_board[down_left_y][down_left_x] ==
                '_') or (
                    temp_board[up_right_y][up_right_x] == '_' and temp_board[down_left_y][down_left_x] ==
                    opposite_color[color]):
                continue
            norm_moves[key].append(step)
    if norm_moves == {}:
        return steps
    else:
        return norm_moves


def is_queen_here():
    queens = []
    for y, vert in enumerate(board):
        for x, hor in enumerate(vert):
            if board[y][x] == color.upper():
                queens.append((y, x))
    return queens


def _test_possible_moves(posible_moves, color):
    answ = defaultdict(list)
    for k, v in posible_moves.items():
        for item in v:
            if board[item[0]][item[1]] == opposite_color[color]:
                continue
            else:
                answ[k].append(item)
    return answ


def checker_eat(eat, cher, board):
    pos_eat = []
    for k, v in eat.items():
        for item in v:
            temp = [k, item]
            i = len(temp)
            while i == len(temp):
                test = eat_all_dir(temp[-1][0], temp[-1][1], cher, board)
                if test != []:
                    if test[-1] in temp[:-1]:
                        break
                    temp.append(test[-1])
                i += 1
            pos_eat.append(temp)
    sorted_moves = sorted(pos_eat, key=lambda x: len(x))
    norm_moves = _dengerous_moves(sorted_moves)

    ans = norm_moves
    return ans


def add_bite(last, m_last, board):
    for y, vert in enumerate(board):
        for x, hor in enumerate(vert):
            if board[y][x] == color.upper():
                board[y][x] = color
    if color == 'b':
        if m_last[1] > last[1]:
            board[6][last[1] + 1] = '_'
        else:
            board[6][last[1] - 1] = '_'
        board[7][last[1]] = 'B'
    if color == 'w':
        if m_last[1] > last[1]:
            board[1][last[1] + 1] = '_'
        else:
            board[1][last[1] - 1] = '_'
        board[0][last[1]] = 'W'
    eat_queen_dir = _all_eats(color.upper(), board)
    try:
        queen_eats = checker_eat(eat_queen_dir, color.upper())
        return queen_eats[1:]
    except:
        queen_eats = []
        return []


def if_i_can_be_beaten():
    import itertools
    global color
    color = opposite_color[color]
    eat_liner_dir = _all_eats(color, board_oppozite)
    eat_queen_dir = _all_eats(color.upper(), board_oppozite)
    under_attack = list(eat_liner_dir.values()) + list(eat_queen_dir.values())
    under_attack = list(itertools.chain(*under_attack))
    color = opposite_color[color]

    go_away = []
    for key, value in eat_liner_dir.items():
        for v in value:
            for dir in directions_dict['W']:
                y1, x1 = dir(key[0], key[1])
                y2, x2 = dir(y1, x1)
                if (y1 < 0 or y1 > board_size - 1 or x1 < 0 or x1 > board_size - 1) and (
                        y2 < 0 or y2 > board_size - 1 or x2 < 0 or x2 > board_size - 1):
                    continue
                if board[y1][x1] in (color, color.upper()) and (y2, x2) == v:
                    go_away.append((y1, x1))
                    break
    for key, value in eat_queen_dir.items():
        for v in value:
            for dir in directions_dict['W']:
                y1, x1 = dir(key[0], key[1])
                y2, x2 = dir(y1, x1)
                if (y1 < 0 or y1 > board_size - 1 or x1 < 0 or x1 > board_size - 1) and (
                        y2 < 0 or y2 > board_size - 1 or x2 < 0 or x2 > board_size - 1):
                    continue
                if board[y1][x1] in (color, color.upper()) and (y2, x2) == v:
                    go_away.append((y1, x1))
                    break
    return under_attack, go_away


def main_func():
    possible_moves = _get_cells_with_moves(board, color)
    possible_moves = _dangerous_moves_non_eat(possible_moves)
    possible_q = _get_cells_with_moves(board, color.upper())
    possible_q = _dangerous_moves_non_eat(possible_q)
    possible_q = _test_possible_moves(possible_q, color)
    possible_moves.update(possible_q)
    eat_liner_dir = _all_eats(color, board)
    eat_queen_dir = _all_eats(color.upper(), board)

    if len(eat_liner_dir) == 0 and len(eat_queen_dir) == 0:
        possible_moves = _test_possible_moves(possible_moves, color)
        under_attack, safe_me = if_i_can_be_beaten()
        if under_attack != [] and list(possible_moves.keys()) != []:
            for k, v in possible_moves.items():
                for vers in v:
                    if vers in under_attack:
                        print(1)
                        print(k[0], k[1])
                        print(vers[0], vers[1])
                        return None
        possible_q = _get_cells_with_moves(board, color.upper())  # вначале спасаем дамку
        possible_q = _test_possible_moves(possible_q, color)
        if safe_me != [] and list(possible_q.keys()) != []:
            for safe in safe_me:
                if safe in list(possible_q.keys()):
                    print(1)
                    print(safe[0], safe[1])
                    ans = possible_q[safe][-1]
                    print(ans[0], ans[1])
                    return None

        if safe_me != [] and list(possible_moves.keys()) != []:
            for safe in safe_me:
                if safe in list(possible_moves.keys()):
                    print(1)
                    print(safe[0], safe[1])
                    ans = possible_moves[safe][-1]
                    print(ans[0], ans[1])
                    return None

        if list(possible_moves.keys()) == []:
            possible_moves = _get_cells_with_moves(board, color)
            possible_moves = _test_possible_moves(possible_moves, color)

        try:
            # a = sorted(list(possible_moves.keys()), key=lambda x: x[0])[-1] if color == 'b' else \
            # sorted(list(possible_moves.keys()), key=lambda x: x[0])[0]
            random_step = choice(list(possible_moves.keys()))
            print(1)
            print(random_step[0], random_step[1])
            next_step = choice(possible_moves[random_step])
            print(next_step[0], next_step[1])
        except:
            possible_moves = _get_cells_with_moves(board, color.upper())
            possible_moves = _test_possible_moves(possible_moves, color)
            if list(possible_moves.keys()) == []:
                possible_moves = _get_cells_with_moves(board, color)
                possible_moves = _test_possible_moves(possible_moves, color)
            random_step = choice(list(possible_moves.keys()))
            print(1)
            print(random_step[0], random_step[1])
            next_step = choice(possible_moves[random_step])
            print(next_step[0], next_step[1])
    else:
        try:
            linear_eats = checker_eat(eat_liner_dir, color, board)

        except:
            linear_eats = []
        try:
            queen_eats = checker_eat(eat_queen_dir, color.upper(), board)
        except:
            queen_eats = []
        ans = sorted([linear_eats, queen_eats], key=lambda x: len(x))[-1]
        if ans[-1][0] == 7:
            if color == 'b':
                ans += add_bite(ans[-1], ans[-2], board)
        if ans[-1][0] == 0:
            if color == 'w':
                ans += add_bite(ans[-1], ans[-2], board)
        print(len(ans) - 1)
        for item in ans:
            print(item[0], item[1])


if __name__ == '__main__':
    # color = input()
    # board_size = int(input())
    # board = [[j for j in input().strip()] for i in range(board_size)]

    color = 'w'
    board_size = 8
    board = [['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', 'b', '_', '_', '_', '_', '_'],
             ['_', 'b', '_', 'b', '_', '_', '_', 'b'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', 'w', '_', 'w', '_', 'b', '_', '_'],
             ['_', '_', '_', '_', 'w', '_', 'w', '_'],
             ['_', '_', '_', '_', '_', 'w', '_', 'w'],
             ['_', '_', '_', '_', '_', '_', '_', '_']]




    board_oppozite = [[board[y][x] for x in range(len(board[0]))] for y in range(len(board))]

    directions_dict = {'w': (_up_right, _up_left),
                       'b': (_down_left, _down_right),
                       'W': (_up_right, _up_left, _down_left, _down_right),
                       'B': (_up_right, _up_left, _down_left, _down_right)}

    opposite_dirs = {_up_right: _down_left,
                     _down_left: _up_right,
                     _up_left: _down_right,
                     _down_right: _up_left}
    opposite_color = {'w': 'b',
                      'b': 'w'}

    for y, vert in enumerate(board):
        for x, hor in enumerate(vert):
            if board[y][x] == opposite_color[color].upper():
                board[y][x] = opposite_color[color]

    for y, vert in enumerate(board_oppozite):
        for x, hor in enumerate(vert):
            if board_oppozite[y][x] == color.upper():
                board_oppozite[y][x] = color

    main_func()

    for i in board:
        print(i)
        print()