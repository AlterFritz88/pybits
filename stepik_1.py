import math
def f(x):
    return 2*math.atan(x)


x0 = 100000000000


lim = round(f(float('inf')), 3)
print (lim)