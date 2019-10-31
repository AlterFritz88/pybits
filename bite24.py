from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number, title):
        self.number = number
        self.title = title
    @abstractmethod
    def verify(self):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    def __init__(self,number, title, merged_prs):
        self.merged_prs = merged_prs
        super(BlogChallenge,self).__init__(number, title)
    @property
    def pretty_title(self):
        return 'PCC{} - {}'.format(self.number, self.title)

    def verify(self, num):
        return num in self.merged_prs


class BiteChallenge(Challenge):
    def __init__(self, number, title, result):
        self.result = result
        super(BiteChallenge, self).__init__(number, title)

    @property
    def pretty_title(self):
        return 'Bite {}. {}'.format(self.number, self.title)

    def verify(self, some):
        return some == self.result

ch = BlogChallenge(1, 'Wordvalues', [41, 42, 44])
print(ch.pretty_title)