class Person():
    def __str__(self):
       return 'I am a person'

class Father(Person):
    def __str__(self):
        return super().__str__() + ' and cool daddy'

class Mother(Person):
    def __str__(self):
        return super().__str__() + ' and awesome mom'

class Child(Father, Mother):
    def __str__(self):
        return 'I am the coolest kid'

person = Person()
dad = Father()
mom = Mother()
child = Child()

print(person)
print(dad)
print(mom)
print(child)

print(Child.__mro__)



import inspect
substr = 'I am a person'
for src in (inspect.getsource(Father), inspect.getsource(Mother)):
    print(src)
    assert substr not in src