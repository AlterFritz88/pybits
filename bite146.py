STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    romb = []
    for i in range(1, width, 2):
        romb.append('{: ^{w}}'.format(STAR*i, w=width))

    for i in range(width, 0, -2):
        romb.append('{: ^{w}}'.format(STAR*i, w=width))
    return romb

romb = gen_rhombus(5)
for row in romb:
    print(row)