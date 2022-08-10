# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean, std_dev = 500, 80
meanS, std_devS = mean, std_dev/(100**0.5)

A = mean - (1.96*std_devS)
B = mean + (1.96*std_devS)

print(round(A, 2))
print(round(B, 2))