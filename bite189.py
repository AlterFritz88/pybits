IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    ans = []
    for name in names:
        if name[0] == IGNORE_CHAR:
            continue
        if len(ans) > MAX_NAMES or name[0] == QUIT_CHAR:
            break
        if len([x for x in name if x.isdigit()]) > 1:
            continue
        ans.append(name)
    return ans

print(filter_names(['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry']))