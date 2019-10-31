from functools import singledispatch


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!

    raise ValueError


@count_down.register(int)
def _print_int(arg):
    arg1 = str(arg)
    for i in range(len(arg1), 0, -1):
        print(arg1[:i])

@count_down.register(float)
def _print_int(arg):
    arg1 = str(arg)
    for i in range(len(arg1), 0, -1):
        print(arg1[:i])

@count_down.register(str)
def _print_int(arg):
    for i in range(len(arg), 0, -1):
        print(arg[:i])

@count_down.register(list)
def _print_int(arg):
    for i in range(len(arg), 0, -1):
        print(''.join(str(x) for x in arg[:i]))

@count_down.register(set)
def _print_int(arg):
    arg = list(arg)
    for i in range(len(arg), 0, -1):
        print(''.join(str(x) for x in arg[:i]))

@count_down.register(tuple)
def _print_int(arg):
    for i in range(len(arg), 0, -1):
        print(''.join(str(x) for x in arg[:i]))

@count_down.register(range)
def _print_int(arg):
    arg = list(arg)
    for i in range(len(arg), 0, -1):
        print(''.join(str(x) for x in arg[:i]))

@count_down.register(dict)
def _print_int(arg):
    keys = list(arg.keys())
    values = list(arg.values())
    for i in range(len(keys), 0, -1):
        print(''.join(str(x) for x in keys[:i]))


count_down('1234')