if __name__ == "__main__":
    #board_size = int(input())
    #board = [[j for j in input().strip()] for i in range(board_size)]
    # print(board)
    board = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', 'h', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
    for i in board:
        print(i)

    def _without_hs():
        for vert in range(len(board)):
            for hor in range(len(board[0])):
                if hor + 5 < len(board[0]) + 1:
                    if 'm' not in board[vert][hor: hor+5] and 'd' not in board[0][hor: hor+5]:
                        for part in range(hor, hor+5):
                            prob_board[vert][part] += 1

        for vert in range(len(board[0])):

            for hor in range(len(board)):
                if hor + 5 < len(board) + 1:
                    line = [board[x][vert] for x in range(hor, hor+5)]
                    if 'm' not in line and 'd' not in line:
                        for part in range(hor, hor+5):
                            prob_board[part][vert] += 1
        maximum = (1000, 1000, 0)

        for i, row in enumerate(prob_board):
            if maximum[2] < max(row):
                maximum = (i, row.index(max(row)), max(row))

        print(maximum[0], maximum[1])


    prob_board = [[0 for x in range(len(board[0]))] for y in range(len(board))]
    for i in prob_board:
        print(i)
    print()


    def _get_hs(board):
        hs = []
        for i, y in enumerate(board):
            for j, x in enumerate(y):
                if board[i][j] == 'h':
                    hs.append((i, j))
        return hs

    hs = _get_hs(board)
    if hs == []:
        _without_hs()

    else:
        for h in hs:

            for size in range(2, 4):
                if h[1]+size < len(board) + 1:
                    line = board[h[0]][h[1]:h[1]+size]
                    if 'm' not in line and 'd' not in line:

                        for part in range(h[1], h[1]+size):
                            prob_board[h[0]][part] += 1
            for size in range(2, 4):
                if h[1]-size >= -1:
                    line = board[h[0]][h[1]-size+1:h[1]+1]
                    if 'm' not in line and 'd' not in line:

                        for part in range(h[1]-size+1, h[1]+1):
                            prob_board[h[0]][part] += 1

            for size in range(2, 4):
                if h[0] + size < len(board[0]) + 1:
                    print((h[0], h[0] + size))
                    #line = board[h[0]][h[1]:h[1] + size]
                    line = [board[x][h[1]] for x in range(h[0], h[0] + size)]
                    print(line)
                    if 'm' not in line and 'd' not in line:

                        for part in range(h[1], h[1] + size):
                            prob_board[h[0]][part] += 1

        for h in hs:
            prob_board[h[0]][h[1]] = 0

    for i in prob_board:
        print(i)