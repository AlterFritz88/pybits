def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    my = set(my_cities)
    other = set(other_cities)
    return len(my.difference(other)) * 2


my_cities = ['Rome', 'Paris', 'Madrid']
other_cities = ['Chicago', 'Seville', 'Berlin']

print(uncommon_cities(my_cities, other_cities))