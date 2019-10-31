names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    fs = {x:[] for x in users.keys()}
    for friends in friendships:
        fs[friends[0]].append(users[friends[1]])
        fs[friends[1]].append(users[friends[0]])
    num_fs = sorted(fs, key= lambda x:len(fs[x]))[-1]
    return users[num_fs], fs[num_fs]

print(get_friend_with_most_friends())

friendships1 = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
print(get_friend_with_most_friends(friendships1))