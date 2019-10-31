import re

string = '#google.org'

def cut_the_string(string):

    if string[0] == '#':
        result = re.sub(r'#', '', string)

    if string[0:4] == 'www.':
        result = re.sub(r'www\.', '', string)
        result = re.sub(r'\.\w+', '', result)

    return result