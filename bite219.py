from datetime import date, timedelta

TODAY = date(2019, 8, 25)


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    while 1:
        start_date += timedelta(days=num_days)
        for i in range(num_bites):

            yield start_date


gen = gen_bite_planning(num_bites=2, num_days=3, start_date=TODAY)
for _ in range(10):
    print(next(gen))