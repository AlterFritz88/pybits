import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
#color_values_module = os.path.join('tmp', 'color_values.py')
#urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
#                           color_values_module)
#sys.path.append('tmp')

# should be importable now
from tmp.color_values import COLOR_NAMES  # noqa E402
print(COLOR_NAMES)

class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = COLOR_NAMES.get(color.upper(), None)
        self.color = color

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts a hex value into an rgb one"""
        if type(rgb) != tuple:
            raise ValueError
        if rgb[0] not in range(0, 256) or rgb[1] not in range(0, 256) or rgb[2] not in range(0, 256):
            raise ValueError
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts an rgb value into a hex one"""
        if type(hex) != str or len(hex) != 7:
            raise ValueError
        return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:], 16))


    def __repr__(self):
        """Returns the repl of the object"""
        return "Color('{}')".format(self.color)

    def __str__(self):
        """Returns the string value of the color object"""
        return '({}, {}, {})'.format(self.rgb[0], self.rgb[1], self.rgb[2])


a = Color('ALICEBLUE')
print(Color.rgb2hex((1, 0, 255)))
print(Color.hex2rgb('#0100ff'))
print(str(a))
print(repr(a))