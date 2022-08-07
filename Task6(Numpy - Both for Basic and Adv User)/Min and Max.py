import numpy as np

a, b = map(int,input().split())
my_array = np.array([list(map(int,input().split())) for i in range(a)])

print(max(np.min(my_array, axis=1)))