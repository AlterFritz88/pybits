from random import choice, seed


def _without_hs():
    list_dead_boats = []
    boat_5 = is_where_5_size_ship(5)
    if boat_5 == 1:
        list_dead_boats.append(5)
    boat_4 = is_where_5_size_ship(4)
    if boat_4 == 1:
        list_dead_boats.append(4)
    boat_3 = is_where_5_size_ship(3)
    if boat_3 == 1:
        list_dead_boats.append(3)
    boat_2 = is_where_5_size_ship(2)
    if boat_2 == 2:
        list_dead_boats.append(2)

    for boat_size in range(1, 6):
        if boat_size in list_dead_boats:
            continue
        for vert in range(len(board)):
            for hor in range(len(board[0])):
                if hor + boat_size < len(board[0]) + 1:
                    if 'm' not in board[vert][hor: hor + boat_size] and 'd' not in board[vert][hor: hor + boat_size]:
                        for part in range(hor, hor + boat_size):
                            prob_board[vert][part] += 1

        for vert in range(len(board[0])):

            for hor in range(len(board)):
                if hor + boat_size < len(board) + 1:
                    line = [board[x][vert] for x in range(hor, hor + boat_size)]
                    if 'm' not in line and 'd' not in line:
                        for part in range(hor, hor + boat_size):
                            prob_board[part][vert] += 1

    # for i in prob_board:
    #     print(i)
    # print()

    for i, y in enumerate(prob_board):
        for j, x in enumerate(y):
            if board[i][j] in ('d', 'm'):
                prob_board[i][j] = 0

    ans = choice(_get_maximum_prob(prob_board))
    print(ans[0], ans[1])


def _with_hs(hs):
    if len(hs) == 1:
        for h in hs:

            for size in range(2, 5):
                if h[1] + size < len(board) + 1:
                    line = board[h[0]][h[1]:h[1] + size]
                    if 'm' not in line and 'd' not in line:

                        for part in range(h[1], h[1] + size):
                            prob_board[h[0]][part] += 1
            for size in range(2, 5):
                if h[1] - size >= -1:
                    line = board[h[0]][h[1] - size + 1:h[1] + 1]
                    if 'm' not in line and 'd' not in line:
                        for part in range(h[1] - size + 1, h[1] + 1):
                            prob_board[h[0]][part] += 1

            for size in range(2, 5):
                if h[0] + size < len(board[0]) + 1:
                    line = [board[x][h[1]] for x in range(h[0], h[0] + size)]
                    if 'm' not in line and 'd' not in line:

                        for part in range(h[0], h[0] + size):
                            prob_board[part][h[1]] += 1

            for size in range(2, 5):
                if h[0] - size >= -1:

                    line = [board[x][h[1]] for x in range(h[0] - size + 1, h[0] + 1)]

                    if 'm' not in line and 'd' not in line:

                        for part in range(h[0] - size + 1, h[0] + 1):
                            prob_board[part][h[1]] += 1
    else:
        where = _get_hor_ver_hitten_boat(board)
        if where == 'horizontal':
            for h in hs:
                for size in range(2, 5):
                    if h[1] + size < len(board) + 1:
                        line = board[h[0]][h[1]:h[1] + size]
                        if 'm' not in line and 'd' not in line:

                            for part in range(h[1], h[1] + size):
                                prob_board[h[0]][part] += 1
                for size in range(2, 5):
                    if h[1] - size >= -1:
                        line = board[h[0]][h[1] - size + 1:h[1] + 1]
                        if 'm' not in line and 'd' not in line:
                            for part in range(h[1] - size + 1, h[1] + 1):
                                prob_board[h[0]][part] += 1
        else:
            for h in hs:
                for size in range(2, 5):
                    if h[0] + size < len(board[0]) + 1:
                        line = [board[x][h[1]] for x in range(h[0], h[0] + size)]
                        if 'm' not in line and 'd' not in line:

                            for part in range(h[0], h[0] + size):
                                prob_board[part][h[1]] += 1

                for size in range(2, 5):
                    if h[0] - size >= -1:

                        line = [board[x][h[1]] for x in range(h[0] - size + 1, h[0] + 1)]

                        if 'm' not in line and 'd' not in line:

                            for part in range(h[0] - size + 1, h[0] + 1):
                                prob_board[part][h[1]] += 1
    for h in hs:
        prob_board[h[0]][h[1]] = 0

    # for i in prob_board:
    #    print(i)

    ans = choice(_get_maximum_prob(prob_board))
    print(ans[0], ans[1])


def _get_hor_ver_hitten_boat(board):
    for i, vert in enumerate(board):
        for j, hor in enumerate(vert[:-1]):
            if board[i][j + 1] == 'h' and board[i][j] == 'h':
                return 'horizontal'

    return 'vertical'


def _get_maximum_prob(prob_board):
    maximum = 0
    for i, row in enumerate(prob_board):
        if maximum < max(row):
            maximum = max(row)
    max_list = []
    for i, y in enumerate(prob_board):
        for j, x in enumerate(y):
            if prob_board[i][j] == maximum:
                max_list.append((i, j))
    return max_list


def _get_hs(board):
    hs = []
    for i, y in enumerate(board):
        for j, x in enumerate(y):
            if board[i][j] == 'h':
                hs.append((i, j))
    return hs


def do_hit(board):
    hs = _get_hs(board)
    if hs == []:
        _without_hs()
    else:
        _with_hs(hs)


def is_where_5_size_ship(size):
    boat_counter = 0
    for vert in range(len(board)):
        for hor in range(len(board[0])):
            if hor + size < len(board[0]) + 1:
                if board_dead[vert][hor: hor + size] == ['d'] * size:
                    boat_counter += 1
                    for part in range(hor, hor + size):
                        board_dead[vert][part] = '-'

    for vert in range(len(board[0])):

        for hor in range(len(board)):
            if hor + size < len(board) + 1:
                line = [board_dead[x][vert] for x in range(hor, hor + size)]
                if line == ['d'] * size:
                    boat_counter += 1
                    for part in range(hor, hor + size):
                        board_dead[part][vert] = '-'


def my_step(board_size):
    global prob_board
    global board_dead
    global board
    board = [[j for j in input().strip()] for i in range(int(board_size))]

    # board = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', 'd', 'd', 'd', 'd', 'd', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', 'd', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', 'd', '-', 'h', 'h', 'h', '-', '-', '-'],
    #          ['-', '-', 'd', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', 'd', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', 'd', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
    seed(5555)
    prob_board = [[0 for x in range(len(board[0]))] for y in range(len(board))]
    board_dead = [[x for x in y] for y in board]

    do_hit(board)
prob_board = []
board_dead = []
board = []
if __name__ == "__main__":


    board_size = input()

    if board_size != 'INIT':
        my_step(board_size)
    else:
        print('3 0')
        print('3 3')
        print('6 4:7 4')
        print('3 7:3 8')
        print('7 7:7 9')
        print('1 4:4 4')
        print('4 0:8 0')