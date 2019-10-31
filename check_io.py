def house(plan):
    if "#" not in plan:
        return 0

    plan = plan.strip().split('\n')
    min_x = 12
    min_y = 12
    max_x = 0
    max_y = 0


    for i, ver in enumerate(plan):
        for j, hor in enumerate(ver):
            if plan[i][j] == '#':
                if i < min_y:
                    min_y = i
                if j < min_x:
                    min_x = j
                if i > max_y:
                    max_y = i
                if j > max_x:
                    max_x = j

    res = ((max_y + 1) - min_y) * ((max_x + 1) - min_x)
    print(res)
    return res



if __name__ == '__main__':
#     print("Example:")
#     print(house('''
# 0000000
# ##00##0
# ######0
# ##00##0
# #0000#0
# '''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")