THUMBS_UP, THUMBS_DOWN = '1👍', '👎0'


class Thumbs:
    def __mul__(self, other):
        if other == 0:
            raise ValueError('Specify a number')
        if other > 0:
            sym = THUMBS_UP
        if other < 0:
            sym = THUMBS_DOWN
        if abs(other) < 4:
            return abs(other) * sym
        else:
            return sym + " ({}x)".format(abs(other))

    def __rmul__(self, other):
        if other == 0:
            raise ValueError('Specify a number')
        if other > 0:
            sym = THUMBS_UP
        if other < 0:
            sym = THUMBS_DOWN
        if abs(other) < 4:
            return abs(other) * sym
        else:
            return sym + " ({}x)".format(abs(other))


th = Thumbs()
th * 1
th * 4
-4 * th