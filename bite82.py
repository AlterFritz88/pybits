from enum import Enum

THUMBS_UP = '*👍'  # in case you go f-string ...

# move these into an Enum:
BEGINNER = 2
INTERMEDIATE = 3
ADVANCED = 4
CHEATED = 1

class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return '{} => {}'.format(self.name, self.value*THUMBS_UP)

    @classmethod
    def average(self):
        return sum([color.value for color_name, color in self.__members__.items()]) / len(self.__members__.items())



a = Score(1)

print(Score.average())