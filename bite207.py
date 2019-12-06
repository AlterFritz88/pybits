from random import random
from time import sleep


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    def wrapper(self):
        if self.mass == None:
            print("NONE")
            func(self)
        else:
            print('here')
            return self.mass
    return wrapper


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'
    mass = None
    def __init__(self, color):
        self.color = color
        #self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    @property
    def mass(self):
        if not hasattr(self, '_mass'):
            scale_factor = random()
            sleep(self.TEMPORAL_SHIFT)
            self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                          f'{self.SOLAR_MASS_UNITS}')
            return self._mass
        else:
            return self._mass

    @mass.setter
    def mass(self, value):
        raise AttributeError
        #self._mass = value


mars = Planet('mars')
print(mars.mass)
print(mars.mass)
print(mars.mass)
mars.mass = 5