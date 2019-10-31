scores = [range(10, 50), range(50, 100), range(100, 175), range(175, 250), range(250, 400), range(400, 600), range(600, 800), range(800, 1000), range(1000, 10000000)]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(ranks, scores))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for k, v in BELTS.items():
            if new_score in v:
                return k

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if type(new_score) != int:
            raise ValueError
        if new_score < self._score:
            raise ValueError
        self._score = new_score

        if self._last_earned_belt != self._get_belt(new_score):
            self._last_earned_belt = self._get_belt(new_score)
            print('Congrats, you earned {} points obtaining the PyBites Ninja {} Belt'.format(self._score, self._last_earned_belt.capitalize()))
        else:
            print('Set new score to {}'.format(self._score))

    score = property(_get_score, _set_score)

nin = NinjaBelt()
nin.score =50
nin.score =70
print(nin.score)