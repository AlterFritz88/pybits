from math import sqrt

a = int(input())

S = 3*a**2 * sqrt(5*(5+2*sqrt(5)))
V = (a**3)/4 * (15+7*sqrt(5))
print(round(S, 2))
print(round(V, 2))