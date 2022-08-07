import numpy

shape = tuple(map(int,input().split()))
print(numpy.zeros(shape,int),numpy.ones(shape,int), sep='\n')