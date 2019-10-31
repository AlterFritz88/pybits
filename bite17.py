from itertools import combinations, permutations

def friends_teams(friends, team_size=2, order_does_matter=False):
    if not order_does_matter:
        return combinations(friends, team_size)
    else:
        return permutations(friends, team_size)

friends = 'Bob Dante Julian Martin'.split()

print(len(list(friends_teams(friends, 3, True))))