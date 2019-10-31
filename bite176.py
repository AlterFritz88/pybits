WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    item1 = ' #'
    item2 = '# '
    horisontal_1 = item1 * int(size/2)
    horisontal_2 = item2 * int(size/2)
    for i in range(int(size / 2)):
        print(horisontal_1)
        print(horisontal_2)


create_chessboard(size=2)