class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        self.temp_balance = self.balance
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.balance < 0:
            self._transactions = [0]

acc = Account()
print(acc.balance)
acc - 5
print(acc.balance)


with acc as a:
    a - 5
print(acc.balance)