def front_x(words):
    words_x =  [x for x in words if len(x) > 1 and  x[0] == 'x']
    not_x = [x for x in words if x not in words_x]
    return sorted(words_x) + sorted(not_x)


print(front_x(['x-files', 'xapple',  '', 'apple', 'extra', 'mix', 'xyz']))