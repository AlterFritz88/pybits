from decimal import Decimal



class IntList(list):


    @property
    def mean(self):
        return sum(self) / len(self)

    @property
    def med(self):
        return self[len(self)//2]

    def append(self, object) -> None:
        try:
            num = int(object)
        except:
            raise TypeError

        super(IntList, self).append(num)

    def __add__(self, other):
        try:
            new = [int(x) for x in other]
            print(new)
            return super(IntList, self).__add__(new)
        except:
            raise TypeError

    def __iadd__(self, other):
        try:
            new = [int(x) for x in other]
            print(new)
            return super(IntList, self).__iadd__(new)
        except:
            raise TypeError

li = IntList([2, 3, 4, 5, 7])
print(li)
print(li.mean)
print(li.med)

li.append(Decimal(11))

li += [14, 88]
print(li)