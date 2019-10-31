from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, n):
        self.n = n
        self.count = 0



    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        else:
            self.count += 1
            return choice(COLORS) + ' egg'

egg = EggCreator(3)

print(next(egg))