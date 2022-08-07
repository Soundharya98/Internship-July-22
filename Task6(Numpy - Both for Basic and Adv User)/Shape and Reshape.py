import numpy

a = list(map(int,input().split()))
my_array = numpy.array(a)
print(numpy.reshape(my_array, (3,3)))