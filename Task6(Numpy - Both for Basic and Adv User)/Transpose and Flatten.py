import numpy

a, b = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(a)], int)

print(array.transpose())
print(array.flatten())
