from dataclasses import dataclass

@dataclass
class Bite():
    number: int
    title: str
    level: str = 'Beginner'

    def __post_init__(self):
        self.title = self.title.capitalize()

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.number < other.number
    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.number > other.number

b1 = Bite(number=1, title="sum of numbers")
print(b1.title)