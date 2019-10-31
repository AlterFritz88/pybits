def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    sets = [set(item) for item in programmers.values()]
    return set.intersection(*sets)


prog = {'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
 'paul': ['C++', 'JS', 'Python'],
 'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
 'tim': ['Python', 'Haskell', 'C++', 'JS']}

print(common_languages(prog))