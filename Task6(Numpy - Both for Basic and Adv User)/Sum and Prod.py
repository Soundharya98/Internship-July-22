import numpy as np

a, b = map(int,input().split())
my_array = np.array([input().split() for _ in range(a)],int)

print(np.prod(np.sum(my_array, axis=0),axis=0))