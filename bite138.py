class Animal:
    counter = 10001
    animal_list = []
    def __init__(self, name):
        self.name = name
        self.count = Animal.counter
        Animal.counter += 1
        Animal.animal_list.append((self.count, self.name))

    def __str__(self):
        return '{}. {}'.format(self.count, self.name.capitalize())
    @classmethod
    def zoo(cls):
        ans = []
        for ani in  cls.animal_list:
            ans.append('{}. {}'.format(ani[0], ani[1].capitalize()))
        return ans


dog = Animal('dog')
cat = Animal('cat')
print(str(cat))
print(Animal.zoo())