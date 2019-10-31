class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""

        matrix = []
        for i in range(1, length+1):
            matrix.append([i*x for x in range(1, length+1)])
        self._table = matrix


    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) * len(self._table[0])

    def __str__(self):
        """Returns a string representation of the table"""
        s = []
        for i in self._table:
            s.append(' | '.join([str(x) for x in i]))
        return '\n'.join(s)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        if x > len(self._table) or y > len(self._table[0]):
            raise IndexError
        return self._table[x-1][y-1]


t = MultiplicationTable(5)
print(str(t))