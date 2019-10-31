import numpy as np

shape = [int(x) for x in input().split(' ')]

Z = np.zeros((shape[0],shape[1]),dtype=float)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(x)