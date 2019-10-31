def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) == dict:
        return data.keys(), data.values()
    else:
        names = [x.name for x in data]
        since_days = [x.since_days for x in data]
        karma_point = [x.karma_point for x in data]
        bitecoin_earned = [x.bitecoin_earned for x in data]
        return names, since_days, karma_point, bitecoin_earned