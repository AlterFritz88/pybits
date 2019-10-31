DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    grid = _transform_grid(grid)
    star_y, star_x = len(grid[0]) // 2, len(grid[0]) // 2

    answer = []
    li, pos_y, pos_x = _right(star_y, star_x, grid)
    answer.append([1])
    answer[0] += li


    while answer[-1][-2] != grid[0][-1]:
        li, pos_y, pos_x = _down(pos_y, pos_x, grid)
        answer.append(li)
        li, pos_y, pos_x = _left(pos_y, pos_x, grid)
        answer.append(li)
        li, pos_y, pos_x = _top(pos_y, pos_x, grid)
        answer.append(li)
        li, pos_y, pos_x = _right(pos_y, pos_x, grid)
        answer.append(li)

    answer[-1] = answer[-1][:-1]
    for row in answer:
        print(' '.join([str(x) for x in row]))


def _right(pos_y, pos_x, grid):
    list_map = []
    while grid[pos_y][pos_x + 1] == grid[pos_y][pos_x] + 1:
        pos_x += 1
        list_map.append(grid[pos_y][pos_x])

        if pos_x + 1 >= len(grid):
            break
    list_map.append(DOWN)
    return list_map, pos_y, pos_x


def _down(pos_y, pos_x, grid):
    list_map = []
    while grid[pos_y + 1][pos_x] == grid[pos_y][pos_x] + 1:
        pos_y += 1
        list_map.append(grid[pos_y][pos_x])

        if pos_y + 1 >= len(grid):
            break
    list_map.append(LEFT)
    return list_map, pos_y, pos_x


def _left(pos_y, pos_x, grid):
    list_map = []
    while grid[pos_y][pos_x - 1] == grid[pos_y][pos_x] + 1:
        pos_x -= 1
        list_map.append(grid[pos_y][pos_x])
        if pos_x - 1 < 0:
            break
    list_map.append(UP)
    return list_map, pos_y, pos_x


def _top(pos_y, pos_x, grid):
    list_map = []
    while grid[pos_y - 1][pos_x] == grid[pos_y][pos_x] + 1:
        pos_y -= 1
        list_map.append(grid[pos_y][pos_x])
        if pos_y - 1 < 0:
            break
    list_map.append(RIGHT)
    return list_map, pos_y, pos_x


def _transform_grid(grid):
    grid = [x for x in grid.split('\n')[1:-1] if '|' not in x]
    new_grid = []
    for line in grid:
        new_line = []
        for char in line.split(' '):
            try:
                new_line.append(int(char))
            except:
                continue
        new_grid.append(new_line)
    grid = new_grid[:]
    return grid


small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

print_sequence_route(small_grid)
