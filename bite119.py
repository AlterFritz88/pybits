def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree = []
    for row in range(1, rows+1):
        tree.append('*'*(row*2-1))
    new_tree = []
    for i, r in enumerate(tree[::-1]):
        new_tree.append(i*' '+r)

    xmas = ''.join([x+'\n' for x in new_tree[::-1]])
    return xmas[:-1]


print(generate_xmas_tree())


default_tree = """
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
"""

print(len(generate_xmas_tree().split('\n')))
assert len(generate_xmas_tree().split('\n')) == 10