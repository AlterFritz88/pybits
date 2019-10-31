MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        #super(BirthdayDict, self).__init__()
        self.update(*args, **kwargs)


    def __setitem__(self, name, birthday):

        if (birthday.day, birthday.month) in [(x.day, x.month) for x in self.values()]:
            print(MSG.format(name))
        #super(BirthdayDict, self).values()
        super(BirthdayDict, self).__setitem__(name, birthday)

from datetime import date

bd = BirthdayDict()
bd['bob'] = date(1987, 6, 15)
bd['tim'] = date(1984, 7, 15)
bd['mary'] = date(1987, 6, 15)  # whole date match
bd['sara'] = date(1987, 6, 14)
bd['mike'] = date(1981, 7, 15)
print(bd)