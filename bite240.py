from functools import total_ordering


@total_ordering
class Account:
    'A simple account class'

    def __init__(self, owner, amount=0):
        'This is the constructor that lets us create objects from this class'
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(self.owner,
                                                               self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = '{}&{}'.format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc


import pytest

def test_repr():
    acc = Account("Sasha", 55)
    assert "Account('Sasha', 55)" == repr(acc)

def test_str():
    acc = Account("Sasha", 55)
    assert 'Account of Sasha with starting amount: 55' == str(acc)

def test_zero_init():
    acc = Account("Sasha")
    assert 0 == acc.balance

def test_transaction_not_int():
    acc = Account("Sasha", 55)
    with pytest.raises(ValueError) as excinfo:
        acc.add_transaction('11212')
    assert str(excinfo.value) == 'please use int for amount'

def test_transaction():
    acc = Account("Sasha", 55)
    acc.add_transaction(32)
    assert len(acc._transactions) == 1

def test_balance():
    acc = Account("Sasha", 55)
    acc.add_transaction(32)
    assert acc.balance == 87

def test_len_trans():
    acc = Account("Sasha", 55)
    acc.add_transaction(32)
    assert 1 == len(acc)

def test_position():
    acc = Account("Sasha", 55)
    acc.add_transaction(14)
    acc.add_transaction(88)
    assert 14 == acc[0]
    assert 88 == acc[1]

def test_equal():
    acc1 = Account("Sasha", 55)
    acc2 = Account("Ivan", 55)
    acc3 = Account("Putin", 14)
    assert acc1 == acc2
    assert not acc1 == acc3

def test_litle():
    acc1 = Account("Sasha", 55)
    acc2 = Account("Ivan", 55)
    acc3 = Account("Putin", 14)
    assert acc3 < acc2
    assert not acc1 < acc3
    assert not acc1 == acc3
    assert not acc1 < acc2


def test_add():
    acc1 = Account("Sasha", 55)
    acc2 = Account("Ivan", 50)
    acc2.add_transaction(50)
    new_acc = acc1 + acc2
    assert 155 == new_acc.balance
    assert "Sasha&Ivan" == new_acc.owner