import numpy as np

P = [float(x) for x in input(). split()]
x = float(input())

print(np.polyval(P, x))
