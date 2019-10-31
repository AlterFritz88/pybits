import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '

def generate_table(*columns):
    print(columns)
    for i in range(len(columns[0])):
        yield SEPARATOR.join([str(x[i]) for x in columns])

print(list(generate_table(names, aliases, points)))