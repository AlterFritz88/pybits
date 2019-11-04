n = 101
def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in range(100, 0, -1):

        if i == 1:
            raise StopIteration
        yield i

cd = countdown()
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))