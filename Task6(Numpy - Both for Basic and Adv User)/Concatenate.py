import numpy

a, b, c = map(int, input().split())
array_1 = numpy.array([input().strip().split() for _ in range(a)],int)
array_2 = numpy.array([input().strip().split() for _ in range(b)],int)

print(numpy.concatenate((array_1, array_2), axis = 0))