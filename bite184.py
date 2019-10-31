from csv import DictReader
from os import path
from urllib.request import urlretrieve

from collections import Counter

DATA = path.join('temp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(data, newline='') as csvfile:
            reader = DictReader(csvfile)
            return [[row['bite'], row['user'], row['completed']] for row in reader]

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(set([x[0] for x in self.rows]))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(set([(x[0], x[2]) for x in self.rows if x[2] == 'True']))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(set([x[1] for x in self.rows]))

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len(set([x[1] for x in self.rows if x[2] == 'True']))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        all_bites = [x[0] for x in self.rows]
        return Counter(all_bites).most_common()[0][0]


    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        all_users = [x[1] for x in self.rows if x[2] == 'True']
        return Counter(all_users).most_common()[0][0]


my_class = BiteStats(DATA)
print(my_class.rows)
print(my_class.number_bites_accessed)
print(my_class.number_bites_resolved)
print(my_class.number_users_active)
print(my_class.number_users_solving_bites)
print(my_class.top_bite_by_number_of_clicks)
print(my_class.top_user_by_bites_completed)