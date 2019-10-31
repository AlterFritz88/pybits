class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.top = 0

    def __call__(self, num):
        if num > self.top:
            self.top = num
            return num
        else:
            return self.top


record = RecordScore()
print(record(10))
print(record(9))
print(record(11))
print(record(7))