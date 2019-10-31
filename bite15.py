names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    n = 1
    for name, countrie in zip(names, countries):
        print('{}. {}'.format(n, name) + ' ' * (11 - len(name)) + countrie)
        n += 1

enumerate_names_countries()