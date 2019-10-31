import math

# import libraries
def def_e(x):
    dx = 0.000001
    return round((math.exp(x+dx) - math.exp(x)) / dx, 3)

print(def_e(3))