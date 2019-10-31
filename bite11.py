class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return '{} account - balance: {}'.format(self.name, self.balance)

    def __getitem__(self, i):
        return self._transactions[i]

    def __iter__(self):
        for each in self._transactions:
            yield each

    def __add__(self, other):
        if type(other) != int:
            raise TypeError
        self._transactions.append(other)

    def __sub__(self, other):
        if type(other) != int:
            raise TypeError
        self._transactions.append(-other)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance



acc = Account('my_acc', 0)


acc + 1

acc + 2

acc - 2



acc1 = Account('master_card', 7)

print(acc.balance)
print(acc1.balance)
print(str(acc1))
print(acc < acc1)


