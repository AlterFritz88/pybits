from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:

    #expired = True if (expires < datetime.now()) else False
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires
        self.expired = True if datetime.now() < self.expires else False

future_date = NOW + timedelta(days=1)
a = Promo('eee', future_date)
print(a.expired)